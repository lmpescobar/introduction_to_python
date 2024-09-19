# Ejercicio
# Reemplazar elementos de la lista

# Descripción
# Para reemplazar elementos de una lista, obtén un subconjunto de la lista y asigna nuevos valores 
# a ese subconjunto. Puedes seleccionar elementos individuales o puedes cambiar listas enteras a la vez.
# Para este y los siguientes ejercicios, continuarás trabajando con la lista 'areas' que contiene 
# los nombres y áreas de diferentes habitaciones de una casa.

# Instrucciones
# 1. Actualiza el área del baño a 10.50 metros cuadrados en lugar de 9.50 usando índice negativo.
# 2. Haz la lista 'areas' más moderna. Cambia "living room" a "chill zone". No uses indexación negativa esta vez.

# Código en Python

# Crear la lista 'areas'
areas = ["hallway", 11.25, "kitchen", 18.0, "living room", 20.0, "bedroom", 10.75, "bathroom", 9.50]
# Se crea una lista con los nombres y las áreas de las habitaciones en el orden especificado.

# Corregir el área del baño
areas[-1] = 10.50  # Se actualiza el último elemento de la lista a 10.50.

# Cambiar "living room" a "chill zone"
areas[4] = "chill zone"  # Se actualiza el nombre "living room" a "chill zone" en la posición 4.

# Imprimir la lista actualizada
print(areas)  # Se imprime la lista actualizada con los cambios realizados.