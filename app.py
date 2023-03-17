

import requests
import os
from flask import Flask,render_template

app = Flask(__name__)


# def main():



@app.route("/", methods=["GET"])
def index():
    
    respuesta = requests.get(f'https://pokeapi.co/api/v2/pokemon/ditto')
    if respuesta.status_code != 200:
        raise Exception("ERROR: Consulta de API no exitosa.")
    datos = respuesta.json()

    nombre = datos["name"]
    habilidades = datos["abilities"]
    sprites = datos["sprites"]

    print(datos)
    return render_template("index.html", nombre=nombre, habilidades=habilidades, sprites=sprites)


@app.route("/<int:id>", methods=["GET"])
def pokemon_by_id(id):

    respuesta = requests.get(f'https://pokeapi.co/api/v2/pokemon/{id}')
    if respuesta.status_code != 200:
        raise Exception("ERROR: Consulta de API no exitosa.")
    datos = respuesta.json()

    nombre = datos["name"]
    habilidades = datos["abilities"]
    sprites = datos["sprites"]

    print(datos)
    return render_template("index.html", nombre=nombre, habilidades=habilidades, sprites=sprites)

