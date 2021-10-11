# Trabajando con Blueprint

from flask import Blueprint

# Crear la ruta del blueprint, con un prefijo de la ruta
auth = Blueprint('auth', __name__,  url_prefix= '/auth')

from . import views