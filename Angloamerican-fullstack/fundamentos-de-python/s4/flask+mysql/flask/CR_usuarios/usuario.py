# Importamos la función que devolverá una instancia de una conexión

from mysqlconnection import connectToMySQL

# Creamos la clase basada en la tabla de mascotas
DATABASE = 'esquema_usuarios'

class Usuario:
    def __init__(self, data):
        self.id = data['id']
        self.nombre = data['nombre']
        self.apellido = data['apellido']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    # Creamos un método de clase para consultar nuestra base de datos
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM usuarios;"
        # Llamamos a función connectToMySQL con el esquema al que te diriges
        resultados = connectToMySQL(DATABASE).query_db(query)
        # Creamos una lista vacía para agregar nuestras instancias de mascota
        usuarios = []
        # Iteramos sobre los resultados de la base de datos y crear instancias de mascota con cls
        for usuario in resultados:
                usuarios.append(cls(usuario))
        return usuarios
    

    # Agregamos un método de clase para generar un nuevo registro 
    # el parámetro "datos" es un diccionario que se pasará al método desde el server
    # con este metodo guardamos o insertamos
    @classmethod
    def save(cls, datos):
        query = "INSERT INTO usuarios (nombre, apellido, email, created_at, updated_at) VALUES (%(nombre)s, %(apellido)s, %(email)s, NOW(), NOW());"
        return connectToMySQL(DATABASE).query_db(query, datos)  

    # seleccionamos especificamente para mostrar 1 usuario
    @classmethod
    def get_by_id(cls, id):
        query = "SELECT * FROM usuarios WHERE id = %(id)s;"
        result = connectToMySQL(DATABASE).query_db(query, {'id': id})
        return cls(result[0]) if result else None # Si no hay resultados, regresamos None
    
    # actualizamos
    @classmethod
    def update(cls, datos):
        query = "UPDATE usuarios SET nombre = %(nombre)s, apellido = %(apellido)s, email = %(email)s, updated_at = NOW() WHERE id = %(id)s;"
        return connectToMySQL(DATABASE).query_db(query, datos)
    
    #eliminamos
    @classmethod
    def delete(cls, id):
        query = "DELETE FROM usuarios WHERE id = %(id)s;"
        return connectToMySQL(DATABASE).query_db(query, {'id': id})
