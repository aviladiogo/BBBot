from pyautogui import *
import pyautogui
from tkinter import *
from tkinter.ttk import*
import keyboard
from pynput.mouse import Button, Controller


mouse = Controller()
root = Tk()
height = root.winfo_screenheight() 
width = root.winfo_screenwidth() 

def click(coords):
    mouse.position = (coords)
    sleep(1)
    mouse.click(Button.left, 1)

def Movimento(x, y):
    mouse.position = (x, y+200)
    sleep(1)
    x = 0
    while x < 200:
        mouse.scroll(0, -1)
        sleep(0.1)
        x+=2

def Menu():
    stop = True
    while stop:
        if pyautogui.locateOnScreen('Menu.png', region = (0,0 ,width,height), grayscale=True, confidence=0.8) != None: #procura a imagem na tela
            print("consigo ver")
            coords = pyautogui.locateCenterOnScreen('Menu.png', region = (0,0 ,width,height), grayscale=True, confidence=0.8) #pega o centro da imagem
            click(coords)
            sleep(2)
            print("Programa rodou com sucesso")
            stop = False
        else:
            print("nao consigo ver")
            sleep(0.5)

def Close():
    stop = True
    while stop:
        if pyautogui.locateOnScreen('Close.png', region = (0,0 ,width,height), grayscale=True, confidence=0.8) != None:
            print("consigo ver")
            coords = pyautogui.locateCenterOnScreen('Close.png', region = (0,0 ,width,height), grayscale=True, confidence=0.8)
            click(coords)
            sleep(2)
            Menu()
            stop = False
        else:
            print("nao consigo ver")
            sleep(0.5)
       
def Works():
    stop = True
    while stop:
        if pyautogui.locateOnScreen('work.png', region = (0,0 ,width,height), grayscale=True, confidence=0.8) != None:
            print("consigo ver")
            coords = pyautogui.locateCenterOnScreen('work.png', region = (0,0 ,width,height), grayscale=True, confidence=0.8)
            x, y = coords
            mouse.position = (x, y)
            coords = x, y+300
            x = 0
            while x < 10:
                click(coords)
                print("click")
                x += 1
            sleep(2)
            print("todos trabalhando")
            Close()
            stop = False
        else:
            print("nao consigo ver")
            sleep(0.5)
        
def Char():
    stop = True
    while stop:
        if pyautogui.locateOnScreen('Character.png', region = (0,0 ,width,height), grayscale=True, confidence=0.8) != None:
            print("consigo ver")
            coords = pyautogui.locateCenterOnScreen('Character.png', region = (0,0 ,width,height), grayscale=True, confidence=0.8)
            x, y = coords
            Movimento(x, y)
            sleep(2)
            Works()
            stop = False
        else:
            print("nao consigo ver")
            sleep(0.5)

def Hero():
    stop = True
    while stop:
        if pyautogui.locateOnScreen('Heroes.png', region = (0,0 ,width,height), grayscale=True, confidence=0.8) != None:
            print("consigo ver")
            coords = pyautogui.locateCenterOnScreen('Heroes.png', region = (0,0 ,width,height), grayscale=True, confidence=0.8)
            click(coords)
            sleep(2)
            Char()
            stop = False
        else:
            print("nao consigo ver")
            sleep(0.5)

def Assinar():
    stop = True
    while stop:
        if pyautogui.locateOnScreen('Assinar.png', region = (0,0 ,width,height), grayscale=True, confidence=0.8) != None:
            print("consigo ver")
            coords = pyautogui.locateCenterOnScreen('Assinar.png', region = (0,0 ,width,height), grayscale=True, confidence=0.8)
            click(coords)
            sleep(2)
            Hero()
            stop = False
        else:
            print("nao consigo ver")
            sleep(0.5)

Close()
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