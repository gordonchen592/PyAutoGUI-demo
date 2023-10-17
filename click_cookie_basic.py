import pyautogui

img_file = "img/Cookie-ss-Cropped.png"

cookie_loc = None
try:
    cookie_loc = pyautogui.locateOnScreen(img_file, confidence=0.5)
except pyautogui.ImageNotFoundException:
    print("Error: No Cookie Found Onscreen!")
except IOError:
    print("Image File Not Found!")

if not cookie_loc:
    print("No Cookie Found Onscreen!")
else:
    cookie_center = pyautogui.center(cookie_loc)
    pyautogui.click(cookie_center.x,cookie_center.y)