from flask import render_template, session, redirect, flash, url_for

from app.forms import LoginForm
from . import auth


@auth.route('/login', methods=['GET', 'POST'])
def login():
    login_form = LoginForm()
    context ={
        'login_form' : LoginForm()

    }

    if login_form.validate_on_submit():
        usuario = login_form.username.data
        session['usuario'] = usuario

        # Creando una alerta con flash
        flash('Nombre del usuario registrado con exito')
        
        return redirect(url_for('home'))

    return render_template('login.html', **context)
