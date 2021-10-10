# Primer archivo de test
# Importacion de la libreria de testing
from flask.helpers import url_for
from flask_testing import TestCase
from flask import current_app

# Importacion de nuestra aplicacion from nombde de mi archivo.py 
# para este ejercicio es app.py
from app import app


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
        # Validar que el POST responde de un formulario
        fake_form = {
            'username': 'fake',
            'password': 'fake-password'
        }
        response = self.client.post(url_for('home'), data=fake_form)
        # Marca error con el index
        #self.assertRedirects(response, url_for('index'))

        # Marca ok cuando le ponemos a la misma ruta
        # self.assertRedirects(response, url_for('home'))
        
        self.assertRedirects(response, url_for('index'))
