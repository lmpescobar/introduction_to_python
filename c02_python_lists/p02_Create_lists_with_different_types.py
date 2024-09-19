# Ejercicio
# Crear listas con diferentes tipos de datos

# Descripción
# Aunque no es muy común, una lista también puede contener una mezcla de tipos de datos en Python,
# incluyendo cadenas de texto (strings), valores flotantes (floats) y booleanos (bool).
# Ahora vas a agregar los nombres de las habitaciones a tu lista, para que puedas ver 
# tanto el nombre de la habitación como su tamaño juntos.

# Parte del código ha sido proporcionado para ayudarte a comenzar. ¡Presta atención aquí!
# "bathroom" es una cadena de texto, mientras que bath es una variable que representa 
# el valor flotante 9.50, que definiste anteriormente.

# Instrucciones
# 1. Completa el código que crea la lista 'areas'. Construye la lista de manera que contenga 
#    primero el nombre de cada habitación como una cadena de texto y luego su área. 
#    En otras palabras, agrega las cadenas de texto "hallway", "kitchen" y "bedroom" 
#    en las ubicaciones apropiadas.
# 2. Imprime 'areas' de nuevo con la función print(). ¿Es la salida más informativa esta vez?

# Código en Python

# Áreas de las habitaciones de la casa
hall = 11.25  # Área del pasillo en metros cuadrados.
kit = 18.0    # Área de la cocina en metros cuadrados.
liv = 20.0    # Área de la sala de estar en metros cuadrados.
bed = 10.75   # Área del dormitorio en metros cuadrados.
bath = 9.50   # Área del baño en metros cuadrados.

# Adaptar la lista 'areas'
areas = ["hallway", hall, "kitchen", kit, "living room", liv, "bedroom", bed, "bathroom", bath]  
# Se crea una lista que incluye los nombres y las áreas de las habitaciones en el orden especificado.

# Imprimir la lista 'areas'
print(areas)  # Se imprime la lista de áreas con los nombres de las habitaciones.