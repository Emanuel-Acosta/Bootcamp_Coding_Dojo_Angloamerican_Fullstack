from flask_app import app #Importamos la app

from flask import render_template,redirect,request,session,flash

from flask_app.models.usuario import Usuario #Importamos desde models

@app.route("/")
def index():
    # Invocamos al método de clase get all para obtener todas las mascotas
    usuarios = Usuario.get_all()
    return render_template("index.html", todos_usuarios = usuarios)

@app.route("/nuevo_usuario", methods=['GET'])
def nuevo_usuario():
    return render_template('nuevo_usuario.html')

@app.route("/crear_usuario", methods=["POST"])
def crear_usuario():
    datos = {
        "nombre": request.form['nombre'],
        "apellido": request.form['apellido'],
        "email": request.form['email']
    }
    Usuario.save(datos)
    return redirect("/")

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.route("/usuarios/<int:id>")
def ver_usuario(id):
    usuario = Usuario.get_by_id(id)
    return render_template("ver_usuario.html", usuario=usuario)

@app.route("/usuarios/editar/<int:id>", methods=["GET"])
def editar_usuario(id):
    usuario = Usuario.get_by_id(id)
    return render_template("editar_usuario.html", usuario=usuario)

@app.route("/usuarios/actualizar/<int:id>", methods=["POST"])
def actualizar_usuario(id):
    data = {
        "nombre": request.form["nombre"],
        "apellido": request.form["apellido"],
        "email": request.form["email"],
        "id": id
    }
    Usuario.update(data)
    return redirect("/")

@app.route("/usuarios/eliminar/<int:id>")
def borrar_usuario(id):
    Usuario.delete(id)
    return redirect("/")