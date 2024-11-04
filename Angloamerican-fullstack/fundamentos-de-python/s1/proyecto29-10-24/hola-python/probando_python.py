import random  # importamos la libreria, siempre al inicio

print('¡Bienvenido a Python!')

print('Este es un bucle que imprime 10 veces')
for num in range(1, 11):  # si le pongo otro numero mas seria para saber de cuanto en cuanto avanza
    print(f'num es: {num}')

semana = ['Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes']
# elige de la semana un dia al azar y lo almacena en la variable dia
dia = random.choice(semana)

print(f'Hoy es: {dia}')

if dia == 'Lunes':
    print('¡Comenzamos la semana con toda la actitud!')
elif (dia == 'Viernes'):
    print('¡Listos para un fin de semana!')
else:
    print('¿Qué día es?')

    '''
    comentario
    '''
    """
    comentarios po
    """
