from app import app 
from flask import Flask, render_template, request, redirect, session, flash
from app.models.usuario import Usuario
from app import app, bcrypt


@app.route('/')
def login_registro():
    return render_template('login.html')

@app.route('/registrar', methods=['POST'])
def registrar():
    data = {
        "nombre": request.form['nombre'],
        "email": request.form['email'],
        "apellido": request.form['apellido'],
        "password": request.form['password'],
        "confirmPassword": request.form['confirmPassword']
    }
    if not Usuario.validar_usuario(data):#crear metodo validar_usuario en el modelo
        return redirect('/')
    else:
        #cuando el usuario es valido
        pw_hash = bcrypt.generate_password_hash(request.form['password']) #Agregar bcrypt
        data = {
        "nombre": request.form['nombre'],
        "email": request.form['email'],
        "apellido": request.form['apellido'],
        "password": pw_hash
        }
        Usuario.save(data)
        return redirect('/')

@app.route('/iniciar_sesion', methods=['POST'])
def iniciar_sesion():
    data= {"email": request.form['email']}
    usuario = Usuario.get_by_email(data)
    if not usuario :
        flash("Email no registrado",'log_in')
        return redirect('/')
    if not bcrypt.check_password_hash(usuario.password, request.form['password']):
        flash("Contraseña incorrecta",'log_in')
        return redirect('/')
    
    session['usuario_id'] = usuario.id
    return redirect('/publicaciones')

@app.route('/log_out' , methods=['POST'])
def log_out():
    session.clear()
    return redirect ('/')