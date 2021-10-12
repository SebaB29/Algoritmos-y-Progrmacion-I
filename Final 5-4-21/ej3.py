# HACER: implementar las funciones
import csv

def matriz_guardar(ruta, matriz):
    """
    -Recibe: la ruta del archivo y una matriz
    Guarda la matriz en el archivo pasado por parámetro
    """
    with open(f"{ruta}.csv", "w", newline="") as archivo:
        archivo_csv = csv.writer(archivo)
        for fila in matriz:
            archivo_csv.writerow(fila)

def matriz_cargar(ruta):
    """
    -Recibe: la ruta del archivo
    -Devuelve: la matriz guardada en el archivo
    """
    with open(ruta) as archivo:
        archivo_csv = csv.reader(archivo)
        return [[int(numero) for numero in linea] for linea in archivo_csv]

def pruebas():
    matriz = [
        [1, 2, 3],
        [4, 5, 6],
    ]

    # HACER:
    # - llamar a matriz_guardar
    # - llamar a matriz_cargar
    # - verificar que la matriz cargada es idéntica a la original

    from os import path
    print(f"{path.basename(__file__)}: OK")

pruebas()