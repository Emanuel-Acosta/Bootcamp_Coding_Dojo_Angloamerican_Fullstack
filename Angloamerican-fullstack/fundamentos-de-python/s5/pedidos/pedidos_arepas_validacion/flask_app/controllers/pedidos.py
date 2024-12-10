from flask import render_template, request, redirect
from flask_app import app
from flask_app.models.pedido import Pedido


@app.route('/arepas')
@app.route('/')
def index():
    pedidos = Pedido.get_all()
    return render_template('pedidos.html', pedidos=pedidos)

# Ruta para agregar un nuevo pedido
@app.route('/nuevo_pedido', methods=['POST'])
def nuevo_pedido():
    # Validar datos antes de guardar
    data = {
        "nombre_cliente": request.form['nombre_cliente'],
        "cantidad": int(request.form['cantidad']),
        "relleno": request.form['relleno']
    }
    if not Pedido.validar_pedido(data):
        return redirect('/nuevos_pedidos')
    else:
        Pedido.save(data)
        return redirect('/nuevos_pedidos')
    

# ruta para rediriguir a la pagina de nuevos_pedidos
@app.route('/nuevos_pedidos')
def nuevos_pedidos():
    pedidos = Pedido.get_all()
    return render_template('nuevos_pedidos.html', pedidos=pedidos)
