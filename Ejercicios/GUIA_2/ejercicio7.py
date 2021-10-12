def es_natural(cantidad):
    '''Recibe un numero, determina si es natural y devuelve True si lo es'''

    if cantidad > 0:
        return True
    return False

def numeros_triangulares():
    '''Le pide al usario un numero que determina la cantidad de numeros triangulares para imprimirlos'''

    cantidad = int( input( 'Diga un numero: ') )

    if es_natural(cantidad):
        
        numTriangular = 0
        for i in range(1, cantidad + 1):
            numTriangular += i
            print( f'{i} - {numTriangular}' )

numeros_triangulares()