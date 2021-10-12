def operaciones_basicas(num1, num2):
    '''Recibe dos numeros, realiza las operaciones matematicas basicas con esos numeros e imprime los resultados'''

    print('Resultado suma:',  num1 + num2 )
    print('Resultado resta:',  num1 - num2 )
    print('Resultado multiplicacion:', num1 * num2 )
    print('Resultado division:', num1 / num2 )

def tabla_producto(num):
    '''Recibe un numero e imprime sus productos'''

    for i in range(10):
        print( num * i )