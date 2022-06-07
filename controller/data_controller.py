

from datetime import  time
import os

# Ordenar los datos recibidos por el archivo
def filter_data(data: dict) -> dict:
    """
        Recibe como parametro los datos obtenidos desde el archivo

        Se encargara de retornar los datos filtrados
    """
    data= time_order(data)
    data['total'] = total_participants(data) 
    data = sex_group(data)
    data = avg_juniors_time(data)
    data = avg_seniors_time(data)
    data = avg_masters_time(data)
    return data

# Ordenar Participantes por mejor tiempo
def time_order(data: dict) -> dict:
    """
        Se encarga de ordenar la lista de participantes por mejor tiempo.
        Y retorna los datos ordenados del participante con mejor tiempo hasta el participante con peor tiempo.  
    """
    participants = data['participants']
    newlist = sorted(participants, key=lambda x: x.time)
    data['participants'] = newlist
    return data
    


# Total de Participantes
def total_participants(data: dict) -> int:
    """
        Devuelve la cantidad total de participantes
    """
    return len(data['participants'])


# Separa por genero y grupo etario
def sex_group(data: dict) -> dict:
    """
        Separa los participantes por grupo etario(Junior, Senior, Master) y sexo(Masculino, Femenino)
        Retorna los datos filtrados
    """
    data['juniors_men'] = [i for i in data['participants'] if i.gender.upper() == 'M' and i.etarian_group == "Juniors"]
    data['juniors_women'] = [i for i in data['participants'] if i.gender.upper() == 'F' and i.etarian_group == "Juniors"]
    data['seniors_men'] = [i for i in data['participants'] if i.gender.upper() == 'M' and i.etarian_group == "Seniors"]
    data['seniors_women'] = [i for i in data['participants'] if i.gender.upper() == 'F' and i.etarian_group == "Seniors"]
    data['masters_men'] = [i for i in data['participants'] if i.gender.upper() == 'M' and i.etarian_group == "Masters"]
    data['masters_women'] = [i for i in data['participants'] if i.gender.upper() == 'F' and i.etarian_group == "Masters"]
    return data

# Tiempo promedio juniors
def avg_juniors_time(data: dict) -> dict:
    """
        Hace el calculo del tiempo promedio de los participantes Juniors
    """
    total_seconds_women = sum(x.total_time for x in data['juniors_women'])
    avg_seconds = total_seconds_women / len(data['juniors_women'])
    minutes, seconds = divmod(avg_seconds,60)
    hours, minutes = divmod(minutes,60)
    data['avg_juniors_women'] = time(round(hours),round(minutes),round(seconds))

    total_seconds_men = sum(x.total_time for x in data['juniors_men'])
    avg_seconds = total_seconds_men / len(data['juniors_men'])
    minutes, seconds = divmod(avg_seconds,60)
    hours, minutes = divmod(minutes,60)
    data['avg_juniors_men'] = time(round(hours),round(minutes),round(seconds))

    return data

# Tiempo promedio seniors
def avg_seniors_time(data: dict) -> dict:
    """
        Hace el calculo del tiempo promedio de los participantes Seniors
    """
    total_seconds_women = sum(x.total_time for x in data['seniors_women'])
    avg_seconds = total_seconds_women / len(data['seniors_women'])
    minutes, seconds = divmod(avg_seconds,60)
    hours, minutes = divmod(minutes,60)
    data['avg_seniors_women'] = time(round(hours),round(minutes),round(seconds))

    total_seconds_men = sum(x.total_time for x in data['seniors_men'])
    avg_seconds = total_seconds_men / len(data['seniors_men'])
    minutes, seconds = divmod(avg_seconds,60)
    hours, minutes = divmod(minutes,60)
    data['avg_seniors_men'] = time(round(hours),round(minutes),round(seconds))

    return data

# Tiempo promedio masters
def avg_masters_time(data: dict) -> dict:
    """
        Hace el calculo del tiempo promedio de los participantes Masters
    """
    total_seconds_women = sum(x.total_time for x in data['masters_women'])
    avg_seconds = total_seconds_women / len(data['masters_women'])
    minutes, seconds = divmod(avg_seconds,60)
    hours, minutes = divmod(minutes,60)
    data['avg_masters_women'] = time(round(hours),round(minutes),round(seconds))

    total_seconds_men = sum(x.total_time for x in data['masters_men'])
    avg_seconds = total_seconds_men / len(data['masters_men'])
    minutes, seconds = divmod(avg_seconds,60)
    hours, minutes = divmod(minutes,60)
    data['avg_masters_men'] = time(round(hours),round(minutes),round(seconds))

    return data

#Limpiar Pantalla dependiendo del SO en que se este ejecutando
def clearScreen() -> None: 
    """
        Limpia pantalla dependiendo del SO
    """
    if os.name == "posix":
        os.system ("clear")
    elif os.name == "ce" or os.name == "nt" or os.name == "dos":
        os.system ("cls")

