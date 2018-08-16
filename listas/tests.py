from django.http import HttpRequest
from django.test import TestCase
from .views import home_page

# Create your tests here.
from django.urls import resolve


class HomePageTest(TestCase):

    def test_verificar_html_pagina_home(self):
        response = self.client.request()
        self.assertTemplateUsed(response, 'listas/home.html')