from flask_app import app
from flask import render_template, redirect,request,session
from flask_app.models.amistad import Amistad
from flask_app.models.usuario import Usuario



@app.route('/')

def main():
    users_with_friendships = Usuario.get_users_with_friends()
    print(users_with_friendships)
    # usarios = Usuario.get_all()
    return render_template('index.html', users_with_friendships = users_with_friendships)


