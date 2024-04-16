import pickle

def hola_mundo():
    print("Hola mundo!")

# Ejemplo de clase vulnerable que utiliza pickle
class MiClase:
    def __reduce__(self):
        return (eval, ("print('¡Hola desde la clase!')",))

# Crear una instancia de la clase
objeto_vulnerable = MiClase()

# Serializar el objeto utilizando pickle
datos_serializados = pickle.dumps(objeto_vulnerable)

# Deserializar los datos (potencialmente peligroso)
objeto_deserializado = pickle.loads(datos_serializados)

# Llamar al método __reduce__ que ejecuta código arbitrario
objeto_deserializado.__reduce__()
