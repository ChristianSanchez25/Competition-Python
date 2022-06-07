from view.histogram_view import histogram
from view.participants_view import (avg_total, table_partcipants, total_participants, winner_participant)
from view.etarian_group_view import (table_participants_etarios, winner_etarian, winner_etarian_sex)
from view.sex_group_view import (total_sex_group, winner_sex)
from error.option_error import WrongOption
from controller.data_controller import (clearScreen)

def action_menu(data: dict) -> dict:
    while(True):
        print('\n')
        print('\n')
        print('\t\t************** MENU ACCIONES *********************')
        print('\n')
        print('\t[1]. Lista con Totalidad de Participantes  \n')
        print('\t[2]. Cantidad Total de Participantes \n')
        print('\t[3]. Cantidad de Participantes por Grupo Etario \n')
        print('\t[4]. Cantidad de Participantes por Sexo \n')
        print('\t[5]. Ganadores por Grupo Etario \n')
        print('\t[6]. Ganadores por Sexo \n')
        print('\t[7]. Ganadores por Grupo Etario y Sexo \n')
        print('\t[8]. Ganador General \n')
        print('\t[9]. Histograma de Participantes por Grupo Etario \n')
        print('\t[10]. Promedio de Tiempo por Grupo Etario y Sexo \n')
        print('\t[11]. Menu Principal \n')
        print('\n')
        print("\tIngrese una opcion --> ", end="") 
        try:
            option = int(input(''))
            if option == 1:
                clearScreen()
                table_partcipants(data)
            elif option == 2:
                clearScreen()
                total_participants(data)
            elif option == 3:
                clearScreen()
                table_participants_etarios(data)
            elif option == 4:
                clearScreen()
                total_sex_group(data)
            elif option == 5:
                clearScreen()
                winner_etarian(data)
            elif option == 6:
                clearScreen()
                winner_sex(data)
            elif option == 7:
                clearScreen()
                winner_etarian_sex(data)
            elif option == 8:
                clearScreen()
                winner_participant(data)
            elif option == 9:
                clearScreen()
                histogram(data)
            elif option == 10:
                clearScreen()
                avg_total(data)
            elif option == 11:
                clearScreen()
                return data
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
        except KeyError as e:
            print(e.__str__())
            input("\tPulsa una tecla para continuar...")
            clearScreen()
        except TypeError:
            print("\tERROR! No hay data en el sistema")
            input("\tPulsa una tecla para continuar...")
            clearScreen()

