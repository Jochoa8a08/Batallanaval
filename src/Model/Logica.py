
class filas_equivocadas ( Exception ):
    pass

class columnas_equivocadas ( Exception ):
    pass

class Except_salto_disparo (Exception):
    """Aun no puedes pasar el turno,  no has elegido la posicion en la que dispararas"""

class Except_Disparo_out_of_Range (Exception):
    pass

class Except_disparo_Repetido (Exception):
    pass

#Verificar el rango para cualquier cosa y si no es el correcto saltar una excepcion
def rango_correcto (filas, columnas ):
    if filas !=10:
        raise filas_equivocadas ("ERROR: El numero de filas no es correcto, numero de filas dieferente de 10")
    
    if columnas !=10:
        raise columnas_equivocadas ("ERROR: El numero de columnas no es correcto, numero de columnas dieferente de 10")
    
#Logica BD con interfaz web
from flask import Flask, request, render_template, redirect, url_for, flash, jsonify
import sys
import psycopg2
import SecretConfigSample
import json
def get_db_connection():
    return psycopg2.connect(
        database=SecretConfigSample.PGDATABASE,
        user=SecretConfigSample.PGUSER,
        password=SecretConfigSample.PGPASSWORD,
        host=SecretConfigSample.PGHOST,
        port=SecretConfigSample.PGPORT
    )

def create_tables():
    with get_db_connection() as conexion:
        with conexion.cursor() as cursor:
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS Partidas (
                    CODIGO_PARTIDA SERIAL PRIMARY KEY,
                    jugador1 TEXT,
                    jugador2 TEXT,
                    tablero_jugador1 JSONB,
                    tablero_jugador2 JSONB
                )
            """)
        conexion.commit()

def guardar_partida(jugador1, jugador2, tablero_jugador1, tablero_jugador2):
    try:
        create_tables()
        data_jugador1 = json.dumps({"jugador1": tablero_jugador1})
        data_jugador2 = json.dumps({"jugador2": tablero_jugador2})

        with get_db_connection() as conexion:
            with conexion.cursor() as cursor:
                cursor.execute("""
                    INSERT INTO Partidas (jugador1, jugador2, tablero_jugador1, tablero_jugador2)
                    VALUES (%s, %s, %s, %s)
                """, (jugador1, jugador2, data_jugador1, data_jugador2))
            conexion.commit()

        flash("Partida guardada exitosamente.")
    except psycopg2.Error as e:
        flash(f"Error al guardar la partida: {e}")