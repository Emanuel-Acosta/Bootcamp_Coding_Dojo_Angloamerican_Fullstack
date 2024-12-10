from flask import Flask, render_template, request, redirect
from models.pedido import Pedido

app = Flask(__name__)

# Ruta para mostrar la tabla de pedidos
@app.route('/')
def index():
    pedidos = Pedido.get_all()
    return render_template('pedidos.html', pedidos=pedidos)

# Ruta para agregar un nuevo pedido
@app.route('/nuevo_pedido', methods=['POST'])
def nuevo_pedido():
    # Validar datos antes de guardar
    if len(request.form['nombre_cliente']) < 2 or int(request.form['cantidad']) <= 0:
        return "Error: Revisa los datos ingresados."
    
    data = {
        "nombre_cliente": request.form['nombre_cliente'],
        "cantidad": int(request.form['cantidad']),
        "relleno": request.form['relleno']
    }
    Pedido.save(data)
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)
