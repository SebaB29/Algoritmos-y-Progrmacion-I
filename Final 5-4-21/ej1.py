class NodoABB:
    def __init__(self, dato, izq=None, der=None):
        self.dato = dato
        self.izq = izq
        self.der = der

    def _buscar(self, dato_actual, dato_buscado):
        """
        -Recibe: el dato buscado y el dato actual.
        -Devuelve: el dato si se encuentra o None en caso contrario.
        """
        if dato_buscado < dato_actual:
            return self._buscar(self.izq.dato, dato_buscado)
        elif dato_buscado > dato_actual:
            return self._buscar(self.der.dato, dato_buscado)
        elif dato_buscado == dato_actual:
            return dato_actual
        return

    def buscar(self, dato):
        # HACER: implementar la funcion
        return self._buscar(self.dato, dato)
            

def pruebas():
    # el árbol ejemplo del enunciado
    n1 = NodoABB(1)
    n4 = NodoABB(4)
    n7 = NodoABB(7)
    n13 = NodoABB(13)
    n14 = NodoABB(14, izq = n13)
    n10 = NodoABB(10, der = n14)
    n6 = NodoABB(6, izq = n4, der = n7)
    n3 = NodoABB(3, izq = n1, der = n6)
    raiz = NodoABB(8, izq = n3, der = n10)

    nodo = raiz.buscar(6)
    assert(nodo is n6)

    # OPCIONAL: pruebas adicionales. Ejemplo: buscar un valor que no exista

    from os import path
    print(f"{path.basename(__file__)}: OK")

pruebas()
