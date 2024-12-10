from flask_app.config.mysqlconnection import connectToMySQL

from flask_app.models import usuario 
DATABASE = 'esquema_canciones'


class Favoritos:
    def __init__(self, data):
        self.usuario_id = data['usuario_id']
        self.cancion_id = data['cancion_id']
    
    @classmethod
    def agregar_favorito(cls, datos): # si Este método se encarga de agregar una canción a la lista de favoritos de un usuario
        query = "INSERT INTO favoritos (usuario_id, cancion_id) VALUES (%(usuario_id)s, %(cancion_id)s);"
        return connectToMySQL(DATABASE).query_db(query, datos)