from flask_app.config.mysqlconnection import connectToMySQL ###Nos podemos conectar a la BD y podemos jugar con la creacion del objeto y sus metodos

#####aqui debes importar otras clases en caso de que sea necesario
from flask import flash
import re


EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
NAME_REGEX = re.compile(r'[a-zA-Z]+$')
NUMERO_REGEX = re.compile(r'^[0-9]*$')
PASSWORD_REGEX = re.compile(r'^(?=.{8,})(?=.*[a-z])(?=.*[0-9])(?=.*[A-Z])(?=.*[@#$%^&+=]).*$')


class Usuario:
    db_schema = 'piloto_naves' ## Cambiar la BD a la que estamos apuntando
    def __init__(self,data):
        self.id = data['id'] 
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.updated_at = data['updated_at']
        self.created_at = data['created_at']
        self.friends = []

    @classmethod
    def get_all(cls):
        query = "select * from pilotos;" ###cambiar la tabla a la que apuntamos.
        resultados = connectToMySQL(cls.db_schema).query_db(query)
        usuarios = [] ###Cambiar el nombre del arreglo para algo que represente la tabla
        for usuario in resultados:
            usuarios.append(cls(usuario))
        return usuarios

    @classmethod
    def validate_one(cls,data):
        query = "select * from pilotos where email=%(email)s;"
        resultado = connectToMySQL(cls.db_schema).query_db(query,data)
        print(len(resultado))
        if len(resultado) > 0:
            flash("El email ya esta registrado","usuario")
            return True
        else:
            return False 
    
    @classmethod
    def save(cls,data):
        query = "insert into pilotos (first_name,last_name,email) values (%(first_name)s, %(last_name)s, %(email)s);"
        return connectToMySQL(cls.db_schema).query_db(query,data)

    @staticmethod
    def validar(data):
        is_valid = True
        query = "select * from pilotos where email=%(email)s;"
        resultado_query = connectToMySQL('piloto_naves').query_db(query,data)
        if len(resultado_query) > 0:
            flash("El email ya esta registrado!","usuario")
            is_valid = False
        if len(data['first_name']) <5 :
            flash("El primer nombre debe tener mas de 5 letras","usuario")
            is_valid = False
        if len(data['first_name']) > 20:
            flash("El primer nombre es muy largo","usuario")
            is_valid = False
        if not NAME_REGEX.match(data['first_name']):
            flash("El nombre no puede tener numeros o caracteres especiales","usuario")
            is_valid = False
        if len(data['last_name']) <5 :
            flash("El apellido debe tener mas de 5 letras","usuario")
            is_valid = False
        if len(data['last_name']) > 20:
            flash("El apellido  es muy largo","usuario")
            is_valid = False
        if not NAME_REGEX.match(data['last_name']):
            flash("El apellido no puede tener numeros ocaracters especiales","usuario")
        if not EMAIL_REGEX.match(data['email']):
            flash("El email no cumple con las caracteristicas minimas solicitadas","usuario")
            is_valid = False
        if not NUMERO_REGEX.match(data['numero']):
            flash("Solo se aceptan numeros en el campo numero","usuario")
            is_valid = False
        if not PASSWORD_REGEX.match(data['password']):
            flash("El password no cumple con las caracterisitas minimas","usuario")
            is_valid = False
        return is_valid