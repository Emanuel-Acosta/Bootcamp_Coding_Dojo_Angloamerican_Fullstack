from app import app 
from flask import Flask, render_template, request, redirect, session, flash
from app.models.comentario import Comentario
from app import app, bcrypt


@app.route('/comentario', methods=['POST'])
def agregar_comentario():
    if 'usuario_id' not in session:
        return redirect('/')
    comentario = request.form['comentario'].strip()
    print(f"Comentario recibido: '{comentario}'")  # Debugging statement
    if not comentario:
        flash("El comentario no puede estar vacío")
        return redirect('/publicaciones')
    data = {
        "comentario": comentario,
        "usuario_id": session['usuario_id'],
        "publicacion_id": request.form['publicacion_id']
    }
    Comentario.create(data)
    return redirect('/publicaciones')