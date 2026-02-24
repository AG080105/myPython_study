import pyautogui
import time
import random
import sys

def anti_sleep(interval=60, subtle=True):
    print("Anti-sleep mode activated. Press Ctrl+C to stop.")
    try:
        while True:
            width, height = pyautogui.size()
            if subtle:
                # Ito yung naggagalwa ng mouse sa kasalukuyang posisyon ng mouse, pero may random na paggalaw
                # Pwede mong baguhin yung range ng paggalaw depende sa gusto mo, pero wag masyadong malaki para hindi halata
                # ahwhawhahashash
                x, y = pyautogui.position()
                x += random.randint(-10, 10)
                y += random.randint(-10, 10)
            else:
                # Ito yung random na paggalaw ng mouse sa screen, pero mas halata siya kaysa sa subtle mode
                # Pwede mo itong tanggalin kung gusto mo yung subtle mode lang, pero kung test, ito gamitin mo
                x = random.randint(0, width)
                y = random.randint(0, height)
                
            pyautogui.moveTo(x, y, duration=0.5)#Depende sa gadget mo ah, pero yung 'Shift' key is hindi gumagana sakin, 
            pyautogui.press('Alt') #'Alt' ang gamit ko, same sa Alphabet keys
            time.sleep(interval)  # Ito ay maghihintay ng specified interval bago ulitin ang proseso
    except KeyboardInterrupt:
        print("Anti-sleep mode deactivated.")
        sys.exit()

anti_sleep(interval=60, subtle=True) # Wag mo kakalimutan toh kung mag code ka ng iyo ah, hindi gumagana pag wala toh eh