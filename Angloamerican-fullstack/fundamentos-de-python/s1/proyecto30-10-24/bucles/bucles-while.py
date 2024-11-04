num = 0

while num < 4:

    print("bucle while -", num)

    num += 1

#Imprime: bucle while - 0, bucle while - 1, bucle while - 2, bucle while - 3

#con else si hay break o return nunca se ejecuta
num = 0

while num < 4:

    print("bucle while -", num)

    num += 1

else:

    print("Acabamos de salir del bucle")

#podemos utilizar el brak para frenar antes de que termine un for o un while
for letra in "detente":

    if letra == "n":

        break

    print(letra)

#Imprime: d, e, t, e  




