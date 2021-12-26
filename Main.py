from pyautogui import *
import pyautogui
from tkinter import *
from tkinter.ttk import*
import keyboard
from pynput.mouse import Button, Controller
from PySimpleGUI import PySimpleGUI as sg

#tempo pra resetar estamina
# ficar abrindo e fechando recompensas ate dar uma hora
#
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

def Back():
    stop = True
    while stop:
        if pyautogui.locateOnScreen('Imagens/Back.png', region = (0,0 ,width,height), grayscale=True, confidence=0.8) != None: #procura a imagem na tela
            print("consigo ver")
            coords = pyautogui.locateCenterOnScreen('Imagens/Back.png', region = (0,0 ,width,height), grayscale=True, confidence=0.8) #pega o centro da imagem
            click(coords)
            sleep(0.1)
            stop = False
        elif pyautogui.locateOnScreen('Imagens/ERROR.png', region = (0,0 ,width,height), grayscale=True, confidence=0.8) != None:
            print("consigo ver")
            coords = pyautogui.locateCenterOnScreen('Imagens/ERROR.png', region = (0,0 ,width,height), grayscale=True, confidence=0.8)
            click(coords)
            sleep(2)
            Menu()
            stop = False
        else:
            print("nao consigo ver")
            sleep(0.5)

def Rewards():
    stop = True
    while stop:
        if pyautogui.locateOnScreen('Imagens/Rewards.png', region = (0,0 ,width,height), grayscale=True, confidence=0.8) != None: #procura a imagem na tela
            print("consigo ver")
            coords = pyautogui.locateCenterOnScreen('Imagens/Rewards.png', region = (0,0 ,width,height), grayscale=True, confidence=0.8) #pega o centro da imagem
            click(coords)
            sleep(0.1)
            stop = False
        elif pyautogui.locateOnScreen('Imagens/ERROR.png', region = (0,0 ,width,height), grayscale=True, confidence=0.8) != None:
            print("consigo ver")
            coords = pyautogui.locateCenterOnScreen('Imagens/ERROR.png', region = (0,0 ,width,height), grayscale=True, confidence=0.8)
            click(coords)
            sleep(2)
            Menu()
            stop = False
        else:
            print("nao consigo ver")
            sleep(0.5)
def Back():
    stop = True
    while stop:
        if pyautogui.locateOnScreen('Imagens/Back.png', region = (0,0 ,width,height), grayscale=True, confidence=0.8) != None:
            print("consigo ver")
            coords = pyautogui.locateCenterOnScreen('Imagens/Back.png', region = (0,0 ,width,height), grayscale=True, confidence=0.8)
            click(coords)
            sleep(2)
            Hero() #apos o loop volta para a tela inicial e bota novamente todos bonecos para trabalhar
            stop = False
        elif pyautogui.locateOnScreen('Imagens/ERROR.png', region = (0,0 ,width,height), grayscale=True, confidence=0.8) != None:
            print("consigo ver")
            coords = pyautogui.locateCenterOnScreen('Imagens/ERROR.png', region = (0,0 ,width,height), grayscale=True, confidence=0.8)
            click(coords)
            sleep(2)
            Menu()
            stop = False
        else:
            print("nao consigo ver")
            sleep(0.5)

def RewardsLoop():
    x = 0
    while x < valores['Horas']: #espera uma hora
        Rewards()
        sleep(60) #um minuto
        Back()
        sleep(60) #segundo minuto
        x += 1
    Back()

def Menu():
    stop = True
    while stop:
        if pyautogui.locateOnScreen('Imagens/Menu.png', region = (0,0 ,width,height), grayscale=True, confidence=0.8) != None: #procura a imagem na tela
            print("consigo ver")
            coords = pyautogui.locateCenterOnScreen('Imagens/Menu.png', region = (0,0 ,width,height), grayscale=True, confidence=0.8) #pega o centro da imagem
            click(coords)
            sleep(2)
            RewardsLoop()
            stop = False
        elif pyautogui.locateOnScreen('Imagens/ERROR.png', region = (0,0 ,width,height), grayscale=True, confidence=0.8) != None:
            print("consigo ver")
            coords = pyautogui.locateCenterOnScreen('Imagens/ERROR.png', region = (0,0 ,width,height), grayscale=True, confidence=0.8)
            click(coords)
            sleep(2)
            Menu()
            stop = False
        else:
            print("nao consigo ver")
            sleep(0.5)

def Close():
    stop = True
    while stop:
        if pyautogui.locateOnScreen('Imagens/Close.png', region = (0,0 ,width,height), grayscale=True, confidence=0.8) != None:
            print("consigo ver")
            coords = pyautogui.locateCenterOnScreen('Imagens/Close.png', region = (0,0 ,width,height), grayscale=True, confidence=0.8)
            click(coords)
            sleep(2)
            Menu()
            stop = False
        elif pyautogui.locateOnScreen('Imagens/ERROR.png', region = (0,0 ,width,height), grayscale=True, confidence=0.8) != None:
            print("consigo ver")
            coords = pyautogui.locateCenterOnScreen('Imagens/ERROR.png', region = (0,0 ,width,height), grayscale=True, confidence=0.8)
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
        if pyautogui.locateOnScreen('Imagens/work.png', region = (0,0 ,width,height), grayscale=True, confidence=0.8) != None:
            print("consigo ver")
            coords = pyautogui.locateCenterOnScreen('Imagens/work.png', region = (0,0 ,width,height), grayscale=True, confidence=0.8)
            x, y = coords
            mouse.position = (x, y)
            coords = x, y+300
            x = 0
            while x < valores['QtdHerois']:
                click(coords)
                print("click")
                x += 1
            sleep(2)
            print("todos trabalhando")
            Close()
            stop = False
        elif pyautogui.locateOnScreen('Imagens/ERROR.png', region = (0,0 ,width,height), grayscale=True, confidence=0.8) != None:
            print("consigo ver")
            coords = pyautogui.locateCenterOnScreen('Imagens/ERROR.png', region = (0,0 ,width,height), grayscale=True, confidence=0.8)
            click(coords)
            sleep(2)
            Menu()
            stop = False
        else:
            print("nao consigo ver")
            sleep(0.5)
        
def Char():
    stop = True
    while stop:
        if pyautogui.locateOnScreen('Imagens/Character.png', region = (0,0 ,width,height), grayscale=True, confidence=0.8) != None:
            print("consigo ver")
            coords = pyautogui.locateCenterOnScreen('Imagens/Character.png', region = (0,0 ,width,height), grayscale=True, confidence=0.8)
            x, y = coords
            Movimento(x, y)
            sleep(2)
            Works()
            stop = False
        elif pyautogui.locateOnScreen('Imagens/ERROR.png', region = (0,0 ,width,height), grayscale=True, confidence=0.8) != None:
            print("consigo ver")
            coords = pyautogui.locateCenterOnScreen('Imagens/ERROR.png', region = (0,0 ,width,height), grayscale=True, confidence=0.8)
            click(coords)
            sleep(2)
            Menu()
            stop = False
        else:
            print("nao consigo ver")
            sleep(0.5)

def Hero():
    stop = True
    while stop:
        if pyautogui.locateOnScreen('Imagens/Heroes.png', region = (0,0 ,width,height), grayscale=True, confidence=0.8) != None:
            print("consigo ver")
            coords = pyautogui.locateCenterOnScreen('Imagens/Heroes.png', region = (0,0 ,width,height), grayscale=True, confidence=0.8)
            click(coords)
            sleep(2)
            Char()
            stop = False
        elif pyautogui.locateOnScreen('Imagens/ERROR.png', region = (0,0 ,width,height), grayscale=True, confidence=0.8) != None:
            print("consigo ver")
            coords = pyautogui.locateCenterOnScreen('Imagens/ERROR.png', region = (0,0 ,width,height), grayscale=True, confidence=0.8)
            click(coords)
            sleep(2)
            Menu()
            stop = False
        else:
            print("nao consigo ver")
            sleep(0.5)

def Assinar():
    stop = True
    while stop:
        if pyautogui.locateOnScreen('Imagens/Assinar.png', region = (0,0 ,width,height), grayscale=True, confidence=0.8) != None:
            print("consigo ver")
            coords = pyautogui.locateCenterOnScreen('Imagens/Assinar.png', region = (0,0 ,width,height), grayscale=True, confidence=0.8)
            click(coords)
            sleep(2)
            Hero()
            stop = False
        elif pyautogui.locateOnScreen('Imagens/ERROR.png', region = (0,0 ,width,height), grayscale=True, confidence=0.8) != None:
            print("consigo ver")
            coords = pyautogui.locateCenterOnScreen('Imagens/ERROR.png', region = (0,0 ,width,height), grayscale=True, confidence=0.8)
            click(coords)
            sleep(2)
            Menu()
            stop = False
        else:
            print("nao consigo ver")
            sleep(0.5)

def Menu():
    stop = True
    while stop:
        if pyautogui.locateOnScreen('Imagens/Connect2.png', region = (0,0 ,width,height), grayscale=True, confidence=0.8) != None:
            print("consigo ver")
            coords = pyautogui.locateCenterOnScreen('Imagens/Connect2.png', region = (0,0 ,width,height), grayscale=True, confidence=0.8)
            print(coords)
            click(coords)
            sleep(2)
            Assinar()
            stop = False
        else:
            print("nao consigo ver")
            sleep(0.5)

#layout 
sg.theme('Reddit')
layout = [
    [sg.Text('Quantos herois voce deseja por em campo por rotação ?'), sg.Input(key='QtdHerois', size = (20, 1))],
    [sg.Text('Depois de quantos minutos voce deseja reiniciar o ciclo ?'), sg.Input(key='Horas', size = (20, 1))],
    [sg.Button('Iniciar')],
    [sg.Button('Instruções')]
]
#layout instruções
sg.theme('Reddit')
layout2 = [
    [sg.Text('1° Certifique se de que seu computador esteja na resolução 1920 x 1080')],
    [sg.Text('2° Certifique se de que seu computador esteja na escala 100%')],
    [sg.Text('3° A senha nao sera colocada automaticamente, entao fique atento')],
    [sg.Text('4° Ao clicar em iniciar basta abrir a pagina do Bomb Crypto e o programa fará o resto')],
    [sg.Text('5° O programa esta em beta, se tiver sujestões: Discord: Avilactea#1855')],
]

#janela
janela = sg.Window('Tela Inicial', layout)
janela2 = sg.Window('Instruções', layout2)

while True:
    eventos, valores = janela.read()
    if eventos == sg.WINDOW_CLOSED:
        break
    if eventos == 'Iniciar':
        if valores['QtdHerois'] != None and valores['Horas'] != None:
            Menu()
    if eventos == 'Instruções':
        eventos2 = janela2.read() 
        if eventos2 == sg.WIN_CLOSED:
                break
        #chama o programa levando os valores
#Close()
