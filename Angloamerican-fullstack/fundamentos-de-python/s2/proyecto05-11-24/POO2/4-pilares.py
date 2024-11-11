#encapsulacion:

class Taco:

    def __init__(self, guiso):

        self.guiso = guiso
        self.tortilla = "Tortilla de maiz"

    def prepararlo(self):

        print(f"Haciendo un taco de {self.guiso}")

        print("¡Calentando el taquito!")
        return self


    def servir(self):

        print(f"Tomamos un plato plano y colocamos el platillo con {self.tortilla} y {self.guiso}")
        return self

taco1 = Taco("carne molida")        
taco1.prepararlo().servir()

#Herencia:

class Enchilada(Taco):


    def __init__(self, guiso):

        super().__init__(guiso)

        self.salsa = "verde"  

    def hacer_enchilada(self):

        super().prepararlo()

        print(f"Agregamos la salsa{self.salsa} a nuestro taco y ahora es enchilada") 

enchilada1 = Enchilada("pollo")
enchilada1.hacer_enchilada()


#polimorfismo: cambio el servir con respecto al padre

class Enchilada(Taco):

    def __init__(self, guiso):

        super().__init__(guiso)

        self.salsa = "verde"

    def hacer_enchilada(self):

        super().prepararlo()

        print("Agregamos la salsa a nuestro taco y ahora es enchilada")


    def servir(self):

        print("Tomamos un plato grande y colocamos el platillo y adornamos con cilantro")


#abstraccion:

class Comensal:

    def __init__(self, nombre):

        self.nombre = nombre

        self.taco = Taco("carne")

    def comer_taco(self):

        self.taco.prepararlo()

        self.taco.servir()

        print("Me como mi delicioso taco") 

comensal1= Comensal("juan")
comensal1.comer_taco()               