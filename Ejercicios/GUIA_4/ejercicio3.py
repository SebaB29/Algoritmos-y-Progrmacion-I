def matriz_identidad(dimension):
    """"""

    matriz = []

    for i in range( dimension ):
        matriz.append( [] )
        for num in range( dimension ):
            matriz[i].insert( dimension, 0 )
            matriz[i].insert( dimension - 1, 1 )
            print(matriz[i][num], end= "")
        print()

matriz_identidad(2)