#1Actualizar valores en diccionarios y listas
matriz = [ [10, 15, 20], [3, 7, 14] ]
matriz[1][0]= 6
print(matriz)

cantantes = [

    {"nombre": "Ricky Martin", "pais": "Puerto Rico"},

    {"nombre": "Chayanne", "pais": "Puerto Rico"}

]
cantantes[0]["nombre"]="Enrique Martin Morales"
print(cantantes)

ciudades = {

    "México": ["Ciudad de México", "Guadalajara", "Cancún"],

    "Chile": ["Santiago", "Concepción", "Viña del Mar"]

}
ciudades["México"][2] = "Monterrey"
print(ciudades)


coordenadas = [

    {"latitud": 8.2588997, "longitud": -84.9399704}

]
coordenadas[0]["latitud"]= 9.9355431
print(coordenadas)


#2Iterar a través de una lista de diccionarios
cantantes = [

    {"nombre": "Ricky Martin", "pais": "Puerto Rico"},

    {"nombre": "Chayanne", "pais": "Puerto Rico"},

    {"nombre": "José José", "pais": "México"},

    {"nombre": "Juan Luis Guerra", "pais": "República Dominicana"}

]


def iterarDiccionario(cantantes):
    print(cantantes[0])
iterarDiccionario(cantantes) # mostrar solo 1

def iterarDiccionario(cantantes):
    for cantante in cantantes:
        print(f"nombre - {cantante['nombre']}, pais - {cantante['pais']}")
        

iterarDiccionario(cantantes)


#3Obtener valores de una lista de diccionarios
#Crea la función iterarDiccionario2(llave, lista) que reciba una cadena con el nombre de una llave y una lista de diccionarios.
#La función debe imprimir el valor almacenado para esa clave de cada diccionario que se encuentra en la lista. Por ejemplo,
# iterarDiccionario2(“nombre”, cantantes) debe de imprimir:
def iterarDiccionario2(llave, lista):
    for i in lista:
        for key, value in i.items():
            if key == llave:
                print(value)


cantantes = [
    {"nombre": "Ricky Martin", "pais": "Puerto Rico"},
    {"nombre": "Chayanne", "pais": "Puerto Rico"},
    {"nombre": "José José", "pais": "México"},
    {"nombre": "Juan Luis Guerra", "pais": "República Dominicana"}
]


iterarDiccionario2("nombre", cantantes)

#4 Iterar a través de un diccionario con valores de lista
#Crea una función imprimirInformacion(diccionario) que reciba un diccionario en donde los valores son listas.
#La función debe imprimir el nombre de cada clave junto con el tamaño de su lista y seguido de esto los valores
#de la lista para esa clave. Por ejemplo:

def imprimirInformacion(diccionario):
    for key, value in diccionario.items():
        print(f"{len(value)} {key.upper()}")
        for item in value:
            print(item)
        print()


costa_rica = {
    "ciudades": ["San José", "Limón", "Cartago", "Puntarenas"],
    "comidas": ["gallo pinto", "casado", "tamales", "chifrijo", "olla de carne"]
}

imprimirInformacion(costa_rica)

