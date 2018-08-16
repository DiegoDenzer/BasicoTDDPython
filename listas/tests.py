from django.http import HttpRequest
from django.test import TestCase
from .views import home_page

# Create your tests here.
from django.urls import resolve


class HomePageTest(TestCase):

    def test_verificar_caminho_raiz(self):
        encontrou_funcao = resolve('/')
        self.assertEquals(encontrou_funcao, home_page)

    def test_verificar_html_pagina_home(self):
        request = HttpRequest()
        response = home_page(request)
        html = response.content.decode('utf8')
        self.assertTrue(html.startswith('<html>'))
        self.assertIn('<title>Lista Tarefas</title>', html)
        self.assertTrue(html.endswith('</html>'))