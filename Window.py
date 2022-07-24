import PySimpleGUI as sg
import pyautogui
import time


layout = [
    [sg.Text("selecione qual aplicativo deseja instalar")],
    [sg.Button("Firefox")],
    [sg.Button("Chrome")],
    [sg.Button("7zip")],
]

janela = sg.Window("Auto installer", layout)

while True:
    event, valores = janela.read()
    if event ==sg.WIN_CLOSED:
        break
    if event == "Firefox":
        time.sleep(5)
        pyautogui.hotkey('win', 'd')
        time.sleep(2)
        pyautogui.press('win')
        time.sleep(2)
        pyautogui.write('brave')
        time.sleep(2)
        pyautogui.press('enter')
        time.sleep(1)
        pyautogui.write("https://www.mozilla.org/pt-BR/firefox/new/")
        time.sleep(2)
        pyautogui.press('enter')
        time.sleep(2)
        pyautogui.moveTo(1426, 130)
        time.sleep(1)
        pyautogui.click()
        pyautogui.moveTo(300, 760)
        time.sleep(2)
        pyautogui.click()
        pyautogui.moveTo(766, 561)
        time.sleep(3)
        pyautogui.click()
        time.sleep(5)
        pyautogui.moveTo(160, 979)
        pyautogui.click()
        time.sleep(5)
        pyautogui.moveTo(801, 694)
        pyautogui.click()

    if event == "Chrome":
        time.sleep(5)
        pyautogui.hotkey('win', 'd')
        pyautogui.press('win')
        time.sleep(2)
        pyautogui.write('brave')
        time.sleep(2)
        pyautogui.press('enter')
        time.sleep(1)
        pyautogui.write("https://www.google.com/intl/pt-BR/chrome/")
        time.sleep(2)
        pyautogui.press('enter')
        # maximizar janela
        pyautogui.moveTo(1422, 131)
        time.sleep(1)
        pyautogui.click()
        # clicar download
        pyautogui.moveTo(944, 644)
        time.sleep(2)
        pyautogui.click()
        # salvar como
        pyautogui.moveTo(748, 559)
        time.sleep(3)
        pyautogui.click()
        time.sleep(5)
        # executando instalador
        pyautogui.moveTo(160, 979)
        pyautogui.click()
        time.sleep(5)

janela.close()