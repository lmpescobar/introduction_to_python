# Ejercicio
# Tu primer arreglo NumPy 2D

# Descripción
# Antes de trabajar con los datos reales de la MLB, intentemos crear un arreglo NumPy 2D a partir de 
# una pequeña lista de listas.

# En este ejercicio, 'baseball' es una lista de listas. La lista principal contiene 4 elementos. 
# Cada uno de estos elementos es una lista que contiene la altura y el peso de 4 jugadores de béisbol, 
# en este orden. 'baseball' ya está codificado para ti en el script.

# Instrucciones
# 1. Usa np.array() para crear un arreglo numpy 2D desde 'baseball'. Nombra este arreglo 'np_baseball'.
# 2. Imprime el tipo de 'np_baseball'.
# 3. Imprime el atributo 'shape' de 'np_baseball'. Usa 'np_baseball.shape'.

# Código en Python

# Importar numpy como np
import numpy as np  # Se importa el paquete numpy con el alias 'np'.

# Lista de listas que contiene altura y peso de jugadores de béisbol
baseball = [[180, 78.4],  # Datos del primer jugador: altura en cm, peso en kg.
            [215, 102.7], # Datos del segundo jugador.
            [210, 98.5],  # Datos del tercer jugador.
            [188, 75.2]]  # Datos del cuarto jugador.

# Crear un arreglo numpy 2D desde 'baseball': np_baseball
np_baseball = np.array(baseball)  # Se convierte la lista de listas 'baseball' en un arreglo numpy 2D.

# Imprimir el tipo de np_baseball
print(type(np_baseball))  # Se imprime el tipo del objeto 'np_baseball' para verificar que es un arreglo numpy.

# Imprimir la forma de np_baseball
print(np_baseball.shape)  # Se imprime la forma (shape) del arreglo 'np_baseball'.