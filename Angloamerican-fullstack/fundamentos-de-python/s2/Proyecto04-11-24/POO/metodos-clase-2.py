## segunda parte:
class TarjetaCredito:

    #Atributos de clase

    banco = "Banco Internacional de Programadores"

    #Agregamos un atributo de clase que guarda todas las tarjetas de crédito

    todas_las_tarjetas = []

    def __init__(self, limite_credito, saldo_pagar):

        #Esteblecemos los atributos de instancia

        self.limite_credito = limite_credito

        self.saldo_pagar = saldo_pagar

        #Cada que se cree una nueva instancia de la clase, se agrega a todas_las_tarjetas

        TarjetaCredito.todas_las_tarjetas.append(self)

    #Método de clase que cambia el banco

    @classmethod

    def cambiar_banco(cls, nombre):

        cls.banco = nombre


    #Método de clase que imprime el total de saldos a pagar de todas las tarjetas

    def todos_saldos(cls):

        total_saldos = 0

        for tarjeta in cls.todas_las_tarjetas: #Usamos cls para hacer referencia a la clase

            total_saldos += tarjeta.saldo_pagar

        return total_saldos



