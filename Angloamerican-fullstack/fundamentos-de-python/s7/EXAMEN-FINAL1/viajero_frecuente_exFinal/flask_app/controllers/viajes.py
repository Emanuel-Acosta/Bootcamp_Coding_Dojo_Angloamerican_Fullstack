from flask_app.config.mysqlconnection import connectToMySQL
from flask import render_template, redirect, request, flash, session, url_for
from flask_app.models.viaje import Viaje
from flask_app.models.usuario import Usuario
from datetime import datetime
from flask_app import app

DATABASE = 'viajeros_frecuentes'

@app.route('/nuevo_viaje', methods=['GET', 'POST']) 
def nuevo_viaje():
    if request.method == 'GET':
        return render_template('nuevo.html')
    
    if request.method == 'POST':
        data = {
            'nombre': request.form['nombre'],
            'fecha_inicio': request.form['fechaInicio'],
            'fecha_de_fin': request.form['fechaFin'],
            'itinerario': request.form['itinerario'],
            'id_organizador': session['usuario_id'] 
        }
        errores = Viaje.validar_viaje(data)
        if errores:
            for error in errores:
                flash(error, 'error')
            return render_template('nuevo.html', data=data)
        viaje_id = Viaje.crear(data)
        if viaje_id:
            flash('viaje creado exitosamente', 'success')
            return redirect(url_for('dashboard'))
        flash('Error al crear el viaje', 'error')
        return render_template('nuevo.html', data=data)

@app.route('/ver_viaje/<int:id>')
def ver_viaje(id):
    viaje = Viaje.obtener_por_id(id)
    if not viaje:
        flash('viaje no encontrado', 'error')
        return redirect(url_for('dashboard'))
    viajeros = Viaje.obtener_viajeros(id)

    usuario_id = session['usuario_id']
    query = """
        SELECT * FROM viajeros
        WHERE viaje_id = %(viaje_id)s AND usuario_id = %(usuario_id)s;
    """
    data = {'viaje_id': id, 'usuario_id': usuario_id}
    usuario_unido = connectToMySQL(DATABASE).query_db(query, data)
    return render_template('ver_viaje.html', viaje=viaje, viajeros=viajeros, usuario_unido=usuario_unido)

@app.route('/eliminar_viaje/<int:id>')
def eliminar_viaje(id):
    if Viaje.eliminar(id):
        flash('viaje eliminado exitosamente', 'success')
    else:
        flash('Error al eliminar el viaje', 'error')
    return redirect(url_for('dashboard'))


@app.route("/editar_viaje/<int:id>")
def editar_viaje(id):
    if 'usuario_id' not in session:
        return redirect('/login')
    
    viaje = Viaje.obtener_por_id(id)
    if viaje.id_organizador != session['usuario_id']:
        flash("No tienes permiso para editar este viaje", "error") 
        return redirect(url_for('dashboard'))
    else:
        return render_template("editar_viaje.html", data=viaje)
    
@app.route("/actualizar_viaje", methods=['GET', 'POST'])  
def actualizar_viaje():
    if 'usuario_id' not in session:
        return redirect('/login')
    
    if request.method == 'POST':
        datos = {
            'id_viaje': request.form['id'],
            'nombre': request.form['nombre'],
            'fecha_inicio': request.form['fechaInicio'],
            'fecha_de_fin': request.form['fechaFin'],
            'itinerario': request.form['itinerario'],
            'id_organizador': session['usuario_id']
        }
        errores = Viaje.validar_viaje(datos)
        if errores:
            for error in errores:
                flash(error, 'error')
            return render_template('editar_viaje.html', data=datos)
        Viaje.actualizar(datos)
        flash('viaje actualizado exitosamente', 'success')
        return redirect(url_for('dashboard'))

@app.route('/unirse/<int:viaje_id>')
def unirse(viaje_id):
    if 'usuario_id' not in session:
        return redirect(url_for('login'))
    usuario_id = session['usuario_id']
    query = """
        SELECT * FROM viajeros 
        WHERE viaje_id = %(viaje_id)s AND usuario_id = %(usuario_id)s;
    """
    data = {'viaje_id': viaje_id, 'usuario_id': usuario_id}
    existe_participante = connectToMySQL(DATABASE).query_db(query, data)

    if existe_participante:
        delete_query = """
            DELETE FROM viajeros 
            WHERE viaje_id = %(viaje_id)s AND usuario_id = %(usuario_id)s;
        """
        connectToMySQL(DATABASE).query_db(delete_query, data)
    else:
        insert_query = """
            INSERT INTO viajeros (viaje_id, usuario_id)
            VALUES (%(viaje_id)s, %(usuario_id)s);
        """
        connectToMySQL(DATABASE).query_db(insert_query, data)
    return redirect(url_for('ver_viaje', id=viaje_id))


