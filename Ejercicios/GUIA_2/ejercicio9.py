def fichas_domino():
    '''Imprime todas las fichas de domino'''

    numIzq = 0
    numDer = 0

    while numIzq <= 6:
        print(f'{numIzq}|{numDer}')
        numDer += 1

        if numDer > 6:
            numIzq += 1
            numDer = numIzq

fichas_domino()

# Otra forma

def mostrar_fichas_domino():
    '''Imprime todas las fichas de domino'''

    incrementador = 0

    for i in range(7):
        for j in range(incrementador,7):
            print(f'{i}|{j}')
        incrementador += 1

mostrar_fichas_domino()