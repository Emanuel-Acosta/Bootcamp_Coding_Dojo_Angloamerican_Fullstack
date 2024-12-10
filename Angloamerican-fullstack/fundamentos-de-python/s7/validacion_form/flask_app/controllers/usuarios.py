from flask import render_template, request, redirect, session, flash
from flask_app import app, bcrypt
from flask_app.models.usuario import Usuario
from datetime import date

# Rutas de la aplicación


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/dashboard")
def dashboard():
    usuario = Usuario.get_by_id(session['usuario_id'])
    return render_template("dashboard.html", usuario=usuario)


@app.route('/register', methods=['POST'])
def crear_usuario():
    data = {
        'nombre': request.form['nombre'],
        'apellido': request.form['apellido'],
        'email': request.form['email'],
        'password': request.form['password'],
        'confirmPassword': request.form['confirmPassword']
    }
    if not Usuario.validar_usuario(data):
        return redirect('/')  # si la validación falla, redirigir al formulario
    else:
        pw_hash = bcrypt.generate_password_hash(request.form['password'])
        data = {
            'nombre': request.form['nombre'],
            'apellido': request.form['apellido'],
            'email': request.form['email'],
            'password': pw_hash
        }
        Usuario.save(data)
        return redirect('/')

@app.route("/login", methods=['POST'])
def login():
    # Verificamos que el email exista en BD
    usuario = Usuario.get_by_email(request.form['loginEmail'])
    if not usuario:  # En caso de no estar registrado mandamos mensaje de error
        flash("E-mail no registrado", "login")
        return redirect("/")
    # Comparamos las contraseñas
    if not bcrypt.check_password_hash(usuario.password, request.form['loginPassword']):
        # Si no coinciden mandamos mensaje error
        flash("Password incorrecto", "login")
        return redirect("/")
    session['usuario_id'] = usuario.id  # Guardamos en sesión el id del usuario
    return redirect("/dashboard")


@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')
