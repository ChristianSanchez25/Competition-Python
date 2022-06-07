
from controller.data_controller import (clearScreen)


def table_participants_etarios(data:dict):
    if not "participants" in data: 
        raise KeyError('       ERROR! no hay data cargada en el sistema, ve a la opcion de archivos para cargar la data')
    
    #Header
    print("\t\t***CANTIDAD PARTICIPANTES POR GRUPO ETARIO***\n")
    print ("-------------------------------")    
    print ("||{:15}||{:10}||".format('Grupo Etario'.center(15),'Cantidad'.center(10)))
    print ("-------------------------------")
    
    print("||{:15}||{:10}||".format('Juniors'.center(15), str(len(data['juniors_men']) + len(data['juniors_women'])).center(10)))
    print ("-------------------------------")
    print("||{:15}||{:10}||".format('Seniors'.center(15), str(len(data['seniors_men']) + len(data['seniors_women'])).center(10)))
    print ("-------------------------------")
    print("||{:15}||{:10}||".format('Masters'.center(15), str(len(data['masters_men']) + len(data['masters_women'])).center(10)))
    print ("-------------------------------")

    input("\nPresione una tecla para continuar")
    clearScreen()


def winner_etarian(data: dict):
    if not "participants" in data: 
        raise KeyError('       ERROR! no hay data cargada en el sistema, ve a la opcion de archivos para cargar la data')
    #Header
    print("\t\t***GANADORES POR GRUPO ETARIO***\n")
    print ("----------------------------------------------------------------------------------------------------")    
    print ("||{:15}||{:15}||{:20}||{:20}||{:10}||".format('Grupo Etario'.center(15),'CI'.center(15), 
                                                           'Primer Nombre'.center(20), 'Primer Apellido'.center(20), 
                                                           'Tiempo'.center(10)))
    print ("----------------------------------------------------------------------------------------------------")

    #Verifica quien tiene mejor tiempo en juniors
    x, y = data["juniors_men"][0], data["juniors_women"][0]
    junior = x if x.total_time < y.total_time else y  

    print ("----------------------------------------------------------------------------------------------------")  
    print ("||{:15}||{:15}||{:20}||{:20}||{:10}||".format('Juniors'.center(15),str(junior.ci).center(15), 
                                                           junior.first_name.center(20), junior.first_last_name.center(20), 
                                                           str(junior.time).center(10)))
    print ("----------------------------------------------------------------------------------------------------")
    
    #Verifica quien tiene mejor tiempo en seniors
    x, y = data["seniors_men"][0], data["seniors_women"][0]
    senior = x if x.total_time < y.total_time else y  

    print ("----------------------------------------------------------------------------------------------------") 
    print ("||{:15}||{:15}||{:20}||{:20}||{:10}||".format('Seniors'.center(15),str(senior.ci).center(15), 
                                                           senior.first_name.center(20), senior.first_last_name.center(20), 
                                                           str(senior.time).center(10)))
    print ("----------------------------------------------------------------------------------------------------")

    #Verifica quien tiene mejor tiempo en masters
    x, y = data["masters_men"][0], data["masters_women"][0]
    master = x if x.total_time < y.total_time else y  

    print ("----------------------------------------------------------------------------------------------------")
    print ("||{:15}||{:15}||{:20}||{:20}||{:10}||".format('Masters'.center(15),str(master.ci).center(15), 
                                                           master.first_name.center(20), master.first_last_name.center(20), 
                                                           str(master.time).center(10)))
    print ("----------------------------------------------------------------------------------------------------")

    input("\nPresione una tecla para continuar ")
    clearScreen()


def winner_etarian_sex(data: dict):
    if not "participants" in data: 
        raise KeyError('       ERROR! no hay data cargada en el sistema, ve a la opcion de archivos para cargar la data')
    #Header
    print("\t\t***GANADORES POR GRUPO ETARIO Y SEXO***\n")
    print ("--------------------------------------------------------------------------------------------------------------")    
    print ("||{:15}||{:15}||{:15}||{:20}||{:20}||{:10}||".format('Grupo Etario'.center(15),'Genero'.center(15),'CI'.center(15), 
                                                           'Primer Nombre'.center(20), 'Primer Apellido'.center(20), 
                                                           'Tiempo'.center(10)))
    print ("--------------------------------------------------------------------------------------------------------------")

    # MUJER JUNIOR
    p = data["juniors_women"][0]
    print ("--------------------------------------------------------------------------------------------------------------")    
    print ("||{:15}||{:15}||{:15}||{:20}||{:20}||{:10}||".format('Juniors'.center(15),'Femenino'.center(15),str(p.ci).center(15), 
                                                           p.first_name.center(20), p.first_last_name.center(20), 
                                                           str(p.time).center(10)))
    print ("--------------------------------------------------------------------------------------------------------------")

    # HOMBRE JUNIOR
    p = data["juniors_men"][0]
    print ("--------------------------------------------------------------------------------------------------------------")    
    print ("||{:15}||{:15}||{:15}||{:20}||{:20}||{:10}||".format('Juniors'.center(15),'Masculino'.center(15),str(p.ci).center(15), 
                                                           p.first_name.center(20), p.first_last_name.center(20), 
                                                           str(p.time).center(10)))
    print ("--------------------------------------------------------------------------------------------------------------")

    # MUJER SENIOR
    p = data["seniors_women"][0]
    print ("--------------------------------------------------------------------------------------------------------------")    
    print ("||{:15}||{:15}||{:15}||{:20}||{:20}||{:10}||".format('Seniors'.center(15),'Femenino'.center(15),str(p.ci).center(15), 
                                                           p.first_name.center(20), p.first_last_name.center(20), 
                                                           str(p.time).center(10)))
    print ("--------------------------------------------------------------------------------------------------------------")

    # HOMBRE SENIOR
    p = data["seniors_men"][0]
    print ("--------------------------------------------------------------------------------------------------------------")    
    print ("||{:15}||{:15}||{:15}||{:20}||{:20}||{:10}||".format('Seniors'.center(15),'Masculino'.center(15),str(p.ci).center(15), 
                                                           p.first_name.center(20), p.first_last_name.center(20), 
                                                           str(p.time).center(10)))
    print ("--------------------------------------------------------------------------------------------------------------")

    # MUJER MASTER
    p = data["masters_women"][0]
    print ("--------------------------------------------------------------------------------------------------------------")    
    print ("||{:15}||{:15}||{:15}||{:20}||{:20}||{:10}||".format('Masters'.center(15),'Femenino'.center(15),str(p.ci).center(15), 
                                                           p.first_name.center(20), p.first_last_name.center(20), 
                                                           str(p.time).center(10)))
    print ("--------------------------------------------------------------------------------------------------------------")

    # HOMBRE MASTER
    p = data["masters_men"][0]
    print ("--------------------------------------------------------------------------------------------------------------")    
    print ("||{:15}||{:15}||{:15}||{:20}||{:20}||{:10}||".format('Masters'.center(15),'Masculino'.center(15),str(p.ci).center(15), 
                                                           p.first_name.center(20), p.first_last_name.center(20), 
                                                           str(p.time).center(10)))
    print ("--------------------------------------------------------------------------------------------------------------")

    input("\nPresione una tecla para continuar ")
    clearScreen()
