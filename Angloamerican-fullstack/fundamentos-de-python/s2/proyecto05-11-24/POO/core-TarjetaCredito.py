class TarjetaCredito:

    def __init__(self, saldo_pagar, limite_credito, intereses):
        self.saldo_pagar = saldo_pagar
        self.limite_credito = limite_credito
        self.interes = intereses

    def compra(self, monto):
        if self.saldo_pagar + monto <= self.limite_credito:
            self.saldo_pagar += monto
        else:
            print("Tarjeta Rechazada, limite de credito alcanzado, no se aceptan las compras donde superes el limite")
        return self        
    
    def pago(self, monto):
        
        self.saldo_pagar -= monto
        return self
    
    def mostrar_info_tarjeta(self):
        print(f" Credito:{self.limite_credito} Saldo a pagar:{self.saldo_pagar}")
        return self

    def cobrar_interes(self):
        self.saldo_pagar += self.saldo_pagar * self.interes
        return self
    

tarjeta1 = TarjetaCredito(3000,15000,0.15)
tarjeta2 = TarjetaCredito(4000,20000,0.25)
tarjeta3 = TarjetaCredito(5000,230000,0.35)

tarjeta1.compra(1000).compra(500).pago(300).cobrar_interes().mostrar_info_tarjeta()
tarjeta2.compra(1200).compra(2000).compra(3000).pago(2500).pago(1300).cobrar_interes().mostrar_info_tarjeta()
tarjeta3.compra(10000).compra(20000).compra(30000).compra(10000).compra(200000).mostrar_info_tarjeta()
