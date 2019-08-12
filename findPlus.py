import pyautogui as gui
import logging
import time
import openpyxl

# logging  
LOG = r"C:\Users\Tyler\Downloads\error.log"                                                     
logging.basicConfig(filename=LOG, filemode="w", level=logging.DEBUG)  

# console handler  
console = logging.StreamHandler()  
console.setLevel(logging.ERROR)  
logging.getLogger("").addHandler(console)
try:
    x1, y1 = gui.locateCenterOnScreen("plus.png", grayscale=False, region=(0,0, 2000,1000))
    gui.click(x=x1, y=y1, button='left')
except:
    logging.error("Couldn't add the following to cart: " + item[0])

print(x1,y1)