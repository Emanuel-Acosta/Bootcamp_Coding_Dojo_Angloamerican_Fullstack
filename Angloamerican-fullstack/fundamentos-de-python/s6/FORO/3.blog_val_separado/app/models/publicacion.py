from app.config.mysqlconnection import connectToMySQL


DATABASE = 'esquema_blog'

class Publicacion:
    def __init__(self, data):
        self.id = data['id']
        self.contenido = data['contenido']
        self.usuario_id = data['usuario_id']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.comentarios = []  # Lista vacía para cargar comentarios
        self.autor = data.get('autor')  # Incluimos el autor si está en los datos

    @classmethod
    def get_all(cls):
        query = """
        SELECT publicaciones.*, usuarios.nombre AS autor
        FROM publicaciones 
        JOIN usuarios ON publicaciones.usuario_id = usuarios.id 
        ORDER BY publicaciones.created_at DESC
        """
        results = connectToMySQL(DATABASE).query_db(query)
        publicaciones = []
        for pub in results:
            publicaciones.append(cls(pub))
        return publicaciones
    


    @classmethod
    def create(cls, data):
        query = """
        INSERT INTO publicaciones (contenido, usuario_id, created_at, updated_at) 
        VALUES (%(contenido)s, %(usuario_id)s, NOW(), NOW())
        """
        return connectToMySQL(DATABASE).query_db(query, data)

    @classmethod
    def delete(cls, data):
        query = "DELETE FROM publicaciones WHERE id = %(id)s"
        return connectToMySQL(DATABASE).query_db(query, data)