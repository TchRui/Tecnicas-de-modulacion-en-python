from matplotlib import pyplot as plt
import numpy as np
from unipolar import unipolo
from threading import Thread

class analogo:
    def __init__(self):
        pass

    def main(self, cadena):
        lista = self.decodificador(cadena)
        
        hilo_graficar = Thread(target=self.graficar, args=(lista,))
        hilo_graficar.start()

        cadena = self.bytecode(lista)

        unipolo(cadena)

    def decodificador(self, cadena):
        # Seprara la cadena de texto en una lista
        lista = cadena.split(",")
        # convierte la cadena en una lista de enteros
        lista = [int(i) for i in lista]

        return lista

    def graficar(self, lista):
        # crea una grafica de barras con la lista
        plt.bar(range(len(lista)), lista, color="blue")
        plt.title("Muestreo de señal analogica a digital")
        plt.xlabel("Tiempo")
        plt.ylabel("Amplitud")
        plt.grid()
        plt.show()

    def bytecode(self, lista):
        lista_resultado = []

        lista_bytecode = [[i, False] if i > 0 else [i, True] for i in lista]

        lista_bytecode = [[abs(i[0]), i[1]] for i in lista_bytecode]

        lista_binario = [[format(i[0], '08b'), i[1]] for i in lista_bytecode]

        for i in range(len(lista_binario)):

            if lista_binario[i][1] == True:
                aux = str(lista_binario[i][0])
                aux = aux.replace(aux[0], "1", 1)

                lista_resultado.append(aux)
            else:
                aux = str(lista_binario[i][0])
                aux = aux.replace(aux[0], "0", 1)

                lista_resultado.append(aux)

        #realiza una cadena con la lista_resultado
        cadena = "".join(lista_resultado)
        
        return cadena

if __name__ == '__main__':
    cadena = "1,5,8,13,7,3,-1,-6,-3,-2,4,8"
    analogo_objeto = analogo()
    analogo_objeto.main(cadena)
    # analogo_objeto.decodificador("1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16")
