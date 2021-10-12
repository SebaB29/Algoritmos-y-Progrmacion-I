from ejercicio1 import *

def sumar_tiempo():
    '''Le pide al usuario dos intervalos de tiempo expresados en horas, minutos y segundos, los suma y devuelve la cantidad de tiempo'''

    print('Ejemplo: horas.minutos.segundos')

    hora1, min1, seg1 = input('Diga un intervalo de tiempo: ').split('.')
    hora2, min2, seg2 = input('Diga otro intervalo de tiempo: ').split('.')

    tiempo1 = cantidad_segundos(int(hora1), int(min1), int(seg1))
    tiempo2 = cantidad_segundos(int(hora2), int(min2), int(seg2))

    tiempoTotal = tiempo1 + tiempo2

    print(f'Tiempo total {horas_minutos_segundos(tiempoTotal)}')