def ingresar_direccion_ipv4():
    """
    Le pide al usuario que ingrese una direccion IPv4, si es valida la devuelve, sino lo es le vuelve a pedir
    que la ingrese hasta que sea valida.
    """

    direccion_ipv4 = []
    
    while not len(direccion_ipv4) == 4:

        direccion_ipv4.clear()
        direccion = (input("Ingrese una direccion ipv4: ")).split(".")

        for num in direccion:
            if num.isdigit():
                if int(num) in range(255 + 1):
                    direccion_ipv4.append(num)

    return ".".join(direccion_ipv4)


def encriptar_cadena(cadena, num):
    """
    -Recibe: una cadena y un numero
    -Devuelve: la encriptacion de la cadena en formato rotN
    """

    from string import ascii_lowercase

    cadena = list(cadena)

    for pos_c, caracter in enumerate(cadena):
        for pos_l, letra in enumerate(ascii_lowercase):
            if caracter == letra and (pos_l + num) <= len(ascii_lowercase):
                cadena[pos_c] = ascii_lowercase[pos_l + num]
            elif caracter == letra and (pos_l + num) > len(ascii_lowercase):
                cadena[pos_c] = ascii_lowercase[abs((pos_l + num) - len(ascii_lowercase))]
    
    return "".join(cadena)


def diferencia_listas(lista1, lista2):
    """
    -Recibe: dos listas, dentro de cada lista no se repiten elementos
    -Dvuelve: una nueva lista con los elementos que aparecen en la primera lista pero no en la segunda lista
    """

    diferencia = []

    for elem in lista1:
        if elem not in lista2:
            diferencia.append(elem)
    
    return diferencia