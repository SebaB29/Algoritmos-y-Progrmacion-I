def norma(x=0, y=0, z=0):
    '''Recibe las coordenadas de un vector en R3 y devuelve su norma'''

    return (x ** 2 + y ** 2 + z ** 2) ** 0.5

def diferencia_vectores(x1=0, y1=0, z1=0, x2=0, y2=0, z2=0):
    '''Recibe las coordenadas de dos vectores y devulve el resultado de su resta'''

    return (x1 - x2, y1 - y2, z1 - z2)

def producto_vectorial(x1=0, y1=0, z1=0, x2=0, y2=0, z2=0):
    '''Recibe las coordenadas de dos vectores y devulve el resultado de su producto vectorial'''

    return (y1 * z2 - z1 * y2, z1 * x2 - x1 * z2, x1 * y2 - y1 * x2)

def area_triangulo(x1=0, y1=0, z1=0, x2=0, y2=0, z2=0, x3=0, y3=0, z3=0):
    '''Recibe las coordenadas de tres puntos y devuelve el area del triangulo que conforman'''

    x4, y4, z4 = diferencia_vectores(x1, y1, z1, x2, y2, z2) # Calculo el vector AB
    x5, y5, z5 = diferencia_vectores(x1, y1, z1, x3, y3, z3) # Calculo el vector AC

    x, y, z = producto_vectorial(x4, y4, z4, x5, y5, z5) # Calculo el producto vectorial entre AB y AC

    return norma(x, y, z) / 2

def area_cuadrilatero(x1, y1, x2, y2, x3, y3, x4, y4):
    '''Recibe las coordenadas de cuatro puntos y devuelve el area del cuadrilatero que conforman'''

    pass