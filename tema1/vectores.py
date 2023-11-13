import random

# Función para generar un vector
def generar_vector(n):
    vector = [random.random() for _ in range(n)]
    return vector

# Solicitar al usuario el tamaño del vector
n = int(input("Introduce el tamaño del vector: "))

# Generar el vector
vector = generar_vector(n)

# Imprimir el vector
print("El vector generado es: ", vector)

#Este programa solicita al usuario que introduzca el tamaño del vector que desea generar. 
# Luego, utiliza la función random.random() de la biblioteca random para generar un vector 
# de tamaño n con valores aleatorios entre 0 y 1. 
# Finalmente, imprime el vector generado.