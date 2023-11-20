def pedirNumero(lista):
    for numero in lista:
        print(numero, end=" ")
    num=int(input("\nIngresa un número de la lista anterior:"))
    return num
def busquedaSecuencial(lista, num):
    for i in range(0,len(lista)):
        if num==lista[i]:
            return True
    return False
lista=[0, 1, 2, 3, 4, 5, 11, 12, 21, 23, 27, 34, 43, 45, 54, 65, 67, 87, 89, 90, 91, 99]
while True:
    num=pedirNumero(lista)
    encontrado=busquedaSecuencial(lista,num)
    if encontrado==True:
        print("Se a encontrado el número deseado")
        break
    else:
        print("Intentalo de nuevo")