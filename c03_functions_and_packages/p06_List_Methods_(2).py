# Ejercicio
# Métodos de listas (2)

# Descripción
# La mayoría de los métodos de lista cambiarán la lista a la que se aplican. Algunos ejemplos son:
# - .append(), que agrega un elemento a la lista en la que se llama.
# - .remove(), que elimina el primer elemento de una lista que coincide con la entrada.
# - .reverse(), que invierte el orden de los elementos en la lista en la que se llama.

# Trabajarás con la lista que contiene las áreas de diferentes partes de la casa: 'areas'.

# Instrucciones
# 1. Usa .append() dos veces para agregar el tamaño de la casa con piscina y el garaje de nuevo: 
#    24.5 y 15.45, respectivamente. Asegúrate de agregarlos en este orden.
# 2. Imprime 'areas'.
# 3. Usa el método .reverse() para invertir el orden de los elementos en 'areas'.
# 4. Imprime 'areas' una vez más.

# Código en Python

# Crear la lista 'areas'
areas = [11.25, 18.0, 20.0, 10.75, 9.50]  # Se crea una lista con las áreas de las habitaciones.

# Usar append() dos veces para agregar los tamaños de la casa con piscina y el garaje
areas.append(24.5)  # Se agrega el tamaño de la casa con piscina al final de la lista.
areas.append(15.45)  # Se agrega el tamaño del garaje al final de la lista.

# Imprimir 'areas'
print(areas)  # Se imprime la lista 'areas' con los elementos añadidos.

# Invertir el orden de los elementos en 'areas'
areas.reverse()  # Se invierte el orden de los elementos en la lista 'areas'.

# Imprimir 'areas' nuevamente
print(areas)  # Se imprime la lista 'areas' después de invertir su orden.