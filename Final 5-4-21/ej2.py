class RegistroDeDesplazamiento:
    # HACER: implementar los metodos
    def __init__(self, n):
        """
        -Recibe: la cantidad de bits del registro(n)
        Crea el registro con n bits
        """
        self.registro_bits = [0 for i in range(n)]
    
    def rshift(self, bit):
        """
        -Recibe: un bit
        Agrega el bit a la izquierda del registro, desplazando el resto hacia la derecha y eliminando el últmo bit
        -Devuelve: el bit eliminiado
        """
        self.registro_bits.insert(0, bit)
        return self.registro_bits.pop()
    
    def lshift(self, bit):
        """
        -Recibe: un bit
        Agrega el bit a la derecha del registro, desplazando el resto hacia la izquierda y eliminando el primer bit
        -Devuelve: el bit eliminiado
        """
        self.registro_bits.append(bit)
        return self.registro_bits.pop(0)
    
    def __str__(self):
        """Devuelve el registro de bit en forma de cadena"""
        return "".join([str(bit) for bit in self.registro_bits])


def pruebas():
    r = RegistroDeDesplazamiento(4)

    assert str(r) == '0000'
    assert r.rshift(0) == 0
    assert str(r) == '0000'
    assert r.rshift(1) == 0
    assert str(r) == '1000'
    assert r.rshift(0) == 0
    assert str(r) == '0100'
    assert r.rshift(0) == 0
    assert str(r) == '0010'
    assert r.rshift(0) == 0
    assert str(r) == '0001'
    assert r.rshift(0) == 1
    assert str(r) == '0000'
    assert r.rshift(0) == 0
    assert str(r) == '0000'

    # OPCIONAL: pruebas adicionales (ej: probar lshift)


    from os import path
    print(f"{path.basename(__file__)}: OK")

pruebas()
