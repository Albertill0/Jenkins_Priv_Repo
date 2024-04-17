import pickle
import django
import requests
import numpy as np
import pandas as pd
from bs4 import BeautifulSoup
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.backends import default_backend
import xml.etree.ElementTree as ET
import yaml

def hola_mundo():
    print("Hola mundo!")

# Ejemplo de clase vulnerable que utiliza pickle
class MiClase:
    def __init__(self, data):
        self.data = data

    def __reduce__(self):
        return (eval, (self.data,))

# Crear una instancia de la clase
objeto_vulnerable = MiClase("__import__('os').system('echo Hola desde la clase')")

# Serializar el objeto utilizando pickle
datos_serializados = pickle.dumps(objeto_vulnerable)

# Deserializar los datos (potencialmente peligroso)
objeto_deserializado = pickle.loads(datos_serializados)

# Llamar al método __reduce__ que ejecuta código arbitrario
objeto_deserializado.__reduce__()

# Vulnerabilidad de inyección de código
nombre = input("Por favor, introduzca su nombre: ")
print("Hola", nombre)

# Vulnerabilidad de manejo inseguro de datos de entrada
url = input("Por favor, introduzca una URL para descargar: ")
requests.get(url)

# Falta de validación de datos
numero = input("Por favor, introduzca un número: ")
resultado = 10 / int(numero)
print("El resultado es:", resultado)
