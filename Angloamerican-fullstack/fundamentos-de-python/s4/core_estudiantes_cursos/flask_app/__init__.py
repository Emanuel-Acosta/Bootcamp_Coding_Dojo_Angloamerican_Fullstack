from flask import Flask # Importamos la clase Flask
app = Flask(__name__) # Creamos una instancia de la clase Flask
app.secret_key = "12345" # Clave secreta es obligatoria para usar sesiones