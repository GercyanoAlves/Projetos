from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pyautogui as pa
import pyperclip
import time

# passo 1: abrir navegador
navegador = webdriver.Chrome()
navegador.get("https://pt-br.facebook.com/")


# passo 2: entrar no facebook
navegador.find_element('xpath', '//*[@id="email"]').send_keys('email@email.com')
navegador.find_element('xpath', '//*[@id="pass"]').send_keys('Sua Senha')
navegador.find_element('xpath', '//*[@id="pass"]').send_keys(Keys.ENTER)
time.sleep(8)
pa.click(x=270, y=164)
time.sleep(5)

# passo 3: entrar no wolverdon filmes
navegador = webdriver.Chrome()
navegador.get('https://wolverdonfilme.net/')
navegador.find_element('xpath', '//*[@id="search-input"]').send_keys('suits temporada 4')
navegador.find_element('xpath', '//*[@id="search-input"]').send_keys(Keys.ENTER)
navegador.find_element('xpath', '//*[@id="posts-container"]/li[5]/h2/a').click()

navegador = webdriver.Chrome()
navegador.get('https://login.live.com/login.srf?wa=wsignin1.0&rpsnv=13&ct=1673536478&rver=7.0.6737.0&wp=MBI_SSL&wreply=https%3a%2f%2foutlook.live.com%2fowa%2f%3fnlp%3d1%26RpsCsrfState%3d9f94485e-6684-d716-2d85-9d84452b76fa&id=292841&aadredir=1&CBCXT=out&lw=1&fl=dob%2cflname%2cwld&cobrandid=90015')
navegador.find_element('xpath','//*[@id="i0116"]').send_keys('Seu email') 
navegador.find_element('xpath','//*[@id="i0116"]').send_keys(Keys.ENTER)
navegador.find_element('xpath', '//*[@id="i0118"]').send_keys('Sua Senha')
time.sleep(1)
navegador.find_element('xpath', '//*[@id="idSIButton9"]').click()
time.sleep(1)
navegador.find_element('xpath', '//*[@id="idSIButton9"]').click()

# Enviar email
time.sleep(10)
navegador.find_element('xpath','//*[@id="innerRibbonContainer"]/div[1]/div/div/div/div[2]/div/div/span/button[1]').click()
time.sleep(2)
# navegador.find_element('xpath', '//*[@id="Ribbon-588Dropdown"]/div/ul/li/div/ul/li[1]/button').click()
navegador.find_element('xpath','//*[@id="docking_InitVisiblePart_0"]/div/div[1]/div[1]/div/div[3]/div/div/div[1]').send_keys('gercyanoalves@gmail.com')
pa.press('tab')

time.sleep(2)
pa.click(x=287, y=353)
assunto = 'Test de de automatização Web'
pyperclip.copy(assunto)
pa.hotkey('ctrl','v')
time.sleep(1)
pa.press('tab')

texto_corpo = """Teste de automatização
Abrir e Entrar no facebook: OK!
Entrar em site de download: OK!
Entrar no Email: OK!
Enviar email: OK!
Fim do teste de automatização por Gercyano Alves""" 

navegador.find_element('xpath', '//*[@id="editorParent_1"]/div/div').send_keys(texto_corpo)
time.sleep(1)
navegador.find_element('xpath', '//*[@id="docking_InitVisiblePart_0"]/div/div[3]/div[5]/div[1]/div/div/span/button[1]').click()
time.sleep(1)
navegador.find_element('xpath', '//*[@id="MainModule"]/div/div/div[1]/div/div/div[1]/div/div[2]/div[4]/div/span[1]').click()
time.sleep(2)
pa.click(x=374, y=415)