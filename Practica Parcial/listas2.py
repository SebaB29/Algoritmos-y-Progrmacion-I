def snakecase_a_camelcase(cadena):
    """
    -Recibe: una cadena escrita en sanke_case
    -Devuelve: la cadena escrita en CamelCase
    """

    cadena = cadena.split("_")

    for i, palabra in enumerate( cadena ):
        cadena[i] = palabra.capitalize()
        
    return "".join(cadena)

print()
print(snakecase_a_camelcase("hoy_es_el_parcial"))