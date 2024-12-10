from flask_app import app
from flask import render_template, redirect,request,session
from flask_app.models.mensaje import Mensaje
from flask_app.models.usuario import Usuario

@app.route('/dashboard')
def dashboard():
    if session.get('id') == None:
        return redirect('/')
    usuarios = Usuario.get_all()
    data = {
        "receiver_id": session['id']
    }
    mensajes = Mensaje.mensajes_recibidos(data)
    print(mensajes)
    return render_template('dashboard.html', usuarios=usuarios, mensajes=mensajes)

