import cv2
import pyautogui
import numpy as np
import time

# Carregue a imagem que você está procurando
imagem_x = cv2.imread('C:\\Users\\caual\\PycharmProjects\\BotDiscord\\espada.png', 0)
imagem_y = cv2.imread('C:\\Users\\caual\\PycharmProjects\\BotDiscord\\pular.png', 0)
imagem_w = cv2.imread('C:\\Users\\caual\\PycharmProjects\\BotDiscord\\won.png', 0)

while True:
    time.sleep(1.5)
    # Tire uma captura de tela
    screenshot = pyautogui.screenshot()
    screenshot = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)
    screenshot_gray = cv2.cvtColor(screenshot, cv2.COLOR_BGR2GRAY)

    # Use o método matchTemplate para encontrar a imagem_w na tela
    resultado_w = cv2.matchTemplate(screenshot_gray, imagem_w, cv2.TM_CCOEFF_NORMED)
    _, max_val_w, _, max_loc_w = cv2.minMaxLoc(resultado_w)

    # Se a imagem_w for encontrada na tela, escreva '/dungeon floor:20' e pressione 'Enter'
    if max_val_w > 0.8:
        time.sleep(4)
        pyautogui.moveTo(max_loc_w)
        pyautogui.click()
        pyautogui.write('/')
        pyautogui.write('dungeon floor:20')
        pyautogui.press('enter')
        continue  # Pule o resto do loop se a imagem_w foi encontrada e clicada

    # Use o método matchTemplate para encontrar a imagem_y na tela
    resultado_y = cv2.matchTemplate(screenshot_gray, imagem_y, cv2.TM_CCOEFF_NORMED)
    _, max_val_y, _, max_loc_y = cv2.minMaxLoc(resultado_y)

    # Se a imagem_y for encontrada na tela, clique nela
    if max_val_y > 0.8:
        time.sleep(1)
        pyautogui.moveTo(max_loc_y)
        pyautogui.click()
        continue  # Pule o resto do loop se a imagem_y foi encontrada e clicada

    # Use o método matchTemplate para encontrar a imagem_x na tela
    resultado_x = cv2.matchTemplate(screenshot_gray, imagem_x, cv2.TM_CCOEFF_NORMED)
    _, max_val_x, _, max_loc_x = cv2.minMaxLoc(resultado_x)

    # Se a imagem_x for encontrada na tela, clique nela
    if max_val_x > 0.8:
        time.sleep(4)
        pyautogui.moveTo(max_loc_x)
        pyautogui.click()
