import mensajes.msg as msg
from funciones import *
import json
import os
from user import *
#FUNCIONES
def menu():
    print('Bienvenido')
    print('1.Registrar usuario')
    print('2. Mirar planes')
    print('3. Salir')

def planes():
    print('1. Fibra optica')
    print('2. Pospago')
    print('3. Prepago')
    print('4. Salir')





    



#MAIN**********************************************************************************************
while (True):
    while True:
        os.system('clear')
        menu()
        opcion = int(input("Seleccione una opción: "))
        
        if opcion == 1:
            user_data = {
                "documento": int(input("Numero de documento: ")),
                "nombres": input("Nombres: "),
                "apellidos": input("Apellidos: "),
               "numero": int(input("Numero de telefono: ")),
               "direccion": input("Dirección: ")
                              
            }
            agregar_usuario(user_data)
            break
        elif opcion == 2:
            while True:
                os.system('clear')
                planes()
                rt = int(input("Seleccione una opción: "))
                match rt:
                    case 1:
                        print('Valores de....')
                        print(input('la opcion seleccionada es invalida'))
                        break
                    case 2:
                        print('Valores de....')
                        print(input('la opcion seleccionada es invalida'))
                        break
                    case 3:
                        print('Valores de....')
                        print(input('la opcion seleccionada es invalida'))
                        break
                    case 4: 
                        break
                    case _:
                        print(input('la opcion seleccionada es invalida'))
            
                break
        elif opcion == 3:
            print(input('Gracias por u visita presione enter para continuar'))
            break