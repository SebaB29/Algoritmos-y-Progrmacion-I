def imprimir_mil_veces():
    '''Le pide al usuario una palabra y la imprime mil veces'''

    palabra = input('Diga una palabra: ')

    for i in range( 1001 ):
        print('@',palabra, end=' ')

imprimir_mil_veces()