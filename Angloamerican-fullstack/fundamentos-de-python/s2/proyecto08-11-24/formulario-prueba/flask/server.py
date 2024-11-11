from flask import Flask, render_template, request, redirect, session #Agregamos request y redirect

app = Flask(__name__)
app.secret_key = 'Esta es tu clave secreta!' #Establecemos una clave secreta

# La ruta raíz renderizará nuestro formulario

@app.route('/')

def index():

    return render_template("index.html")

# /crear_usuario recibe la información

@app.route('/crear_usuario', methods=['POST'])

def crear_usuario():
    

    print("Recibiendo información")

    print(request.form)
    
    #Creamos dos propiedades de sesión y almacenamos el nombre e email recibido del formulario

    session['nombre_usuario'] = request.form['nombre']

    session['email_usuario'] = request.form['email']

    #JAMAS renderizamos una plantilla ante una solicitud POST

    return redirect('/mostrar_usuario') #En su lugar, redirigimos a otra ruta


@app.route('/mostrar_usuario')

def mostrar_usuario():
    
    
    print("Usuario redirigido")

    print(session['nombre_usuario'])

    print(session['email_usuario'])

    print(request.form) #Imprime un diccionario vacío, porque no tenemos acceso a esta información

    return render_template("mostrar.html")



if __name__ == "__main__":

    app.run(debug=True)