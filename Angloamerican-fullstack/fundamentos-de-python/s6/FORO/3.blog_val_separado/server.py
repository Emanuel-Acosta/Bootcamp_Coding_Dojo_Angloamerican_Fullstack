from app import app  # Importamos la app de la carpeta flask_app
from app.controllers import publicaciones, comentarios, usuarios  # Importamos los controladores

if __name__ == "__main__":  # Ejecutamos la aplicación

    app.run(debug=True)
