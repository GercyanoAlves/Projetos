#Codigo feito pelo Jupyter Notebook

import pyautogui as pa
import pyperclip
import time

#pyautogui.click -> Clicar
#pyautogui.write -> escrever
#pyautogui.press -> pressionar
#pyautogui.hotkey -> atalho

#Abre o email
pa.PAUSE = 1

pa.hotkey("ctrl","t")
pyperclip.copy("outlook.com") # Tambem pelo Gmail, mas a configuração está para outlook
pa.hotkey("ctrl","v")
pa.press("enter")

time.sleep(5)

pa.click(x=142, y=205) # muda de acordo com monitor
time.sleep(2)

#Mandar email

pyperclip.copy("email@email.com") # Email do destinatario
pa.hotkey("ctrl","v")
pa.press("tab") #confimar email
assunto = "Teste de Automatização"
pyperclip.copy(assunto)
pa.hotkey("ctrl", "v")

pa.press("tab") #corpo email
texto = """Teste de email para
automatização feito por Gercyano"""
pyperclip.copy(texto)
pa.hotkey("ctrl","v")
time.sleep(1)
pa.hotkey("ctrl","enter")