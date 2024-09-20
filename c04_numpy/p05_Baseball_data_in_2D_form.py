# Ejercicio
# Datos de béisbol en forma 2D

# Descripción
# Te das cuenta de que tiene más sentido reestructurar toda esta información en un arreglo numpy 2D.

# Tienes una lista de listas de Python. En esta lista de listas, cada sublista representa la altura y el peso 
# de un solo jugador de béisbol. El nombre de esta lista es 'baseball' y ya ha sido cargada para ti 
# (aunque no puedas verla).

# Almacena los datos como un arreglo 2D para desbloquear la funcionalidad adicional de numpy.

# Instrucciones
# 1. Usa np.array() para crear un arreglo numpy 2D a partir de 'baseball'. Nombra este arreglo 'np_baseball'.
# 2. Imprime el atributo 'shape' de 'np_baseball' para mostrar las dimensiones del arreglo.

# Código en Python

# Importar numpy como np
import numpy as np  # Se importa el paquete numpy con el alias 'np'.

# Lista de listas que contiene altura y peso de jugadores de béisbol
baseball = [
    [180, 78.4],  # Datos del primer jugador: altura en cm, peso en kg.
    [215, 102.7], # Datos del segundo jugador.
    [210, 98.5],  # Datos del tercer jugador.
    [188, 75.2],  # Datos del cuarto jugador.
    [190, 82.1],  # Datos del quinto jugador.
    [205, 99.3],  # Datos del sexto jugador.
    [200, 95.1],  # Datos del séptimo jugador.
    [185, 80.5],  # Datos del octavo jugador.
    [195, 89.4],  # Datos del noveno jugador.
    [210, 99.9]   # Datos del décimo jugador.
]

# Crear un arreglo numpy 2D desde 'baseball': np_baseball
np_baseball = np.array(baseball)  # Se crea un arreglo numpy 2D a partir de la lista 'baseball'.

# Imprimir la forma (shape) de np_baseball
print(np_baseball.shape)  # Se imprime la forma del arreglo 'np_baseball', que indica el número de filas y columnas.