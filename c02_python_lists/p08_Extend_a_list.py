# Ejercicio
# Extender una lista

# Descripción
# Si puedes cambiar elementos en una lista, seguramente también querrás poder agregar elementos a ella, ¿verdad?
# Puedes usar el operador '+'.

# Ejemplo:
# x = ["a", "b", "c", "d"]
# y = x + ["e", "f"]
# Ahora la lista 'y' es ["a", "b", "c", "d", "e", "f"].

# ¡Acabas de ganar la lotería, increíble! Decides construir una casa con piscina y un garaje.
# ¿Puedes agregar esta información a la lista 'areas'?

# Instrucciones
# 1. Usa el operador '+' para agregar la lista ["poolhouse", 24.5] al final de la lista 'areas'.
#    Almacena el resultado en una nueva lista llamada 'areas_1'.
# 2. Extiende aún más 'areas_1' agregando datos sobre tu garaje. Agrega la cadena de texto 
#    "garage" y el flotante 15.45. Nombra la lista resultante 'areas_2'.

# Código en Python

# Crear la lista 'areas' y realizar algunos cambios
areas = ["hallway", 11.25, "kitchen", 18.0, "chill zone", 20.0, "bedroom", 10.75, "bathroom", 10.50]
# Se crea una lista con los nombres y las áreas de las habitaciones en el orden especificado, actualizada.

# Agregar datos de la casa con piscina a 'areas', nueva lista es 'areas_1'
areas_1 = areas + ["poolhouse", 24.5]  # Se agrega la casa con piscina al final de la lista 'areas'.

# Agregar datos del garaje a 'areas_1', nueva lista es 'areas_2'
areas_2 = areas_1 + ["garage", 15.45]  # Se agrega el garaje al final de la lista 'areas_1'.

# Imprimir las listas actualizadas
print(areas_1)  # Se imprime la lista 'areas_1' que incluye la casa con piscina.
print(areas_2)  # Se imprime la lista 'areas_2' que incluye la casa con piscina y el garaje.