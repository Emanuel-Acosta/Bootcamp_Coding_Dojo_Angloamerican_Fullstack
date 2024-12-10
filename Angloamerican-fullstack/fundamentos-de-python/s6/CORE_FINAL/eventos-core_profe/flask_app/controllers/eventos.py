# controladores/eventos.py
from flask import render_template, redirect, request, flash, session, url_for
from flask_app.models.evento import Evento
from flask_app.models.usuario import Usuario
from datetime import datetime
from flask_app import app


@app.route('/nuevo_evento', methods=['GET', 'POST'])
def nuevo_evento():
    if request.method == 'GET':
        return render_template('nuevo.html')
    
    if request.method == 'POST':
        # Crear diccionario con los datos del formulario
        data = {
            'nombre': request.form['nombre'],
            'ubicacion': request.form['ubicacion'],
            'fecha_inicio': request.form['fechaInicio'],
            'detalles': request.form['detalles'],
            'id_organizador': session['usuario_id']  # Desde la sesión
        }

        # Validar los datos
        errores = Evento.validar_evento(data)
        if errores:
            for error in errores:
                flash(error, 'error')
            return render_template('nuevo.html', data=data)

        # Crear el evento
        evento_id = Evento.crear(data)
        if evento_id:
            flash('evento creado exitosamente', 'success')
            return redirect(url_for('dashboard'))
        
        flash('Error al crear el evento', 'error')
        return render_template('nuevo.html', data=data)

@app.route('/ver_evento/<int:id>')
def ver_evento(id):
    evento = Evento.obtener_por_id(id)
    if not evento:
        flash('evento no encontrado', 'error')
        return redirect(url_for('dashboard'))
    
    return render_template('ver_evento.html', evento=evento)

@app.route('/eliminar_evento/<int:id>')
def eliminar_evento(id):
    if Evento.eliminar(id):
        flash('evento eliminado exitosamente', 'success')
    else:
        flash('Error al eliminar el evento', 'error')
    return redirect(url_for('dashboard'))


@app.route("/editar_evento/<int:id>")
def editar_evento(id):
    if 'usuario_id' not in session:
        return redirect('/login')
    
    evento = Evento.obtener_por_id(id)
    if evento.id_organizador != session['usuario_id']:
        flash("No tienes permiso para editar este evento", "error") 
        return redirect(url_for('dashboard'))
    else:
        ##mostrar usuarios que no esten en el evento solamente
        print(evento)
        return render_template("editar_evento.html", data=evento)
    
@app.route("/actualizar_evento", methods=['POST'])
def actualizar_evento():
    if 'usuario_id' not in session:
        return redirect('/login')
    
    datos = {
        "id_evento": request.form['id'],
        'nombre': request.form['nombre'],
        "ubicacion": request.form['ubicacion'],
        "fecha_inicio": request.form['fechaInicio'],
        "detalles": request.form['detalles'],
    }
    Evento.actualizar(datos)

    flash("evento actualizado exitosamente", "success")
    return redirect(url_for('dashboard'))

