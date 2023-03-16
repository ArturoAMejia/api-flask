

import requests
import os

def main():
    respuesta = requests.get("https://pokeapi.co/api/v2/pokemon/ditto")
    if respuesta.status_code != 200:
        raise Exception("ERROR: Consulta de API no exitosa.")
    datos = respuesta.json()

    habilidades = datos["abilities"][1]
    print(habilidades)

if __name__ == "__main__":
    main()