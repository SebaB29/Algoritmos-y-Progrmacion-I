def monto_final(pesos, interes, anios):
    '''Recibe la cantidad de pesos, la tasa de interes y la cantidad de años y devuelve el monto final a obtener'''

    return pesos * (1 + interes / 100) ** anios