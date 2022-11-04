import turtle


class manchester:
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
            vic.forward(15)
            vic.right(90)
            vic.forward(30)
            vic.left(90)
            vic.forward(15)

        def cero():
            vic.forward(15)
            vic.left(90)
            vic.forward(30)
            vic.right(90)
            vic.forward(15)

        for i in range(0, len(cadena)):
            if cadena[i] == "1" and i == 0:
                vic.right(90)
                vic.forward(15)
                vic.left(90)
                vic.forward(15)
                vic.left(90)
                vic.forward(30)
                vic.right(90)
                vic.forward(15)
            elif cadena[i] == "0" and i == 0:
                vic.left(90)
                vic.forward(15)
                vic.right(90)
                vic.forward(15)
                vic.right(90)
                vic.forward(30)
                vic.left(90)
                vic.forward(15)
            else:
                if cadena[i] == "1" and cadena[i-1] != "1":
                    vic.forward(15)
                    vic.left(90)
                    vic.forward(30)
                    vic.right(90)
                    vic.forward(15)
                elif cadena[i] == "0" and cadena[i-1] != "0":
                    vic.forward(15)
                    vic.right(90)
                    vic.forward(30)
                    vic.left(90)
                    vic.forward(15)
                elif cadena[i] == "1" and i == len(cadena)-1:
                    vic.right(90)
                    vic.forward(30)
                    vic.left(90)
                    vic.forward(15)
                elif cadena[i] == "0" and i == len(cadena)-1:
                    vic.left(90)
                    vic.forward(30)
                    vic.right(90)
                    vic.forward(15)
                elif cadena[i] == "1":
                    vic.right(90)
                    vic.forward(30)
                    vic.left(90)
                    vic.forward(15)
                    vic.left(90)
                    vic.forward(30)
                    vic.right(90)
                    vic.forward(15)
                elif cadena[i] == "0":
                    vic.left(90)
                    vic.forward(30)
                    vic.right(90)
                    vic.forward(15)
                    vic.right(90)
                    vic.forward(30)
                    vic.left(90)
                    vic.forward(15)

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

    a = manchester(numeros)
