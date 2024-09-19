# Ejercicio
# Lista de listas

# Descripción
# Como científico de datos, a menudo trabajarás con muchos datos, y tendrá sentido agrupar
# algunos de estos datos.
# En lugar de crear una lista que contenga cadenas de texto y valores flotantes, representando 
# los nombres y las áreas de las habitaciones de tu casa, puedes crear una lista de listas.

# Recuerda: "hallway" es una cadena de texto, mientras que 'hall' es una variable 
# que representa el valor flotante 11.25 que especificaste anteriormente.

# Instrucciones
# 1. Completa la lista de listas para que también contenga los datos del dormitorio y el baño.
#    Asegúrate de ingresar estos valores en el orden correcto.
# 2. Imprime 'house'; ¿tiene más sentido estructurar los datos de esta manera?

# Código en Python

# Áreas de las habitaciones de la casa
hall = 11.25  # Área del pasillo en metros cuadrados.
kit = 18.0    # Área de la cocina en metros cuadrados.
liv = 20.0    # Área de la sala de estar en metros cuadrados.
bed = 10.75   # Área del dormitorio en metros cuadrados.
bath = 9.50   # Área del baño en metros cuadrados.

# Información de la casa como lista de listas
house = [["hallway", hall],  # Se crea una lista con el nombre y área del pasillo.
         ["kitchen", kit],   # Se añade una lista con el nombre y área de la cocina.
         ["living room", liv],  # Se añade una lista con el nombre y área de la sala de estar.
         ["bedroom", bed],   # Se añade una lista con el nombre y área del dormitorio.
         ["bathroom", bath]]  # Se añade una lista con el nombre y área del baño.

# Imprimir la lista 'house'
print(house)  # Se imprime la lista de listas que contiene los datos de las habitaciones.