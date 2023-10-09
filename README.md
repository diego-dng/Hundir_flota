# **Hundir la flota.**
Juego de Hundir la flota en modo consola, realizado en Python.




## Descripción del juego.
Juego de Hundir la flota, en la que el jugador compite contra la máquina.
El tablero se representa con una matriz de tamaño 10x10.


Cada jugador tiene 10 barcos:
- 1 barco de tamaño 4.
- 2 barcos de tamaño 3.
- 3 barcos de tamaño 2.
- 4 barcos de tamaño 1.


Los barcos se colocarán de manera aleatoria para ambos jugadores.


Los barcos se representarán en la matriz con una "O".
Los impactos en posiciones en las que hay un barco se representarán en la matriz con "X".
Los disparos al agua se representarán en la matriz con "#".


## Funciones.
Funciones del código:


- "colocar_barco(tablero, lista_barcos)": Función que coloca los barcos en su posición correspondiente en la matriz(tablero).
    Recibe dos argumentos:
    - tablero: Indica el tablero de cada jugador.
    - lista_barcos: Indica la lista de barcos de cada jugador.


- "turno_jugador(tablero, lista_barcos)": Función del turno del jugador.
    Recibe 2 argumentos:
    - tablero: Indica el tablero de cada jugador.
    - lista_barcos: Indica la lista de barcos de cada jugador.


    En esta función se introduce mediante inputs la posición de disparo.
    Después, se llama desde esta a la función "disparar()".


- "turno_rival(tablero, lista_barcos)": Función del turno del rival.
    Recibe 2 argumentos:
    - tablero: Indica el tablero de cada jugador.
    - lista_barcos: Indica la lista de barcos de cada jugador.


    En esta función se asigna aleatoriamente la posición de disparo.
    Después, se llama desde esta a la función "disparar()".


- "disparar(tablero, fila, columna, lista_barcos)": Función que realiza el disparo.
    Recibe 4 argumentos:
    - tablero: El tablero al que se va a disparar.
    - fila.
    - columna.
    - lista_barcos: La lista de barcos del jugador al que se dispara.
   


- "turnos(tablero_jugador, tablero_rival, lista_jugador, lista_rival)":
    Recibe 4 argumentos:
    - tablero_jugador.
    - tablero_rival.
    - lista_jugador.
    - lista_rival.


## Clases.
Los barcos están almacenados en una clase. En ella se especifica el nombre del barco y su tamaño.
El primer turno siempre es del jugador.