estudiante = {"nombre": "Gonzalo", "curso": "Python"} #Notación Literal

paises = {} #Diccionario vacío

paises["MEX"] = "México" #Agregando valores

paises["COL"] = "Colombia"

paises["CHL"] = "Chile"


print(paises)

#para acceder :

print(estudiante["nombre"]) #Imprime: Gonzalo

#modificar :
estudiante["nombre"] = "Vicente"

print(estudiante["nombre"]) #Imprime: Vicente


#puede ser que exista uno que estamos creando para eso verificamos:
if "CRI" in paises: #Preguntamos si existe la clave en el diccionario

    print("¿Deseas reemplazar el valor?")

else: #No existe esa clave

    paises["CRI"] = "Costa Rica"

print(paises)

#formas de eliminar son 2 
valor_removido = paises.pop("MEX") #Elimina el elemento y devuelve su valor

del paises["COL"] #Elimina el elemento

print(paises) #Imprime: {'CHL': 'Chile'}


#puedes escribir los diccionarios tambien de forma mas legible:
pintor = { "nombre": "Frida Kahlo", "pais": "México", "fecha_nacimiento": "6 de julio de 1907"}

pintor = {

    "nombre": "Frida Kahlo",

    "pais": "México",

    "fecha_nacimiento": "6 de julio de 1907"

}

# podemos meter listas o diccionario dentro de otro:
escuela = {

    "nombre": "Coding Dojo LATAM",

    "profesores": [

        {"nombre": "Alfredo", "apellido": "Salazar", "cursos": ["Python", "Java"]},

        {"nombre": "Valeria", "apellido": "Romero", "cursos": ["Fundamentos", "Java"]},

        {"nombre": "Marcelo", "apellido": "Argotti", "cursos":["MERN", "Python"]}

    ]

}

print(escuela)

# len(diccionario) : regresa el tamaño de un diccionario . 
# str(diccionario): crea una representación de cadena (imprimible) de un diccionario. 
# type(diccionario) : regresa el tipo de la variable. Si la variable es un diccionario, devolverá un tipo de dict. 
# Veamos también algunos métodos de los diccionarios. La sintaxis puede ser dict.method(tu_diccionario) o tu_diccionario.method(), donde method es el método a utilizar.

# .clear(): elimina todos los elementos del diccionario 
# .copy() : regresa una copia del diccionario
# .get(clave, default=None): regresa el valor establecido para una clave o None si la clave no se encuentra en el diccionario. 
# .has_key(clave) : regresa verdadero (True) si la clave proporcionada está disponible en el diccionario; de lo contrario, devuelve False. 
# .items(): regresa una lista de pares de tuplas (clave, valor) del diccionario. 
# .keys(): regresa una lista de claves de diccionario. 
# .update(pares_actualizar): agrega y actualiza los pares clave-valor del diccionario enviado al diccionario existente. 
# .values(): regresa una lista de valores del diccionario. 
