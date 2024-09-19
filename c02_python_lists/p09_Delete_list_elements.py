# Ejercicio
# Eliminar elementos de una lista

# Descripción
# Finalmente, también puedes eliminar elementos de tu lista. Puedes hacerlo con la declaración 'del'.

# Ejemplo:
# x = ["a", "b", "c", "d"]
# del x[1]
# Esto eliminaría el elemento en la posición 1, que es "b", de la lista 'x'.

# Presta atención aquí: tan pronto como elimines un elemento de una lista, los índices de los elementos
# que vienen después del elemento eliminado cambiarán.

# Desafortunadamente, el monto que ganaste en la lotería no es tan grande después de todo y parece que 
# la casa con piscina no va a suceder. Tendrás que eliminarla de la lista. Decides eliminar la cadena 
# correspondiente y el valor flotante de la lista 'areas'.

# Instrucciones
# 1. Elimina la cadena de texto y el valor flotante correspondientes a "poolhouse" de la lista 'areas'.
# 2. Imprime la lista actualizada 'areas'.

# Código en Python

# Crear la lista 'areas'
areas = ["hallway", 11.25, "kitchen", 18.0, "chill zone", 20.0, "bedroom", 10.75, 
         "bathroom", 10.50, "poolhouse", 24.5, "garage", 15.45]
# Se crea una lista con los nombres y las áreas de las habitaciones en el orden especificado, incluyendo la casa con piscina y el garaje.

# Eliminar los elementos correspondientes a 'poolhouse' de la lista
del areas[10:12]  # Se eliminan los elementos en las posiciones 10 y 11, que corresponden a "poolhouse" y su área (24.5).

# Imprimir la lista actualizada
print(areas)  # Se imprime la lista 'areas' actualizada sin "poolhouse".