from pickle import FALSE
import turtle
import math

from matplotlib.pyplot import phase_spectrum


class hdb3:
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
                au = True
                met = True
                if i+7 <= len(cadena)-1:
                    for k in range(8):
                        if cadena[i+k] != "0":
                            au = False
                if i+7 > len(cadena)-1:
                    au = False

                if au == True:
                    for u in range(3):
                        continua()
                    if refer == 1 and i+3 < len(cadena)-1:
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
                        vic.forward(30)
                        vic.right(90)
                        vic.forward(15)
                        vic.left(90)
                        vic.forward(15)
                        vic.left(90)
                        vic.forward(15)
                        vic.right(90)
                        i = i+7
                        refer = 1
                    elif refer == 0 and i+3 < len(cadena)-1:
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
                        vic.forward(30)
                        vic.left(90)
                        vic.forward(15)
                        vic.right(90)
                        vic.forward(15)
                        vic.right(90)
                        vic.forward(15)
                        vic.left(90)
                        i = i+7
                        refer = 0
                    else:
                        continua()
                    contador = 0
                    met = False

                if i+3 <= len(cadena)-1 and au == False:
                    print("aqui")
                    for j in range(4):
                        if cadena[i+j] != "0":
                            band = False
                    """ print(band)
                    print(refer) """
                    if refer == 0 and band == True:
                        vic.right(90)
                        vic.forward(15)
                        vic.left(90)
                        vic.forward(15)
                        vic.left(90)
                        vic.forward(15)
                        vic.right(90)
                        vic.forward(30)
                        vic.right(90)
                        vic.forward(15)
                        vic.left(90)
                        vic.forward(15)
                        vic.left(90)
                        vic.forward(15)
                        vic.right(90)
                        i = i+3
                        refer = 1
                    elif refer == 1 and band == True:
                        print("aca")
                        vic.left(90)
                        vic.forward(15)
                        vic.right(90)
                        vic.forward(15)
                        vic.right(90)
                        vic.forward(15)
                        vic.left(90)
                        vic.forward(30)
                        vic.left(90)
                        vic.forward(15)
                        vic.right(90)
                        vic.forward(15)
                        vic.right(90)
                        vic.forward(15)
                        vic.left(90)
                        i = i+3
                        refer = 0
                    else:
                        continua()
                else:
                    if met == True:
                        continua()

            # vic.goto(100,100)

            # print(i)
            i = i+1

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

    a = hdb3(numeros)
