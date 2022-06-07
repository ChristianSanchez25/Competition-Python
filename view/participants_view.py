from controller.data_controller import (clearScreen)

#Tabla Participantes
def table_partcipants(data:dict):
    if not 'participants' in data:
        raise KeyError('       ERROR! no hay data cargada en el sistema, ve a la opcion de archivos para cargar la data')
    #header
    print("\t\t\t\t ***TABLA DE PARTICIPANTES***\n")
    print ("-------------------------------------------------------------------------------------------------------------------------------------------")
    print ("{8}{0:15}{8}{1:20}{8}{2:20}{8}{3:20}{8}{4:20}{8}{5:6}{8}{6:6}{8}{7:12}{8}".format('CI'.center(15),'Primer Nombre'.center(20),'Segundo Nombre'.center(20), 
                                                                    'Primer Apellido'.center(20),'Segundo Apellido'.center(20) , 'Sexo'.center(6), 
                                                                    'Edad'.center(6), 'Tiempo'.center(12), '||'.center(2)))
    print ("-------------------------------------------------------------------------------------------------------------------------------------------")
    
    
    
    for p in data['participants']:
        
        #datos de los participantes
        print ("{8}{0:15}{8}{1:20}{8}{2:20}{8}{3:20}{8}{4:20}{8}{5:6}{8}{6:6}{8}{7:12}{8}".format(str(p.ci).center(15), p.first_name.center(20),p.char_second_name.center(20),
                                                                        p.first_last_name.center(20), p.second_last_name.center(20),p.gender.center(6),
                                                                        str(p.age).center(6), str(p.time).center(12),'||'.center(2)))
        print ("-------------------------------------------------------------------------------------------------------------------------------------------")
        
    input("\nPresione una tecla para continuar ")
    clearScreen()



def total_participants(data: dict):
    if not 'total' in data:
        raise KeyError('       ERROR! no hay data cargada en el sistema, ve a la opcion de archivos para cargar la data')
    # total
    print(f"\tTOTAL DE PARTICIPANTES: {data['total']}")
    input("\nPresione una tecla para continuar ")
    clearScreen()


def winner_participant(data: dict):
    if not 'total' in data:
        raise KeyError('       ERROR! no hay data cargada en el sistema, ve a la opcion de archivos para cargar la data')
    # Ganador general
    print(f"\tGANADOR: PARTICIPANTE: {data['participants'][0].__str__()} con un tiempo de: {data['participants'][0].time}")
    input("\nPresione una tecla para continuar ")
    clearScreen()


def avg_total(data: dict):
    if not 'total' in data:
        raise KeyError('       ERROR! no hay data cargada en el sistema, ve a la opcion de archivos para cargar la data')
    #Promedio por genero y grupo etario
    print("\t\t\t ***PROMEDIO DE TIEMPO POR GRUPO***\n")
    #header
    print ("-------------------------------------------------")
    print ("|{:15}|{:15}|{:15}|".format('Grupo Etario'.center(15),'Femenino'.center(15), 'Masculino'.center(15)))
    print ("-------------------------------------------------")

    #juniors
    print ("-------------------------------------------------")
    print ("|{:15}|{:15}|{:15}|".format('Juniors'.center(15),str(data['avg_juniors_women']).center(15), str(data['avg_juniors_men']).center(15)))
    print ("-------------------------------------------------")

    #seniors
    print ("-------------------------------------------------")
    print ("|{:15}|{:15}|{:15}|".format('Seniors'.center(15),str(data['avg_seniors_women']).center(15), str(data['avg_seniors_men']).center(15)))
    print ("-------------------------------------------------")

    #masters
    print ("-------------------------------------------------")
    print ("|{:15}|{:15}|{:15}|".format('Seniors'.center(15),str(data['avg_masters_women']).center(15), str(data['avg_masters_men']).center(15)))
    print ("-------------------------------------------------")

    input("\nPresione una tecla para continuar ")
    clearScreen()