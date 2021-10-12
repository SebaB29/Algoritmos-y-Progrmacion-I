from vectores import *

def area_triangulo(x1, y1, z1, x2, y2, z2, x3, y3, z3):
    '''Recibe las coordenadas de tres puntos y devuelve el area del triangulo que conforman'''

    x4, y4, z4 = diferencia(x1, y1, z1, x2, y2, z2) # Calculo el vector AB
    x5, y5, z5 = diferencia(x1, y1, z1, x3, y3, z3) # Calculo el vector AC

    x, y, z = producto_vectorial(x4, y4, z4, x5, y5, z5) # Calculo el producto vectorial entre AB y AC

    return norma(x, y, z) / 2

assert area_triangulo(1,2,3,4,5,6,7,8,9) == 0.0
assert area_triangulo(9,8,7,6,5,4,3,2,1) == 0.0
assert area_triangulo(1,2,3,0,0,0,1,2,3) == 0.0