from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models.estudiante import Estudiante
from flask import flash


class Curso:
    db_schema = "esquema_estudiantes_cursos"
    def __init__(self,data):
        self.id = data['id']
        self.nombre = data['nombre']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.estudiantes = []
    @classmethod
    def get_all(cls):
        query = "select * from cursos;"
        resultados = connectToMySQL(cls.db_schema).query_db(query)
        cursos = []
        for curso in resultados:
            cursos.append(cls(curso))
        return cursos
    
    @classmethod
    def crear(cls,data):
        query = "insert into cursos (nombre) values (%(nombre)s);"
        return connectToMySQL(cls.db_schema).query_db(query,data)

    @classmethod
    def get_curso_y_estudiantes(cls,data):
        query = "select * from cursos left join estudiantes on estudiantes.curso_id = cursos.id where cursos.id= %(id)s;"
        resultados = connectToMySQL(cls.db_schema).query_db(query,data)
        curso = cls(resultados[0])
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
    
    @staticmethod
    def validar(data):
        is_valid = True
        if len(data['nombre'])< 4:
            flash("El curso no puede tener menos de 4 letras")
            is_valid = False
        return is_valid


