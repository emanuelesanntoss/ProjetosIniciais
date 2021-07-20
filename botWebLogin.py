#chrome --> chromedriver
#firefox --> geckodriver

from selenium import webdriver
import time

navegador = webdriver.Chrome()

navegador.get('https://login.microsoftonline.com/')
time.sleep(3)
navegador.find_element_by_xpath('//*[@id="i0116"]').send_keys("teste@teste.com.br")
navegador.find_element_by_xpath('//*[@id="idSIButton9"]').click()
time.sleep(3)
navegador.find_element_by_xpath('//*[@id="i0118"]').send_keys("xxxxxxx")
navegador.find_element_by_xpath('//*[@id="idSIButton9"]').click()
navegador.find_element_by_xpath('//*[@id="idSIButton9"]').click()