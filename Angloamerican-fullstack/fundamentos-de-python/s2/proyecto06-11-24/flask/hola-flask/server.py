from flask import Flask, render_template  # Importamos render_template

app = Flask(__name__)

@app.route('/listas')

def renderizar_listas():

    #Próximamente estas listas serán extraidas de la base de datos

    listado_estudiantes = [

        {'nombre': 'Florencia', 'edad': 25},

        {'nombre': 'Valentina', 'edad': 30},

        {'nombre': 'José', 'edad': 27},

        {'nombre': 'Patricio', 'edad': 21}

    ]

    return render_template('listas.html', numeros=[7, 15, 22], estudiantes=listado_estudiantes)


@app.route('/bienvenido')

def bienvenido():

    #En vez de regresar una cadena, regresamos el resultado del método render_template

    #enviando el nombre del archivo de HTML que queremos renderizar

    return render_template('index.html', cancion="dale a tu cuerpo alegría macarena", repite=5)


#La ruta sería: /saludo/_______ <- Cualquier cosa después de '/saludo/' se recibe como variable 'nombre'
@app.route('/saludo/<nombre>')

def saludo(nombre):

    print(nombre) #Imprime en la terminal el nombre enviado a través de la URL

    return (f'¡Hola {nombre}!') #Regresa al navegador '¡Hola ____!' con el nombre enviado a través de la URL


#La ruta sería: /color/_____/_____ , se envían 2 parámetros a través de la URL como nombre y color
@app.route('/color/<nombre>/<color>')

def color_favorito(nombre, color):

    print(nombre)

    print(color)

    return f'Hola {nombre}, tu color favorito es el {color}'

#El segundo parámetro se convierte en número entero antes de ser pasado a la función
@app.route('/saludo/<nombre>/<int:num>')

def hola_cantidad(nombre, num):

    return f'¡Hola {nombre}!'*num


if __name__=="__main__":   

    app.run(debug=True)