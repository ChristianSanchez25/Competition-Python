
from error.file_error import EmptyFile, IncompleteParticipantData
from controller.data_controller import filter_data
from model.participant import Participant

def isnotEmpty(file) -> bool:
    """
        Valida que el archivo recibido no este vacio, si esta vacio lanza la excepcion 'EmptyFile'
        Si el archivo no esta vacio retorna TRUE
    """
    file.read()
    file.seek(0,0)
    if (file.read() == ""):
        raise EmptyFile("ERROR! el archivo esta vacio. ")
    file.seek(0,0)
    return True



def get_data(file) -> list:
    """
        Recibe como parametro el archivo que esta abierto en modo lectura 
        Crea una lista de las llaves de los datos del participante
        Se iterada cada linea del archivo, valido que los datos obtenidos esten en las llaves del participante
        Si no estan completo lanzo la excepcion 'IncompleteParticipantData'
        Si esta completo creo un Objeto de la clase Participante con los valores obtenidos y lo guardo en una lista
        Se retorna la lista de participantes 
    """

    participants = []
    participants_keys = [
        "ci",
        "first_last_name",
        "second_last_name",
        "first_name",
        "char_second_name",
        "gender",
        "age",
        "hours",
        "minutes",
        "seconds"
    ]

    for line in file.readlines():
        participant_value = line.strip().strip('\n').split(',')
        if len(participant_value) != len(participants_keys):
            raise IncompleteParticipantData('ERROR! el archivo no tiene los campos requeridos')
        participant = Participant(participant_value[0], participant_value[1], 
                                  participant_value[2], participant_value[3], 
                                  participant_value[4], participant_value[5], 
                                  participant_value[6], participant_value[7], 
                                  participant_value[8], participant_value[9])
        participants.append(participant)
    return participants





def load(filename: str, data: dict) -> dict:
    """
        Recibe como parametros el nombre del archivo y la data donde se almacera la lectura de ese archivo
        valida que el nombre del archivo no este vacio, abre el archivo carga la data obtenida del archivo
        se filtra la data obtenida y retorna los datos.
    """
    
    try:
        if filename is None:
            raise FileNotFoundError('ERROR! El nombre del archivo esta vacio.')
        with open(filename, "r") as file:
            if(isnotEmpty(file)):
                data_participants = get_data(file)
                data["participants"] = data_participants
                #Filtrar los datos del archivo
                data = filter_data(data)
                file.seek(0,0)
    except FileNotFoundError:
        print('ERROR! el archivo no existe')
    except EmptyFile as e:
        print(e.__str__())
    except IncompleteParticipantData as e:
        print(e.__str__())
    except ValueError:
        print('ERROR! el archivo ingresado no es de texto')
    else:
        print('\tArchivo cargado exitosamente !!')
    finally:
        return data

    




   