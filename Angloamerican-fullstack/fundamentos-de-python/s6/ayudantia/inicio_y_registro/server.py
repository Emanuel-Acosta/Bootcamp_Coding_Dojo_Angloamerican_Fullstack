from flask_app import app
#####Importacion de los controladores de su proyecto

from flask_app.controllers import usuarios

if __name__=="__main__":
    app.run(debug=True)