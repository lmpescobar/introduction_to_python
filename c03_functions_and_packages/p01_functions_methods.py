# Ejercicio
# Explicación sobre funciones y métodos en Python.

# Instrucciones
# 1. Definir qué son las funciones y métodos.
# 2. Explicar la diferencia entre ambos.
# 3. Proporcionar ejemplos claros y prácticos para ilustrar ambos conceptos.

# Funciones en Python

# Una función es un bloque de código reutilizable que realiza una tarea específica.
# Puede recibir parámetros y devolver un valor. Se define utilizando la palabra clave 'def'.

# Código en Python
def suma(a, b):
    # Devuelve la suma de los dos parámetros a y b
    return a + b

# Llamada a la función suma con los argumentos 3 y 5
resultado = suma(3, 5)
print("Resultado de la función suma:", resultado)  # Imprime 8

# Métodos en Python

# Un método es similar a una función, pero está asociado a un objeto específico.
# Se define dentro de una clase y opera sobre instancias de esa clase.

# Código en Python
class Circulo:
    # Método de inicialización que define el radio del círculo
    def __init__(self, radio):
        # Asigna el valor del radio al atributo de la instancia
        self.radio = radio

    # Método para calcular el área del círculo
    def area(self):
        # Calcula y devuelve el área del círculo
        return 3.1416 * (self.radio ** 2)

# Creación de un objeto de la clase Circulo con un radio de 5
mi_circulo = Circulo(5)
# Llamada al método area() para calcular el área del círculo
area_circulo = mi_circulo.area()
print("Área del círculo:", area_circulo)  # Imprime 78.54

# Diferencias clave entre funciones y métodos:
# 1. Función: se utiliza de manera independiente y se define con 'def' fuera de cualquier clase.
#    Ejemplo: print(), suma()
# 2. Método: se utiliza en relación con un objeto o clase y se define dentro de una clase.
#    Ejemplo: mi_circulo.area()