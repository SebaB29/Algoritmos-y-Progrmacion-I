def en_ambas_secuencias(secuencia1, secuencia2):
    """
    -Recibe: dos secuencias
    -Devuelve: una lista con los elementos que se encuentran en ambas secuencias
    """

    elementos_comunes = []
    for elem in secuencia1:
        if elem in secuencia2 and elem not in elementos_comunes:
            elementos_comunes.append(elem)
    
    return elementos_comunes

secuencia1 = [7, 9, 7, 1]
secuencia2 = [6, 9, 7]
print(en_ambas_secuencias(secuencia1, secuencia2))