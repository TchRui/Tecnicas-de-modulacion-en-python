class analogo:
    def __init__(self):
        pass

    def decodificador(self, cadena):
        #Seprara la cadena de texto en una lista
        lista = cadena.split(",")
        
        print(lista)

if __name__ == '__main__':
    analogo_objeto = analogo()
    analogo_objeto.decodificador("1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16")