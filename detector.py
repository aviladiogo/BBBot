from pyautogui import *
import pyautogui
from tkinter import *
from tkinter.ttk import*
import time
import keyboard
from pynput.mouse import Button, Controller

import random
import win32api, win32con

mouse = Controller()
root = Tk()
height = root.winfo_screenheight() 
width = root.winfo_screenwidth() 
#iml = pyautogui.screenshot(region=(0,0,width,heiqqqqght))
#iml.save(r"C:/Users/Diogo/Desktop/Python/jokes/Alvo.png")
#pyautogui.displayMousePosition()
# cores connect (255,170,35)
#sleep(2)
def click(coords):
    mouse.position = (coords) # envia o cursor para o botao de enviar do twitter
    sleep(1)
    mouse.click(Button.left, 1)

def Movimento(x, y):
    mouse.position = (x, y+200)

def Char():
    while 1:
        sleep(1)
        if pyautogui.locateOnScreen('Character.png', region = (0,0 ,width,height), grayscale=True, confidence=0.8) != None:
            print("consigo ver")
            coords = pyautogui.locateCenterOnScreen('Character.png', region = (0,0 ,width,height), grayscale=True, confidence=0.8)
            x, y = coords
            Movimento(x, y)
            sleep(2)
        else:
            print("nao consigo ver")
            sleep(0.5)

def Hero():
    while 1:
        if pyautogui.locateOnScreen('Heroes.png', region = (0,0 ,width,height), grayscale=True, confidence=0.8) != None:
            print("consigo ver")
            coords = pyautogui.locateCenterOnScreen('Heroes.png', region = (0,0 ,width,height), grayscale=True, confidence=0.8)
            click(coords)
            sleep(2)
            Char()
        else:
            print("nao consigo ver")
            sleep(0.5)

def Assinar():
    while 1:
        if pyautogui.locateOnScreen('Assinar.png', region = (0,0 ,width,height), grayscale=True, confidence=0.8) != None:
            print("consigo ver")
            coords = pyautogui.locateCenterOnScreen('Assinar.png', region = (0,0 ,width,height), grayscale=True, confidence=0.8)
            click(coords)
            sleep(2)
            Hero()
        else:
            print("nao consigo ver")
            sleep(0.5)

Char()
while keyboard.is_pressed('q') == False:
    if pyautogui.locateOnScreen('Connect.png', region = (0,0 ,width,height), grayscale=True, confidence=0.8) != None:
        print("consigo ver")
        coords = pyautogui.locateCenterOnScreen('Connect.png', region = (0,0 ,width,height), grayscale=True, confidence=0.8)
        click(coords)
        sleep(2)
        Assinar()
    else:
        print("nao consigo ver")
        sleep(0.5)