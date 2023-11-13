#clear para poder limpiar el terminal
print("Hola mundo")
a = 2
b = 3
suma = a+b 

print("la suma de 2 + 3 es igual a", suma)

numero = 12
numero += 9
print(numero)

i = [0,0]
s = [0,1]
r = [0,2]
a = [0,3]
e = [0,4]
l = [0,5]
print( i, s, r, a, e, l)
m = [1,0]
a = [1,1]
r = [1,2]
i = [1,3]
n = [1,4]

e = [2,0]
s = [2,1]
p = [2,2]
i = [2,3]
n = [2,4]
o = [2,5]
z = [2,6]
a = [2,7]

def fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fib(n-1) + fib(n-2)

if __name__ == '__main__':
    fibonacci = fib(10)
    print('Fibonacci de orden 10:')
    print(fibonacci)

#from turtle import *
#home()

#forward(100)
#left(60)
#forward(66)
#left(180)
#forward(66)
#left(60)
#forward(66)


mi_lista = ['Juan', 'Pedro', 'Laura', 'Carmen', 'Susana']
print(mi_lista[0]) # Muestra Juan (la primera posición es la 0)
print(mi_lista[-1]) # Muestra Susana
print(mi_lista[1]) # Muestra Pedro
print(mi_lista[2]) # Muestra Laura
print(mi_lista[-2]) # Muestra Carmen

mi_lista = ['i', 's', 'r', 'a', 'e','l']
print(mi_lista[0]) # Muestra Juan (la primera posición es la 0)
print(mi_lista[1]) # Muestra Susana
print(mi_lista[2]) # Muestra Pedro
print(mi_lista[3]) # Muestra Laura
print(mi_lista[4]) # Muestra Carmen
print(mi_lista[5]) #Muestra la letras L