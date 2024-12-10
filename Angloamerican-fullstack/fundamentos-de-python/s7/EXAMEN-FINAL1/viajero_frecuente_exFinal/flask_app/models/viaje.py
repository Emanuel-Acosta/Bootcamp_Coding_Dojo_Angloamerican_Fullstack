from flask_app.config.mysqlconnection import connectToMySQL
from datetime import datetime
from flask import flash

DATABASE = 'viajeros_frecuentes'

class Viaje:
    def __init__(self, data):
        self.id_viaje = data['id_viaje']
        self.nombre = data['nombre']
        self.fecha_inicio = data['fecha_inicio']
        self.fecha_de_fin = data['fecha_de_fin']
        self.itinerario = data['itinerario']
        self.id_organizador = data['id_organizador']
        self.fecha_creacion = data['fecha_creacion']
        self.fecha_actualizacion = data['fecha_actualizacion']
        self.organizador = data.get('organizador', None)  

    @classmethod
    def get_all(cls): 
        query = """
            SELECT v.*, u.nombre as organizador 
            FROM viajes v
            JOIN usuarios u ON v.id_organizador = u.id_usuario
            ORDER BY v.fecha_inicio;
        """
        results = connectToMySQL(DATABASE).query_db(query)
        viajes = []
        if results:
            for row in results:
                viajes.append(cls(row))
        return viajes
    
    @classmethod
    def crear(cls, data): 
        query = """
            INSERT INTO viajes (nombre, fecha_inicio, fecha_de_fin, itinerario, id_organizador, fecha_creacion, fecha_actualizacion)
            VALUES (%(nombre)s, %(fecha_inicio)s, %(fecha_de_fin)s, %(itinerario)s, %(id_organizador)s, NOW(), NOW());
        """
        return connectToMySQL(DATABASE).query_db(query, data)
        
    @classmethod
    def actualizar(cls, data):
        query = """
            UPDATE viajes 
            SET nombre = %(nombre)s,
                itinerario = %(itinerario)s,
                fecha_inicio = %(fecha_inicio)s,
                fecha_de_fin = %(fecha_de_fin)s
            WHERE id_viaje = %(id_viaje)s;
        """
        return connectToMySQL(DATABASE).query_db(query, data)

    @classmethod
    def obtener_por_id(cls, id_viaje): 
        query = """
            SELECT v.*, u.nombre as organizador 
            FROM viajes v
            JOIN usuarios u ON v.id_organizador = u.id_usuario
            WHERE v.id_viaje = %(id_viaje)s;
        """
        data = {'id_viaje': id_viaje}
        results = connectToMySQL(DATABASE).query_db(query, data)
        return cls(results[0]) if results else None

    @classmethod
    def eliminar(cls, id_viaje): 
        query1 = "DELETE FROM participantes_viaje WHERE id_viaje = %(id_viaje)s;"
        query2 = "DELETE FROM viajes WHERE id_viaje = %(id_viaje)s;"
        data = {'id_viaje': id_viaje}
        connectToMySQL(DATABASE).query_db(query1, data)
        connectToMySQL(DATABASE).query_db(query2, data)
        return True

    @classmethod
    def obtener_por_organizador(cls, id_organizador): 
        query = """
            SELECT v.*, u.nombre as organizador 
            FROM viajes v
            JOIN usuarios u ON v.id_organizador = u.id_usuario
            WHERE v.id_organizador = %(id_organizador)s
            AND v.fecha_de_fin >= NOW()
            ORDER BY v.fecha_inicio;
        """
        data = {'id_organizador': id_organizador}
        results = connectToMySQL(DATABASE).query_db(query, data)
        viajes = []
        if results:
            for row in results:
                viajes.append(cls(row))
        return viajes

    @staticmethod
    def validar_viaje(data): 
        errores = []
        if not data['itinerario']:
            errores.append("el itinerario es obligatoria")
        
        if len(data['itinerario']) > 40:
            errores.append("El itinerario no puede tener más de 40 caracteres")    
        
        if not data['fecha_inicio']:
            errores.append("La fecha de inicio es obligatoria")
            
        if not data['fecha_de_fin']:
            errores.append("La fecha de fin es obligatoria")

        fecha_inicio = datetime.strptime(data['fecha_inicio'], '%Y-%m-%dT%H:%M')
        if fecha_inicio <= datetime.now():
            errores.append("La fecha de inicio debe ser una fecha futura")

        fecha_de_fin = datetime.strptime(data['fecha_de_fin'], '%Y-%m-%dT%H:%M')
        if fecha_de_fin <= fecha_inicio:
            errores.append("La fecha de fin debe ser posterior a la fecha de inicio")    
        return errores

    @classmethod 
    def last_insert_id(cls): 
        return connectToMySQL(DATABASE).query_db("SELECT LAST_INSERT_ID() as id;")[0]['id']
    
    @classmethod
    def obtener_viajeros(cls, id_viaje):
        query = """
            SELECT u.nombre 
            FROM viajeros v
            JOIN usuarios u ON v.usuario_id = u.id_usuario
            WHERE v.viaje_id = %(viaje_id)s;
        """
        data = {'viaje_id': id_viaje}
        results = connectToMySQL(DATABASE).query_db(query, data)
        return results
    
    