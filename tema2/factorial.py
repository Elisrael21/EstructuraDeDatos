print ("Programa que calcula el factorial")
numero = int(input("Introduzca el número: "))
factorial = 1
i = 1
while (i <= numero):
    factorial = factorial * i
    i = i + 1
print ("El factorial de " + str(numero) + " es " + str(factorial))


# Función para calcular el factorial
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

# Solicitar al usuario el número
n = int(input("Introduce un número: "))

# Calcular el factorial
fact = factorial(n)

# Imprimir el factorial
print(f"El factorial de {n} es {fact}")
