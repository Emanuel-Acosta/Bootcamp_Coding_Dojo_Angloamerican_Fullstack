from flask import Flask, render_template, request, redirect, session 

app = Flask(__name__)
app.secret_key = 'Esta es tu clave secreta!' 

@app.route('/')
def index():
    if 'visitas' not in session:
        session['visitas'] = 0
        session['visitas'] += 1
    else:
        session['visitas'] +=1

    if 'reinicios' not in session:
        session['reinicios'] = 0    
    return render_template("index.html", visitas = session['visitas'], reinicios=session['reinicios'])

@app.route('/destruir_sesion')
def destruir_sesion():
    #session.clear()
    session.pop('visitas') #Elimina una propiedad específica
    return redirect('/')    

@app.route('/aumentar_dos')
def incrementar_visitas():
    if 'visitas' not in session:
        session['visitas'] = 0  
    session['visitas'] += 1  
    return redirect('/') 

@app.route('/reiniciar_visitas', methods= ['GET','POST'])
def reiniciar_visitas():
    session['visitas'] = 0
    session['reinicios'] += 1
    return redirect('/')

@app.route('/incrementar_num', methods=['POST'])
def incrementar_num_visitas():
    incremento = int(request.form['incremento'])  
    session['visitas'] += (incremento - 1)  
    return redirect('/')


if __name__ == "__main__":
    app.run(debug=True)