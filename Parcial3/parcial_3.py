from pilas_colas_listas import *

class ColaDistribuidora:
    def __init__(self, identificadores, funcion):
        self.ids = identificadores
        self.funcion = funcion
    
    def encolar(self, elemento):
        """
        -Recibe un elemento
        Aplica self.funcion al elemento y segun el identificador obtenido lo encola
        """
        self.ids.encolar(self.funcion(elemento))
    
    def desencolar(self, identificador):
        """
        Desencola y deveulve el elemento desencolado al frente de la cola
        """
        if self.ids.esta_vacia():
            raise ValueError("No hay identificadores")

        elemento = self.ids.desencolar()
        self.ids.encolar(self.funcion(elemento))
    
    def esta_vacia(self):
        return len(self.ids) == 0

class ListaEnlazada:
    def __init__(self):
        self.primero = None
    
    def empezar_con_menor(self):
        """..."""
        menor = self.primero
        anterior_al_menor = self.primero
        anterior = None
        actual = self.primero
        while actual:
            if actual < menor:
                menor = actual
            

            actual = actual.proximo
            if self.primero.proximo and actual == self.primero.proximo:
                anterior = self.primero
            else:
                anterior = anterior.proximo
        
        if anterior_al_menor and menor:
            anterior_al_menor.proximo = menor.proximo
        menor.proximo = self.primero
        self.primero = menor

### EJERCICIO 3
"""
NO es ninguna de las dos opciones ya que:

Cola: < 1, 2, 3, 4, 5 >
Al ser encolados de menor a mayor el primero en ser desencolado es el 1 ya que fue el primero en ser encolado.

Luego en el Paso 1 se apila en la Pila 1:
    Paso 1: Pila 1: || 1, 2, 3, 4, 5 > <-Tope

En el Paso 2: se desapila la Pila 1, comenzando con el 5 ya que fue el ultimo en apilar y lo apila en la Pila 2
    Paso 2: Pila 2: || 5, 4, 3, 2, 1 > <-Tope 

En el Paso 3 desapila la Pila 2 empezando con el 1 que fue el ultimo en apilar, y los imprime
    Paso 3: Imprime 1 2 3 4 5
"""