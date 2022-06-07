from controller.data_controller import (clearScreen)


def histogram(data:dict):
    if not 'participants' in data:
        raise KeyError('       ERROR! no hay data cargada en el sistema, ve a la opcion de archivos para cargar la data')

    # Histograma
    print("\t\t ***HISTOGRAMA***\n")
    juniors = len(data["juniors_women"]) + len(data["juniors_men"])
    seniors= len(data["seniors_women"]) + len(data["seniors_men"])
    masters= len(data["masters_women"]) + len(data["masters_men"])
    
    print("{:7}({:3}): |{}".format('Juniors', juniors,juniors*'*'))
    print("{:7}({:3}): |{}".format('Seniors', seniors,seniors*'*'))
    print("{:7}({:3}): |{}".format('Masters', masters,masters*'*'))
    

    input("\nPresione una tecla para continuar")
    clearScreen()