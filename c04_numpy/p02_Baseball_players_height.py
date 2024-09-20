# Ejercicio
# Altura de los jugadores de béisbol

# Descripción
# Eres un gran fanático del béisbol. Decides llamar a la MLB (Major League Baseball) y preguntar 
# algunas estadísticas más sobre la altura de los jugadores principales. Te pasan datos sobre 
# más de mil jugadores, que se almacenan como una lista regular de Python: 'height_in'. 
# La altura se expresa en pulgadas. ¿Puedes crear un arreglo numpy a partir de ella y convertir 
# las unidades a metros?

# La lista 'height_in' ya está disponible y el paquete numpy está cargado, así que puedes comenzar de inmediato.
# (Fuente: stat.ucla.edu).

# Instrucciones
# 1. Crea un arreglo numpy desde 'height_in'. Nombra este nuevo arreglo 'np_height_in'.
# 2. Imprime 'np_height_in'.
# 3. Multiplica 'np_height_in' por 0.0254 para convertir todas las medidas de altura de pulgadas a metros.
#    Almacena los nuevos valores en un nuevo arreglo, 'np_height_m'.
# 4. Imprime 'np_height_m' y verifica que la salida tenga sentido.

# Código en Python

# Importar el paquete numpy como np
import numpy as np  # Se importa el paquete numpy con el alias 'np'.

# Lista de alturas de jugadores de béisbol en pulgadas
height_in = [74, 74, 72, 75, 75, 73, 75, 76, 74, 72, 70, 76, 76, 73, 72, 74, 74, 73, 72, 74, 75, 76, 75, 75, 73, 73, 75, 74, 74, 72]

# Crear un arreglo numpy desde 'height_in': np_height_in
np_height_in = np.array(height_in)  # Se convierte la lista 'height_in' en un arreglo numpy.

# Imprimir np_height_in
print(np_height_in)  # Se imprime el arreglo numpy 'np_height_in' que contiene las alturas en pulgadas.

# Convertir np_height_in a metros: np_height_m
np_height_m = np_height_in * 0.0254  # Se multiplica cada valor por 0.0254 para convertirlo a metros.

# Imprimir np_height_m
print(np_height_m)  # Se imprime el arreglo numpy 'np_height_m' que contiene las alturas en metros.