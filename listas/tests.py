from django.http import HttpRequest
from django.test import TestCase
from .views import home_page
from .models import Item
# Create your tests here.
from django.urls import resolve


class HomePageTest(TestCase):

    def test_verificar_html_pagina_home(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'listas/home.html')

    def test_post_request(self):
        response = self.client.post('/', data={'tarefa':'item fake'})
        self.assertEquals(Item.objects.count(), 1)
        novo_item = Item.objects.first()
        self.assertEquals(novo_item.texto, 'item fake')

    def test_redirecionamento_apos_post(self):
        response = self.client.post('/', data={'tarefa': 'item fake'})
        self.assertEquals(response.status_code, 302)
        self.assertEquals(response['location'],'/')

    def test_mostrar_todos_os_itens(self):
        Item.objects.create(texto='item 1')
        Item.objects.create(texto='item 2')

        response = self.client.get('/')

        self.assertIn('item 1', response.content.decode())
        self.assertIn('item 1', response.content.decode())

class ItemTest(TestCase):

    def test_sem_insercao_em_branco(self):
        response = self.client.get('/')
        self.assertEquals(Item.objects.count(), 0)

    def test_salvando_item_e_buscando_banco(self):
        # Criando objeto do tipo Item
        item_1 = Item()
        # Setando o texto nesse objeto
        item_1.texto = 'Primeiro Item'
        # Salvando Item
        item_1.save()
        # mesmo fluxo para o segundo item
        item_2 = Item()
        item_2.texto = 'Segundo Item'
        item_2.save()
        # Obtendo objtos salvos no banco
        items = Item.objects.all()
        item_salvo_1 = items[0]
        item_salvo_2 = items[1]
        # Fazendo os asserts
        self.assertEquals(item_salvo_1.texto, 'Primeiro Item')
        self.assertEquals(item_salvo_2.texto, 'Segundo Item')