# EJERCICIO 1
ruta_Archivo = "C:/Users/Seba.Nelly-PC.000/Desktop/archivo.txt"
def ver_personas_en_contacto(ruta_archivo, nombre_persona):
    """
    -Recibe: la ruta del archivo y el nombre de una presona
    -Devuelve: un conjunto con los nombres de las personas con las que estuvo en contacto
    """
    with open(ruta_archivo) as archivo:
        personas = archivo.readlines()

    personas_en_contacto = set()
    datos_persona = []
    for i, persona in enumerate(personas):
        personas[i] = persona.rstrip("\n")
        personas[i] = persona.split(";")
        if nombre_persona in personas[i]:
            datos_persona.append((personas[i][1], personas[i][2]))

    for persona in personas:
        for lugar, momento in datos_persona:
            if persona[1] == lugar and persona[2] == momento and persona[0] != nombre_persona:
                personas_en_contacto.add(persona[0])
    
    return personas_en_contacto

# EJERCICIO 2
def gimnasios_cercanos(ruta_archivo, gimnasios):
    """
    -Recibe: la ruta de un archivo y diccionario con gimnasios
    Escribe en otro archivo los datos del pokemon con el gimnasio mas cercano
    """
    with open(ruta_archivo) as archivo:
        with open(ruta_archivo_salida, "a") as archivo_salida:
            for linea in archivo:
                linea = linea.split(";")
            for gimnasio in gimnasios:
                distancia = calcular_distancia(linea[2], gimnasios[gimnasio])
                archivo_salida.write(f"{linea[0]}; {linea[1]}; {distancia}")

def calcular_distancia(distancia_1, distancia_2):
    """
    -Recibe: dos tuplas con coordenadas x e y
    -Devuelve: la distancia entre ellas
    """
    return distancia_1[0] - distancia_2[0] + distancia_1[1] - distancia_2[1]

# EJERCICIO 3
class App:

    def __init__(self, nombre_app, espacio_app):
        """
        Recibe: el objeto App, el nombre de la app y el espacio que ocupa
        Inicializa el objeto App
        """
        self.nombre_app = nombre_app
        self.espacio_app = espacio_app

class Smartphone:

    def __init__(self, modelo, memoria_total):
        """
        Recibe: el objeto Smartphone, el modelo y la memoria
        Inicializa el objeto Smartphone
        """
        self.modelo = modelo
        self.memoria_total = memoria_total
        self.app_instaladas = []
    
    def instalar_app(self, aplicacion):
        """
        -Recibe una aplicacion y el objeto Smartphone
        Instala la app del Smartphone

        """
        if not aplicacion.nombre_app in self.app_instaladas:
            if aplicacion.espacio_app < self.memoria_total:
                self.memoria_total -= aplicacion.espacio_app
                self.app_instaladas.append(aplicacion.nombre_app)
            else:
                raise Exception("El smartphone no cuenta con el espacio necesario")
        else:
            raise Exception("La app ya está instalada")

    def desinstalar_app(self, aplicacion):
        """
        -Recibe una aplicacion y el objeto Smartphone
        Desinstala la app del Smartphone
        """
        if aplicacion in self.app_instaladas:
            self.app_instaladas.remove(aplicacion)
        else:
            raise Exception("El smartphone no tiene esa app instalada")

    def __str__(self):
        """
        Recibe: el objeto Smartphone
        Devuelve una cadena con la informacion del objeto Smartphone
        """
        return f"{self.modelo}, espacio libre: {self.memoria_total}, apps instaladas: {self.app_instaladas}"