import pyautogui as gui
import time

def get_pos():
    time.sleep(3)
    return gui.position()

def clear_cart(items):
    for i in range(items):
        gui.click(1106,400)
        time.sleep(.35)
        try:
            x1 , y1 = gui.locateCenterOnScreen("remove.png")
            gui.click(x1,y1)
            time.sleep(.25)
        except:
            pass

#print(get_pos())
clear_cart(36)