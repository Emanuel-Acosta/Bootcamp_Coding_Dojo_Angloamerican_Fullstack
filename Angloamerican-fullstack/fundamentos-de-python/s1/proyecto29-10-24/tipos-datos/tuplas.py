tupla_letras = ("a", "e", "i", "o", "u")

tupla_sin_parentesis = "a", "e", "i", "o", "u"

gato = ("Miu", 5, "persa", False)

print(gato[0]) #Imprime: Miu

gato[0] = "Michi" #ERROR: TypeError: 'tuple' object does not support item assignment


gato = gato + ("4.1",)

print(gato) #Imprime: ('Miu', 5, 'persa', False, '4.1')


# len(secuencia): devuelve la longitud (cantidad de elementos) de una secuencia.
# max(secuencia): devuelve el valor más alto en una secuencia.
# min(secuencia): devuelve el valor más bajo en una secuencia.
# sorted(secuencia): devuelve una secuencia ordenada.
# sum(secuencia): devuelve la suma de los valores de la secuencia.

#para retornar varior valores en una funcion
def suma_multiplicacion(x, y):

    suma = x + y

    multiplicacion = x * y

    return (suma, multiplicacion)



