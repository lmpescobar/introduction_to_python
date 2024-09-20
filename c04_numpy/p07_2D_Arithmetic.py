# Ejercicio
# Aritmética con arreglos 2D

# Descripción
# Los arreglos numpy 2D pueden realizar cálculos elemento a elemento, al igual que los arreglos numpy 1D.

# 'np_baseball' ya está codificado para ti; es nuevamente un arreglo numpy 2D con 3 columnas que representan
# la altura (en pulgadas), el peso (en libras) y la edad (en años). 'baseball' está disponible como una lista
# de listas regular y 'updated' está disponible como un arreglo numpy 2D.

# Instrucciones
# 1. Has logrado obtener los cambios en la altura, peso y edad de todos los jugadores de béisbol. 
#    Está disponible como un arreglo numpy 2D, 'updated'. Suma 'np_baseball' y 'updated' e imprime el resultado.
# 2. Deseas convertir las unidades de altura y peso a métricas (metros y kilogramos, respectivamente). 
#    Como primer paso, crea un arreglo numpy con tres valores: 0.0254, 0.453592 y 1. Nombra este arreglo 'conversion'.
# 3. Multiplica 'np_baseball' por 'conversion' e imprime el resultado.

# Código en Python

# Importar numpy como np
import numpy as np  # Se importa el paquete numpy con el alias 'np'.

# Lista de listas con altura (pulgadas), peso (libras) y edad (años) de jugadores de béisbol
baseball = [
    [180, 78.4, 25], [215, 102.7, 30], [210, 98.5, 28], [188, 75.2, 22], [190, 82.1, 24],
    [205, 99.3, 29], [200, 95.1, 27], [185, 80.5, 23], [195, 89.4, 26], [210, 99.9, 28],
    [183, 78.1, 24], [195, 90.7, 27], [197, 92.4, 30], [212, 105.3, 29], [190, 83.4, 25],
    [180, 77.8, 24], [192, 88.9, 26], [198, 94.3, 28], [215, 102.1, 32], [205, 97.5, 29]
]

# Crear un arreglo numpy 2D desde 'baseball': np_baseball
np_baseball = np.array(baseball)  # Se convierte la lista de listas 'baseball' en un arreglo numpy 2D.

# Arreglo numpy con cambios en altura (pulgadas), peso (libras) y edad (años)
updated = np.array([
    [1, -0.5, 1], [-1, 0.3, 0], [0, 0, -1], [2, -0.1, 2], [-1, 0.4, -1],
    [0, -0.2, 1], [1, 0.6, 0], [-1, -0.3, 1], [0, 0.1, -2], [-1, -0.4, 1],
    [1, 0.2, 1], [0, 0.1, 0], [0, -0.3, -1], [-1, 0.5, 2], [2, -0.2, 1],
    [-1, -0.1, -1], [1, 0.2, 0], [0, -0.4, 1], [-1, 0.3, 0], [1, 0.1, 2]
])  # Se define el arreglo 'updated' con cambios en altura, peso y edad.

# Sumar np_baseball y updated e imprimir el resultado
print(np_baseball + updated)  # Se imprime la suma de 'np_baseball' y 'updated'.

# Crear un arreglo numpy con valores de conversión: conversion
conversion = np.array([0.0254, 0.453592, 1])  # Valores de conversión para altura (m), peso (kg) y edad.

# Multiplicar np_baseball por conversion e imprimir el resultado
print(np_baseball * conversion)  # Se imprime el resultado de la multiplicación elemento a elemento.