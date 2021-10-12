def invertir_letras(cadena):
    """
    -Recibe: un cadena de palabras
    -Devuelve: una cadena con las letras de las palabras invertidas
    """

    cadena = cadena.split(" ")

    for i, palabra in enumerate( cadena ):
        cadena[i] = palabra[::-1]
    
    return " ".join(cadena)

cadena = "Qué día tan bonito"
print()
print(invertir_letras(cadena))