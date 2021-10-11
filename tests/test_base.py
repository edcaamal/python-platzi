# Primer archivo de test
# Importacion de la libreria de testing
from flask.helpers import url_for
from flask_testing import TestCase
from flask import current_app

# Importacion de nuestra aplicacion from nombde de mi archivo.py 
# para este ejercicio es app.py
from main import app


class MainTest(TestCase):
    def create_app(self):
        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLED'] = False

        return app
    
    def test_app_exist(self):
        # Valida que si esxite el nombre de la aplicaion
        # self.assertIsNotNone(current_app)

        self.assertIsNotNone(current_app)

        # Valida que la aplicaicon no tenga nombre
        #self.assertIsNone(current_app)

    def test_app_in_test_mode(self):
        # test para validar que nuestra aplicacion se encuentra en modo de testeo
        self.assertTrue(current_app.config['TESTING'])

    def test_index_redirect(self):
        # Validar que nuetro index nos manda a la ruta /home
        response = self.client.get(url_for('index'))
        self.assertRedirects(response, url_for('home'))
        
    def test_home_get(self):
        # validar que home nos regresa un 200 de exitoso
        response = self.client.get(url_for('home'))
        self.assert200(response)

    def test_home_post(self):
        # Codigo para formularios 405
        response = self.client.post(url_for('home'))
        self.assertTrue(response.status_code, 405)

    def test_auth_blueprint_exists(self):
        self.assertIn('auth', self.app.blueprints)

    def test_auth_login_get(self):
        # Validar que la vista nos retorna un valor 200, 
        # el nombre de la funcion debe ser igual a la declarada
        response = self.client.get(url_for('auth.login'))
        self.assert200(response)

    def test_auth_login_template(self):
        # Validar que se retorna una vista template a traves de auth
        self.client.get(url_for('auth.login'))
        self.assertTemplateUsed('login.html')

    def test_auth_login_post(self):
        fake_form = {
            'username': 'fake',
            'password': 'fake-password'
        }

        response = self.client.post(url_for('auth.login'), data=fake_form)
        self.assertRedirects(response, url_for('home'))
