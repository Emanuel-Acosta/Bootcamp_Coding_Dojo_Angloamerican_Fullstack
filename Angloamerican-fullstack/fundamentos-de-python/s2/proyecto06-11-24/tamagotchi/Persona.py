from Tamagotchi import Tamagotchi

class Persona:
    def __init__(self,nombre,apellido,tamagotchi):
        self.nombre = nombre
        self.apellido= apellido
        self.tamagotchi = Tamagotchi(tamagotchi.nombre,tamagotchi.color)

    def jugar_con_tamagotchi(self):
        self.tamagotchi.jugar()
        print(f"El tamagotchi de {self.nombre} ha jugado")
        print(f"energia : {self.tamagotchi.energia} , felicidad : {self.tamagotchi.felicidad}, salud: {self.tamagotchi.salud}")

    def darle_comida(self):
        self.tamagotchi.comer()
        print(f"El tamagotchi de {self.nombre} ha comido")
        print(f"energia : {self.tamagotchi.energia} , felicidad : {self.tamagotchi.felicidad}, salud: {self.tamagotchi.salud}")

    def curarlo(self):
        self.tamagotchi.curar()
        print(f"El tamagotchi de {self.nombre} se ha curado")
        print(f"energia : {self.tamagotchi.energia} , felicidad : {self.tamagotchi.felicidad}, salud: {self.tamagotchi.salud}")

persona1 = Persona("pepe","perez", Tamagotchi("pepito", "Azul"))
persona1.darle_comida()
persona1.jugar_con_tamagotchi()
persona1.curarlo()

print(f"nombre del tamagotchi {persona1.nombre} : {persona1.tamagotchi.nombre}")


# crear individuales con nombres. bonus