"""
Escribir una función que reciba una lista de números y un número n 
e imprima todos los números de la lista en n columnas ordenados por fila.

Por ejemplo, si recibe: [1,2,3,4,5,6] y 3 Debe imprimir:

1 2 3
4 5 6 
"""

def imprimir_matriz(numeros, n_columnas):
    """
    -Recibe: una lista de numeros
    -Imprime: los numeros de la lista en n_columnas ordenados por fila
    """

    numeros.sort()
    for i, numero in enumerate( numeros ):
        if i == n_columnas:
            print()
        print(numero, end=' ')

imprimir_matriz([2,1,3,5,4,6], 3)