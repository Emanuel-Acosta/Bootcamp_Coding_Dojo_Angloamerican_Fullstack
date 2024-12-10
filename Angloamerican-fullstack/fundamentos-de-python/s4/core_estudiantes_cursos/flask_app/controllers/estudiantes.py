from flask_app import app 
from flask import render_template,redirect,request
from flask_app.models.estudiante import Estudiante 
from flask_app.models.curso import Curso 


@app.route('/estudiantes/nuevo') # Ruta que se encarga de mostrar la vista de nuevo estudiante
def nuevo_estudiante():
    cursos = Curso.get_all() # Obtenemos todos los cursos para el despliegue en el formulario
    print(cursos)
    return render_template('nuevo_estudiante.html',cursos = cursos)

@app.route('/estudiantes/guardar', methods = ['POST']) # Ruta que se encarga de guardar un estudiante
def guardar_estudiante():
    data = { # Creamos un diccionario con los datos del estudiante
        'nombre' : request.form['nombre'],
        'apellido' : request.form['apellido'],
        'edad' : request.form['edad'],
        'curso_id' : request.form['curso_id'],
    }
    Estudiante.crear(data) # Creamos el estudiante
    return redirect('/')