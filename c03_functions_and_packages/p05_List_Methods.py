# Ejercicio
# Métodos de listas (List Methods)

# Descripción
# Las cadenas no son los únicos tipos de Python que tienen métodos asociados. Las listas, flotantes, 
# enteros y booleanos también son tipos que vienen con un montón de métodos útiles. En este ejercicio,
# experimentarás con:

# .index(), para obtener el índice del primer elemento de una lista que coincide con su entrada.
# .count(), para obtener el número de veces que un elemento aparece en una lista.

# Trabajarás con la lista que contiene las áreas de diferentes partes de una casa: 'areas'.

# Instrucciones
# 1. Usa el método .index() para obtener el índice del elemento en 'areas' que es igual a 20.0.
#    Imprime este índice.
# 2. Llama al método .count() en 'areas' para averiguar cuántas veces aparece 9.50 en la lista.
#    Nuevamente, simplemente imprime este número.

# Código en Python

# Crear la lista 'areas'
areas = [11.25, 18.0, 20.0, 10.75, 9.50]  # Se crea una lista con las áreas de las habitaciones.

# Imprimir el índice del elemento 20.0
print(areas.index(20.0))  # Se imprime el índice donde aparece el valor 20.0 en la lista 'areas'.

# Imprimir cuántas veces aparece 9.50 en 'areas'
print(areas.count(9.50))  # Se cuenta cuántas veces aparece el valor 9.50 en la lista 'areas' y se imprime.