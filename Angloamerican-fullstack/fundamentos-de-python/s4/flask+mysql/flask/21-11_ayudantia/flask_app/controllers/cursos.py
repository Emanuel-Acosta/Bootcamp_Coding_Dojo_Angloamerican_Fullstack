from flask_app import app
from flask import render_template,redirect,request
from flask_app.models.curso import Curso

@app.route('/')
@app.route('/cursos')
def cursos():
    cursos = Curso.get_all()
    return render_template('dashboard.html',cursos = cursos)


@app.route('/cursos/<int:id>')
def courso_id(id):
    data = {
        'id': id
    }
    curso = Curso.get_curso_y_estudiantes(data)
    return render_template('curso_id.html', curso = curso)




@app.route('/cursos/guardar', methods = ['POST'])
def guardar_curso():
    data = {
        'nombre' : request.form['nombre']

    }
    Curso.crear(data)
    return redirect('/')