from flask_app import app  # Importamos la instancia de la app
from flask import render_template,redirect,request # Importamos render_template para renderizar vistas, redirect para redireccionar y request para obtener datos de formularios
from flask_app.models.curso import Curso # Importamos el modelo de Curso

@app.route('/') 
@app.route('/cursos') # Ruta que se encarga de mostrar la vista de cursos
def cursos():
    cursos = Curso.get_all() # Obtenemos todos los cursos
    return render_template('principal.html',cursos = cursos) # Renderizamos la vista de cursos

@app.route('/cursos/<int:id>') # Ruta que se encarga de mostrar la vista de un curso en específico
def curso_id(id):
    data = {  # Creamos un diccionario con el id del curso
        'id': id 
    }
    # necesito crear aqui una variable donde pueda mostar en el html el curso segun el id de la ruta
    curso = Curso.get_curso_y_estudiantes(data) # Obtenemos el curso y sus estudiantes
    return render_template('curso_id.html', curso = curso ) # Renderizamos la vista de curso en específico

@app.route('/cursos/guardar', methods = ['POST']) # Ruta que se encarga de guardar un curso
def guardar_curso():
    data = { # Creamos un diccionario con los datos del curso
        'nombre' : request.form['nombre'] # Obtenemos el nombre del curso

    }
    Curso.crear(data) # Creamos el curso
    return redirect('/')