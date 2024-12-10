from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
import re
from flask_bcrypt import Bcrypt

bcrypt = Bcrypt()


EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
NAME_REGEX= re.compile(r'[a-zA-Z]+$') 
PASSWORD_REGEX= re.compile(r'^(?=.{8,})(?=.*[a-z])(?=.*[0-9])(?=.*[A-Z])(?=.*[@#$%^&+=]).*$')
NUMBER_REGEX= re.compile(r'^[0-9]*$') 

DB = 'validate_form'

class User:
    def __init__( self , data ):
        self.id_usuario = data['id_usuario']
        self.nombre = data['nombre']
        self.apellido = data['apellido']
        self.email = data['email']
        self.password = data['password']

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM usuarios order by nombre;"
        results = connectToMySQL(DB).query_db(query)
        users = []
        for user in results:
            users.append( cls(user) )
        return users
    
    @classmethod
    def save(cls,data):
        query = "INSERT INTO usuarios (nombre, apellido, email, password) VALUES (%(nombre)s, %(apellido)s, %(email)s, %(password)s);"
        mysql = connectToMySQL(DB)
        result = mysql.query_db(query, data)
        data_usuario = {'id_usuario': result}
        return cls.getId(data_usuario)
    
    @classmethod
    def getId(cls, data):
        query = "select * from usuarios where id_usuario = %(id_usuario)s;"
        mysql = connectToMySQL(DB)
        result = mysql.query_db(query, data)
        if len(result) > 0:
            return cls(result[0])
        else:
            return None
        
    @classmethod
    def getbyemail(cls, data):
        query = "select * from usuarios where email = %(email)s;"
        mysql = connectToMySQL(DB)
        result = mysql.query_db(query, data)
        if len(result) > 0:
            return cls(result[0])
        else:
            return None
        
    @staticmethod
    def validate_entry(data):
        is_valid = True
        
        # Validación para el formulario de registro
        if data['which_form'] == 'register_user':
            
            # Validaciones para nombre
            if not data['nombre']:
                flash(["El nombre no puede estar vacío", 0])
                is_valid = False
            elif len(data['nombre']) < 2:
                flash(["El nombre debe tener al menos 2 caracteres", 0])
                is_valid = False
            elif not NAME_REGEX.match(data['nombre']):
                flash(["Su nombre debe ser solo letras", 0])
                is_valid = False

            # Validaciones para apellido
            if not data['apellido']:
                flash(["El apellido no puede estar vacío", 0])
                is_valid = False
            elif len(data['apellido']) < 2:
                flash(["El apellido debe tener al menos 2 caracteres", 0])
                is_valid = False
            elif not NAME_REGEX.match(data['apellido']):
                flash(["Tu apellido debe ser solo letras", 0])
                is_valid = False

            # Validaciones para email
            if not data['email']:
                flash(["El correo electrónico no puede estar vacío", 0])
                is_valid = False
            elif not EMAIL_REGEX.match(data['email']):
                flash(["Formato incorrecto de correo!", 0])
                is_valid = False
            else:
                user = User.getbyemail(data)
                if user is not None:
                    flash(["La dirección de correo electrónico ya ha sido registrada!", 0])
                    is_valid = False

            # Validaciones para contraseña
            if not data['password']:
                flash(["La contraseña no puede estar vacía", 0])
                is_valid = False
            elif len(data['password']) < 8:
                flash(["La contraseña debe tener al menos 8 caracteres", 0])
                is_valid = False
            elif not PASSWORD_REGEX.match(data['password']):
                flash(["Su contraseña debe tener al menos 8 caracteres con al menos un carácter ASCII en minúsculas y otro en mayúsculas y también al menos un carácter del conjunto @#$%^&+=, más un número", 0])
                is_valid = False
            elif data['passwordconfir'] != data['password']:
                flash(["La confirmación de la contraseña no coincide con la contraseña original", 0])
                is_valid = False

        # Validación para el formulario de inicio de sesión
        else:
            if not data['email']:
                flash(["El correo electrónico no puede estar vacío", 1])
                is_valid = False
            elif not EMAIL_REGEX.match(data['email']):
                flash(["Dirección de correo electrónico no válida!", 1])
                is_valid = False
            else:
                user = User.getbyemail(data)
                if user is None:
                    flash(["Correo electrónico/Contraseña inválidos", 1])
                    is_valid = False

            if not data['password']:
                flash(["La contraseña no puede estar vacía", 1])
                is_valid = False
            elif len(data['password']) < 8:
                flash(["La contraseña debe tener al menos 8 caracteres", 1])
                is_valid = False
            else:
                user = User.getbyemail(data)
                if user and not bcrypt.check_password_hash(user.password, data['password']):
                    flash(["Contraseña inválida", 1])
                    is_valid = False

        return is_valid


    
    




