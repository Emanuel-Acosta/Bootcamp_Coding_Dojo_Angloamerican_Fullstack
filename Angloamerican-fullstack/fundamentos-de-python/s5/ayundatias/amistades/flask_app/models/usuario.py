from flask_app.config.mysqlconnection import connectToMySQL ###Nos podemos conectar a la BD y podemos jugar con la creacion del objeto y sus metodos
from flask_app.models import amistad 
#####aqui debes importar otras clases en caso de que sea necesario


class Usuario:
    db_schema = 'friendships_schema' ## Cambiar la BD a la que estamos apuntando
    def __init__(self,data):
        self.id = data['id'] 
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.updated_at = data['updated_at']
        self.created_at = data['created_at']
        self.friends = []

    @classmethod
    def get_all(cls):
        query = "select * from users;" ###cambiar la tabla a la que apuntamos.
        resultados = connectToMySQL(cls.db_schema).query_db(query)
        usuarios = [] ###Cambiar el nombre del arreglo para algo que represente la tabla
        for usuario in resultados:
            usuarios.append(cls(usuario))
        return usuarios

    @classmethod
    def get_users_with_friends(cls):
        query = "select * from users as t1 join friendships as t2 on t1.id = t2.user_id join users as t3 on t2.friend_id=t3.id;"
        results = connectToMySQL(cls.db_schema).query_db(query)
        all_users = []
        counter = 0
        for usuario in results:
            all_users.append(cls(usuario))
            friends_data = {
                'id': usuario['t3.id'],
                'first_name': usuario['t3.first_name'],
                'last_name': usuario['t3.last_name'],
                'created_at': usuario['t3.created_at'],
                'updated_at': usuario['t3.updated_at'],
            }
            all_users[counter].friends.append(cls(friends_data))
            counter += 1
        return all_users
    
