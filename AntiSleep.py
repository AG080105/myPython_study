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
                # Move the mouse slightly to prevent sleep
                x, y = pyautogui.position()
                x += random.randint(-10, 10)
                y += random.randint(-10, 10)
            else:
                # Move the mouse to a random position on the screen
                x = random.randint(0, width)
                y = random.randint(0, height)
                
            pyautogui.moveTo(x, y, duration=0.5)
            pyautogui.press('Alt')
            time.sleep(interval)  # Wait for the specified interval before moving again
    except KeyboardInterrupt:
        print("Anti-sleep mode deactivated.")
        sys.exit()

anti_sleep(interval=60, subtle=True)