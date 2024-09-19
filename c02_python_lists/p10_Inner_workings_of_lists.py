# Ejercicio
# Funcionamiento interno de las listas

# Descripción
# Se te ha proporcionado parte del código para este ejercicio: una lista con el nombre 'areas' 
# y una copia llamada 'areas_copy'.

# Actualmente, se cambia el primer elemento de 'areas_copy' y se imprime la lista 'areas'.
# Si presionas el botón para ejecutar el código, verás que, aunque cambiaste 'areas_copy', 
# el cambio también se refleja en la lista 'areas'. Esto se debe a que 'areas' y 'areas_copy' 
# apuntan a la misma lista.

# Si deseas evitar que los cambios en 'areas_copy' también afecten a 'areas', tendrás que hacer 
# una copia explícita de la lista 'areas' usando 'list()' o con [:].

# Instrucciones
# 1. Cambia el segundo comando, que crea la variable 'areas_copy', para que 'areas_copy' sea 
#    una copia explícita de 'areas'. Después de hacer esto, los cambios en 'areas_copy' no 
#    deberían afectar a 'areas'. Envía la respuesta para verificar esto.

# Código en Python

# Crear la lista 'areas'
areas = [11.25, 18.0, 20.0, 10.75, 9.50]  # Se crea la lista original con los valores de las áreas.

# Cambiar este comando
areas_copy = list(areas)  # Se hace una copia explícita de la lista 'areas' usando list().

# Cambiar 'areas_copy'
areas_copy[0] = 5.0  # Se cambia el primer elemento de 'areas_copy' a 5.0.

# Imprimir 'areas'
print(areas)  # Se imprime la lista original 'areas' para verificar que no se haya modificado.