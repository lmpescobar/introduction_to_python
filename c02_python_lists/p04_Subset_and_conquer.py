# Ejercicio
# Subconjuntos y conquistas

# Descripción
# Obtener subconjuntos de listas en Python es muy sencillo. Toma el siguiente ejemplo de código,
# que crea una lista 'x' y luego selecciona "b" de ella. Recuerda que este es el segundo elemento, 
# por lo que tiene el índice 1. También puedes usar índices negativos.

# Ejemplo:
# x = ["a", "b", "c", "d"]
# x[1]  # Devuelve "b"
# x[-3]  # ¡Mismo resultado!

# Recuerda la lista 'areas' del ejercicio anterior, que contiene tanto cadenas de texto como flotantes.
# Su definición ya está en el script. ¿Puedes agregar el código correcto para obtener algunos subconjuntos de 'areas'?

# Instrucciones
# 1. Imprime el segundo elemento de la lista 'areas' (tiene el valor 11.25).
# 2. Obtén e imprime el último elemento de 'areas', que es 9.50. Usar un índice negativo tiene sentido aquí.
# 3. Selecciona el número que representa el área de la sala de estar (20.0) e imprímelo.

# Código en Python

# Crear la lista 'areas'
areas = ["hallway", 11.25, "kitchen", 18.0, "living room", 20.0, "bedroom", 10.75, "bathroom", 9.50]  
# Se crea una lista con los nombres y las áreas de las habitaciones en el orden especificado.

# Imprimir el segundo elemento de la lista 'areas'
print(areas[1])  # Se imprime el segundo elemento de la lista, que es el área del pasillo (11.25).

# Imprimir el último elemento de la lista 'areas'
print(areas[-1])  # Se imprime el último elemento de la lista, que es el área del baño (9.50).

# Imprimir el área de la sala de estar
print(areas[5])  # Se imprime el área de la sala de estar (20.0).