import turtle

def copo_de_nieve(t, longitud, nivel):
    if nivel == 0:
        t.forward(longitud)
    else:
        longitud /= 3.0
        copo_de_nieve(t, longitud, nivel-1)
        t.left(60)
        copo_de_nieve(t, longitud, nivel-1)
        t.right(120)
        copo_de_nieve(t, longitud, nivel-1)
        t.left(60)
        copo_de_nieve(t, longitud, nivel-1)

def main():
    window = turtle.Screen()
    window.bgcolor("white")
    t = turtle.Turtle()
    t.speed(0)
    t.penup()
    t.goto(-150, 90)
    t.pendown()

    nivel = 4  # Cambia el nivel del fractal aquí

    for _ in range(3):
        copo_de_nieve(t, 300, nivel)
        t.right(120)

    window.exitonclick()

if __name__ == "_main_":
    main()