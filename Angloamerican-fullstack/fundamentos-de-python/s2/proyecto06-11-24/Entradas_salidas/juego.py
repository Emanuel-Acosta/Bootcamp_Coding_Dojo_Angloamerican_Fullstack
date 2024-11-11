import random

def trivia():
    #¡Puedes colocar más preguntas en este formato!
    preguntas = [
        #Cada diccionario tiene como clave 'pregunta' y 'respuesta' con sus respectivos valores
        {'pregunta': '¿Cómo se llama la parte de la paella que queda un poco quemada y pegada al recipiente?',
        'respuesta': 'socarrat'},
        {'pregunta': '¿Cuál es el animal más lento del mundo?',
        'respuesta': 'perezoso'},
        {'pregunta': '¿Qué es completamente tuyo y encambio todos usan?',
        'respuesta': 'tu nombre'}
    ]

    pregunta_aleatoria = random.randint(0,len(preguntas)-1)
    respuesta = input(f"{preguntas[pregunta_aleatoria]['pregunta']}\n")

    if respuesta.lower() == preguntas[pregunta_aleatoria]['respuesta']:
        print("¡FELICIDADES! Ganaste el juego")
        return False
    else:
        print("Upsi, sigue intentando")
        return True

juega = True

nombre = input("¿Cuál es tu nombre? \n")

print(f"¡Hola {nombre}! Bienvenido a la trivia, te daremos una serie de preguntas, si contestas una de ellas correctamente ganas el juego.  \n ¡COMENCEMOS!")

while juega:
    juega = trivia()