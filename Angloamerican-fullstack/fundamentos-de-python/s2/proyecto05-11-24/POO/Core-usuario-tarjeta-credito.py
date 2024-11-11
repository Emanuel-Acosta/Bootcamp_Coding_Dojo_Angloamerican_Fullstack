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
    


class Usuario:


    def __init__(self, nombre, apellido, email):

        self.nombre = nombre

        self.apellido = apellido

        self.email = email

        self.tarjeta = TarjetaCredito(0, 20000, 0.015) #Agregamos esta línea

        

    def hacer_compra(self, monto):  
        self.tarjeta += monto
        return self
    
    def pagar_tarjeta(self, monto):
        self.tarjeta -= monto
        return self
    
    def mostrar_saldo_usuario(self):
        print(f"Usuario: {self.nombre}, Saldo a pagar: ${self.tarjeta.saldo_pagar}")
        return self    

    
    def metodo_ejemplo(self):

        #Llamar a los métodos de tarjeta

        self.tarjeta.compra(1000).compra(200).pago(500).cobrar_interes()

        #Acceder a sus atributos

        print(f"Saldo a pagar actual del usuario: {self.tarjeta.saldo_pagar}")
        return self

usuario1 = Usuario("emanuel","acosta","emanuel@correo.cl")
usuario1.mostrar_saldo_usuario().metodo_ejemplo()



