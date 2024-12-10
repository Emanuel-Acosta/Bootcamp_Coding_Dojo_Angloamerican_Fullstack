from flask_app import app

####importar los controladores de nuestro proyecto
from flask_app.controllers import estudiantes
from flask_app.controllers import cursos


if __name__=="__main__":
    app.run(debug=True)