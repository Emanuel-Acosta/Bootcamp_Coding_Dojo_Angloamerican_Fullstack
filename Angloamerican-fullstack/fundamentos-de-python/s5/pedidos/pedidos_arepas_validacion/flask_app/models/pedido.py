from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash

database = 'pedidos_db'

class Pedido:
    def __init__(self, data):
        self.id = data['id']
        self.nombre_cliente = data['nombre_cliente']
        self.cantidad = data['cantidad']
        self.relleno = data['relleno']
        self.fecha_creacion = data['fecha_creacion']

    @staticmethod
    def get_all():
        query = "SELECT * FROM pedidos;"
        return connectToMySQL(database).query_db(query)

    @staticmethod
    def save(data):
        query = """
            INSERT INTO pedidos (nombre_cliente, cantidad, relleno)
            VALUES (%(nombre_cliente)s, %(cantidad)s, %(relleno)s);
        """
        return connectToMySQL(database).query_db(query, data)

    @staticmethod
    def validar_pedido(pedido):
        es_valido = True  # Asumimos que la información en válida
        # Si la cantidad de caracteres para el campo tortilla es menor a 3
        if len(pedido['nombre_cliente']) < 2:
            # Generamos el mensaje
            flash("El nombre debe tener al menos 2 caracteres", 'warning')
            es_valido = False  # El formulario deja de ser válido
        
        # el campo nombre cliente y relleno debe ser requerido
        if len(pedido['nombre_cliente']) == 0:
            flash("El nombre cliente es requerido", 'warning')
            es_valido = False
        if len(pedido['relleno']) == 0:
            flash("El relleno es requerido", 'warning')
            es_valido = False
        

        # la cantidad debe ser mayor a 0
        if pedido['cantidad'] <= 0:
            flash("La cantidad debe ser mayor a 0", 'warning')
            es_valido = False

        # si un pedido se agrego correctamente
        if es_valido:
            flash("Pedido agregado correctamente", 'success')    
        return es_valido    
