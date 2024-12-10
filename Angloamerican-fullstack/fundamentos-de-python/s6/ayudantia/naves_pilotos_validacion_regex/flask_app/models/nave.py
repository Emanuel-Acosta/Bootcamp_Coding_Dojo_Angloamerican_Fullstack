from flask_app.config.mysqlconnection import connectToMySQL ###Nos podemos conectar a la BD y podemos jugar con la creacion del objeto y sus metodos
#####aqui debes importar otras clases en caso de que sea necesario
from flask_app.models import usuario 
from flask import flash

class Nave:
    db_schema = 'piloto_naves' ## Cambiar la BD a la que estamos apuntando
    def __init__(self,data):
        self.id = data['id'] 
        self.user_id = data['user_id']
        self.nombre = data['nombre']
        self.capacidad = data['capacidad']
        self.updated_at = data['updated_at']
        self.created_at = data['created_at']
        self.piloto = None

    @classmethod
    def get_all(cls):
        query = "select * from naves;" ###cambiar la tabla a la que apuntamos.
        resultados = connectToMySQL(cls.db_schema).query_db(query)
        naves = [] ###Cambiar el nombre del arreglo para algo que represente la tabla
        for nave in resultados:
            naves.append(cls(nave))
        return naves
    
    
    
    @classmethod
    def save(cls,data):
        query = "insert into naves (user_id,nombre,capacidad) values (%(user_id)s,%(nombre)s,%(capacidad)s);"
        return connectToMySQL(cls.db_schema).query_db(query,data)

    @classmethod
    def naves_con_pilotos(cls):
        query = "select * from naves as t1 left join pilotos as t2 on t1.user_id=t2.id;"
        results = connectToMySQL(cls.db_schema).query_db(query)
        all_users = []
        counter = 0
        for registro in results:
            all_users.append(cls(registro))
            data = {
                'id': registro['t2.id'],
                'first_name': registro['first_name'],
                'last_name': registro['last_name'],
                'email': registro['email'],
                'created_at': registro['t2.created_at'],
                'updated_at': registro['t2.updated_at']
            }
            all_users[counter].piloto = usuario.Usuario(data)
            counter += 1
        return all_users
    
    @staticmethod
    def validar(data):
        is_valid = True
        if len(data['nombre']) <5  :
            flash("El nombre de la nave no puede ser de menos de 5 letras","nave")
            is_valid = False
        if len(data['nombre']) > 15 :
            flash("El nombre es muy largo","nave")
            is_valid = False
        if int(data['capacidad']) < 1:
            flash('La nave debe tener por lo menos un piloto',"nave")
            is_valid = False
        return is_valid



