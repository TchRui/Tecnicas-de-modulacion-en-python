# importacion de todos los archivos necesarios
from unipolar import unipolo
from NRZL import nrzl
from NRZI import nrzi
from RZ import rz
from manchester import manchester
from manchesterdif import manchesterdif
from AMI import ami
from B8ZS import b8zs
from HDB3 import hdb3
from PSK4 import fpsk
from QAM8 import epsk
from analogoDigital import analogo

class main():

    def menu(self):
        flag = True
        while flag:
            print("---- MENU ----")
            print("1. Unipolar")
            print("2. NRZ-L")
            print("3. RZ")
            print("4. Manchester")
            print("5. Manchester Diferencial")
            print("6. AMI")
            print("7. B8ZS")
            print("8. HDB3")
            print("9. PSK4")
            print("10. QAM8")
            print("11. Analogo")
            print("12. Salir")
            print("--------------")
            opcion = int(input("Ingrese una opcion: "))

            if opcion == 1:
                cadena = self.ingreso_datos()
                unipolo(cadena)

            elif opcion == 2:
                cadena = self.ingreso_datos()
                nrzl(cadena)

            elif opcion == 3:
                cadena = self.ingreso_datos()
                rz(cadena)

            elif opcion == 4:
                cadena = self.ingreso_datos()
                manchester(cadena)

            elif opcion == 5:
                cadena = self.ingreso_datos()
                manchesterdif(cadena)

            elif opcion == 6:
                cadena = self.ingreso_datos()
                ami(cadena)

            elif opcion == 7:
                cadena = self.ingreso_datos()
                b8zs(cadena)

            elif opcion == 8:
                cadena = self.ingreso_datos()
                hdb3(cadena)

            elif opcion == 9:
                cadena = self.ingreso_datos()
                fpsk(cadena)

            elif opcion == 10:
                cadena = self.ingreso_datos()
                epsk(cadena)
            
            elif opcion == 11:
                cadena = str(input("Ingrese la cadena de numeros separados por comas: "))
                analogo_objeto = analogo()
                analogo_objeto.decodificador(cadena)

            elif opcion == 12:
                print("Hasta luego")
                flag = False
                exit()

            else:
                print("Opcion no valida")
                self.menu()

    def ingreso_datos(self):
        cadena = str(input("Ingrese la cadena de texto: "))

        numeros = ""

        for caracter in cadena:
            aux = ord(caracter)

            numero = bin(aux)
            numero = numero[2:]
            numero = numero.zfill(8)
            numeros = numeros+numero

        return numeros

if __name__ == "__main__":
    main().menu()