from pickle import FALSE
import turtle
import math

from matplotlib.pyplot import phase_spectrum


class b8zs:
    def __init__(self, cadena):
        # cadena="0000000011111111"
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
            vic.forward(15)
            vic.right(90)
            vic.forward(15)
            vic.right(90)
            vic.forward(15)
            vic.left(90)

        def continua():
            vic.forward(15)

        def cero():
            vic.right(90)
            vic.forward(15)
            vic.left(90)
            vic.forward(15)
            vic.left(90)
            vic.forward(15)
            vic.right(90)

        refer = 1
        contador = 0
        i = 0
        while i < len(cadena):
            # for i in range(0,len(cadena)):
            if cadena[i] == "1":
                if refer == 1:
                    inicio1()
                    refer = 0
                    contador = 0
                elif refer == 0:
                    cero()
                    refer = 1
                    contador = 0
            elif cadena[i] == "0":
                contador = contador+1
                band = True
                aux = i
                if i+5 < len(cadena)-1:
                    for j in range(4):
                        if cadena[aux] == "1":
                            band = False
                        aux = aux+1

                if contador == 4 and band == True:

                    if refer == 0 and i+3 < len(cadena)-1:
                        vic.left(90)
                        vic.forward(15)
                        vic.right(90)
                        vic.forward(15)
                        vic.right(90)
                        vic.forward(30)
                        vic.left(90)
                        vic.forward(15)
                        vic.left(90)
                        vic.forward(15)
                        vic.right(90)
                        vic.forward(15)
                        vic.right(90)
                        vic.forward(15)
                        vic.left(90)
                        vic.forward(15)
                        vic.left(90)
                        vic.forward(30)
                        vic.right(90)
                        vic.forward(15)
                        vic.right(90)
                        vic.forward(15)
                        vic.left(90)
                        i = i+4
                        refer = 0
                    elif refer == 1 and i+3 < len(cadena)-1:
                        vic.right(90)
                        vic.forward(15)
                        vic.left(90)
                        vic.forward(15)
                        vic.left(90)
                        vic.forward(30)
                        vic.right(90)
                        vic.forward(15)
                        vic.right(90)
                        vic.forward(15)
                        vic.left(90)
                        vic.forward(15)
                        vic.left(90)
                        vic.forward(15)
                        vic.right(90)
                        vic.forward(15)
                        vic.right(90)
                        vic.forward(30)
                        vic.left(90)
                        vic.forward(15)
                        vic.left(90)
                        vic.forward(15)
                        vic.right(90)

                        i = i+4
                        refer = 1
                    contador = 0
                else:
                    continua()
            i = i+1
            # print(i)
        # vic.goto(500,100)
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
        print(numero)

    a = b8zs(numeros)
