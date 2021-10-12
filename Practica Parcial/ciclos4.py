"""
Escribir una función que reciba una cadena y 
devuelva el resultado de reemplazar todas las apariciones 
de la primera letra (ignorando mayúsculas o minúsculas) con un asterisco.

Nota: no se puede usar la funcion str.replace() de Python.
"""

def reemplazar_letra(cadena):
    """
    -Recibe: una cadena
    -Devuelve el resultado de reemplazar las apariciones de la primer letra con un asterisco
    """

    primera_letra = cadena[0]
    cadena = cadena.split()

    for i, palabra in enumerate( cadena ):
        palabra = list( palabra )
        for j, letra in enumerate( palabra ):
            if letra in ( primera_letra.lower(), primera_letra.upper() ):
                palabra[j] = "*"
        cadena[i] = "".join(palabra)
    cadena = " ".join(cadena)

    return cadena