# Mi primer proyecto web en python y flask
# Octubre 2021

from flask import Flask, redirect, url_for, render_template, request, session
from flask.helpers import make_response
# Librerias de BootStrap
from flask_bootstrap import Bootstrap
# Librerias de wft
from flask_wtf import FlaskForm
from wtforms.fields import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired

# Declaracion de la app
app = Flask (__name__)
bootstrap = Bootstrap(app)

# Configurando la llave secreta
app.config['SECRET_KEY'] = 'MY LLAVE SECRETA'

todos = ['Comprar cafe', 'Enviar solicitud de compra', 'Enviar video']

class LoginForm(FlaskForm):
    username = StringField('Nombre del usuario', validators=[DataRequired()])
    password = StringField('Password', validators=[DataRequired()])
    submit = SubmitField('Enviar')


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
        
        return redirect(url_for('home'))


    return render_template('home.html', **contex)

@app.route('/nosotros')
def nosotros():
    return render_template('nosotros.html')


if __name__ == '__main__':
    app.run(debug=True)