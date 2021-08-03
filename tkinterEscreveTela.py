from tkinter import *
import tkinter as tk

root = Tk()
#criacao da tela
tela = tk.Canvas(root,width =200 , height = 50)
tela.pack()
#criacao campo label
label = Label(root, text="Inserir algo")
label.pack(side="left")

entry_content = StringVar()

# Associando "entry_content" a propriedade "textvariable".
# O que escreves no "entry" é "absorvido" pelo "entry_content"

entry = Entry(root, textvariable=entry_content) 
entry.pack(side="left",padx=10)

# O valor do "entry_content" é modificado no "entry"
# E essa modificação vai-se refletir nesta "label"    

label = Label(root, text="", textvariable=entry_content)
label.pack(side="left")

root.mainloop()