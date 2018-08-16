import unittest

import time
from selenium import webdriver
#TESTE NO CHROME navegador_chrome = webdriver.Chrome()#navegador_chrome.get('http://localhost:8000')#assert 'Django' in navegador_chrome.title
from selenium.webdriver.common.keys import Keys


class NovaVisitaTest(unittest.TestCase):

    def setUp(self):
        self.browser= webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

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

        # Entao ele verifica sua tarefas
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')

        self.assertTrue(any(row.text == 'Lavar o carro' for row in rows))


        # entao ele decide sair


if __name__ == '__main__':
    unittest.main(warnings='ignore')