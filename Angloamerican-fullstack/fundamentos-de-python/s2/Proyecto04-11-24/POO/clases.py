class Perro:
    def __init__(self, nombre, edad,raza):
        self.name=nombre
        self.age=edad
        self.race=raza

#instanciar
perro1= Perro("Firulais",5,"Pastor Aleman")   
print(perro1)     
        

class Usuario:
    def __init__(self):
        self.nombre = "Nariyoshi"

        self.apellido = "Miyagi"

        self.email = "miyagi@codingdojo.la"

        self.limite_credito = 30000

        self.saldo_pagar = 0
        

miyagi = Usuario()

daniel = Usuario()

#Accedemos a los atributos de la instancia

print(miyagi.nombre) #Imprime: Nariyoshi

print(daniel.nombre) #Imprime: Nariyoshi

daniel.nombre = "Daniel"

daniel.apellido = "Larusso"

print(daniel.nombre +" "+ daniel.apellido) #Imprime: Daniel


#
#
#

class Usuario: 
    def __init__(self, nombre, apellido, email):

        self.nombre = nombre

        self.apellido = apellido

        self.email = email

        self.limite_credito = 30000

        self.saldo_pagar = 0

miyagi = Usuario("Nariyoshi", "Miyagi", "miyagi@codingdojo.la")

daniel = Usuario("Daniel", "Larusso", "daniel@codingdojo.la")

print(miyagi.nombre) #Imprime: Nariyoshi

print(daniel.nombre) #Imprime: Daniel

# metodos a la clase:

class Usuario:


    def __init__(self, nombre, apellido, email):

        self.nombre = nombre

        self.apellido = apellido

        self.email = email

        self.limite_credito = 30000

        self.saldo_pagar = 0

    def hacer_compra(self, monto):  #recibe como argumento el monto de la compra

        self.saldo_pagar += monto   #el saldo a pagar del usuario aumenta en la cantidad del valor recibido


miyagi = Usuario("Nariyoshi", "Miyagi", "miyagi@codingdojo.la")

daniel = Usuario("Daniel", "Larusso", "daniel@codingdojo.la")

miyagi.hacer_compra(150)

miyagi.hacer_compra(300)

daniel.hacer_compra(45)

print(miyagi.saldo_pagar) #Imprime: 350

print(daniel.saldo_pagar) #Imprime: 45

