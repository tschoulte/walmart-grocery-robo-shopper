import pyautogui as gui
import time

current_milli_time = lambda: int(round(time.time() * 1000))

def load_url(itemURL, failed):
    if failed == True:
        return True
    #load the url

    gui.tripleClick(x=300, y=100)
    gui.typewrite(itemURL)
    gui.hotkey('enter')
    startTime = current_milli_time()
    timeDelta = 0
    imageFound = None
    while (imageFound == None and timeDelta  < 3000 ):
        imageFound = gui.locateOnScreen("heart.png", grayscale=False, confidence=.5, region=(0,0, 1000,1000))
        timeDelta = (current_milli_time() - startTime)
        print(imageFound, timeDelta)
    #time.sleep(3)


db = [["https://grocery.walmart.com/ip/Great-Value-Deli-Style-Sliced-Pepper-Jack-Cheese-8-oz-12-count/155066735" , 13],["https://grocery.walmart.com/ip/Sam-s-Choice-Sliced-Monterey-Jack-Cheese-with-Jalapenos-Habaneros-and-Ghost-Peppers-8-Oz/146364618", 4],["https://grocery.walmart.com/ip/Great-Value-Cracker-Cuts-Pepper-Jack-Cheese-Slices-10-Oz/681794103" , 3],["https://grocery.walmart.com/ip/Wonder-Classic-White-Bread-20-oz-Loaf/37858875", 5]]
load_url(db[1][0], False)