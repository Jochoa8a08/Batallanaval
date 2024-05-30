from flask import Flask, request, render_template, redirect, url_for, flash, jsonify
import sys
import psycopg2
import json
sys.path.append("src")
sys.path.append(".")
from Model import Juego_principal
from Model.Logica import get_db_connection,guardar_partida
# Inicializar los tableros para los dos jugadores
player_board = Juego_principal.TableroBatallaNaval(10, 10)
opponent_board = Juego_principal.TableroBatallaNaval(10, 10)

# Colocar barcos en los tableros
player_board.nave_de_3_casillas()
player_board.nave_de_5_casillas()
player_board.nave_de_2_casillas()
opponent_board.nave_de_3_casillas()
opponent_board.nave_de_5_casillas()
opponent_board.nave_de_2_casillas()

app = Flask(__name__)
app.secret_key = 'supersecretkey'  


@app.route('/')
def index():
    try:
        with get_db_connection() as conexion:
            with conexion.cursor() as cursor:
                cursor.execute("SELECT CODIGO_PARTIDA, jugador1, jugador2 FROM Partidas")
                partidas = cursor.fetchall()
        return render_template('index.html', partidas=partidas)
    except psycopg2.Error as e:
        flash(f"Error al consultar las partidas: {e}")
        return redirect(url_for('index'))


@app.route('/guardar', methods=['POST'])
def guardar():
    jugador1 = request.form['jugador1']
    jugador2 = request.form['jugador2']

    tablero_jugador1 = [
        [request.form.get(f'tablero_jugador1[{i}][{j}]', 'O') for j in range(10)]
        for i in range(10)
    ]
    
    tablero_jugador2 = [
        [request.form.get(f'tablero_jugador2[{i}][{j}]', 'O') for j in range(10)]
        for i in range(10)
    ]
    
    guardar_partida(jugador1, jugador2, tablero_jugador1, tablero_jugador2)
    return redirect(url_for('index'))

@app.route('/partidas')
def partidas():
    try:
        with get_db_connection() as conexion:
            with conexion.cursor() as cursor:
                cursor.execute("SELECT * FROM Partidas")
                partidas = cursor.fetchall()
        return render_template('partidas.html', partidas=partidas)
    except psycopg2.Error as e:
        flash(f"Error al consultar las partidas: {e}")
        return redirect(url_for('index'))

@app.route('/eliminar/<int:id>', methods=['POST'])
def eliminar(id):
    try:
        with get_db_connection() as conexion:
            with conexion.cursor() as cursor:
                cursor.execute("DELETE FROM Partidas WHERE CODIGO_PARTIDA = %s", (id,))
            conexion.commit()
        flash("Partida eliminada exitosamente.")
    except psycopg2.Error as e:
        flash(f"Error al eliminar la partida: {e}")
    return redirect(url_for('partidas'))

@app.route('/cargar_partida/<int:id>', methods=['GET'])
def cargar_partida(id):
    try:
        with get_db_connection() as conexion:
            with conexion.cursor() as cursor:
                cursor.execute("SELECT jugador1, jugador2, tablero_jugador1, tablero_jugador2 FROM Partidas WHERE CODIGO_PARTIDA = %s", (id,))
                partida = cursor.fetchone()

        if partida:
            tablero_jugador1 = partida[2]  
            tablero_jugador2 = partida[3]  
            return jsonify({
                'jugador1': partida[0],
                'jugador2': partida[1],
                'tablero_jugador1': tablero_jugador1['jugador1'],
                'tablero_jugador2': tablero_jugador2['jugador2']
            })
        else:
            return jsonify({'error': 'Partida no encontrada'}), 404
    except psycopg2.Error as e:
        return jsonify({'error': str(e)}), 500

@app.route('/make_move', methods=['POST'])
def make_move():
    data = request.get_json()
    x, y = data['x'], data['y']
    result = {'hit': False, 'sink': False, 'game_over': False}
    
    hit_result = opponent_board.disparar(x + 1, y + 1, opponent_board.tablero)
    
    if hit_result == 'X':
        result['hit'] = True
        if opponent_board.barco_hundido():
            result['sink'] = True
    
    if not opponent_board.buscar_barco():
        result['game_over'] = True
    
    return jsonify(result)


if __name__ == '__main__':
    app.run(debug=True)
