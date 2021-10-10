# Para crear una app factory
from flask import Flask
from flask_bootstrap import Bootstrap

# Archivo de configuracion
from .config import Config

# Declaracion de la app
# Se crea una clase creatr_app

def create_app():
    app = Flask (__name__)
    bootstrap = Bootstrap(app)

    # Configurando la llave secreta
    #app.config['SECRET_KEY'] = 'MY LLAVE SECRETA'
    app.config.from_object(Config)

    return app
