# Ejercicio
# Importar paquetes

# Descripción
# Supongamos que deseas calcular la circunferencia y el área de un círculo. Estas son las fórmulas:
# Circunferencia: C = 2 * π * r
# Área: A = π * r^2
# En lugar de escribir el número para π, puedes usar el paquete 'math' que contiene el número.

# Como referencia, ** es el símbolo para exponenciación. Por ejemplo, 3**4 es 3 elevado a la potencia 
# de 4 y dará 81.

# Instrucciones
# 1. Importa el paquete 'math'.
# 2. Usa math.pi para calcular la circunferencia del círculo y almacénalo en 'C'.
# 3. Usa math.pi para calcular el área del círculo y almacénalo en 'A'.

# Código en Python

# Importar el paquete 'math'
import math  # Se importa el paquete 'math' para usar funciones matemáticas como 'pi'.

# Calcular la circunferencia C
C = 2 * 0.43 * math.pi  # Se calcula la circunferencia usando la fórmula C = 2 * π * r.

# Calcular el área A
A = math.pi * 0.43 ** 2  # Se calcula el área usando la fórmula A = π * r^2.

# Imprimir la circunferencia
print("Circumference: " + str(C))  # Se imprime el valor de la circunferencia.

# Imprimir el área
print("Area: " + str(A))  # Se imprime el valor del área.