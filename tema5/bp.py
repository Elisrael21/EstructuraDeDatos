def burbuja(array):
    n=len(array)
    for i in range (n):
        swapped = False
        for j in range (n-i-1):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
                swapped = True
                if (swapped == False):
                    break
                
print("Metodo burbuja")                
array = [12,13,23,45,67,89,91,90,2,8,4]
print("desordenado" + str(array))
burbuja(array)
print("ordenado" + str(array))