# Ejercicio
# Tu primer arreglo NumPy

# Descripción
# Ahora vas a adentrarte en el mundo del béisbol. A lo largo del camino, te familiarizarás con 
# lo básico de numpy, un paquete poderoso para hacer ciencia de datos.

# Se ha definido una lista 'baseball' en el script de Python, que representa la altura de algunos 
# jugadores de béisbol en centímetros. ¿Puedes agregar algún código para crear un arreglo numpy a partir de ella?

# Instrucciones
# 1. Importa el paquete numpy como 'np', para que puedas referirte a numpy con 'np'.
# 2. Usa np.array() para crear un arreglo numpy desde 'baseball'. Nombra este arreglo 'np_baseball'.
# 3. Imprime el tipo de 'np_baseball' para verificar que lo hiciste correctamente.

# Código en Python

# Importar el paquete numpy como np
import numpy as np  # Se importa el paquete numpy y se le asigna el alias 'np' para usarlo más fácilmente.

# Lista de alturas de jugadores de béisbol en centímetros
baseball = [180, 215, 210, 210, 188, 176, 209, 200]  # Lista con las alturas de los jugadores.

# Crear un arreglo numpy desde 'baseball': np_baseball
np_baseball = np.array(baseball)  # Se convierte la lista 'baseball' en un arreglo numpy y se almacena en 'np_baseball'.

# Imprimir el tipo de 'np_baseball'
print(type(np_baseball))  # Se imprime el tipo de 'np_baseball' para verificar que es un arreglo numpy.