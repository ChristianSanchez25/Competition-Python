from controller.data_controller import (clearScreen)

def total_sex_group(data: dict):
    if not 'participants' in data:
        raise KeyError('       ERROR! no hay data cargada en el sistema, ve a la opcion de archivos para cargar la data') 
    # Total por sexo
    total_men = len(data["juniors_men"]) + len(data["seniors_men"]) + len(data["masters_men"])
    total_women = len(data["juniors_women"]) + len(data["seniors_women"]) + len(data["masters_women"])
    print(f'\tTOTAL DE PARTICIPANTES: MASCULINOS = {total_men} FEMENINOS = {total_women}')
    input("\nPresione una tecla para continuar ")
    clearScreen()


def winner_sex(data: dict):
    if not 'participants' in data:
        raise KeyError('       ERROR! no hay data cargada en el sistema, ve a la opcion de archivos para cargar la data') 
    
    print("\t\t***GANADORES POR SEXO***\n")
    print ("----------------------------------------------------------------------------------------------------")   
    print ("||{:15}||{:15}||{:20}||{:20}||{:10}||".format('Genero'.center(15),'CI'.center(15), 
                                                           'Primer Nombre'.center(20), 'Primer Apellido'.center(20), 
                                                           'Tiempo'.center(10)))
    print ("----------------------------------------------------------------------------------------------------")
    
    # Mujer con mejor tiempo
    if (data["juniors_women"][0].total_time <= data["seniors_women"][0].total_time) and (data["juniors_women"][0].total_time <= data["masters_women"][0].total_time):
        woman = data["juniors_women"][0]
    elif(data["seniors_women"][0].total_time <= data["juniors_women"][0].total_time) and (data["seniors_women"][0].total_time <= data["masters_women"][0].total_time):
        woman = data["seniors_women"][0]
    else:
        woman = data["masters_women"][0]
    
    print ("----------------------------------------------------------------------------------------------------")   
    print ("||{:15}||{:15}||{:20}||{:20}||{:10}||".format('Femenino'.center(15),str(woman.ci).center(15), 
                                                           woman.first_name.center(20), woman.first_last_name.center(20), 
                                                           str(woman.time).center(10)))
    print ("----------------------------------------------------------------------------------------------------")
    
    # Hombre con mejor tiempo
    if (data["juniors_men"][0].total_time <= data["seniors_men"][0].total_time) and (data["juniors_men"][0].total_time <= data["masters_men"][0].total_time):
        man = data["juniors_men"][0]
    elif(data["seniors_men"][0].total_time <= data["juniors_men"][0].total_time) and (data["seniors_men"][0].total_time <= data["masters_men"][0].total_time):
        man = data["seniors_men"][0]
    else:
        man = data["masters_men"][0]

    print ("----------------------------------------------------------------------------------------------------")   
    print ("||{:15}||{:15}||{:20}||{:20}||{:10}||".format('Masculino'.center(15),str(man.ci).center(15), 
                                                           man.first_name.center(20), man.first_last_name.center(20), 
                                                           str(man.time).center(10)))
    print ("----------------------------------------------------------------------------------------------------")
    input("\nPresione una tecla para continuar ")
    clearScreen()