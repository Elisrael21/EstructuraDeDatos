# Solicitar al usuario el tamaño de la lista
n = int(input("Introduce el tamaño de la lista: "))

# Crear una lista vacía
lista = []

# Llenar la lista con números ingresados por el usuario
for i in range(n):
    num = int(input(f"Introduce el número {i+1}: "))
    lista.append(num)

# Imprimir la lista
print("La lista generada es: ", lista)


#Este programa solicita al usuario que introduzca el tamaño de la lista que desea generar y
# luego los números que desea agregar a la lista. 
# La memoria para la lista se asigna dinámicamente a medida que se agregan los números.
# Finalmente, imprime la lista generada.