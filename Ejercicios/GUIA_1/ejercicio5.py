def factorial(num):
    '''Recibe un numero e imprime su factorial'''
    
    x = 1
    for i in range(2, num+1):
        x *= i

    print(f'El factorial de { num } es { x }')