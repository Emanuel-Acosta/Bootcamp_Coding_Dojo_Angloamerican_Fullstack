from flask import Flask, render_template

app = Flask(__name__)

@app.route('/juego')
def home():
    return render_template('index.html', pelotas =3)

@app.route('/juego/<int:num>')
def home_num(num):
    return render_template('index.html', pelotas = num)

@app.route('/juego/<int:num>/<color>')
def home_num_color(num,color):
    return render_template('index.html', pelotas = num , color = color)

if __name__ == '__main__':
    app.run(debug=True)