#1Básico: imprime todos los números enteros del 0 al 100.
for enteros in range(0,101):
    print(enteros)

#2Múltiples de 2: imprime todos los números múltiplos de 2 entre 2 y 500
for multiplos in range(2,502,2):
    print(multiplos)

#3Contando Vanilla Ice: imprime los números enteros del 1 al 100. Si es divisible por 5 imprime “ice ice” en vez del número. Si es divisible por 10, imprime “baby”
for enteros in range(1,101):
    if enteros % 10 == 0:
        
        print("ice ice") 
        print("baby")

    elif enteros % 5 == 0:
        
        print("ice ice")  
    
    else: 
        print(enteros)


#4Wow. Número gigante a la vista: suma los números pares del 0 al 500,000 e imprime la suma total. (Sorpresa, será un número gigante).
suma = 0
for pares in range(0,500002,2):
    suma += pares
print(suma)  

#5Regrésame al 3: imprime los números positivos comenzando desde 2024, en cuenta regresiva de 3 en 3.
for resta in range(2024,0,-3):
    print(resta)

#6Contador dinámico: establece tres variables: numInicial, numFinal y multiplo.     
#Comenzando en numInicial y pasando por numFinal, imprime los números enteros que sean múltiplos de multiplo. 
#Por ejemplo: si numInicial = 3, numFinal = 10, y multiplo = 2, el bucle debería de imprimir 4, 6, 8, 10 (en líneas sucesivas).
numInicial = 5
numFinal= 30
multiplo = 3
for i in range(numInicial,numFinal+1,1):
    if i % multiplo == 0:
        print(i)


