from flask import Flask, jsonify, render_template
import random
import os

from data import pokeneas

app = Flask(__name__)

@app.route('/json')
def json_info():
    pokenea = random.choice(pokeneas)
    container_id = os.getenv("HOSTNAME", "local")  # HOSTNAME es una variable de entorno común en contenedores
    return jsonify({
        "id": pokenea["id"],
        "nombre": pokenea["nombre"],
        "altura": pokenea["altura"],
        "habilidad": pokenea["habilidad"],
        "container_id": container_id
    })

@app.route('/')
def image_and_phrase():
    pokenea = random.choice(pokeneas)
    container_id = os.getenv("HOSTNAME", "local")
    # Asumiendo que tienes una plantilla `display.html` para mostrar la imagen y la frase
    return render_template('display.html', image=pokenea["imagen"], phrase=pokenea["frase_filosofica"], container_id=container_id)

if __name__ == '__main__':
    app.run(debug=True)
