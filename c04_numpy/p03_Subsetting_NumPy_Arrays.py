# Ejercicio 
# Subconjuntos de arreglos NumPy

# Descripción
# Obtener subconjuntos (usando la notación de corchetes en listas o arreglos) funciona exactamente igual 
# con listas y arreglos.

# Este ejercicio ya tiene dos listas, 'height_in' y 'weight_lb', cargadas en segundo plano para ti. 
# Estas contienen la altura y el peso de los jugadores de la MLB como listas regulares de Python. 
# También hay dos arreglos de numpy, 'np_weight_lb' y 'np_height_in' preparados para ti.

# Instrucciones
# 1. Obtén un subconjunto de 'np_weight_lb' imprimiendo el elemento en el índice 50.
# 2. Imprime un subarreglo de 'np_height_in' que contenga los elementos desde el índice 100 hasta 
#    e incluyendo el índice 110.

# Código en Python

# Importar numpy como np
import numpy as np  # Se importa el paquete numpy con el alias 'np'.

# Listas de alturas y pesos de jugadores de béisbol en pulgadas y libras (valores de ejemplo, extendidos)
height_in = [74, 74, 72, 75, 75, 73, 75, 76, 74, 72, 70, 76, 76, 73, 72, 74, 74, 73, 72, 74,
             75, 76, 75, 75, 73, 73, 75, 74, 74, 72, 72, 73, 75, 74, 75, 75, 76, 76, 75, 75,
             73, 73, 75, 74, 74, 72, 70, 76, 76, 73, 74, 75, 76, 76, 75, 75, 75, 74, 75, 74,
             75, 75, 76, 75, 74, 74, 73, 72, 74, 75, 76, 75, 75, 74, 74, 75, 75, 76, 75, 75,
             73, 72, 74, 75, 75, 76, 75, 75, 75, 74, 75, 74, 75, 76, 76, 75, 75, 75, 74, 75,
             74, 75, 72, 74, 74, 76, 76, 74, 75, 75, 75, 73, 73, 75, 74, 75, 74, 74, 73, 75,
             72, 74, 76, 74, 73, 75, 74, 75, 76, 76, 75, 75, 75, 75, 73, 75, 74, 74, 75, 75, 
             76, 75, 74, 75, 75, 75, 75, 76, 75, 75, 73, 74, 75, 75, 73, 74, 75, 75, 76, 75]

weight_lb = [180, 215, 210, 210, 188, 176, 209, 200, 188, 180, 185, 195, 200, 210, 187, 180,
             188, 200, 210, 190, 200, 200, 210, 210, 180, 170, 210, 195, 200, 180, 185, 200,
             210, 195, 210, 210, 215, 210, 210, 220, 210, 180, 200, 190, 188, 200, 185, 210,
             210, 200, 195, 210, 210, 200, 210, 210, 210, 210, 220, 210, 210, 220, 200, 210,
             210, 210, 215, 210, 210, 210, 210, 190, 210, 210, 215, 210, 210, 210, 210, 215,
             210, 210, 210, 200, 210, 210, 215, 210, 210, 210, 210, 210, 215, 210, 220, 210,
             210, 210, 210, 220, 210, 210, 210, 220, 210, 210, 220, 210, 210, 210, 220, 210,
             180, 200, 190, 188, 200, 185, 210, 210, 200, 195, 210, 210, 200, 210, 210, 210]

# Crear los arreglos numpy desde las listas
np_weight_lb = np.array(weight_lb)  # Se crea un arreglo numpy a partir de la lista 'weight_lb'.
np_height_in = np.array(height_in)  # Se crea un arreglo numpy a partir de la lista 'height_in'.

# Verificar si hay suficientes elementos en np_height_in
if len(np_height_in) > 110:
    # Imprimir un subarreglo de np_height_in: desde el índice 100 hasta e incluyendo el índice 110
    print(np_height_in[100:111])  # Se imprime un subarreglo que incluye elementos desde el índice 100 hasta el 110.
else:
    print("El arreglo np_height_in no tiene suficientes elementos para el rango de índices 100:110.")

# Imprimir el peso en el índice 50
print(np_weight_lb[50])  # Se imprime el valor del peso en la posición 50 de 'np_weight_lb'.