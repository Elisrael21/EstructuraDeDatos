print("Lista sin arreglar")
Lista=[0,11,21,34,54,67,89,43,45,90,87,65,91,27,23,99,1,2,12,3,4,5]
print(Lista)
print("Lista arreglada")
Lista.sort()
print(Lista)

#1ro. Buscar el punto medio(puntero)
#2do. Comprobar si el punto medio es el valor que buscamos
#3ro. Si el número es menor al valor que buscamos aumentamos el valor de inicio 1 sobre el puntero
#4to. Si el número es mayor al valor que buscamos aumentamos el vamor de final bajo el puntero
#5to. Si inicio es mayor o igual que final entonces el valor no se encuentra en la lista

def busqueda_binaria(valor):
    inicio = 0
    final = len(Lista)-1
    while inicio <= final:
        puntero = (inicio + final)//2
        if valor == Lista[puntero]:
            return puntero
        elif valor > Lista[puntero]:
            inicio = puntero + 1
        else:
            final = puntero - 1
    return None

def buscar_valor(valor):
    res_busqueda = busqueda_binaria(valor)
    if res_busqueda is None:
        return f"El número {valor} no esta en la lista"
    else:
        return f"El número {valor} esta en la posición {res_busqueda}"
    
print("Resultado del número buscado")
print(buscar_valor(21))