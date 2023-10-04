import funciones
# Tablero del rival.
tablero_rival = funciones.crear_tablero()
# Tablero del jugador.
tablero_jugador = funciones.crear_tablero()

# Colocamos dos barcos del rival.
#funciones.colocar_barco(funciones.crear_barco_random(4, ), tablero_rival)
#funciones.colocar_barco(funciones.crear_barco_random(3), tablero_rival)

# PREGUNTAR SI LOS BARCOS DEL JUGADOR SE METEN POR INPUTS O SON RANDOM.
funciones.crear_barco(3, tablero_rival)
funciones.crear_barco(2, tablero_rival)
# Mediante inputs, colocar los barcos del jugador.
funciones.crear_barco(3, tablero_jugador)
funciones.crear_barco(2, tablero_jugador)

print(tablero_rival)
print("\n___________________________________________\n")
print(tablero_jugador)

# Primer disparo del jugador.
funciones.disparar(tablero_rival, True)
funciones.disparar(tablero_jugador)


print(tablero_rival)
print("\n___________________________________________\n")
print(tablero_jugador)

# 20 posiciones en total.
