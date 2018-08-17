import unittest
import time
from django.test import LiveServerTestCase
from selenium import webdriver
# TESTE NO CHROME navegador_chrome = webdriver.Chrome()
# #navegador_chrome.get('http://localhost:8000')#assert 'Django' in navegador_chrome.title
from selenium.webdriver.common.keys import Keys


class NovaVisitaTest(LiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def verificar_linha_da_tabela(self, linha):
        # Entao ele verifica sua tarefas
        # Pega a tabela pelo seu elemento id
        table = self.browser.find_element_by_id('id_list_table')
        # Pega as linhas da tabela pelo elemento de tag <tr>
        linhas = table.find_elements_by_tag_name('tr')
        # [resultado para linha em linhas]-> Isso e uma lista conphanions for para usar o for em um linha
        self.assertIn(linha, [l.text for l in linhas])

    def test_deve_entrar_cadastrar_e_mostrar_lista(self):
        # Fulano ficou sabendo de uma app para cadastrar atividades e decide verificar
        self.browser.get(self.live_server_url)
        # Fulano verifica que a um title descrito lista de tarefas
        self.assertIn('Lista Tarefas', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('Lista Tarefas', header_text)
        # Fulano decide colocar uma tarefa
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEquals(inputbox.get_attribute('placeholder'), 'Nova Tarefa')
        # Fulano tecla para colocar um item
        inputbox.send_keys('Lavar o carro')
        # Fulado presiona Enter
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)
        # Fulano ve seu item na lista.
        self.verificar_linha_da_tabela('Lavar o carro')
        # Fulano decide colocar
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('Limpar a casa')
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)
        self.verificar_linha_da_tabela('Lavar o carro')
        self.verificar_linha_da_tabela('Limpar a casa')
        # entao ele decide sair


    def test_multiplos_usuarios_cada_um_com_sua_lista(self):
        # Fulano ficou sabendo de uma app para cadastrar atividades e decide verificar
        self.browser.get(self.live_server_url)
        # Fulano verifica que a um title descrito lista de tarefas
        self.assertIn('Lista Tarefas', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('Lista Tarefas', header_text)
        # Fulano decide colocar uma tarefa
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEquals(inputbox.get_attribute('placeholder'), 'Nova Tarefa')
        # Fulano tecla para colocar um item
        inputbox.send_keys('Lavar o carro')
        # Fulado presiona Enter
        inputbox.send_keys(Keys.ENTER)
        # Fulano ve seu item na lista.
        time.sleep(1)
        self.verificar_linha_da_tabela('Lavar o carro')
        # Fulano recebe uma url
        fulano_list_url = self.browser.current_url
        self.assertRegex(fulano_list_url, '/lists/.+')

        ## Vamos reiniciar o navegador para garantir que não fique cookie
        self.browser.quit()
        self.browser = webdriver.Firefox()
        # Novo usario loga na aplicação
        self.browser.get(self.live_server_url)
        # Ciclano verifica que a um title descrito lista de tarefas
        self.assertIn('Lista Tarefas', self.browser.title)
        # Ciclano vai colocar novo Item na lista.
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('Andar de Patinete')
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)
        self.verificar_linha_da_tabela('Andar de Patinete')
        # Ciclano recebe uma url
        ciclano_list_url = self.browser.current_url
        self.assertRegex(ciclano_list_url, '/lists/.+')

        # Procurando vestigios da lista de Fulano
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertNotIn('Lavar o carro')

        # Verificando se as duas url são diferentes
        self.assertNotEqual(fulano_list_url,ciclano_list_url)
        # Fim Teste