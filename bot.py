import pyautogui
import time
from tkinter import *

def bot():
    visor.insert(END, "Começando o programa...\n")
    janela.update()
    pyautogui.alert("começando o programa")

    pyautogui.PAUSE = 10
    visor.insert(END, "Pressionando tecla Win...\n")
    janela.update()
    pyautogui.press('winleft')

    visor.insert(END, "Digitando 'ed'...\n")
    janela.update()
    pyautogui.write('ed')

    visor.insert(END, "Pressionando Enter...\n")
    janela.update()
    pyautogui.press('enter')

    time.sleep(50)

    visor.insert(END, "Digitando 'https://www.google.com.br/'...\n")
    janela.update()
    pyautogui.write('https://www.google.com.br/')

    visor.insert(END, "Pressionando Enter...\n")
    janela.update()
    pyautogui.press('enter')

    visor.insert(END, "Digitando 'github'...\n")
    janela.update()
    pyautogui.write('github')

    visor.insert(END, "Pressionando Enter...\n")
    janela.update()
    pyautogui.press('enter')

    visor.insert(END, "Movendo o mouse...\n")
    janela.update()
    pyautogui.moveTo(450, 280)
    pyautogui.mouseDown()
    pyautogui.mouseUp()

    visor.insert(END, "Fim do programa.\n")
    janela.update()
    pyautogui.alert("fim do programa")

janela = Tk()
janela.title("Programa Bot")
janela.geometry("")
texto = Label(janela, text='Clique no botão para começar o programa')
texto.grid(column=0, row=0, padx=10, pady=10)

botao = Button(janela, text='Pressionar', command=bot)
botao.grid(column=0, row=1, padx=10, pady=10)

visor = Text(janela, height=10, width=50)
visor.grid(column=0, row=2, padx=10, pady=10)

janela.mainloop()
