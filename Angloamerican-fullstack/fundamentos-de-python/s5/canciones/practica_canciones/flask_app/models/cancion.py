from flask_app.config.mysqlconnection import connectToMySQL

DATABASE = 'esquema_canciones'

class Canciones:
    def __init__(self, data):
        self.id = data['id']
        self.titulo = data['titulo']
        self.artista = data['artista']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM canciones;"
        resultados = connectToMySQL(DATABASE).query_db(query)
        canciones = []
        for cancion in resultados:
            canciones.append(cls(cancion))
        return canciones
    