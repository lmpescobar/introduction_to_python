# Ejercicio
# Subconjuntos de listas de listas

# Descripción
# Una lista de Python también puede contener otras listas.
# Para obtener subconjuntos de listas de listas, puedes usar la misma técnica que antes: corchetes.
# Esto se vería algo así para una lista 'house':
# house[2][0]

# Instrucciones
# 1. Obtén un subconjunto de la lista 'house' para obtener el valor flotante 9.5.

# Código en Python

# Información de la casa como lista de listas
house = [["hallway", 11.25],   # Pasillo y su área
         ["kitchen", 18.0],    # Cocina y su área
         ["living room", 20.0],  # Sala de estar y su área
         ["bedroom", 10.75],   # Dormitorio y su área
         ["bathroom", 9.50]]   # Baño y su área

# Obtener un subconjunto de la lista 'house'
house[4][1]  # Se accede al elemento 1 de la sublista 4, que corresponde al área del baño (9.50).