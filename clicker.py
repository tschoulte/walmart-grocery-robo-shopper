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

wb = openpyxl.load_workbook(r'/Users/tyler/Downloads/Steward Logistics.xlsx')
ws = wb['Sheet2']

db = []
not_added = []

for rownum in range(1,ws.max_row):
    try:
        hyperlink = ws.cell(row=rownum, column=1).hyperlink.target
        quantity = ws.cell(row=rownum, column=2).value

        #print(hyperlink)
        #print(quantity)
        if quantity != None:
            db.append([hyperlink, quantity])
        else:
            not_added.append([hyperlink, quantity])
    except:
        logging.error("Did not add " + str(rownum))

for item in db:
    #load the url
    gui.tripleClick(x=300, y=100)
    gui.typewrite(item[0])
    gui.hotkey('enter')
    time.sleep(3)

    #find add to cart, click, update quantity
    try:
        x1, y1 = gui.locateCenterOnScreen("add.png", grayscale=False, confidence=.7, region=(0,0, 2000,1000))
        gui.tripleClick(x=x1, y=y1, button='left')
        gui.typewrite(str(int(item[1])))
        gui.hotkey('enter')
    except:
        logging.error("Couldn't add the following to cart: " + item[0])

        print()
