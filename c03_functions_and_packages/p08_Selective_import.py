# Ejercicio
# Importación selectiva

# Descripción
# Las importaciones generales, como import math, hacen que toda la funcionalidad del paquete 'math' 
# esté disponible para ti. Sin embargo, si decides usar solo una parte específica de un paquete, 
# siempre puedes hacer tu importación más selectiva.

# Ejemplo:
# from math import pi

# Intenta lo mismo otra vez, pero esta vez solo usa 'pi'.

# Instrucciones
# 1. Realiza una importación selectiva desde el paquete 'math' donde solo importes la función 'pi'.
# 2. Usa 'pi' para calcular la circunferencia del círculo y almacénala en 'C'.
# 3. Usa 'pi' para calcular el área del círculo y almacénala en 'A'.

# Código en Python

# Importar la función 'pi' del paquete 'math'
from math import pi  # Se importa solo la constante 'pi' del paquete 'math'.

# Calcular la circunferencia C
C = 2 * 0.43 * pi  # Se calcula la circunferencia usando la fórmula C = 2 * π * r.

# Calcular el área A
A = pi * 0.43 ** 2  # Se calcula el área usando la fórmula A = π * r^2.

# Imprimir la circunferencia
print("Circumference: " + str(C))  # Se imprime el valor de la circunferencia.

# Imprimir el área
print("Area: " + str(A))  # Se imprime el valor del área.