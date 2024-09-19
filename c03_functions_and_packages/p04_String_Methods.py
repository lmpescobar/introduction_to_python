# Ejercicio
# Métodos de cadenas (String Methods)

# Descripción
# Las cadenas de texto (strings) vienen con una serie de métodos. Sigue las instrucciones de cerca 
# para descubrir algunos de ellos. Si quieres conocer más en detalle, siempre puedes escribir 
# help(str) en la consola de IPython.

# Se ha creado una cadena de texto 'place' para que experimentes con ella.

# Instrucciones
# 1. Usa el método .upper() en 'place' y guarda el resultado en 'place_up'. Usa la sintaxis 
#    para llamar a métodos que aprendiste en el video anterior.
# 2. Imprime 'place' y 'place_up'. ¿Ambos cambiaron?
# 3. Imprime el número de letras 'o' en la variable 'place' llamando a .count() en 'place' y pasando 
#    la letra "o" como entrada del método. Estamos hablando de la variable 'place', ¡no de la palabra "Place"!

# Código en Python

# Cadena de texto para experimentar: place
place = "poolhouse"  # Se asigna la cadena de texto "poolhouse" a la variable 'place'.

# Usar el método upper() en 'place'
place_up = place.upper()  # Se convierte 'place' a mayúsculas y se guarda en 'place_up'.

# Imprimir 'place' y 'place_up'
print(place)      # Se imprime la cadena original 'place'.
print(place_up)   # Se imprime la cadena 'place_up' en mayúsculas.

# Imprimir el número de "o" en 'place'
print(place.count("o"))  # Se cuenta el número de veces que aparece la letra "o" en 'place'.