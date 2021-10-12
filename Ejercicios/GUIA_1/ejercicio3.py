from math import pi, sqrt

def perimetro_rectangulo(base, altura):
    '''Recibe la base y altura de un rectangulo y calcula su perimetro'''

    return 2 * ( base + altura )

def area_rectangulo(base, altura):
    '''Recibe la base y altura de un rectangulo y calcula su area'''

    return base * altura

def perimetro_circulo(radio):
    '''Recibe el radio de un circulo y devuelve su perimetro'''

    return 2 * pi * radio

def area_circulo(radio):
    '''Recibe el radio de un circulo y devuelve su area'''

    return pi * ( radio ** 2 )

def volumen_esfera(radio):
    '''Recibe el radio de una esfera y devuelve su volumen'''

    return ( 4/3 ) * pi * ( radio ** 2 )

def hipotenusa_triangulo(cateto1, cateto2):
    '''Recibe los catetos de un triangulo y calcula su hipotenusa'''

    return sqrt( ( cateto1 ** 2 ) + ( cateto2 ** 2 ))