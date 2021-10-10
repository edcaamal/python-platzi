# Mi primer proyecto web en python y flask
# Octubre 2021

from flask import Flask, redirect, url_for, render_template, request, session
from flask.helpers import flash, make_response
# Librerias de BootStrap
# from flask_bootstrap import Bootstrap

# iportamos libreias de unittest
import unittest

#importando archivo para crear la app
from app import create_app

# importanto las formas
from app.forms import LoginForm

app = create_app()

# Declaracion de la app
#app = Flask (__name__)
#bootstrap = Bootstrap(app)

# Configurando la llave secreta
#app.config['SECRET_KEY'] = 'MY LLAVE SECRETA'

todos = ['Comprar cafe', 'Enviar solicitud de compra', 'Enviar video']

# Se mueve hacia un archivo denominado forms.py
# Creacion de formularios con wtf
# class LoginForm(FlaskForm):
#    username = StringField('Nombre del usuario', validators=[DataRequired()])
#    password = StringField('Password', validators=[DataRequired()])
#    submit = SubmitField('Enviar')

# Testing
@app.cli.command()
def test():
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner().run(tests)



# Creando las rutas, a traves de decoradores
@app.errorhandler(404)
def not_found(error):
    return render_template('404.html', error=error)

@app.errorhandler(500)
def server_error(error):
    return render_template('500.html', error=error)

@app.route('/')
def index():
    usuario = request.remote_addr
    response = make_response(redirect('/home'))
    #response.set_cookie('usuario', usuario)
    session['usuario'] = usuario

    # return redirect(url_for('home'))
    return response

@app.route('/home', methods=['GET', 'POST'])
def home():
    #usuario = request.cookies.get('usuario')
    usuario = session.get('usuario')
    user_ip = request.remote_addr
    texto = '[-] Con las manos en el <strong>codigo<strong> {}{}'.format(user_ip, usuario)
    login_form = LoginForm()
    contex = {
        'user_ip': user_ip,
        'todos': todos,
        'usuario': usuario,
        'texto': texto,
        'login_form': login_form,
    }
    
    if login_form.validate_on_submit():
        usuario = login_form.username.data
        session['usuario'] = usuario

        # Creando una alerta con flash
        flash('Nombre del usuario registrado con exito')
        
        return redirect(url_for('home'))


    return render_template('home.html', **contex)

@app.route('/nosotros')
def nosotros():
    return render_template('nosotros.html')

# Programa principal
if __name__ == '__main__':
    app.run(debug=True)