from flask_app.config.mysqlconnection import connectToMySQL

database = "esquema_estudiantes_cursos"

class Estudiante:
    def __init__(self,data):
        self.id = data['id']
        self.nombre = data['nombre']
        self.apellido = data['apellido']
        self.edad = data['edad']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def crear(cls,data):
        query = "insert into estudiantes (nombre,apellido,edad,curso_id) values (%(nombre)s,%(apellido)s,%(edad)s,%(curso_id)s);"
        return connectToMySQL(database).query_db(query,data)