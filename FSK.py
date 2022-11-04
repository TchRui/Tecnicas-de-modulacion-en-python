import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style
class fsk:
    def __init__(self,cadena):
        fig = plt.figure()
        ax1 = fig.add_subplot(1,1,1)

        g=lambda x:np.sin(x)
        h=lambda x1:np.sin(x1*3)


        pi=0
        pi2=2*np.pi
        pi3=2*np.pi
        pi4=4*np.pi
        """ cadena="011001" """

        for i in range(0,len(cadena)):
        
            if cadena[i]=="0":

                if pi<pi3 and pi2<pi4:
                    pi=pi4
                    pi2=pi+2*np.pi
                else:
                    pi=pi+2*np.pi
                    pi2=pi+2*np.pi
                x=np.linspace(pi,pi2,100)
                plt.plot(x,g(x),color="red")

            else:
            
                if pi3<pi and pi4<pi2:
                    pi3=pi2
                    pi4=pi3+2*np.pi
                else:
                    pi3=pi3+2*np.pi
                    pi4=pi3+2*np.pi 
                x1=np.linspace(pi3,pi4,100)
                plt.plot(x1,h(x1),color="blue")

        plt.grid()
        plt.show()

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

    a=fsk(numeros)







