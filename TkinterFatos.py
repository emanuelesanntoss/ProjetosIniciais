#########################################
#necessário instalar = pip install randfacts

#O bloco do layout da página fica no final
#########################################

#importar as bibliotecas utilizadas
import tkinter as tk 
from tkinter import *
import randfacts 
import time 

#criar função de movimento (para adicionar os fatos)  
def move(): 
    facts = randfacts.getFact(True) 
    IniciarFrase = "*** "
    label = Label(root, text=IniciarFrase+facts)
    label.pack(pady=10)
  
#criar função destruir para limpar a janela 
def destroy(): 
    root.destroy() 

#Criar os botões do código.     
root = tk.Tk() 
root.config(bg='grey') 
root.geometry('800x500') 
button = tk.Button(root, text='Clique aqui para exibir um fato aleatório',font=('Helvetica 15 bold'),fg="Green", command=move)
button2 = tk.Button(root, text='Limpar e fechar tela',font=('Helvetica 12 bold'),fg="red", command=destroy)
button.pack() 
button2.pack(side=BOTTOM)    

#executar  
root.mainloop() 

