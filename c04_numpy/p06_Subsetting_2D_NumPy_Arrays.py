# Ejercicio
# Subconjuntos de arreglos NumPy 2D

# Descripción
# Si tu arreglo numpy 2D tiene una estructura regular, es decir, cada fila y columna tiene un número fijo de valores,
# las formas complicadas de crear subconjuntos se vuelven muy fáciles. 

# Instrucciones
# 1. Imprime la fila 50 de np_baseball.
# 2. Crea una nueva variable, np_weight_lb, que contenga toda la segunda columna de np_baseball.
# 3. Selecciona la altura (primera columna) del jugador de béisbol número 124 en np_baseball e imprímela.

# Código en Python

# Importar numpy como np
import numpy as np  # Se importa el paquete numpy con el alias 'np'.

# Lista de listas que contiene la altura y el peso de 200 jugadores de béisbol (valores de ejemplo)
baseball = [
    [180, 78.4], [215, 102.7], [210, 98.5], [188, 75.2], [190, 82.1], [205, 99.3], [200, 95.1], [185, 80.5],
    [195, 89.4], [210, 99.9], [183, 78.1], [195, 90.7], [197, 92.4], [212, 105.3], [190, 83.4], [180, 77.8],
    [192, 88.9], [198, 94.3], [215, 102.1], [205, 97.5], [190, 85.2], [203, 96.3], [210, 101.5], [187, 79.8],
    [192, 88.5], [205, 96.9], [215, 102.7], [210, 100.5], [187, 79.4], [195, 89.6], [203, 95.9], [210, 100.8],
    [185, 80.3], [195, 89.2], [200, 94.0], [190, 85.7], [185, 81.0], [193, 91.3], [210, 101.2], [200, 94.7],
    [195, 89.8], [190, 85.1], [192, 88.0], [188, 83.9], [197, 92.1], [210, 100.9], [203, 96.7], [187, 78.9],
    [192, 87.9], [205, 97.2], [210, 101.4], [187, 79.1], [195, 89.3], [200, 93.8], [190, 85.4], [185, 80.8],
    [193, 91.1], [210, 100.7], [200, 94.5], [195, 89.9], [190, 84.9], [192, 87.8], [188, 83.5], [197, 91.8],
    [210, 100.4], [203, 96.4], [187, 78.6], [192, 87.6], [205, 97.0], [210, 101.0], [187, 79.0], [195, 89.4],
    [200, 93.7], [190, 85.5], [185, 80.7], [193, 90.9], [210, 100.6], [200, 94.6], [195, 89.7], [190, 85.0],
    [192, 87.7], [188, 83.3], [197, 91.6], [210, 100.3], [203, 96.2], [187, 78.8], [192, 87.7], [205, 96.9],
    [210, 101.1], [187, 78.8], [195, 89.2], [200, 94.1], [190, 85.6], [185, 81.0], [193, 91.3], [210, 101.2],
    [200, 94.7], [195, 89.8], [190, 85.1], [192, 88.0], [188, 83.9], [197, 92.1], [210, 100.9], [203, 96.7],
    [187, 78.9], [192, 87.9], [205, 97.2], [210, 101.4], [187, 79.1], [195, 89.3], [200, 93.8], [190, 85.4],
    [185, 80.8], [193, 91.1], [210, 100.7], [200, 94.5], [195, 89.9], [190, 84.9], [192, 87.8], [188, 83.5],
    [197, 91.8], [210, 100.4], [203, 96.4], [187, 78.6], [192, 87.6], [205, 97.0], [210, 101.0], [187, 79.0],
    [195, 89.4], [200, 93.7], [190, 85.5], [185, 80.7], [193, 90.9], [210, 100.6], [200, 94.6], [195, 89.7],
    [190, 85.0], [192, 87.7], [188, 83.3], [197, 91.6], [210, 100.3], [203, 96.2], [187, 78.8], [192, 87.7],
    [205, 96.9], [210, 101.1], [187, 78.8], [195, 89.2], [200, 94.1], [190, 85.6], [185, 81.0], [193, 91.3],
    [210, 101.2], [200, 94.7], [195, 89.8], [190, 85.1], [192, 88.0], [188, 83.9], [197, 92.1], [210, 100.9],
    [203, 96.7], [187, 78.9], [192, 87.9], [205, 97.2], [210, 101.4], [187, 79.1], [195, 89.3], [200, 93.8]
]  # Lista extendida con 200 jugadores.

# Crear un arreglo numpy 2D desde 'baseball': np_baseball
np_baseball = np.array(baseball)  # Se convierte la lista de listas 'baseball' en un arreglo numpy 2D.

# Imprimir la fila 50 de np_baseball
print(np_baseball[49])  # Imprime la fila 50 del arreglo 'np_baseball'.

# Seleccionar la segunda columna completa de np_baseball: np_weight_lb
np_weight_lb = np_baseball[:, 1]  # Se selecciona la segunda columna completa, que contiene los pesos en kg.

# Imprimir el peso de np_weight_lb para verificar
print(np_weight_lb)

# Imprimir la altura (primera columna) del jugador de béisbol número 124
print(np_baseball[123, 0])  # Se selecciona la altura del jugador 124 (índice 123) y se imprime.