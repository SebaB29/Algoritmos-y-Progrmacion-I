"""
Escribir una función que recibe una lista de números y devuelve una nueva lista con los elementos reordenados,
de forma tal que todos los números pares aparecen antes que todos los números impares. 
No es necesario mantener el orden relativo de los elementos originales. Ejemplo: f([3,5,2,6,18,7,40,11]) → [2,6,18,40,11,3,5,7]
"""

def ordenar_pares_e_impares(numeros):
    """
    -Recibe: una lista de numeros
    -Devuelve: una nueva lista con los elementos reordenados de forma que los pares aparecen primero
    """

    nueva_lista = []

    for n in numeros:
        if n % 2 == 0:
            nueva_lista.insert(0, n )
        else:
            nueva_lista.append( n )

    print( nueva_lista )

ordenar_pares_e_impares([3,5,2,6,18,7,40,11])    