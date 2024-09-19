# Ejercicio
# Operaciones con otros tipos de datos

# Descripción
# Las variables en Python pueden tener diferentes tipos de datos. Puedes ver el tipo de una variable usando type().
# Por ejemplo, para ver el tipo de 'a', ejecuta: type(a).
# Los diferentes tipos se comportan de manera distinta en Python. Cuando sumas dos cadenas de texto (strings),
# obtendrás un comportamiento diferente que cuando sumas dos enteros o dos valores booleanos.
# Es momento de probar esto.

# Instrucciones 1/2
# 1. Suma 'savings' y 'new_savings' y asígnalo a 'total_savings'.
# 2. Usa type() para imprimir el tipo de dato resultante de 'total_savings'.

# Código en Python

# Crear variables iniciales
savings = 100          # Se asigna el valor entero 100 a la variable 'savings'.
new_savings = 40       # Se asigna el valor entero 40 a la variable 'new_savings'.

# Calcular 'total_savings' usando 'savings' y 'new_savings'
total_savings = savings + new_savings  # Se suman 'savings' y 'new_savings' y el resultado se asigna a 'total_savings'.

# Imprimir 'total_savings'
print(total_savings)   # Se imprime el valor de 'total_savings'.

# Imprimir el tipo de 'total_savings'
print(type(total_savings))  # Se imprime el tipo de dato de 'total_savings' usando la función type().

# Instrucciones 2/2
# 1. Calcula la suma de 'intro' y 'intro' y asígnala a 'doubleintro'.
# 2. Imprime 'doubleintro'. ¿Esperabas este resultado?

# Código en Python

# Crear una variable de cadena de texto
intro = "Hello! How are you?"  # Se asigna el valor de la cadena de texto a la variable 'intro'.

# Asignar la suma de 'intro' e 'intro' a 'doubleintro'
doubleintro = intro + intro  # Se concatenan dos veces el valor de 'intro' y se asigna a 'doubleintro'.

# Imprimir 'doubleintro'
print(doubleintro)  # Se imprime el valor de 'doubleintro', que es la concatenación de la cadena 'intro' dos veces.