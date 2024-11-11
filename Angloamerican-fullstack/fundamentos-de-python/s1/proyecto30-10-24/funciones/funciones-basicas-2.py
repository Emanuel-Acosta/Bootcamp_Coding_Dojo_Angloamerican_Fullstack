#1Multiplica por 2: crea una función que reciba un número y devuelva una lista que contenga los números enteros multiplicados por dos, desde el 0 hasta el número proporcionado como entrada.
#Ejemplo: multiplica_por_2(5) debe regresar [0, 2, 4, 6, 7, 10]

def multiplica_por_2(n):
    return [i * 2 for i in range(n + 1)]

# Ejemplo de uso:
resultado = multiplica_por_2(5)
print(resultado)  # Debería imprimir [0, 2, 4, 6, 8, 10]

def multiplicar_por_2(numero=10):
    lista = []
    for i in range(0,numero + 1,2):
        lista.append(i)
    return lista

print(multiplicar_por_2())

#2Suma y resta: crea una función que reciba una lista con dos números. Imprime la suma de los dos números y regresa la resta de los dos números.
#Ejemplo: suma_y_resta([5, 4]) debe de imprimir 9 y regresar 1

def suma_y_resta(numeros):
    suma = numeros[0] + numeros[1]  # Suma de los dos números
    resta = numeros[0] - numeros[1]  # Resta del primer número menos el segundo
    print(suma)  # Imprime la suma
    return resta  # Devuelve la resta

# Ejemplo de uso:
resultado = suma_y_resta([6, 4])
print(resultado)  # Debería imprimir 2


#3Sumatoria menos longitud: crea una función que reciba una lista de números y regresa la sumatoria de estos menos la longitud de la lista.
#Ejemplo: sumatoria_menos_longitud([1, 2, 3, 4]) debe devolver 6 (sumatoria de números: 10 – longitud: 4)

def sumatoria_menos_longitud(lista):
    
    return sum(lista) - len(lista)

x = sumatoria_menos_longitud([2,4,6,9,5,13])
print(x)

#Valores multiplicados por el segundo: escribe una función que reciba una lista y crea una nueva lista con todos los valores multiplicados por el segundo número. Imprime la longitud de la lista y regresa la nueva lista. Si la lista tiene menos de 2 elementos, haz que la función regrese una lista vacía.
#Ejemplo: valores_multiplicados_segundo([1, 3, 5, 7]) debe imprimir 4 y devolver [3, 9, 15, 21]
#Ejemplo: valores_multiplicados_segundo([1]) debe imprimir 1 y devolver [ ]

def valores_multiplicados_segundo (lista):
    if len(lista) < 2:  # Verifica si la lista tiene menos de 2 elementos
        return []  # Regresa una lista vacía
    
    nuevaLista=[]
    for i in lista:
        nuevaLista.append( i * lista[1])

    print(len(nuevaLista))
    return nuevaLista
x = valores_multiplicados_segundo([1,3,5,8])
print(x)
y = valores_multiplicados_segundo([1])
print(y)

#5Valor multiplado y longitud: escribe una función que reciba dos números enteros: valor y longitud. La función debe crear y regresar una lista cuyo tamaño sea igual a la longitud recibida y los valores sean igual a la longitud multiplicada por el valor dado.
#Ejemplo: valor_multiplicado_longitud(5, 2) regresa [10, 10]
#Ejemplo: valor_multiplicado_longitud(7, 5) regresa [35, 35, 35, 35, 35]

def valor_multiplicado_longitud(valor,longitud):
    
    # Calcula el valor multiplicado por la longitud
    valor_multiplicado = valor * longitud
    # Crea una lista con el tamaño de 'longitud', todos los elementos son 'valor_multiplicado'
    return [valor_multiplicado] * longitud

# Ejemplo de uso:
resultado1 = valor_multiplicado_longitud(5, 2)
print(resultado1)  # Debería imprimir [10, 10]

resultado2 = valor_multiplicado_longitud(7, 5)
print(resultado2)  # Debería imprimir [35, 35, 35, 35, 35]