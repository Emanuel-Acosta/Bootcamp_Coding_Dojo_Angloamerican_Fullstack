from flask import Flask, render_template, redirect, request, session


#######cracion de instancia de flask
app = Flask(__name__)

app.secret_key = '123445678'



usuario = "Kevin"
password = "1234"

################rutas
@app.route('/')
def main():
    return render_template('index.html')

@app.route('/ingresar', methods=['POST'])
def ingresar():
    print("recibiendo informacion")
    print(request.form)

    if request.form['usuario'] == usuario and request.form['password']==password:
        session['usuario'] = usuario
        return redirect('/panel_de_naves')
    else:
        return redirect('/')
    

@app.route('/panel_de_naves', methods=['POST','GET'])
def panel_de_naves():
    if 'contador' not in session:
        session['contador'] = 0
    else:
        session['contador'] += 1
    return render_template("index2.html",usuario = session['usuario'], numero_de_naves = session['contador'])

@app.route('/mas_2', methods=['POST'])
def mas_2():
    session['contador'] += 1
    return redirect("/panel_de_naves")

@app.route('/menos_1', methods=['POST'])
def menos_1():
    session['contador'] -= 2
    if session['contador'] < 0 :
        session['contador'] = -1
    return redirect('panel_de_naves') 

@app.route('/destruir_session', methods=['POST'])
def destruir_session():
    session['contador'] = -1
    return redirect('/panel_de_naves')

@app.route('/cerrar_session', methods=['POST'])
def cerrar_session():
    session.clear()
    return redirect('/')

######Iniciamos flask en modo debug
if __name__== "__main__":
    app.run(debug=True)