from ejercicio1 import monto_final

def main():
    print('Calcular monto final')

    pesos = int( input( 'Cantidad de pesos: ') )
    interes = int( input( 'Tasa de interes: ') )
    años = int( input( 'Cantidad de años: ') )

    print('El monto final a obtener es $', monto_final(pesos, interes, años))

main()