
from error.option_error import WrongOption
from view.action_menu import action_menu
from view.files_menu import f_menu
from controller.data_controller import (clearScreen)

def main_menu():
    data: dict = {}
    while(True):
        print('\n')
        print('\n')
        print('\t\t************** MENU PRINCIPAL*********************')
        print('\n')
        print('\t[1]. Archivos \n')
        print('\n')
        print('\t[2]. Acciones \n')
        print('\n')
        print("\tIngrese una opcion --> ", end="") 
        try:
            option = int(input(''))
            if option == 1:
                clearScreen()
                data = f_menu(data)
            elif option == 2:
                clearScreen()
                data = action_menu(data)
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

        



