import turtle


class rz:
    def __init__(self, cadena):
        vic = turtle.Turtle()
        vic.shape("turtle")
        vic.speed(0)
        vic.pencolor("green")
        turtle.setworldcoordinates(-1000, -100, 1000, 100)
        vic.penup()
        vic.goto(-1000, 0)
        vic.pendown()
        vic.goto(1000, 0)
        vic.goto(-1000, 0)

        refer = cadena[0]

        def uno():
            vic.left(90)
            vic.forward(15)
            vic.right(90)
            vic.forward(15)
            vic.right(90)
            vic.forward(15)
            vic.left(90)
            vic.forward(15)

        def cero():
            vic.right(90)
            vic.forward(15)
            vic.left(90)
            vic.forward(15)
            vic.left(90)
            vic.forward(15)
            vic.right(90)
            vic.forward(15)

        for i in range(0, len(cadena)):
            if cadena[i] == "1":
                uno()
            elif cadena[i] == "0":
                cero()

        turtle.mainloop()

if __name__ == "__main__":
    numeros = ""
    letra = input("ingrese texto: ")
    for i in range(0, len(letra)):
        aux = ord(letra[i])

    # meter numero por consola
        numero = bin(aux)
        numero = numero[2:]
        numero = numero.zfill(8)
        numeros = numeros+numero

    a = rz(numeros)
