class Animal:

    def hacer_sonido(self):

        raise NotImplementedError

class Perro(Animal):

    def hacer_sonido(self):

        print("woof woof")

class Gato(Animal):

    def hacer_sonido(self):

        print("miiiaaaaauuu")

perro1= Perro()
perro1.hacer_sonido()

gato1=Gato()
gato1.hacer_sonido()