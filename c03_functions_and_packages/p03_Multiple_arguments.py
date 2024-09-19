# Ejercicio
# Múltiples argumentos

# Descripción
# En el ejercicio anterior, identificaste argumentos opcionales viendo la documentación con help(). 
# Ahora aplicarás esto para cambiar el comportamiento de la función sorted().

# Echa un vistazo a la documentación de sorted() escribiendo help(sorted) en la consola de IPython.
# Verás que sorted() toma tres argumentos: iterable, key y reverse.
# En este ejercicio, solo tendrás que especificar iterable y reverse, no key.

# Se han creado dos listas para ti.
# ¿Puedes unirlas y ordenarlas en orden descendente?

# Instrucciones
# 1. Usa '+' para combinar el contenido de 'first' y 'second' en una nueva lista llamada 'full'.
# 2. Llama a sorted() en 'full' y especifica el argumento reverse como True.
#    Guarda la lista ordenada como 'full_sorted'.
# 3. Termina imprimiendo 'full_sorted'.

# Código en Python

# Crear listas 'first' y 'second'
first = [11.25, 18.0, 20.0]  # Se crea la lista 'first' con tres elementos flotantes.
second = [10.75, 9.50]       # Se crea la lista 'second' con dos elementos flotantes.

# Combinar 'first' y 'second' en una lista: 'full'
full = first + second  # Se combinan las dos listas usando el operador '+'.

# Ordenar 'full' en orden descendente: 'full_sorted'
full_sorted = sorted(full, reverse=True)  # Se usa sorted() para ordenar la lista en orden descendente.

# Imprimir 'full_sorted'
print(full_sorted)  # Se imprime la lista ordenada 'full_sorted'.