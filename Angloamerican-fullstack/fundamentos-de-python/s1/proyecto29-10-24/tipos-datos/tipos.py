lista_vacia = []

gatos = ["Garfield", "Silvestre", "Hello Kitty"]

print(gatos[2]) #Imprime: hello kitty

gatos[1] = "Tom"

gatos.append("Felix") 

print(gatos) #Imprime: ['Garfield', 'Tom', 'Hello Kitty', 'Felix']

gatos.pop()

print(gatos) #Imprime: ['Garfield', 'Tom', 'Hello Kitty']

gatos.pop(1)

print(gatos) #Imprime: ['Garfield', 'Hello Kitty']

#duplas
perro = ("Scooby Doo", "Gran Danés", "Scooby Galletas", 7)

print(perro[0]) #Imprime: Scooby Doo

perro[2] = "comida de perro" #ERROR: Las tuplas no pueden ser modificadas (TypeError: 'tuple' object does not support item assignment)

#diccionarios
diccionario_vacio = {}

persona = {'nombre': 'Carmen', 'edad': 31, 'altura': 1.71, 'usa_lentes': False}

persona['nombre'] = 'Valeria'  # Actualiza si el valor de la llave existente

persona['hobbies'] = ['jugar videojuegos', 'programación'] 

# Agrega esa clave-valor si no existía previamente

print(persona)

# Imprime: {'nombre': 'Carmen', 'edad': 31, 'altura': 1.71, 'usa_lentes': False, 'hobbies': ['jugar videojuegos', 'programación']}

altura = persona.pop('altura')  # Elimina la clave indicada y devuelve el valor

print(altura)    # Imprime: 1.71

print(persona) 

# salida: {'nombre': 'Carmen', 'edad': 31, 'usa_lentes': False, 'hobbies': ['jugar videojuegos', 'programación']} 


print(len(persona)) #Imprime: 4 (la cantidad de pares de clave-valor)

print(len("Me encanta programar")) #Imprime: 20

# para concatenar cadenas con int.
print("¿Cuántas vocales hay? " + 5) 

#ERROR: TypeError: can only concatenate str (not "int") to str

print("¿Cuántas vocales hay? " + str(5)) #Imprime: ¿Cuántas vocales hay? 5

#de cadena a int
tiempo_preparacion = 1

tiempo_horneado = "2"

tiempo_total = tiempo_preparacion + tiempo_horneado 

#ERROR: TypeError: unsupported operand type(s) for +: 'int' and 'str'

tiempo_total = tiempo_preparacion + int(tiempo_horneado) #Imprime: 3


#concatenar con f
nombre = "Marcelo"

edad = 29

print(f"Mi nombre es {nombre} y tengo {edad} años de edad.")


#antes se hacia asi:
nombre = "Marcelo"

edad = 29

print("Mi nombre es {} y tengo {} años de edad.".format(nombre, edad))

#Imprime: Mi nombre es Marcelo y tengo 29 años de edad.

print("Tengo {} años de edad y mi nombre es {}".format(edad, nombre))

#Imprime: Tengo 29 años de edad y mi nombre es Marcelo.

# y tambien antes se utilizaba el %
nombre = "Marcelo"

edad = 29

print("Mi nombre es %s y tengo %d años de edad." % (nombre, edad))

#Imprime: Mi nombre es Marcelo y tengo 29 años de edad.


# aqui tenemos otros meodos de cadenas integrado
# string.upper(): regresa la cadena con todos los caracteres en mayúscula.
# string.lower(): regresa la cadena con todos los caracteres en minúscula.
# string.count(substring): regresa el número de recurrencias de una subcadena de una cadena.
# string.split(caracter):regresa una lista de valores donde la cadena es dividida en el carácter especificado. En caso de no enviar el carácter, la división se hace en cada espacio.
# string.find(substring): regresa el índice del comienzo de la primer recurrencia de la subcadena dentro de una cadena.
# string.isalnum(): regresa un booleano dependiendo de si la longitud de la cadena es > 0 y todos los caracteres sean alfanuméricos (solo letras y números). Las cadenas que incluyen espacios y puntuación devolverán False con este método. Métodos similares incluyen .isalpha(), .isdigit(), .islower(), .isupper(),  entre otros. Todos devuelven booleanos.
# string.join(lista): regresa una cadena que contiene todas las cadenas de nuestro conjunto (en este caso, una lista) concatenadas.
# string.endswith(substring): regresa True o False si los últimos caracteres de la cadena coinciden con la subcadena.