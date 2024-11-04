
#aqui imprimira de o a 3
for i in range(4):

    print(i)

#el 2 es el inicio y el 8 el fin, per no llega al 8
for i in range(2, 8):

    print(i)

#el 3 o tercer numero hace aumentar por cada vuelta en 3
for i in range(2, 10, 3):

    print(i)
    
#para restar 
for i in range(0, 15, 3):

    print(i)
#Imprime: 0, 3, 6, 9, 12

for i in range(10, 1, -3):

    print(i)

#Imprime: 10, 7, 4

#podemos recorrer tambien 
for letra in 'Python':

    print(letra)

#Imprime: 'P', 'y', 't', 'h', 'o', 'n'


#Para recorrer una lista podemos hacerlo de dos maneras distintas. En caso de necesitar los índices, podemos usar la función range y enviar como parámetro la longitud de la lista. En caso de solo necesitar los valores, podemos directamente hacer el recorrido de la lista.

lista = ['brócoli', 'pepino', 'pimiento']

for i in range( len(lista) ):

    print(i, lista[i])

#Imprime: 0 brócoli, 1 pepino, 2 pimiento

for verdura in lista:

    print(verdura)

#Imprime: brócoli, pepino, pimiento


#recorrer diccionarios:
estudiante = {"nombre": "Gonzalo", "curso": "Python"}

for clave in estudiante:

    print(clave)

#Imprime: nombre, curso

#para acceder al valor no a la llave
estudiante = {"nombre": "Gonzalo", "curso": "Python"}

for clave in estudiante:

    print(estudiante[clave])

#Imprime: Gonzalo, Python


platillos_tipicos = {"México": "Tacos", "Colombia": "Ajiaco", "Costa Rica": "Casado"}

#Otra forma de iterar a través de las claves

for clave in platillos_tipicos.keys():

    print(clave)

#Imprime: México, Colombia, Costa Rica

#Iteramos a través de los valores

for valor in platillos_tipicos.values():

    print(valor)

#Imprime: Tacos, Ajiaco, Casado

#Iteramos a través de los elementos (clave-valor)

for clave, valor in platillos_tipicos.items():

    print(clave, "=", valor)

#Imprime: México = Tacos, Colombia = Ajiaco, Costa Rica = Casado


#tenemos tambien continue el cual regresar y pasa de largo elque no queremos:
for letra in "detente":

    if letra == "n":

        continue

    print(letra)

#Imprime: d, e, t, e, t, e


#colocarle un else no sirve para un break:
x = 6

while x > 2:

    print(x)

    x -= 1

    if x == 3:

        break

else: #Recuerda: Solo se ejecuta en una salida normal, NO en un break

    print("Sentencia final")




print("hola" + "python")