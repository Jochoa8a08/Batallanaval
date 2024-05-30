import unittest
import psycopg2
from unittest.mock import MagicMock, patch
from io import StringIO
import sys
import json

sys.path.append("src")
sys.path.append(".")

from Controller.Control import guardar_partida, eliminar_partida, cargar_partida, consultar_numero_de_partidas_existentes
import Model.Juego_principal as Juego_principal

class TestFunciones(unittest.TestCase):

    def setUp(self):
        self.jugador1 = "jugador1"
        self.jugador2 = "jugador2"
        self.tablero_jugador1 = {"fila1": [0, 0, 0], "fila2": [0, 0, 0], "fila3": [0, 0, 0]}
        self.tablero_jugador2 = {"fila1": [0, 0, 0], "fila2": [0, 0, 0], "fila3": [0, 0, 0]}

    @patch('psycopg2.connect')
    @patch('sys.stdout', new_callable=StringIO)
    def test_guardar_partida(self, mock_stdout, mock_connect):
        guardar_partida(self.jugador1, self.jugador2, self.tablero_jugador1, self.tablero_jugador2)
        self.assertEqual(mock_stdout.getvalue().strip(), "Partida guardada exitosamente.")

    @patch('psycopg2.connect')
    @patch('sys.stdout', new_callable=StringIO)
    def test_eliminar_partida(self, mock_stdout, mock_connect):
        eliminar_partida()
        self.assertEqual(mock_stdout.getvalue().strip(), "Partida eliminada exitosamente.")

    @patch('psycopg2.connect')
    def test_consultar_numero_de_partidas_existentes_exito(self, mock_connect):
        mock_connection = MagicMock()
        mock_cursor = MagicMock()
        mock_connect.return_value = mock_connection
        mock_connection.cursor.return_value = mock_cursor

        mock_cursor.fetchall.return_value = [(self.jugador1, self.jugador2, json.dumps({"jugador1": self.tablero_jugador1}), json.dumps({"jugador2": self.tablero_jugador2}))]

        result = consultar_numero_de_partidas_existentes()
        self.assertEqual(result, 1)

    @patch('psycopg2.connect')
    @patch('sys.stdout', new_callable=StringIO)
    def test_guardar_partida_error(self, mock_stdout, mock_connect):
        mock_connect.side_effect = psycopg2.Error

        guardar_partida(self.jugador1, self.jugador2, self.tablero_jugador1, self.tablero_jugador2)
        self.assertIn("Error al guardar la partida:", mock_stdout.getvalue().strip())

    @patch('psycopg2.connect')
    def test_cargar_partida_sin_datos(self, mock_connect):
        mock_cursor = MagicMock()
        mock_connect.return_value.cursor.return_value = mock_cursor
        mock_cursor.fetchone.return_value = None

        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            cargar_partida()
            self.assertEqual(mock_stdout.getvalue().strip(), "No hay partidas guardadas.")

    @patch('psycopg2.connect')
    def test_cargar_partida_no_existente(self, mock_connect):
        mock_cursor = MagicMock()
        mock_connect.return_value.cursor.return_value = mock_cursor
        mock_cursor.fetchone.return_value = None

        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            jugador1, jugador2 = cargar_partida()
            self.assertIsNone(jugador1)
            self.assertIsNone(jugador2)
            self.assertEqual(mock_stdout.getvalue().strip(), "No hay partidas guardadas.")

    @patch('psycopg2.connect')
    def test_consultar_numero_de_partidas_existentes_error(self, mock_connect):
        mock_connect.side_effect = psycopg2.Error

        result = consultar_numero_de_partidas_existentes()
        self.assertIsNone(result)

if __name__ == '__main__':
    unittest.main()
