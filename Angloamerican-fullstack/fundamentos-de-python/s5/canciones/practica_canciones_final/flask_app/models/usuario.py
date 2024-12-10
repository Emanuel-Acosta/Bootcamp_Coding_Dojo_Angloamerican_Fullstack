# Nos podemos conectar a la BD y podemos jugar con la creacion del objeto y sus metodos
from flask_app.config.mysqlconnection import connectToMySQL
# aqui debes importar otras clases en caso de que sea necesario

DATABASE = 'esquema_canciones'


class Usuario:
    def __init__(self, data):
        self.id = data['id']
        self.nombre = data['nombre']
        self.email = data['email']
        self.contraseña = data['contrasena']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.mis_favoritas = []

    @classmethod
    def get_all(cls):  # si este método se utiliza para obtener todos los usuarios de la base de datos
        query = "SELECT * FROM usuarios;"
        resultados = connectToMySQL(DATABASE).query_db(query)
        usuarios = []  # Lista vacía donde guardaremos los objetos de Usuario
        for usuario in resultados:
            usuarios.append(cls(usuario))
        return usuarios

    # @classmethod
    # def get_canciones_y_usuarios(cls, datos): #Este método se encarga de traer las canciones favoritas de un usuario
    #     query = """SELECT canciones.id AS cancion_id, canciones.titulo,
    #                 canciones.artista,
    #                 canciones.created_at AS cancion_created_at,
    #                 canciones.updated_at AS cancion_updated_at,
    #                 usuarios.id AS usuario_id, usuarios.nombre,
    #                 usuarios.email, usuarios.contrasena,
    #                 usuarios.created_at AS usuario_created_at,
    #                 usuarios.updated_at AS usuario_updated_at
    #                 FROM canciones
    #                 LEFT JOIN favoritos ON favoritos.cancion_id = canciones.id
    #                 LEFT JOIN usuarios ON favoritos.usuario_id = usuarios.id
    #                 WHERE usuarios.id = %(id)s;"""
    #     resultados = connectToMySQL(DATABASE).query_db(query, datos)
    #     if len(resultados) == 0:
    #         return None
    #     # Para obtener los datos del usuario basta con obtener la primera fila de resultados
    #     usuario_data = {
    #         'id': resultados[0]['usuario_id'],
    #         'nombre': resultados[0]['nombre'],
    #         'email': resultados[0]['email'],
    #         'contrasena': resultados[0]['contrasena'],
    #         'created_at': resultados[0]['usuario_created_at'],
    #         'updated_at': resultados[0]['usuario_updated_at']
    #     }
    #     # Creamos una instancia de Usuario con los datos obtenidos
    #     usuario = Usuario(usuario_data)

    #     for fila_en_db in resultados:
    #         datos_cancion = {
    #             'id': fila_en_db['cancion_id'],
    #             'titulo': fila_en_db['titulo'],
    #             'artista': fila_en_db['artista'],
    #             'created_at': fila_en_db['cancion_created_at'],
    #             'updated_at': fila_en_db['cancion_updated_at']
    #         }
    #         usuario.mis_favoritas.append(datos_cancion)

    #     return usuario

    @classmethod
    def get_favoritas(cls, datos): #si con esta si puedo crear usuario y pasarle las canciones favoritas asi no tengan canciones favoritas
        query = """
        SELECT usuarios.id AS usuario_id, usuarios.nombre, usuarios.email, usuarios.contrasena, 
        usuarios.created_at AS usuario_created_at, usuarios.updated_at AS usuario_updated_at,
        canciones.id, canciones.titulo, canciones.artista 
        FROM canciones
        JOIN favoritos ON canciones.id = favoritos.cancion_id
        JOIN usuarios ON usuarios.id = favoritos.usuario_id
        WHERE usuarios.id = %(id)s;
        """
        
        resultados = connectToMySQL(DATABASE).query_db(query, datos)
        
        # Si no hay resultados (el usuario no tiene canciones favoritas)
        if len(resultados) == 0:
            # Crear el usuario con una lista vacía de canciones favoritas
            usuario_data = {
                'id': datos['id'],  # Usamos el ID proporcionado en los datos
                'nombre': '',
                'email': '',
                'contrasena': '',
                'created_at': None,
                'updated_at': None
            }
            usuario = cls(usuario_data)
            usuario.mis_favoritas = []  # Lista vacía si no tiene canciones favoritas
            return usuario
        
        # Si hay resultados, procesamos las canciones favoritas
        usuario_data = {
            'id': resultados[0]['usuario_id'],
            'nombre': resultados[0]['nombre'],
            'email': resultados[0]['email'],
            'contrasena': resultados[0]['contrasena'],
            'created_at': resultados[0]['usuario_created_at'],
            'updated_at': resultados[0]['usuario_updated_at']
        }
        
        # Crear un objeto usuario con los datos obtenidos
        usuario = cls(usuario_data)
        
        # Añadir canciones favoritas a la lista
        for fila_en_db in resultados:
            datos_cancion = {
                'id': fila_en_db['id'],
                'titulo': fila_en_db['titulo'],
                'artista': fila_en_db['artista']
            }
            usuario.mis_favoritas.append(datos_cancion)
        
        return usuario

    # @classmethod  # si
    # # Este método se encarga de traer las canciones favoritas de un usuario
    # def get_favoritas(cls, datos):
    #     query = """SELECT usuarios.id AS usuario_id, usuarios.nombre, usuarios.email, usuarios.contrasena, 
    #                 usuarios.created_at AS usuario_created_at, usuarios.updated_at AS usuario_updated_at,
    #                 canciones.id, canciones.titulo, canciones.artista 
    #                 FROM canciones
    #                 JOIN favoritos ON canciones.id = favoritos.cancion_id
    #                 JOIN usuarios ON usuarios.id = favoritos.usuario_id
    #                 WHERE usuarios.id = %(id)s;"""
    #     resultados = connectToMySQL(DATABASE).query_db(query, datos)
    #     if len(resultados) == 0:
    #         return None
    #     # Para obtener los datos del usuario basta con obtener la primera fila de resultados
    #     usuario_data = {
    #         'id': resultados[0]['usuario_id'],
    #         'nombre': resultados[0]['nombre'],
    #         'email': resultados[0]['email'],
    #         'contrasena': resultados[0]['contrasena'],
    #         'created_at': resultados[0]['usuario_created_at'],
    #         'updated_at': resultados[0]['usuario_updated_at']
    #     }
    #     # Creamos una instancia de Usuario con los datos obtenidos
    #     usuario = cls(usuario_data)

    #     for fila_en_db in resultados:
    #         datos_cancion = {
    #             'id': fila_en_db['id'],
    #             'titulo': fila_en_db['titulo'],
    #             'artista': fila_en_db['artista']
    #         }
    #         usuario.mis_favoritas.append(datos_cancion)
    #     return usuario

    @classmethod  # si
    # Este método se encarga de agregar un usuario a la base de datos
    def agregar_usuario(cls, datos):
        query = "INSERT INTO usuarios (nombre, email, contrasena) VALUES (%(nombre)s, %(email)s, %(contrasena)s);"
        return connectToMySQL(DATABASE).query_db(query, datos)
    
    @classmethod
    def get_one(cls, data):
        query = "SELECT * FROM usuarios WHERE id = %(id)s;"
        resultado = connectToMySQL(DATABASE).query_db(query, data)
        if len(resultado) < 1:
            return None
        return cls(resultado[0])
