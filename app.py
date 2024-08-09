from flask import Flask, request, jsonify, send_from_directory
import os

app = Flask(__name__)

# Definir las opciones del menú USSD
menu = {
    "1": "Consultar Saldo",
    "2": "Comprar Tiempo Aire",
    "3": "Comprar Datos",
    "4": "Atención al Cliente"
}

@app.route('/')
def home():
    return send_from_directory(os.path.abspath(os.path.dirname(__file__)), 'index.html')

@app.route('/ussd', methods=['POST'])
def ussd():
    seleccion = request.form.get('seleccion')
    if seleccion in menu:
        response = f"Seleccionaste: {menu[seleccion]}"
    else:
        response = "Selección inválida. Por favor, inténtalo de nuevo."
    
    return jsonify({"response": response})

if __name__ == '__main__':
    app.run(debug=True)
