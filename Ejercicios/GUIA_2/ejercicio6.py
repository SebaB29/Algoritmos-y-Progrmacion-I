def imprimir_pares():
    '''Le pide al usuario dos numeros e imprime todos los numeros pares que hay entre esos numeros'''

    num1 = int( input( 'Diga un número: ') )
    num2 = int( input( 'Diga otro número: ') )

    mayor = max(num1, num2)
    menor = min(num1, num2)

    for i in range(menor + 1, mayor):
        if i % 2 == 0:
            print(i)