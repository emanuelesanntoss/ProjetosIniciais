#https://pyautogui.readthedocs.io/en/latest/quickstart.html --> teclas de atalho


#importar bibliotecas
import pyautogui
import time
#mensagem de alerta
pyautogui.alert('O backup vai iniciar agora! Não use o computador nesse intervalo de tempo OK? (Tempo aproximado de duração = 1 minuto)')
#esperar antes de executar a próxima linha de código
pyautogui.PAUSE = 1
#ver lista de atalho
    #pyautogui.KEYBOARD_KEYS
#abrir o google no computador
pyautogui.press('winleft')
time.sleep(1)
#abrir o chrome
pyautogui.write('chrome')
pyautogui.press('enter')
time.sleep(1)
pyautogui.click(x=1858, y=25)
#abrir o google drive
pyautogui.write('https://drive.google.com/drive/my-drive')
pyautogui.press('enter')
#exibir area de trabalho do computador
pyautogui.hotkey('winleft', 'd')
#descobrir posição do arquivo que quero arrastar
pyautogui.moveTo(x=108, y=243)
#precionar o botao no mouse e arrastar
pyautogui.mouseDown()
#soltar o arquivo no google drive
pyautogui.moveTo(x=1180, y=713)
#enquanto esta arrastando tem que voltar para o google drive
pyautogui.hotkey('alt', 'tab')
#aguardar para upload
time.sleep(3)
#largar o mouse
pyautogui.mouseUp()
#aguardar para upload
time.sleep(4)
#mensagem que o código terminou de rodar
pyautogui.alert('O backup foi finalizado! O computador está liberado para uso.')
