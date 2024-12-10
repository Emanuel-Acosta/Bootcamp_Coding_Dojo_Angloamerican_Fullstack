from flask_app import app
from flask import render_template, redirect,request,session
from flask_app.models.nave import Nave
from flask_app.models.usuario import Usuario



@app.route('/')
def main():
    naves_con_pilotos = Nave.naves_con_pilotos()
    print(naves_con_pilotos)
    usarios = Usuario.get_all()
    print(usarios)
    return render_template('index.html', naves_con_pilotos = naves_con_pilotos, usarios = usarios)

@app.route('/naves/crear', methods = ['POST'])
def crear_amistad():
    data = {
        'user_id' : request.form['user_id'],
        'nombre' : request.form['nombre'],
        'capacidad' : request.form['capacidad']
    }
    if not Nave.validar(data):
        return redirect('/')
    Nave.save(data)
    return redirect('/')
