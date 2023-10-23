import keyboard
import pyautogui

# code starts here
def calibrate():
    while True:
        bounds = []
        pyautogui.alert(text="Move the mouse to the top left corner of the region and press ESC.",title="PyAutoGUI Demo",button="OK")
        mouse_toggle = False
        while True:
            if (not mouse_toggle) and keyboard.is_pressed("esc"):
                position = pyautogui.position()
                print(position)
                bounds.append(position.x)
                bounds.append(position.y)
                mouse_toggle = True
            if mouse_toggle and not keyboard.is_pressed("esc"):
                mouse_toggle = False
                break
        pyautogui.alert(text="Move the mouse to the bottom right corner of the region and press ESC.",title="PyAutoGUI Demo",button="OK")
        while True:
            if (not mouse_toggle) and keyboard.is_pressed("esc"):
                position = pyautogui.position()
                print(position)
                width = position.x - bounds[0]
                height = position.y - bounds[1]
                bounds.append(width)
                bounds.append(height)
                mouse_toggle = True
            if mouse_toggle and not keyboard.is_pressed("esc"):
                mouse_toggle = False
                break
        print(f"The region is (top,left,width,height): {tuple(bounds)}")
        confirm_text = f"The result is a box from ({bounds[0]},{bounds[1]}) to ({bounds[0]+bounds[2]},{bounds[1]+bounds[3]}).\nThe region is (top,left,width,height): {tuple(bounds)}\n\nRun again?: "
        input_ = pyautogui.confirm(text=confirm_text, title='PyAutoGUI Demo', buttons=['OK', 'Exit'])
        if input_ == "Exit":
            return tuple(bounds)

if __name__ == '__main__':
    calibrate()