from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, win32con

# pos 718, 546
# cor 83
def click():
    #win32api.SetCursorPos((x,y))
    keyboard.press_and_release('Space')
    sleep(0.15)

def click2():
    #win32api.SetCursorPos((x,y))
    keyboard.press_and_release('Space')
    sleep(0.01)

#pyautogui.displayMousePosition()q
while keyboard.is_pressed('q') == False:
    if(pyautogui.pixel(765, 555)) [0] == 83:
       print("aperta")
       click()