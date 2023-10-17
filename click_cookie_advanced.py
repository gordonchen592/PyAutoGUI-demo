import pyautogui
import os
import psutil
import multiprocessing
import keyboard
import mouse

# edit vars here
num_clicks = -1
cookie_img_file = "img/Cookie-ss-Cropped.png"
pyautogui.PAUSE = 0.02
exit_key = "esc"
bounds = ()

# code starts here
def calibrate():
    while True:
        bounds = []
        print("click top left corner")
        mouse_toggle = False
        while True:
            if (not mouse_toggle) and mouse.is_pressed(button='left'):
                position = pyautogui.position()
                print(position)
                bounds.append(position.x)
                bounds.append(position.y)
                mouse_toggle = True
            if mouse_toggle and not mouse.is_pressed(button='left'):
                mouse_toggle = False
                break
        print("click bottom right corner")
        toggle_ = 0
        while True:
            if (not mouse_toggle) and mouse.is_pressed(button='left'):
                position = pyautogui.position()
                print(position)
                width = position.x - bounds[0]
                height = position.y - bounds[1]
                bounds.append(width)
                bounds.append(height)
                mouse_toggle = True
            if mouse_toggle and not mouse.is_pressed(button='left'):
                mouse_toggle = False
                break
        print(bounds)
        print(f"The result is a box from ({bounds[0]},{bounds[1]}) to ({bounds[0]+bounds[2]},{bounds[1]+bounds[3]})")
        print(f"The region is (top,left,width,height): {bounds}")
        input_ = input("Is this correct? (y/n): ")
        if input_ == "y":
            return tuple(bounds)

def click_cookies(l,t,w,h):
    cookie_loc = None
    bounds = (l,t,w,h)
    print(bounds)
    try:
        cookie_loc = pyautogui.locateOnScreen(cookie_img_file, confidence=0.5,region=bounds)
    except pyautogui.ImageNotFoundException:
        print("Error: No Cookie Found Onscreen!")
    except IOError:
        print("Image File Not Found!")

    if not cookie_loc:
        print("No Cookie Found Onscreen!")
    else:
        cookie_center = pyautogui.center(cookie_loc)

        print("Cookie Center: ",cookie_center.x,", ",cookie_center.y, sep="")
        if num_clicks > 0:
            for i in range(num_clicks):
                pyautogui.click(cookie_center)
        else:
            while True:
                pyautogui.click(cookie_center)


def on_press(main_pid):
    process = psutil.Process(main_pid)
    for proc in process.children(recursive=True):
        proc.terminate()
    process.terminate()


if __name__ == "__main__":
    main_pid = os.getpid()
    keyboard.add_hotkey(exit_key, on_press, args=[main_pid])
    # determine bounds of region if not specified
    if not bounds:
        bounds = calibrate()
    
    # start thread with clicking loop
    multiprocessing.Process(target=click_cookies, args=(bounds)).start()