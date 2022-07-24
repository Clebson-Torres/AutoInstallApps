import pyautogui
import time

time.sleep(5)
pyautogui.hotkey ('win', 'd')
pyautogui.press('win')
time.sleep(2)
pyautogui.write('brave')
time.sleep(2)
pyautogui.press('enter')
time.sleep(1)
pyautogui.write("https://www.google.com/intl/pt-BR/chrome/")
time.sleep(2)
pyautogui.press('enter')
#maximizar janela
pyautogui.moveTo(1422, 131)
time.sleep(1)
pyautogui.click()
#clicar download
pyautogui.moveTo(944, 644)
time.sleep(2)
pyautogui.click()
#salvar como
pyautogui.moveTo(748, 559)
time.sleep(3)
pyautogui.click()
time.sleep(5)
#executando instalador
pyautogui.moveTo(160, 979)
pyautogui.click()
time.sleep(5)






#time.sleep(2)
#pyautogui.click()
#time.sleep(2)




