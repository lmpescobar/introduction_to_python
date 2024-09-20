# Ejercicio
# Comparación entre media y mediana

# Descripción
# Ahora sabes cómo usar las funciones de numpy para tener una mejor idea de tus datos.
# Los datos de béisbol están disponibles como un arreglo numpy 2D con 3 columnas (altura, peso, edad) y 1015 filas.
# El nombre de este arreglo numpy es 'np_baseball'. 

# Después de reestructurar los datos, sin embargo, te das cuenta de que algunos valores de altura son anormalmente
# altos. Sigue las instrucciones y descubre qué estadística descriptiva se adapta mejor si estás tratando con
# valores atípicos (outliers).

# Instrucciones
# 1. Crea un arreglo numpy, 'np_height_in', que sea igual a la primera columna de 'np_baseball'.
# 2. Imprime la media de 'np_height_in'.
# 3. Imprime la mediana de 'np_height_in'.

# Código en Python

# Importar numpy como np
import numpy as np  # Se importa el paquete numpy con el alias 'np'.

# Generar datos de ejemplo utilizando distribución normal
np.random.seed(42)  # Fijar la semilla para reproducibilidad

# Generar alturas (en pulgadas) y pesos (en libras) simulados para 1015 jugadores
heights = np.round(np.random.normal(70, 5, 1015), 2)  # Media 70 pulgadas, desviación estándar 5, 1015 jugadores
weights = np.round(np.random.normal(200, 20, 1015), 2)  # Media 200 libras, desviación estándar 20, 1015 jugadores
ages = np.random.randint(20, 40, 1015)  # Edad aleatoria entre 20 y 40 años

# Combinar alturas, pesos y edades en un arreglo numpy 2D
np_baseball = np.column_stack((heights, weights, ages))  # Crear un arreglo numpy 2D con altura, peso y edad

# Crear np_height_in desde np_baseball (primera columna)
np_height_in = np_baseball[:, 0]  # Se selecciona la primera columna que contiene las alturas

# Imprimir la media de np_height_in
print(np.mean(np_height_in))  # Imprimir la media de las alturas

# Imprimir la mediana de np_height_in
print(np.median(np_height_in))  # Imprimir la mediana de las alturas