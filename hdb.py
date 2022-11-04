from pickle import FALSE
import turtle
import math

from matplotlib.pyplot import phase_spectrum

class hdb:
    def __init__(self,cadena):
        vic=turtle.Turtle()
        vic.shape("turtle")
        vic.speed(0)
        vic.pencolor("green")
        turtle.setworldcoordinates(-1000,-100,1000,100)
        vic.penup()
        vic.goto(-1000,0)
        vic.pendown()
        vic.goto(1000,0)
        vic.goto(-1000,0) 

        refer=cadena[0]

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
        def fin1():
            vic.right(90)
            vic.forward(15)
        def fin0():
            vic.left(90)
            vic.forward(15)

        refer=1
        conta=0

        for i in range(0,len(cadena)):
            if cadena[i]=="1":
                if refer==1:
                    inicio1()
                    refer=0
                    conta=0
                elif refer==0:
                    cero()
                    refer=1
                    conta=0
            elif cadena[i]=="0":
                conta=conta+1
                if conta==4 and i+7<len(cadena)-1:
                    if refer==1:
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
                        i=i+7
                        refer=1
                    elif refer==0:
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
                        i=i+7
                        refer=0
                    conta=0
                else:
                    continua()

        turtle.mainloop()

if __name__ == "__main__":
    numeros=""
    letra=input("ingrese texto: ")
    for i in range(0,len(letra)):
        aux=ord(letra[i])

    #meter numero por consola
        numero=bin(aux)
        numero=numero[2:]
        numero=numero.zfill(8)
        numeros=numeros+numero

    a=hdb(numeros) 