import pyautogui
import time 

#retorna mensagem de inicialização do processo
pyautogui.alert('A partir desse momento será executada a limpeza dos arquivos temporários da máquina! Você está ciente disto?')
pyautogui.PAUSE = 1

#teclas de atalho pyautogui
#pyautogui.KEYBOARD_KEYS

#abrir opções do windows
pyautogui.press('Win')
#abrir através de atalho o caminho onde ficam os arquivos temporários da máquina
pyautogui.write('%temp%')
pyautogui.press('enter')
#aguardar um momento para abrir o explorer
time.sleep(1)
#selecionar todos os arquivos
pyautogui.hotkey('ctrlleft', 'a')
#deletar os arquivos selecionados
pyautogui.press('delete')
#aguardar um momento (caso tenha muitos arquivos)
time.sleep(8)
#selecionar opçao repetir ação para todos os arquivos
pyautogui.click(x=770, y=448)
#ignorar\cancelar os arquivos que não foram deletados
pyautogui.click(x=1102, y=479)
#Fechar o explorer do windows
pyautogui.click(x=1895, y=9)
#retorna mensagem de conclusão do processo
pyautogui.alert('Limpeza dos arquivos temporários concluído com sucesso!')