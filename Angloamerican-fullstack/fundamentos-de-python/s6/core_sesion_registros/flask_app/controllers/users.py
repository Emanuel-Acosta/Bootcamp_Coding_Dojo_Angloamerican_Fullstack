from flask_app import app
from flask import render_template,redirect,request,session,flash
from flask_app.models.user import User 
from flask_bcrypt import Bcrypt

# Creación de objeto Bcrypt
bcrypt = Bcrypt(app)


@app.route('/', methods=['GET', 'POST']) #GET para mostrar la página, POST para enviar datos
def index():
    if request.method =='POST': 
        if not User.validate_entry(request.form): 
            return redirect('/')
        if request.form.get("which_form")=='register_user': 
            data = {
            "nombre" : request.form.get("nombre"),
            "apellido" : request.form.get("apellido"),
            "email" : request.form.get("email"),
            "password" : bcrypt.generate_password_hash(request.form.get("password")),
            }
            user=User.getbyemail(data)
            if user is not None:
                flash(["Email address has been already registered!",0])
                return redirect('/')
            user=User.save(data)
            session["id_usuario"] = user.id_usuario
            session["nombre"] = user.nombre
            session["apellido"] = user.apellido
            session["email"] = user.email
            data = {'sender_id': session['id_usuario']}
            return redirect('/dashboard')
        elif request.form.get("which_form")=='log_in':
            data = {
            "email" : request.form.get("email"),
            "password" : request.form.get("password")
            }
            user=User.getbyemail(data)
            if user is None or  not bcrypt.check_password_hash(user.password, data['password']):
                flash(["Invalid Email/Password",1])
                return redirect('/')
            session["id_usuario"] = user.id_usuario
            session["nombre"] = user.nombre
            session["apellido"] = user.apellido
            session["email"] = user.email
            return redirect('/dashboard')
    else:
        return render_template("index.html")
    

@app.route('/dashboard')
def dashboard():
    if 'id_usuario' not in session:
        return redirect('/')
    return render_template('dashboard.html')  # Renderiza la plantilla del dashboard    


@app.route('/log_out' , methods=['POST'])
def log_out():
    session.clear()
    return redirect ('/')