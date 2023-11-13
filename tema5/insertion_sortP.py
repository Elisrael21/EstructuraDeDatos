def insertionSort(array):
    for i in range(1,len(array)):
        key = array[i]
        j = i-1
        while j >= 0 and key < array[j]:
            array[j+1]= array[j]
            j-=1
            array[j+1]=key
            
print("Insertion Sort")            
array = [12,13,23,45,67,89,91,90,2,8,4]
print("desordenado" + str(array))
insertionSort(array)
print("ordenado" + str(array))


def insertar(array):
    for i in range(1,len(array)):
        key = array[i]
        j=i-1
        while j>= 0 and key < array[j]:
            array[j+1] = array[j]
            j-=1
            array[j+1] = key
            
print("metodo prueba")            
array=[12,34,5,6,7,88,87,65,3]            
print("desordenado" + str(array))
insertar(array)
print("ordenado" + str(array))
