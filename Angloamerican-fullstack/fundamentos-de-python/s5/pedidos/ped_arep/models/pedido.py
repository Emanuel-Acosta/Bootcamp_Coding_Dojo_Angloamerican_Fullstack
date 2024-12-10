from config.mysqlconnection import connectToMySQL

class Pedido:
    @staticmethod
    def get_all():
        query = "SELECT * FROM pedidos;"
        return connectToMySQL('pedidos_db').query_db(query)
    
    @staticmethod
    def save(data):
        query = """
            INSERT INTO pedidos (nombre_cliente, cantidad, relleno) 
            VALUES (%(nombre_cliente)s, %(cantidad)s, %(relleno)s);
        """
        return connectToMySQL('pedidos_db').query_db(query, data)
