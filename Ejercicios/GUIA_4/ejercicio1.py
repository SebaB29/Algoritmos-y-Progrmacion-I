def par_impar(n):
    '''Recibe un numero n y devuelve True si es par, False en caso contrario'''

    if n % 2 == 0:
        return True
    return False

def primo(n):
    '''Recibe un numero n, devuelve True si es primo y False si no lo es'''

    for num in range(2, n):
        if n % num == 0:
            return False
    return True