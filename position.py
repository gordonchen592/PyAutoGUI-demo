import pyautogui

prev_pos = 0
while True:
    if pyautogui.position() != prev_pos:
        prev_pos = pyautogui.position()
        print(prev_pos)
        