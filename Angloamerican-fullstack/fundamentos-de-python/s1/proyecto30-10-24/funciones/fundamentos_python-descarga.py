# -*- coding: utf-8 -*-
"""Fundamentos_Python.ipynb

Automatically generated by Colab.

Original file is located at
   https://colab.research.google.com/drive/1a73qCySOUg1VVXuv_ZHbwIUjU_LU6nv3

# Fundamentos de python

### Variables y tipos de datos
"""

nombre = "María"
edad = 25
altura = 1.65
es_estudiante = True

print(f"Tipo de nombre: {type(nombre)}")
print(f"Tipo de edad: {type(edad)}")
print(f"Tipo de altura: {type(altura)}")
print(f"Tipo de es_estudiante: {type(es_estudiante)}")

"""### Operadores aritmeticos"""

a = 10
b = 3
suma = a+b
print(f"Suma: {suma}")
print(f"Resta: {a - b}")
print(f"Multiplicación: {a * b}")
print(f"División: {a / b}")
print(f"División entera: {a // b}")
print(f"Módulo: {a % b}")
print(f"Potencia: {a ** b}")

"""## Estructuras de Control

### Condicionales:
Una sentencia condicional es una estructura de control de flujo que nos permite ejecutar distintos bloques de código dependiendo de si una condición es verdadera o falsa. En Python, las palabras clave para estas sentencias son: if, elif y else. Veamos estas sentencias trabajar:
"""

num = 15

if num > 20:

   print("Número mayor a 20")

else:

   print("Número menor a 20")

"""### Bucles
Un **bucle** es una estructura de control de flujo que nos permite repetir la ejecución de un bloque de código varias veces, siempre y cuando se cumpla una condicional.
"""

for i in range(4):

   print(i)

for i in range(2, 8):
   print(i)

for i in range(10, 1, -3):
   print(i)

for letra in 'Python':

   print(letra)

lista = ['brócoli', 'pepino', 'pimiento']
print(len(lista))
for i in range( len(lista) ):
   print(i, lista[i])

for verdura in lista:
   print(verdura)

tupla = ('fresa', 'manzana', 'cereza')

for i in range( len(tupla) ):

   print(i, tupla[i])

estudiante = {"nombre": "Gonzalo", "curso": "Python"}

for clave in estudiante:

   print(clave)

estudiante = {"nombre": "Gonzalo", "curso": "Python"}

for clave in estudiante:

   print("Valor asociado a clave",clave,":",estudiante[clave])

platillos_tipicos = {"México": "Tacos", "Colombia": "Ajiaco", "Costa Rica": "Casado"}

#Otra forma de iterar a través de las claves

for clave in platillos_tipicos.values():

   print(clave)

for clave, valor in platillos_tipicos.items():
  print(clave, valor)

num = 0

while num<4:
  print("bucle while :", num)
  if num == 2:
    break
  num += 1
else:
  print("Se acabo el conteo")
  print("Acabamos de salir del bucle")

for letra in "detente":

   if letra == "n":

       break

   print(letra)

x = 6

while x > 2:

   print(x)

   x -= 1

   if x == 3:
   print("Es igual a 3")

else: #Recuerda: Solo se ejecuta en una salida normal, NO en un break

   print("Sentencia final")