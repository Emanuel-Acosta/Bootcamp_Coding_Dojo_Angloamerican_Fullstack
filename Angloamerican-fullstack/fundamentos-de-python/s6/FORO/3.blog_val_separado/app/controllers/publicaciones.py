from app import app 
from flask import Flask, render_template, request, redirect, session, flash
from app.models.publicacion import Publicacion
from app.models.comentario import Comentario
from app.models.usuario import Usuario
from app import app, bcrypt

@app.route('/publicaciones')
def publicaciones():
    nombre = Usuario.get_by_id({"id": session['usuario_id']}).nombre
    if 'usuario_id' not in session:
        return redirect('/')
    publicaciones = Publicacion.get_all() #lista de publicaciones
    for pub in publicaciones:
        pub.comentarios = Comentario.get_by_publicacion_id({"publicacion_id": pub.id}) # Obtiene lISTA de comentarios de cada publicación
        autor = Usuario.get_by_id({"id": pub.usuario_id}) # Obtiene el usuario de cada publicación
        pub.autor = autor.nombre  # Accede al campo nombre del objeto autor y lo asigna a la publicación
    return render_template('publicaciones.html', publicaciones=publicaciones, nombre=nombre)

@app.route('/publicar', methods=['POST'])
def publicar():
    if 'usuario_id' not in session:
        return redirect('/')
    data = {
        "contenido": request.form['contenido'],
        "usuario_id": session['usuario_id']
    }
    Publicacion.create(data)
    return redirect('/publicaciones')

@app.route('/eliminar/<int:id>')
def eliminar(id):
    if 'usuario_id' not in session:
        return redirect('/')
    data = {"id": id}
    Publicacion.delete(data)
    return redirect('/publicaciones')

