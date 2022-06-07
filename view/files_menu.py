from data.load_data import load
from error.option_error import WrongOption
from controller.data_controller import (clearScreen)
import sys

def f_menu(data: dict):
    # Menu de Archivos
    while(True):
        print('\n')
        print('\n')
        print('\t\t************** MENU ARCHIVOS*********************')
        print('\n')
        print('\t[1]. Cargar Archivo \n')
        print('\n')
        print('\t[2]. Regresar Menu Principal \n')
        print('\n')
        print('\t[0]. Salir \n')
        print('\n')
        print("\tIngrese una opcion --> ", end="") 
        try:
            option = int(input(''))
            if option == 1:
                file_name: str = input('\tPor favor ingrese el nombre del archivo a cargar: ')
                data = load(file_name, data)
                input('\tPulse cualquier tecla para continuar')
                clearScreen()
            elif option == 2:
                clearScreen()
                return data
            elif option == 0:
                clearScreen()
                print("\n")
                print("\tHecho por: Christian Sanchez")
                print("\t¡ADIOS!")
                print("\n")
                input("\tPulsa una tecla para salir...")
                sys.exit()
            else:
                raise WrongOption(f"\n\tERROR! esta opcion no se encuentra en el menu: {option}")
        except ValueError:
            print("\n\tERROR! La opción a digitar debe ser un numero \n\t", end="")
            input("\tPulsa una tecla para continuar...")
            clearScreen()
        except WrongOption as e:
            print(e.__str__())
            input("\tPulsa una tecla para continuar...")
            clearScreen()