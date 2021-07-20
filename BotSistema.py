import pyautogui
import time 

pyautogui.PAUSE = 2

pyautogui.press('Win')
pyautogui.write('login.xlsx')
pyautogui.press('backspace')
pyautogui.press('enter')
pyautogui.click (x=488, y=289)
pyautogui.write('Teste')
pyautogui.click (x=490, y=326)
pyautogui.write('123')
pyautogui.click(x=469, y=414)
pyautogui.click(x=544, y=617)