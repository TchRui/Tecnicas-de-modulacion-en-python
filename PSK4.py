#from symbol import raise_stmt
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style


class fpsk:

    def __init__(self, cadena):
        fig = plt.figure()
        ax1 = fig.add_subplot(1, 1, 1)

        def g(x): return np.sin(x*5)
        def h(x1): return -2*np.sin(x1)

        # funciones de 4 PSK
        def r(x): return np.cos(x*3)
        def s(x): return -np.cos(x*3)
        def t(x1): return np.sin(x1*3)
        def u(x1): return -np.sin(x1*3)

        # funciones de 8-QAM
        # son las mismas funciones que las de arriba ademas de unas copias de ellas con mas amplitud de onda

        pi = 0
        pi2 = 2*np.pi
        pi3 = 2*np.pi
        pi4 = 4*np.pi
        for i in range(0, len(cadena)-1, 2):
            # print(cadena[i],cadena[i+1])

            if cadena[i] == '0' and cadena[i+1] == '1':
                if pi < pi3 and pi2 < pi4:
                    pi = pi4
                    pi2 = pi+2*np.pi
                else:
                    pi = pi+2*np.pi
                    pi2 = pi+2*np.pi
                x = np.linspace(pi, pi2, 100)
                plt.plot(x, r(x), color="red")
            elif cadena[i] == '1' and cadena[i+1] == '0':
                if pi < pi3 and pi2 < pi4:
                    pi = pi4
                    pi2 = pi+2*np.pi
                else:
                    pi = pi+2*np.pi
                    pi2 = pi+2*np.pi
                x = np.linspace(pi, pi2, 100)
                plt.plot(x, s(x), color="pink")
            elif cadena[i] == '1' and cadena[i+1] == '1':
                if pi3 < pi and pi4 < pi2:
                    pi3 = pi2
                    pi4 = pi3+2*np.pi
                else:
                    pi3 = pi3+2*np.pi
                    pi4 = pi3+2*np.pi
                x1 = np.linspace(pi3, pi4, 100)
                plt.plot(x1, t(x1), color="green")
            elif cadena[i] == '0' and cadena[i+1] == '0':
                if pi3 < pi and pi4 < pi2:
                    pi3 = pi2
                    pi4 = pi3+2*np.pi
                else:
                    pi3 = pi3+2*np.pi
                    pi4 = pi3+2*np.pi
                x1 = np.linspace(pi3, pi4, 100)
                plt.plot(x1, u(x1), color="blue")
            # print(i)

        plt.grid()
        plt.show()

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

    a = fpsk(numeros)
