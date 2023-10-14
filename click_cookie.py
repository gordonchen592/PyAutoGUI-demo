import pyautogui

# edit vars here
num_clicks = 1
img_file = "img/Cookie-ss-Cropped.png"
pyautogui.PAUSE = 0.05

# code starts here
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

    print("Cookie Center: ",cookie_center.x,", ",cookie_center.y, sep="")
    for i in range(num_clicks):
        pyautogui.moveTo(cookie_center)