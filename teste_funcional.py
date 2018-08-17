import unittest

import time
from selenium import webdriver
# TESTE NO CHROME navegador_chrome = webdriver.Chrome()
# #navegador_chrome.get('http://localhost:8000')#assert 'Django' in navegador_chrome.title
from selenium.webdriver.common.keys import Keys


class NovaVisitaTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def verificar_linha_da_tabela(self, linha):
        # Entao ele verifica sua tarefas
        # Pega a tabela pelo seu elemento id
        table = self.browser.find_element_by_id('id_list_table')
        # Pega as linhas da tabela pelo elemento de tag <tr>
        rows = table.find_elements_by_tag_name('tr')
        # [resultado para linha em linhas]-> Isso e uma lista conphanions for para usar o for em um linha
        self.assertIn(linha == [row.text for row in rows])

    def test_deve_entrar_cadastrar_e_mostrar_lista(self):
        # Fulano ficou sabendo de uma app para cadastrar atividades e decide verificar
        self.browser.get('http://localhost:8000')
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
        self.verificar_linha_da_tabela('Limpar a casa')
        # entao ele decide sair


if __name__ == '__main__':
    unittest.main(warnings='ignore')
