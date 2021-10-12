def par_o_impar(numEntero):
    '''Recibe un numero entero, devuelve 1 si el numero es impar y 0 si es par'''

    if numEntero % 2 == 0:
        return 0
    return 1

def impar_o_par(numEntero):
    '''Recibe un numero entero, devuelve 1 si el numero es impar y 0 si es par'''

    if numEntero % 2 != 0:
        return 0
    return 1

def cantidad_digitos(numEntero):
    '''Recibe un numero entero y devuelve la cantidad de digitos que tiene'''

    return 'Cantidad de digitos:', len ( str (numEntero) )

def multiplo_diez_menor(num):
    '''Recibe un numero y devuelve el primer numero multiplo de diez inferior al numero recibido'''

    for i in range(num, 0, -1):
        if i % 10 == 0:
            return i