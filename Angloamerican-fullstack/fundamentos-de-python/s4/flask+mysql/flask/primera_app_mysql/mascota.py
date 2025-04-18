# Importamos la función que devolverá una instancia de una conexión

from mysqlconnection import connectToMySQL

# Creamos la clase basada en la tabla de mascotas
DATABASE = 'primera_flask'

class Mascota:
    def __init__(self, data):
        self.id = data['id']
        self.nombre = data['nombre']
        self.tipo = data['tipo']
        self.color = data['color']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    # Creamos un método de clase para consultar nuestra base de datos
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM mascotas;"
        # Llamamos a función connectToMySQL con el esquema al que te diriges
        resultados = connectToMySQL(DATABASE).query_db(query)
        # Creamos una lista vacía para agregar nuestras instancias de mascota
        mascotas = []
        # Iteramos sobre los resultados de la base de datos y crear instancias de mascota con cls
        for mascota in resultados:
                mascotas.append(cls(mascota))
        return mascotas
    

    # Agregamos un método de clase para generar un nuevo registro de mascota
    # el parámetro "datos" es un diccionario que se pasará al método desde el server
    @classmethod
    def save(cls, datos):
        query = "INSERT INTO mascotas (nombre, tipo, color, created_at, updated_at) VALUES (%(nombre)s, %(tipo)s, %(color)s, NOW(), NOW());"
        return connectToMySQL('primera_flask').query_db(query, datos)    
