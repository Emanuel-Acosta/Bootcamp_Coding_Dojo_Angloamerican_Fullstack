
class Tamagotchi:
    def __init__(self,nombre, color):
        self.nombre = nombre
        self.color = color
        self.energia = 100
        self.felicidad = 100
        self.salud =100

    def jugar(self):
        self.energia -= 20
        self.felicidad +=10
        self.salud += 10

    def comer(self):
        self.energia +=10
        self.felicidad += 10
        self.salud += 10

    def curar(self):
        self.energia += 10
        self.felicidad +=10
        self.salud += 10     
