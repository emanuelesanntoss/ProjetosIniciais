import random
from tkinter import *
import time

#declara classe
class DiceRoller(object):

    def __init__(self, master):
        frame = Frame(master)
        frame.pack()
        self.label = Label(master, font=('times', 300))
        button = Button(master, text='Jogar dados', command=self.roll, activebackground= 'black' , highlightthickness =10,pady = 10, background='black',fg='red')
        button.place(x=350, y= 0)

                   
    def roll(self):
        symbols = ['\u2680','\u2681','\u2682','\u2683','\u2684','\u2685']
        self.label.config(text=f'{random.choice(symbols)}{random.choice(symbols)}')
        time.sleep(1);
        self.label.pack()
                       

#funcao cria tela
if __name__ == "__main__":
    root = Tk()
    root.configure(background="gray")
    root.title('Jogo de Dados')
    root.geometry('800x500')
    DiceRoller(root)
    
    root.mainloop()