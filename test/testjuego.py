import unittest
import sys
sys.path.append("src")
sys.path.append(".")

from Controller import Control
import Model.Juego_principal as Juego_principal
import Model.Logica as Logica
from colorama import Fore, Style
player= Juego_principal.TableroBatallaNaval(10,10)

class tests(unittest.TestCase):
    
    def testcuadricula_dimensiones(self):
        result= player.contador_filas_columnas()
        expected= 100
        if result==expected:
            print("Prueba testcuadricula_dimensiones superada")
        
        self.assertEqual( expected, result  )
        
    
    def testcuadricula_dibujo(self):
        expected=[
        ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O']
            ]
        TestOk= True
        for fila in expected:
            for elemento in fila:
                if elemento != "0":
                    TestOk= False

        if TestOk:
            print("Prueba testcuadricula_dibujo superada")


    def testnaves(self):
        num_filas= 10
        num_columnas= 10
        result = 19
        contador= 0
        player= [
            ['0', 'B', 'B', 'O', 'B', 'O', 'O', 'O', 'O', 'O'],
            ['0', '0', 'O', 'O', 'B', 'O', 'O', 'O', 'O', 'O'],
            ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'B', 'O'],
            ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'B', 'O'],
            ['O', 'B', 'B', 'B', 'B', 'B', 'O', 'O', 'O', 'O'],
            ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'B'],
            ['O', 'O', 'B', 'O', 'O', 'O', 'O', 'O', 'O', 'B'],
            ['O', 'O', 'B', 'O', 'O', 'B', 'B', 'B', 'O', 'O'],
            ['O', 'O', 'B', 'O', 'O', 'O', 'O', 'O', 'O', 'O'],
            ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O']
            ]
        for fila in player:
            for elemento in fila:
                if elemento== "B":
                    contador+=1
        if result==contador:
            print("Prueba testnaves superada")
        self.assertEqual( contador, result, 2  )


    def test_puntaje(self): 
        puntaje= 0
        player= [
            ['B', 'X', 'B', 'O', 'B', 'O', 'O', 'O', 'O', 'O'],
            ['B', 'X', 'O', 'O', 'B', 'O', 'O', 'O', 'O', 'O'],
            ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'B', 'O'],
            ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'B', 'O'],
            ['O', 'B', 'B', 'B', 'B', 'X', 'O', 'O', 'O', 'O'],
            ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'B'],
            ['O', 'O', 'B', 'O', 'O', 'O', 'O', 'O', 'O', 'B'],
            ['O', 'O', 'B', 'O', 'O', 'B', 'B', 'B', 'O', 'O'],
            ['O', 'O', 'B', 'O', 'O', 'O', 'O', 'O', 'O', 'O'],
            ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O']
            ]
        for fila in player:
            for elemento in fila:
                if elemento== "X":
                    puntaje+= 10
        print("Prueba test_puntaje superada")            
        print("Tu puntaje es:" , puntaje)
        

    def test_disparo_repetido(self):
        expected=[
        ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'X', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O']
            ]
        pos_fila = 2
        pos_columna = 6
        disparo = player.disparar(pos_fila, pos_columna, expected)
        if disparo == expected[pos_fila-1][pos_columna-1]:
            raise Logica.Except_Disparo_Repetido("Ya has disparado a esta posición antes.")
        print("TestOk")
            

    def test_disparo_esquina_izquierdaarriba(self):
        pos_fila= 0
        pos_columna = 0
        expected= [
        ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O']
        ]
        Ok= True
        disparo= player.disparar(pos_fila, pos_columna, expected)
        for fila in range(len(expected)):
            for columna in range(len(expected[fila])):
                if expected[fila][columna] != disparo:
                    Ok= False
        if Ok is True:

            print("Prueba disparo_esquina_izquierdaarriba superada")

    
    def test_disparo_esquina_derechaarriba(self):
        pos_fila= 9
        pos_columna = 0
        expected= [
        ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O']
        ]
        Ok= True
        disparo= player.disparar(pos_fila, pos_columna, expected)
        for fila in range(len(expected)):
            for columna in range(len(expected[fila])):
                if expected[fila][columna] != disparo:
                    Ok= False
        if Ok is True:

            print("Prueba disparo_esquina_derechaarriba superada")


    def test_disparo_esquina_izquierdaabajo(self):
        pos_fila= 0
        pos_columna = 9
        expected= [
        ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O']
        ]
        Ok= True
        disparo= player.disparar(pos_fila, pos_columna, expected)
        for fila in range(len(expected)):
            for columna in range(len(expected[fila])):
                if expected[fila][columna] != disparo:
                    Ok= False
        if Ok is True:

            print("Prueba disparo_esquina_izquierdaabajo superada")



    def test_disparo_esquina_derechaabajo(self):
        pos_fila= 9
        pos_columna = 9
        expected= [
        ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O']
        ]
        Ok= True
        disparo= player.disparar(pos_fila, pos_columna, expected)
        for fila in range(len(expected)):
            for columna in range(len(expected[fila])):
                if expected[fila][columna] != disparo:
                    Ok= False
        if Ok is True:

            print("Prueba disparo_esquina_derechaabajo superada")

    def test_disparo_out_of_range(self):
        pos_fila = 13
        pos_columna = 12
        expected = [
            ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O'],
            ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O'],
            ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O'],
            ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O'],
            ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O'],
            ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O'],
            ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O'],
            ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O'],
            ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O'],
            ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O']
        ]

        if (pos_fila + pos_columna)/2 > 10:
            raise Logica.Except_Disparo_out_of_Range("Disparo fuera de rango")
        else:
            player.disparar(pos_fila, pos_columna, expected)
        

    def test_Exception_salto_disparo(self):
        pos_fila= ""
        pos_columna = ""
        TestOk= False
        if pos_fila == "" or pos_columna == "":
            TestOk= True
            print("La prueba test_Exception_salto_disparo ha sido superada")
            self.assertRaises(Logica.Except_salto_disparo)
            
        


    def test_disparo_esquina_izquierdaarriba_barco(self):
        pos_fila= 0
        pos_columna = 0
        expected= [
            ['B', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'B'],
            ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O'],
            ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O'],
            ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O'],
            ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O'],
            ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O'],
            ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O'],
            ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O'],
            ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O'],
            ['B', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'B']
        ]


        disparo= player.disparar(pos_fila, pos_columna,expected)
        if expected[pos_fila][pos_columna]== disparo:
            print("Prueba test_disparo_esquina_izquierdaarriba_barco superada")
          

    def test_disparo_esquina_derechaarriba_barco(self):
        pos_fila= 9
        pos_columna = 0
        expected= [
    ['B', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'B'],
    ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O'],
    ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O'],
    ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O'],
    ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O'],
    ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O'],
    ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O'],
    ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O'],
    ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O'],
    ['B', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'B']
]


        disparo= player.disparar(pos_fila, pos_columna,expected)
        if expected[pos_fila][pos_columna]== disparo:
            print("Prueba test_disparo_esquina_derechaarriba_barco superada")


    def test_disparo_esquina_izquierdaabajo_barco(self):
        pos_fila= 0
        pos_columna = 9
        expected= [
    ['B', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'B'],
    ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O'],
    ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O'],
    ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O'],
    ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O'],
    ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O'],
    ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O'],
    ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O'],
    ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O'],
    ['B', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'B']
]


        disparo= player.disparar(pos_fila, pos_columna,expected)
        if expected[pos_fila][pos_columna]== disparo:
            print("Prueba test_disparo_esquina_izquierdaabajo_barco superada")


    def test_disparo_esquina_derechaabajo_barco(self):
        pos_fila= 9
        pos_columna = 9
        expected= [
    ['B', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'B'],
    ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O'],
    ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O'],
    ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O'],
    ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O'],
    ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O'],
    ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O'],
    ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O'],
    ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O'],
    ['B', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'B']
]


        disparo= player.disparar(pos_fila, pos_columna,expected)
        if expected[pos_fila][pos_columna]== disparo:
            print("Prueba test_disparo_esquina_derechaabajo_barco superada")



    def testdisparo(self):
        pos_fila = 4
        pos_columna = 6
        expected = [
            ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O'],
            ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O'],
            ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O'],
            ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O'], 
            ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O'],
            ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O'],
            ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O'],
            ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O'],
            ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O'],
            ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O']
        ]
        disparo = player.disparar(pos_fila, pos_columna, expected)
        self.assertEqual(disparo, expected[pos_fila][pos_columna])
        print("Prueba testdisparo superada")
        

       

if __name__ == '__main__':
    unittest.main()






