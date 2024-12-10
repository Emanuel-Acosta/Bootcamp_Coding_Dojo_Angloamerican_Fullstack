from app.config.mysqlconnection import connectToMySQL


DATABASE = 'esquema_blog'

class Comentario:
    def __init__(self, data):
        self.id = data['id']
        self.comentario = data['comentario']
        self.usuario_id = data['usuario_id']
        self.publicacion_id = data['publicacion_id']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.autor = data.get('autor')  # Incluimos el autor si está en los datos

    @classmethod
    def get_by_publicacion_id(cls, data):
        query = """
        SELECT comentarios.*, usuarios.nombre AS autor 
        FROM comentarios 
        JOIN usuarios ON comentarios.usuario_id = usuarios.id 
        WHERE publicacion_id = %(publicacion_id)s
        """
        results = connectToMySQL(DATABASE).query_db(query, data)
        comentarios = []
        for com in results:
            comentarios.append(cls(com))
        return comentarios

    @classmethod
    def create(cls, data):
        query = """
        INSERT INTO comentarios (comentario, usuario_id, publicacion_id, created_at, updated_at) 
        VALUES (%(comentario)s, %(usuario_id)s, %(publicacion_id)s, NOW(), NOW())
        """
        return connectToMySQL(DATABASE).query_db(query, data)