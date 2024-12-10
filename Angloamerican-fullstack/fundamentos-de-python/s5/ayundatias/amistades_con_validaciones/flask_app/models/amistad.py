from flask_app.config.mysqlconnection import connectToMySQL ###Nos podemos conectar a la BD y podemos jugar con la creacion del objeto y sus metodos
#####aqui debes importar otras clases en caso de que sea necesario
from flask import flash

class Amistad:
    db_schema = 'friendships_schema' ## Cambiar la BD a la que estamos apuntando
    def __init__(self,data):
        self.id = data['id'] 
        self.user_id = data['user_id']
        self.friend_id = data['friend_id']
        self.updated_at = data['updated_at']
        self.created_at = data['created_at']



    @classmethod
    def get_all(cls):
        query = "select * from friendships;" ###cambiar la tabla a la que apuntamos.
        resultados = connectToMySQL(cls.db_schema).query_db(query)
        amistades = [] ###Cambiar el nombre del arreglo para algo que represente la tabla
        for amistad in resultados:
            amistades.append(cls(amistad))
        return amistades
    
    @classmethod
    def save(cls,data):
        query = "insert into friendships (user_id, friend_id) values (%(user_id)s,%(friend_id)s);"
        return connectToMySQL(cls.db_schema).query_db(query,data)
    
    @staticmethod
    def validar(data):
        is_valid = True
        if data['user_id'] == data['friend_id']:
            flash(["Tu no puedes seguirte a ti mismo",1])
            is_valid = False

        query = """
            SELECT * FROM friendships
            WHERE user_id = %(user_id)s AND friend_id = %(friend_id)s;
            """
        # Ejecutamos la consulta para verificar si ya existe la relación
        result = connectToMySQL(Amistad.db_schema).query_db(query, data)
    
        if len(result) > 0:
            flash(["Ya existe la amistad",1])
            is_valid = False  
        return is_valid

        
        
        
        
        

