import cv2
import pyautogui
import numpy as np
import time

# Carregue a imagem que você está procurando
imagem_x = cv2.imread('C:\\Users\\caual\\PycharmProjects\\BotDiscord\\espada.png', 0)
imagem_y = cv2.imread('C:\\Users\\caual\\PycharmProjects\\BotDiscord\\pular.png', 0)
imagem_w = cv2.imread('C:\\Users\\caual\\PycharmProjects\\BotDiscord\\won.png', 0)
imagem_z = cv2.imread('C:\\Users\\caual\\PycharmProjects\\BotDiscord\\inicio.png', 0)
imagem_v = cv2.imread('C:\\Users\\caual\\PycharmProjects\\BotDiscord\\exit.png', 0)

# Variáveis para controlar se a imagem_v e imagem_z foram encontradas
imagem_v_encontrada = False
imagem_z_encontrada = True

while True:
    time.sleep(1.5)
    # Tire uma captura de tela
    screenshot = pyautogui.screenshot()
    screenshot = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)
    screenshot_gray = cv2.cvtColor(screenshot, cv2.COLOR_BGR2GRAY)

    # Se a imagem_v foi encontrada anteriormente e imagem_z não foi encontrada, não procure as outras imagens
    if imagem_v_encontrada and not imagem_z_encontrada:
        continue

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

    # Use o método matchTemplate para encontrar a imagem_v na tela
    resultado_v = cv2.matchTemplate(screenshot_gray, imagem_v, cv2.TM_CCOEFF_NORMED)
    _, max_val_v, _, max_loc_v = cv2.minMaxLoc(resultado_v)

    # Use o método matchTemplate para encontrar a imagem_z na tela a
    resultado_z = cv2.matchTemplate(screenshot_gray, imagem_z, cv2.TM_CCOEFF_NORMED)
    _, max_val_z, _, max_loc_z = cv2.minMaxLoc(resultado_z)

    # Se a imagem_z não for encontrada na tela, pule o resto do loop
    if max_val_z < 0.8:
        imagem_z_encontrada = False
    else:
        imagem_z_encontrada = True

    # Se a imagem_v for encontrada na tela, defina a variável imagem_v_encontrada como True
    if max_val_v > 0.8:
        imagem_v_encontrada = True
