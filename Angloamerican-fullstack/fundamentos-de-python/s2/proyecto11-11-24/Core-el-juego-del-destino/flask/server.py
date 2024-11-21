from flask import Flask, render_template, request, redirect, session , url_for
import random

app = Flask(__name__)
app.secret_key = 'Esta es tu clave secreta!'

@app.route('/')
def principal():
    return render_template('index.html')

@app.route('/enviar', methods=['POST'])
def enviar():
    print(request.form)
    session['nombre'] = request.form['nombre']
    session['lugar'] = request.form['lugar']
    session['numero'] = request.form['numero']
    session['comida_preferida'] = request.form['comida_preferida']
    print(session['nombre'], session['lugar'], session['numero'], session['comida_preferida'])
    session['profesion'] = request.form['profesion']
    return redirect(url_for('futuro'))

@app.route('/futuro')
def futuro():
    destino = random.choice(['buena', 'mala'])  # Mensaje aleatorio para poder saber si acerto o no.
    nombre = session.get('nombre')
    lugar = session.get('lugar')
    numero = session.get('numero')
    comida_preferida = session.get('comida_preferida')
    profesion = session.get('profesion')
    return render_template('futuro.html', destino = destino, nombre = nombre , lugar = lugar , numero = numero, comida_preferida = comida_preferida, profesion = profesion)

if __name__ == '__main__':
    app.run(debug=True)