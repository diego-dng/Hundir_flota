import funciones
import numpy as np
import random

class barco:
    def __init__(self, nombre, eslora):
        self.nombre = nombre
        self.eslora = eslora
        self.posiciones = []

    def generar_posiciones(self):
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        fila_random = random.randint(0, 9)
        columna_random = random.randint(0, 9)
        direction = random.choice(directions)

        for _ in range(self.eslora):
            if 0 <= fila_random < 10 and 0 <= columna_random < 10:
                self.posiciones.append((fila_random, columna_random))
                fila_random += direction[0]
                columna_random += direction[1]
            else:
                print("Error")
                self.posiciones = []
                self.generar_posiciones()