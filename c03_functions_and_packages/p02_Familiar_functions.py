# Ejercicio
# Funciones familiares

# Descripción
# Python ofrece un montón de funciones integradas para facilitarte la vida como científico de datos.
# Ya conoces dos de estas funciones: print() y type(). También existen funciones como str(), int(), 
# bool() y float() para cambiar entre tipos de datos. Puedes obtener más información sobre estas funciones aquí.

# Llamar a una función es sencillo. Para obtener el tipo de 3.0 y almacenar el resultado como una nueva variable 'result', 
# puedes usar lo siguiente:
# result = type(3.0)

# Instrucciones
# 1. Usa print() en combinación con type() para imprimir el tipo de 'var1'.
# 2. Usa len() para obtener la longitud de la lista 'var1'. Envuélvelo en una llamada a print() para imprimirlo directamente.
# 3. Usa int() para convertir 'var2' a un entero. Almacena la salida como 'out2'.

# Código en Python

# Crear variables 'var1' y 'var2'
var1 = [1, 2, 3, 4]  # Se crea una lista de enteros y se asigna a 'var1'.
var2 = True          # Se crea un valor booleano y se asigna a 'var2'.

# Imprimir el tipo de 'var1'
print(type(var1))  # Se imprime el tipo de la variable 'var1' usando type().

# Imprimir la longitud de 'var1'
print(len(var1))  # Se imprime la longitud de la lista 'var1' usando len().

# Convertir 'var2' a un entero: 'out2'
out2 = int(var2)  # Se convierte el valor booleano 'var2' a un entero y se almacena en 'out2'.

# Imprimir 'out2'
print(out2)  # Se imprime el valor de 'out2' después de la conversión.