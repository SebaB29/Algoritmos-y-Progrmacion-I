def mayor_producto(num1, num2, num3, num4):
    '''Recibe cuatro numeros y devuelve el mayor producto entre ellos'''

    x = 0

    for i in [num2, num3, num4]:
        if num1 * i > x:
            x = num1 * i

    for i in [num3, num4]:
        if num2 * i > x:
            x = num2 * i
    
    if num3 * num4 > x:
        x = num3 * num4
    
    return x