def imprimir_factoriales():
    '''Le pide al usuario numeros, calcula sus factoriales utilizando la funcion factorial importada e imprime el resultado junto con el numero utilizado'''

    num1 = int( input( 'Diga un numero: ') )
    num2 = int( input( 'Diga otro numero: ') )
    num3 = int( input( 'Diga otro numero: ') )

    print(f'Numero: {num1} - Factorial: {factorial(num1)}')
    print(f'Numero: {num2} - Factorial: {factorial(num2)}')
    print(f'Numero: {num3} - Factorial: {factorial(num3)}')