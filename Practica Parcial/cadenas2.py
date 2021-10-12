def empieza_con_letra(nombres, letra):
    """
    -Recibe: lista de nombres y una letra
    -Devuelve: nueva lista con los nombres que comiencen con la letra recibida
    """

    lista_nombres = []

    for nombre in nombres:
        if nombre[0] in ( letra.lower(), letra.upper() ):
            lista_nombres.append(nombre)
    
    return lista_nombres