import turtle


class nrzi:
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

        def inicio1():
            vic.left(90)
            vic.forward(30)
            vic.right(90)
            vic.forward(15)

        def continua():
            vic.forward(15)

        def cero():
            vic.right(90)
            vic.forward(30)
            vic.left(90)
            vic.forward(15)

        def fin1():
            vic.right(90)
            vic.forward(15)

        def fin0():
            vic.left(90)
            vic.forward(15)
        band = True
        cer = ""
        uno = ""
        cer = refer
        for i in range(0, len(cadena)):
            if cadena[i] == "1" and i == 0:
                vic.left(90)
                vic.forward(15)
                vic.right(90)
                vic.forward(15)
                band = True
            elif cadena[i] == "0" and i == 0:
                vic.right(90)
                vic.forward(15)
                vic.left(90)
                vic.forward(15)
                band = False
            elif i > 0:
                if cadena[i] == "1" and band == False:
                    inicio1()
                    if i == len(cadena)-1:
                        fin1()
                    band = True
                elif cadena[i] == "1" and band == True:
                    cero()
                    if i == len(cadena)-1:
                        fin0()
                    band = False
                else:
                    continua()
                    if i == len(cadena)-1 and cadena[i] == "1" and band == True:
                        fin1()
                    elif i == len(cadena)-1 and cadena[i] == "0" and band == False:
                        fin0()
                    elif i == len(cadena)-1 and cadena[i] == "1" and band == False:
                        fin0()
                    elif i == len(cadena)-1 and cadena[i] == "0" and band == True:
                        fin1()

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

    a = nrzi(numeros)