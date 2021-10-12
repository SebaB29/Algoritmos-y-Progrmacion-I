
# HACER: implementar las funciones

class Libro:
    def __init__(self, titulo, autor, año):
        self.titulo = titulo
        self.autor = autor
        self.año = año

    def __eq__(self, otro):
        """
        -Recibe: otro libro.
        -Devuelve: True si las características de los libros son iguales(título, autor, año) y False en caso contrario.
        """
        return (self.titulo, self.autor, self.año) == (otro.titulo, otro.autor, otro.año)

def ordenar_libros(libros):
    """
    -Recibe: una lista de libros.
    Ordena la lista alfabéticamente según sus títulos.
    """
    for posicion_libro in range(len(libros) - 1):
        posicion_minimo_libro = buscar_minimo(libros, posicion_libro)
        libros[posicion_minimo_libro], libros[posicion_libro] = libros[posicion_libro], libros[posicion_minimo_libro]

def buscar_minimo(lista, i):
    """Devuelve la posición del elemento mínimo en lista"""
    posicion_minimo = i
    while i < len(lista):
        if lista[i].titulo < lista[posicion_minimo].titulo:
            posicion_minimo = i
        i += 1
    
    return posicion_minimo

def buscar_libro(libros, titulo):
    """
    -Recibe: una lista de libros y el título de un libro.
    -Devuelve: los datos del libro buscado o NOne en caso de que no esté en la lista.
    """
    return busqueda_binaria(libros, titulo, 0, len(libros) - 1)

def busqueda_binaria(lista, elemento, desde, hasta):
    """
    -Recibe: una lista, un elemento, el primer indice y el último indice de la lista.
    Busca el elemento en la lista.
    -Devuelve: el elemento en caso de estar en la lista y None en caso conrtario.
    """
    if desde > hasta:
        return 
    medio = (hasta + desde) // 2
    if lista[medio].titulo == elemento:
        return lista[medio]
    if lista[medio].titulo > elemento:
        return busqueda_binaria(lista, elemento, desde, medio - 1)
    return busqueda_binaria(lista, elemento, medio + 1, hasta)

def pruebas():

    libros = [
        Libro("The Sittaford Mystery", "Agatha Christie", 1931),
        Libro("The Seven Dials Mystery", "Agatha Christie", 1929),
        Libro("The Murder at the Vicarage", "Agatha Christie", 1930),
        Libro("The Mystery of the Blue Train", "Agatha Christie", 1928),
        Libro("The Floating Admiral", "Agatha Christie", 1931),
        Libro("Giant's Bread", "Agatha Christie", 1930),
    ]

    ordenar_libros(libros)

    assert libros == [
        Libro("Giant's Bread", "Agatha Christie", 1930),
        Libro("The Floating Admiral", "Agatha Christie", 1931),
        Libro("The Murder at the Vicarage", "Agatha Christie", 1930),
        Libro("The Mystery of the Blue Train", "Agatha Christie", 1928),
        Libro("The Seven Dials Mystery", "Agatha Christie", 1929),
        Libro("The Sittaford Mystery", "Agatha Christie", 1931),
    ]

    libro = buscar_libro(libros, "The Floating Admiral")
    assert libro is libros[1]

    # OPCIONAL: pruebas adicionales. Ejemplo: buscar un libro que no exista

    from os import path
    print(f"{path.basename(__file__)}: OK")

pruebas()
