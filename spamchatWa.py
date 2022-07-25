#rann

import pyautogui, time

position =pyautogui.position()
pesan = "Yok Temu Pengen Peyukkkk"
for a in range(25):
    pyautogui.click(position.x,position.y)
    pyautogui.typewrite(pesan)
    print(pesan)
    time.sleep(0.5)
    pyautogui.typewrite(["enter"])