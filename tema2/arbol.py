import turtle

def dibujar_arbol(longitud, nivel):
    if nivel == 0:
        return
    turtle.forward(longitud)
    turtle.left(45)
    dibujar_arbol(0.6 * longitud, nivel - 1)
    turtle.right(90)
    dibujar_arbol(0.6 * longitud, nivel - 1)
    turtle.left(45)
    turtle.backward(longitud)

turtle.speed(0)
turtle.penup()
turtle.goto(0, -200)
turtle.pendown()
turtle.left(90)
dibujar_arbol(100, 5)
turtle.done()