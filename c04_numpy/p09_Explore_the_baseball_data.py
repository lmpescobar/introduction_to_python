# Ejercicio
# Explorando los datos de béisbol

# Descripción
# Debido a que la media y la mediana son tan diferentes, decides quejarte a la MLB. 
# Encuentran el error y te envían los datos corregidos. Ahora están disponibles como 
# un arreglo numpy 2D, 'np_baseball', con tres columnas: altura (en pulgadas), peso 
# (en libras) y edad (en años).

# El script de Python en el editor ya incluye el código para imprimir mensajes informativos
# con diferentes estadísticas resumidas sobre las alturas y pesos. 'np_baseball' está cargado 
# como 'numpy'. ¿Puedes completar el trabajo?

# Instrucciones
# 1. El código para imprimir la altura media ya está incluido. Completa el código para calcular 
#    la mediana de la altura. Reemplaza 'None' con el código correcto.
# 2. Usa np.std() en la primera columna de 'np_baseball' para calcular 'stddev'. Reemplaza 'None' 
#    con el código correcto.
# 3. ¿Los jugadores grandes tienden a ser más pesados? Usa 'np.corrcoef()' para almacenar la 
#    correlación entre la primera y la segunda columna de 'np_baseball' en 'corr'. 
#    Reemplaza 'None' con el código correcto.

# Código en Python

# Importar numpy como np
import numpy as np  # Se importa el paquete numpy con el alias 'np'.

# Generar datos corregidos de ejemplo para np_baseball
np.random.seed(42)  # Fijar la semilla para reproducibilidad

# Generar alturas (en pulgadas), pesos (en libras) y edades para 1015 jugadores de béisbol
heights_corrected = np.round(np.random.normal(70, 3, 1015), 2)  # Media 70 pulgadas, desviación estándar 3
weights_corrected = np.round(np.random.normal(180, 15, 1015), 2)  # Media 180 libras, desviación estándar 15
ages_corrected = np.random.randint(20, 40, 1015)  # Edad aleatoria entre 20 y 40 años

# Crear el arreglo numpy 2D con los datos corregidos
np_baseball = np.column_stack((heights_corrected, weights_corrected, ages_corrected))

# Calcular la media de la altura
avg = np.mean(np_baseball[:, 0])  # Media de la primera columna (alturas)
print("Average: " + str(avg))  # Imprimir la media de la altura

# Calcular la mediana de la altura
med = np.median(np_baseball[:, 0])  # Mediana de la primera columna (alturas)
print("Median: " + str(med))  # Imprimir la mediana de la altura

# Calcular la desviación estándar de la altura
stddev = np.std(np_baseball[:, 0])  # Desviación estándar de la primera columna (alturas)
print("Standard Deviation: " + str(stddev))  # Imprimir la desviación estándar de la altura

# Calcular la correlación entre altura y peso
corr = np.corrcoef(np_baseball[:, 0], np_baseball[:, 1])  # Correlación entre la primera y segunda columna
print("Correlation: " + str(corr))  # Imprimir la correlación entre altura y peso