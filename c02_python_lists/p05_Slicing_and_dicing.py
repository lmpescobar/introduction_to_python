# Ejercicio
# Rebanado y troceado (Slicing and dicing)

# Descripción
# Seleccionar valores únicos de una lista es solo una parte de la historia. También es posible 
# "rebanar" (slice) tu lista, lo que significa seleccionar múltiples elementos de la lista.
# Usa la siguiente sintaxis:
# my_list[start:end]
# El índice 'start' será incluido, mientras que el índice 'end' no lo será. Sin embargo, también 
# es posible no especificar estos índices. Si no especificas el índice 'start', Python asumirá 
# que deseas comenzar a rebanar desde el principio de la lista.

# Instrucciones
# 1. Usa rebanado (slicing) para crear 'downstairs', que contiene los primeros 6 elementos de 'areas'.
# 2. Crea 'upstairs', como los últimos 4 elementos de 'areas'. Esta vez, simplifica el rebanado
#    omitiendo el índice 'end'.
# 3. Imprime tanto 'downstairs' como 'upstairs' usando print().

# Código en Python

# Crear la lista 'areas'
areas = ["hallway", 11.25, "kitchen", 18.0, "living room", 20.0, "bedroom", 10.75, "bathroom", 9.50]
# Se crea una lista con los nombres y las áreas de las habitaciones en el orden especificado.

# Usar rebanado para crear 'downstairs'
downstairs = areas[:6]  # Se seleccionan los primeros 6 elementos de la lista 'areas'.

# Usar rebanado para crear 'upstairs'
upstairs = areas[6:]  # Se seleccionan los últimos 4 elementos de la lista 'areas', omitiendo el índice 'end'.

# Imprimir 'downstairs' y 'upstairs'
print(downstairs)  # Se imprime la lista 'downstairs' con los primeros 6 elementos de 'areas'.
print(upstairs)    # Se imprime la lista 'upstairs' con los últimos 4 elementos de 'areas'.