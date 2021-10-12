def cantidad_segundos(horas, minutos, segundos):
    '''Recibe una cantidad de horas, minutos y segundos y devuelve la equivalencia en segundos'''

    horas *= 3600 # Convierto las horas a segundos
    minutos *= 60 # Convierto los minutos a segundos

    return horas + minutos + segundos

def horas_minutos_segundos(segundos):
    '''Recibe una cantidad de segundos y devuelve lo equivalente en horas, minutos y segundos'''

    horas = segundos // 3600
    minutos = (segundos % 3600) // 60
    segundo = (segundos % 3600) % 60

    return f'Horas: {horas}h   Minutos: {minutos}min  Segundos: {segundo}s'