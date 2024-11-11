class TarjetaCredito:


    def hacer_compra(self, monto):  #recibe como argumento el monto de la compra

        #Evaluamos si puede realizar la compra con un método estático

        if TarjetaCredito.puede_comprar(self.limite_credito, self.saldo_pagar, monto):

            self.saldo_pagar += monto   #el saldo a pagar del usuario aumenta en la cantidad del valor recibido

        else:

            print("Tarjeta Rechazada, has alcanzado tu límite de crédito")

        return self


    #Solamente tienen acceso a los argumentos que reciben

    @staticmethod

    def puede_comprar(limite, saldo_utilizado, monto):

        #Revisamos si con la compra, el saldo sobrepasa el límite de crédito

        if (saldo_utilizado + monto) > limite:

            return False

        else:

            return True