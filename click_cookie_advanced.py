import pyautogui
import os
import psutil
import multiprocessing
import keyboard

# change the confidence ratio if a match still isn't found
confidence_ = 0.5
# maximum clicks (less than 0 is infinite)
num_clicks = -1
# image file to match to
cookie_img_file = "img/Cookie-ss-2160p-Cropped.png"
# time between pyautogui commands (ie. time between clicks)
pyautogui.PAUSE = 0.02

# keybinds
exit_key = "esc"
toggle_key = "alt"

# manual override for search region
bounds = ()

def click_cookies():
    global bounds, confidence_
    cookie_loc = None
    if not bounds:
        bounds = None
    try:
        cookie_loc = pyautogui.locateOnScreen(cookie_img_file, confidence=confidence_,region=bounds)
    except pyautogui.ImageNotFoundException:
        print("Error: No Cookie Found Onscreen!")
    except IOError:
        print("Image File Not Found!")

    # pyautogui sometimes returns None instead of throwing the exception
    if not cookie_loc:
        print("No Cookie Found Onscreen!")
    else:
        cookie_center = pyautogui.center(cookie_loc)

        print(f"Cookie Found! Clicking {num_clicks if num_clicks >= 0 else 'unlimited'} time{'s' if not num_clicks==1 else ''}")
        if num_clicks > 0:
            for i in range(num_clicks):
                pyautogui.click(cookie_center)
        else:
            while True:
                pyautogui.click(cookie_center)
    print("Clicking Finished")


def on_press_exit(main_pid):
    main_process = psutil.Process(main_pid)
    for proc in main_process.children(recursive=True):
        proc.terminate()
    main_process.terminate()

def on_press_toggle():
    global click_process
    if (not click_process.is_alive()):
        print("Starting Auto Clicker")
        click_process = multiprocessing.Process(target=click_cookies)
        click_process.start()
    else:
        print("Stopping Auto Clicker")
        click_process.terminate()

if __name__ == "__main__":
    click_process = multiprocessing.Process(target=click_cookies)
    main_pid = os.getpid()
    keyboard.add_hotkey(exit_key, on_press_exit, args=[main_pid])
    keyboard.add_hotkey(toggle_key, on_press_toggle)
    keyboard.wait(exit_key)