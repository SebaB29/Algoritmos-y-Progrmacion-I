def fichas_juego(cantidadFichas):
    '''Imprime todas las fichas de domino'''

    numIzq = 0
    numDer = 0

    while numIzq <= cantidadFichas:
        print(f'{numIzq}|{numDer}')
        numDer += 1

        if numDer > cantidadFichas:
            numIzq += 1
            numDer = numIzq

# Otra forma

def mostrar_fichas_domino(cantidadFichas):

    incrementador = 0

    for i in range(cantidadFichas + 1):
        for j in range(incrementador, cantidadFichas + 1):
            print(f'{i}|{j}')
        incrementador += 1