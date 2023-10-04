import numpy as np
import random

def crear_tablero(tamaño=(10,10)):
    return np.full(tamaño, " ")

def colocar_barco(barco, tablero):
    for casilla in barco:
        tablero[casilla] = "O"
    return tablero

def disparar(tablero, turno_jugador = False):
    if turno_jugador == True:
        # Input para pedir la posición a la que quiere disparar.
        x = input("posición X: ")
        y = input("posición Y: ")
        print("Las cordenadas del jugador son:",x,"-",y)
    else:
        x = random.randrange(0, 9)
        y = random.randrange(0, 9)
        print("Las cordenadas del rival son:",x,"-",y)

    #casilla = (x,y)
    x = int(x)
    y = int(y)
    if tablero[x,y] == " ":
        print("Agua")
        tablero[x,y] = "-"
        #disparar(tablero, turno_jugador)
    else:
        print("Tocado")
        tablero[x,y] = "X"
        #disparar(tablero, turno_jugador)
    return tablero

def crear_barco(eslora, tablero):
    filas = random.randrange(0, 9)
    columnas = random.randrange(0, 9)
    
    orientacion = random.choice(["N", "S", "E", "O"])
    print(filas, "|", columnas, "|", orientacion, "|", eslora)

    if tablero[filas, columnas] == " ":
        tablero[filas, columnas] = "O"
        if orientacion == "N":
            while eslora > 0: 
                tablero[filas - 1, columnas] = "O"
                filas = filas - 1
                eslora = eslora-1

        elif orientacion == "S":
            while eslora > 0: 
                tablero[filas + 1, columnas] = "O"
                filas = filas + 1
                eslora = eslora-1
        
        elif orientacion == "E":
            while eslora > 0:
                tablero[filas, columnas + 1] = "O"
                columnas = columnas + 1
                eslora = eslora-1

        elif orientacion == "O":
            while eslora > 0:
                tablero[filas, columnas - 1] = "O"
                columnas = columnas - 1
                eslora = eslora-1
        

    else:
        # Revisar tema de argumento eslora.
        crear_barco(3, tablero)
    