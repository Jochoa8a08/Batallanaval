import psycopg2
import sys
sys.path.append("src")
sys.path.append(".")
import SecretConfig
#from Model.Juego_principal import TableroBatallaNaval
# Do not expose your Neon credentials to the browser
import json

def guardar_partida (jugador1, jugador2, tablero_jugador1, tablero_jugador2):
    try:
        data_jugador1 ={"jugador1": tablero_jugador1,}
        informacion_jugador1 = json.dumps(data_jugador1) 
        data_jugador2 ={"jugador2": tablero_jugador2,}
        informacion_jugador2 = json.dumps(data_jugador2)          

            # Conectar a la base de datos PostgreSQL
        conexion = psycopg2.connect(
            database= SecretConfig.PGDATABASE, 
            user= SecretConfig.PGUSER, 
            password= SecretConfig.PGPASSWORD, 
            host= SecretConfig.PGHOST, 
            port= SecretConfig.PGPORT
        )
            
        cursor = conexion.cursor()

        # Insertar los datos de la nueva partida en la tabla
        cursor.execute("""CREATE TABLE IF NOT EXISTS Partidas (
                            CODIGO_PARTIDA SERIAL PRIMARY KEY,
                            jugador1 TEXT,
                            jugador2 TEXT,
                            tablero_jugador1 JSONB,
                            tablero_jugador2 JSONB
                        )""")
        cursor.execute("SELECT CODIGO_PARTIDA FROM Partidas")
        partida_existente = cursor.fetchone()

        if partida_existente:            
    # Si ya hay una partida guardada, actualizarla
            cursor.execute("UPDATE Partidas SET jugador1 = %s, jugador2 = %s, tablero_jugador1 = %s, tablero_jugador2 = %s",
                           (jugador1, jugador2, informacion_jugador1, informacion_jugador2))
        else:
            # Si no hay ninguna partida guardada, insertar una nueva
            cursor.execute("INSERT INTO Partidas (jugador1, jugador2, tablero_jugador1, tablero_jugador2) "
               "VALUES (%s, %s, %s, %s)", (jugador1, jugador2, informacion_jugador1, informacion_jugador2))

        
        
        # Guardar los cambios y cerrar la conexión
        conexion.commit()

        print("Partida guardada exitosamente.")
    except psycopg2.Error as Except_No_Partidas_Existentes:
        print("Error al guardar la partida:", Except_No_Partidas_Existentes)


def eliminar_partida():
    try:
        conexion = psycopg2.connect(database= SecretConfig.PGDATABASE, 
            user= SecretConfig.PGUSER, 
            password= SecretConfig.PGPASSWORD, 
            host= SecretConfig.PGHOST, 
            port= SecretConfig.PGPORT)  
        cursor = conexion.cursor()
        cursor.execute("DELETE FROM partidas WHERE id = (SELECT MAX(id) FROM partidas)")
        conexion.commit()
        print("Partida eliminada exitosamente.")
    except Exception as e:
        print(f"Error al eliminar la partida: {e}")
    finally:
        if conexion:
            cursor.close()
            conexion.close()


def cargar_partida():
    from Model.Juego_principal import TableroBatallaNaval
    try:
        # Conectar a la base de datos PostgreSQL
        conexion = psycopg2.connect(
            database=SecretConfig.PGDATABASE,
            user=SecretConfig.PGUSER,
            password=SecretConfig.PGPASSWORD,
            host=SecretConfig.PGHOST,
            port=SecretConfig.PGPORT
        )
        cursor = conexion.cursor()

        # Obtener la última partida guardada
        cursor.execute("SELECT jugador1, jugador2, tablero_jugador1, tablero_jugador2 FROM Partidas")
        partida_guardada = cursor.fetchone()

        if partida_guardada:            
    # Si ya hay una partida guardada, cargarla
            tablero_jugador1 = partida_guardada[2]
            tablero_jugador2 = partida_guardada[3]
            jugador1 = tablero_jugador1["jugador1"]
            jugador2 = tablero_jugador2["jugador2"]

            Jugador1 = TableroBatallaNaval(10, 10)
            Jugador1.tablero = tablero_jugador1["jugador1"]
            Jugador2 = TableroBatallaNaval(10, 10) 
            Jugador2.tablero = tablero_jugador2["jugador2"]
            print("Partida cargada exitosamente.")
            return jugador1, jugador2
        else:
            print("No hay partidas guardadas.")
            return None, None

    except psycopg2.Error as Error_al_cargar_la_partida:
        print("Error al cargar la partida:", Error_al_cargar_la_partida)
        return None, None
def consultar_numero_de_partidas_existentes():
    try:
        conexion = psycopg2.connect(
            database=SecretConfig.PGDATABASE,
            user=SecretConfig.PGUSER,
            password=SecretConfig.PGPASSWORD,
            host=SecretConfig.PGHOST,
            port=SecretConfig.PGPORT
        )
        cursor = conexion.cursor()

        cursor.execute("SELECT jugador1, jugador2, tablero_jugador1, tablero_jugador2 FROM Partidas")
        partidas_guardadas = cursor.fetchall()

        if partidas_guardadas:
            numero_partidas = len(partidas_guardadas)
            return numero_partidas
        else:
            return 0
    except psycopg2.Error as Error_No_Existen_partidas_guardadas:
        print("Error al consultar el numero de partidas guardadas:", Error_No_Existen_partidas_guardadas)
        return None
