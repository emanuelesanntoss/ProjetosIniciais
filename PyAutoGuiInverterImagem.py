import pyautogui
import time

#retorna mensagem de inicialização do processo
pyautogui.alert('A partir desse momento o programa será executado!')

#clicar em qualquer lugar na tela do desktop e digita o nome da pasta para localizar a pasta
pyautogui.click(874,228);pyautogui.typewrite('imagem')
#seguido de Enter para abri-la
pyautogui.press('enter');time.sleep(2)
pyautogui.click(321,154);time.sleep(1)
#para ir para o arquivo de imagem seguinte
for i in range(3):
#botão direito do mouse para selecionar o arquivo de imagem
    pyautogui.press('right');time.sleep(2)
#abrindo o arquivo de imagem pressionando Enter
    pyautogui.press('enter');time.sleep(4)
#em seguida pela tecla de atalho ‘Ctrl’ + ‘r’ para girar a imagem
    pyautogui.hotkey('ctrl','r');time.sleep(3)
# fechar o arquivo e repetir o processo
    pyautogui.hotkey('alt','f4');time.sleep(1)
    #pyautogui.click(x=1895, y=20)
   

