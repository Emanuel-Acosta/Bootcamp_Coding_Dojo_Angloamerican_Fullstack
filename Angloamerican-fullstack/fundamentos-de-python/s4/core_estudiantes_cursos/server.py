from flask_app import app # Importamos la instancia de la app
from flask_app.controllers import estudiantes # Importamos el controlador de estudiantes
from flask_app.controllers import cursos # Importamos el controlador de cursos


if __name__=="__main__": # Si el archivo es el principal
    app.run(debug=True) # Ejecutamos la app en modo debug