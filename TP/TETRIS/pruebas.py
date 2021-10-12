pos = ((0, 0), (1, 0), (0, 1), (1, 1))
ANCHO_JUEGO = 9

def trasladar(pieza, dx, dy): # Funciona

    posiciones = list(pieza)
    for i, tupla in enumerate( posiciones ):
        posiciones[i] = list( tupla )
        posiciones[i] = tuple( (posiciones[i][0] + dx, posiciones[i][1] + dy) )


    print( tuple( posiciones ) )

def matriz(fil, col): # Funciona

    # juego = []

    # for fila in range(fil):
    #     juego.append([])
    #     for columna in range(col):
    #         juego[fila].append("0")
    
    juego = [[ "0" for columna in range(col)] for fila in range(fil)]
    
    for f in range(len(juego)):
        for c in range(len(juego[f])):
            print(juego[f][c],end= "")
        print()

matriz(10, 10)

def hay_superficie(juego, x, y):
    """
    Devuelve True si la celda (x, y) está ocupada por la superficie consolidada.
    
    La coordenada (0, 0) se refiere a la posición que está en la esquina 
    superior izquierda de la grilla.
    """
    
    """ if not juego[x][y]:
        return False """

    return bool(juego[x][y])

x = ((0, 0), (1, 0), (0, 1), (1, 1))

def mover(x, dx, dy):

    nueva = ()

    for pos in x:
        nueva += ((pos[0] + dx, pos[1] + dy), )
    
    print(nueva)

def terminar():

    juego = [['2','2','2'],['g','2','w']] 

    if juego != []:
        for columna in juego[0]:
            if columna != "":
                return True
    return False