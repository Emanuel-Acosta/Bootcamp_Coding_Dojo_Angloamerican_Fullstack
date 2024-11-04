numero1 = 70  # variable tipo entera
numero2 = 3.14  # variable tipo decimal
booleano = False  # variable booleana
cadena = 'Hola Mundo'  # variable tipo cadena
ingredientes_pastel = ['Harina', 'Leche','Huevos', 'Vainilla', 'Chocolate']  # lista
persona = {'nombre': 'Patricio', 'pais': 'México','edad': 35, 'soltero': False}  # diccionario 
frutas = ('guayaba', 'fresa', 'papaya')  # tupla
print(type(frutas))
print(ingredientes_pastel[2])
ingredientes_pastel.append('Mantequilla')
print(persona['nombre'])
persona['nombre'] = 'Kevin'
persona['color_ojos'] = 'cafe'
print(frutas[2])

if numero1 > 45:
    print("Numero mayor")
else:
    print("Numero menor")

if len(cadena) < 5:
    print("Cadena corta")
elif len(cadena) > 15:
    print("Cadena larga")
else:
    print("Cadena perfecta")

for x in range(8):
    print(x)
for x in range(2, 8):
    print(x)
for x in range(2, 8, 2):
    print(x)
x = 0
while (x < 8):
    print(x)
    x += 1

ingredientes_pastel.pop()
ingredientes_pastel.pop(1)

print(persona)
persona.pop('color_ojos')
print(persona)

for ingrediente in ingredientes_pastel:
    if ingrediente == 'Harina':
        continue
    print('Después de la primera sentencia')
    if ingrediente == 'Chocolate':
        break


def imprime_hola_10_veces():
    for numero in range(10):
        print('Hola')


imprime_hola_10_veces()


def imprime_hola_n_veces(n):
    for numero in range(n):
        print('Hola')


imprime_hola_n_veces(5)


def imprime_hola_n_o_diez_veces(n=10):
    for numero in range(n):
        print('Hola')


imprime_hola_n_o_diez_veces()
imprime_hola_n_o_diez_veces(5)


"""
Sección BONUS
"""

# print(numero3)
# numero3 = 86
# frutas[0] = 'naranja'
# print(persona['hobbies'])
# print(ingredientes_pastel[11])
#   print(booleano)
# frutas.append('manzana')
# frutas.pop(1)
