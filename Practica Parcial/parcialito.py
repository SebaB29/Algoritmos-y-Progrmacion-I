### Ejercicio 1

def filtrar_terminados_en_cero(numeros):
    '''Recibe una lista de numeros y devuelve una nueva lista con numeros terminados en cero'''

    terminados_en_cero = []

    for num in numeros:
        if (num % 10) == 0:
            terminados_en_cero.append( num )
    
    return terminados_en_cero

### Ejercicio 2

def separar_input_en_palabras(): # Forma de hacerlo con While True
    '''
    Le pide al usuario que ingrese cadenas hasta que ingrese una cadena vacia.
    Devuelve una lista con las palabras ingresadas.
    '''

    sumatoria = ''

    while True:
        entrada = input('Ingresar cadena: ')
        sumatoria += entrada
        if not entrada:
            break
    return sumatoria.split()

def separar_input_en_palabras2(): # Forma de hacerlo con centinela
    '''
    Le pide al usuario que ingrese cadenas hasta que ingrese una cadena vacia.
    Devuelve una lista con las palabras ingresadas.
    '''

    sumatoria = ''
    entrada = "."

    while not entrada:
        entrada = input('Ingresar cadena: ')
        sumatoria += entrada
    return sumatoria.split()

### Ejercicio 3

def maximo_de_columna(matriz):
    '''Recibe una matriz y devuelve una lista con los maximos de cada columna'''
    pass