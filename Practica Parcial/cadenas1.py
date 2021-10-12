from string import ascii_lowercase

def es_pangrama(cadena):
    """
    -Recibe: una cadena
    -Devuelve:
    - True,  si la cadena contiene todas las letras del alfabeto
    - False, en caso contrario
    """

    for letra in ascii_lowercase:
        if letra not in cadena:
            return False
    return True

cadena = 'the quick brown fox jumps over the lazy dog'
print(es_pangrama(cadena))