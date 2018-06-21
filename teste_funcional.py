from selenium import webdriver

#navegador_chrome = webdriver.Chrome()
#navegador_chrome.get('http://localhost:8000')

#assert 'Django' in navegador_chrome.title

navegador_firefox = webdriver.Firefox()
navegador_firefox.get('http://localhost:8000')

assert 'Django' in navegador_firefox.title