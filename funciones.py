import random
import time
import variables

# Función para colocar los barcos en el tablero.
def colocar_barco(tablero, lista_barcos):
    # Recibe como argumentos el tablero del jugador y la lista de barcos.
    # Bucle para recorrer la lista de barcos.
    for barco in lista_barcos:
        # Bucle para recorrer la lista de las posiciones de cada barco.
        for i, (fila, columna) in enumerate(barco.posiciones, start=1):
            # Marco con una 'X' cada posición.
            tablero[fila, columna] = "O"

# Función disparar.
def disparar(tablero, fila, columna, lista_barcos):
    time.sleep(1)
    # Recibe como argumentos: Tablero al que se dispara, la fila, la columna y la lista de barcos.
    if tablero[fila, columna] == " ":  # Si es una casilla vacía
        print("¡Agua!")
        tablero[fila, columna] = "#"
        time.sleep(2) 
    elif tablero[fila, columna] == "X": 
        print("Ya has disparado aquí antes.")
    else:
        # Resultado de la condición si se acierta el disparo.
        print("¡Impacto!")
        time.sleep(2)
        barco_atacado = None
        
        # Bucle para recorrer la lista de barcos.
        for barco in lista_barcos:
            if (fila, columna) in barco.posiciones:
                barco_atacado = barco
                # Fuerza la salida del bucle.
                break
        # If para marcar cada barco atacado y comprobar si ha sido hundido.    
        if barco_atacado:
            # Sustituye el valor a 'O'.
            tablero[fila, columna] = "X"
            # Eliminó esa posición de las posiciones de la clase.
            barco_atacado.posiciones.remove((fila, columna)) 
            # Compruebo si le quedan posiciones a ese barco.
            if not barco_atacado.posiciones:
                print(f"Hundiste el barco {barco_atacado.nombre}.")
                time.sleep(2) 
        if not any(barco.posiciones for barco in lista_barcos):
                print("¡¡HAS GANADO!!.")
                return False
        return True


# Funcion para el turno del jugador.
def turno_jugador(tablero, lista_barcos, tablero_vista):
    print("\n___________________________________________\n")
    print(tablero_vista)
    print("\n___________________________________________\n")
    print("Turno del jugador:")
    # Muestro la lista de posiciones a las que se ha disparado.
    print("Posiciones a las que se ha disparado: ", variables.lista_disparos_jugador)
    fila = int(input("Ingresa la fila (0-9): "))
    columna = int(input("Ingresa la columna (0-9): "))
   
    if 0 <= fila < 10 and 0 <= columna < 10:
        variables.lista_disparos_jugador.append((fila, columna))
        resultado = disparar(tablero, fila, columna, lista_barcos)
        
        if resultado == True:
            turno_jugador(tablero, lista_barcos, tablero_vista)  # Repetir turno del jugador
    else:
        print("Coordenadas fuera del rango.")
   


# Función para que el rival realice un turno.
def turno_rival(tablero, lista_barcos):
    print("\n___________________________________________\n")
    print("Turno del rival:")
    fila = random.randrange(0, 9)
    columna = random.randrange(0, 9)
    print("El rival ha disparado a la posición:", fila, ",",  columna)
    variables.lista_disparos_rival.append((fila, columna))
    resultado = disparar(tablero, fila, columna, lista_barcos)
    if resultado == False:
        print("¡Agua!")
    elif resultado == True:
        turno_rival(tablero, lista_barcos)
   


# Sistema de turnos
def turnos(tablero_jugador, tablero_rival, lista_jugador, lista_rival):
    jugador_actual = 1  # Inicia el juego con el jugador 1


    while True:
        if jugador_actual == 1:
            turno_jugador(tablero_rival, lista_rival, tablero_jugador)
            time.sleep(1)
            if not any(barco.posiciones for barco in lista_rival):
                print("¡¡HAS DERROTADO A TU RIVAL!!.")
                break
            
        else:
            turno_rival(tablero_jugador, lista_jugador)
            time.sleep(1)
            if not any(barco.posiciones for barco in lista_jugador):
                print("¡¡HAS PERDIDO!!.")
                break
           
   
        # Cambiar de jugador solo si no hubo un hundimiento
        if jugador_actual == 1:
            jugador_actual = 2
        else:
            jugador_actual = 1
