""" 
Escribir una función que recibe un número entero $n$ e imprime un tablero de ajedrez de tamaño $N \times N$. Por ejemplo, el tablero deberá imprimirse de la siguiente forma para un tablero de $N = 3$:

b n b
n b n
b n b
Nota: b denota un casillero blanco, n denota un casillero negro. 
"""

def crear_tablero_ajedrez(num):
    """
    -Recibe: un numero entero que representa la dimension del tablero
    -Imprime: tablero de ajedrez
    """
    
    color = 'b'

    for fila in range( num ):
        for columna in range( num ):
            print(color, end=" ")
            if color == 'b':
                color = 'n'
            else:
                color = 'b'
        print()

crear_tablero_ajedrez(3)