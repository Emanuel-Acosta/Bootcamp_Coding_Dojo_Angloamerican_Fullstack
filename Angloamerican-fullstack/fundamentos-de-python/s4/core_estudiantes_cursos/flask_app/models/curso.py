from flask_app.config.mysqlconnection import connectToMySQL # Importamos la conexión a la base de datos
from flask_app.models.estudiante import Estudiante 

database = "esquema_estudiantes_cursos" # estoy creando una variable que contiene el nombre de la base de datos
class Curso: 
    def __init__(self,data):
        self.id = data['id']
        self.nombre = data['nombre']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.estudiantes = [] # estoy creando una lista vacía para los estudiantes 

    @classmethod 
    def get_all(cls): # estoy creando un método de clase que obtiene todos los cursos 
        query = "select * from cursos;" # estoy creando una variable que contiene la consulta a la base de datos
        resultados = connectToMySQL(database).query_db(query) # estoy creando una variable que contiene la conexión a la base de datos y la consulta a la base de datos
        cursos = [] # estoy creando una lista vacía para los cursos
        for curso in resultados: 
            cursos.append(cls(curso)) # estoy agregando a la lista de cursos los cursos que se encuentran en la base de datos
        return cursos
    
    @classmethod
    def crear(cls,data): # estoy creando un método de clase que crea un curso
        query = "insert into cursos (nombre) values (%(nombre)s);" # estoy creando una variable que contiene la consulta a la base de datos
        return connectToMySQL(database).query_db(query,data)

    @classmethod
    def get_curso_y_estudiantes(cls,data): # estoy creando un método de clase que obtiene un curso y sus estudiantes
        query = "select * from cursos left join estudiantes on estudiantes.curso_id = cursos.id where cursos.id= %(id)s;" 
        resultados = connectToMySQL(database).query_db(query,data) 
        curso = cls(resultados[0]) #obtengo el primer resultado de la consulta el cual es un diccionario con los datos del curso
        for estudiante in resultados:
            data_estudiante = {
                'id' : estudiante['estudiantes.id'], 
                'nombre' : estudiante['estudiantes.nombre'], 
                'apellido' : estudiante['apellido'], 
                'edad' : estudiante['edad'],
                "created_at" : estudiante['created_at'],
                "updated_at" : estudiante['updated_at']
            }
            curso.estudiantes.append(Estudiante(data_estudiante))

        return curso
    
    


