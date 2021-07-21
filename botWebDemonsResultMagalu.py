# da biblioteca do selenium importa o webdriver //pip install selenium
from selenium import webdriver
import time
import pyautogui
#*********quando tem SELENIUM*********
# importar biblioteca webdriver_manager import ChromeDriverManager (para funcionar no vscode) // pip install webdriver-manager
#o chomedriver.exe tem que está no mesmo caminho onde está o (arquivo.py)
from webdriver_manager.chrome import ChromeDriverManager

#mensagem de alerta
pyautogui.alert('O código vai iniciar. Não use o computador nesse intervalo de tempo OK?')

#abre navegador chrome
navegador = webdriver.Chrome(ChromeDriverManager().install())
pyautogui.PAUSE = 2
pyautogui.click (x=872, y=24)

#navegar até uma pagina especifica
navegador.get('https://ri.magazineluiza.com.br')

#caminho do elemento (campo) que quer clicar no site
navegador.find_element_by_xpath('//*[@id="owl-destaques"]/div[1]/div/div[4]/div/a/img').click()

#caminho do elemento (campo) para download
navegador.find_element_by_xpath('//*[@id="qh+HU4D7Db023fFZvApelg=="]').click()
time.sleep (3)

pyautogui.alert('Finalizado')