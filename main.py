import funciones
import clases
import variables

# Bucle con el que recorro el diccionario del rival.
for nombre, eslora in variables.barcos_rival.items():
    barco = clases.barco(nombre, eslora)
    barco.generar_posiciones()
    variables.lista_rival.append(barco)


for nombre, eslora in variables.barcos_jugador.items():
    barco = clases.barco(nombre, eslora)
    barco.generar_posiciones()
    variables.lista_jugador.append(barco)

# Imprimir los barcos creados
"""print("-------------------------BARCOS RIVAL")
for barco in variables.lista_rival:
    print(f"Nombre: {barco.nombre}, Eslora: {barco.eslora}, Posiciones: {barco.posiciones}")"""

print("-------------------------BARCOS JUGADOR")
for barco in variables.lista_jugador:
    print(f"Nombre: {barco.nombre}, Eslora: {barco.eslora}, Posiciones: {barco.posiciones}")

funciones.colocar_barco(variables.tablero_rival, variables.lista_rival)
funciones.colocar_barco(variables.tablero_jugador, variables.lista_jugador)

funciones.turnos(variables.tablero_jugador, variables.tablero_rival, variables.lista_jugador, variables.lista_rival)










