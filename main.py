from flask import Flask, jsonify, render_template
import random
import os

from data import pokeneas

app = Flask(__name__)

@app.route('/json')
def json_info():
    pokenea = random.choice(pokeneas)
    container_id = os.getenv("HOSTNAME", "local")  
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
    return render_template('display.html', image=pokenea["imagen"], phrase=pokenea["frase_filosofica"], container_id=container_id)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
