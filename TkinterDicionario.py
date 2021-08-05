###################################
# A pesquisa somente é usar para palavras em inglês, se pesquisar em português vai apresentar o seguinte erro: TypeError: 'NoneType' object is not subscriptable
####################################


#importar bibliotecas
from tkinter import *
from PyDictionary import PyDictionary

encoding='utf-8'

#criar objeto
dictionary = PyDictionary()
root = Tk()

#Design tela
root.geometry("1600x400")

#cria função (essa função vai obter o significado, sinônimo e antônimo das palavras)
def dict():
    meaning.config(text=dictionary.meaning(word.get())['Noun'][0])
    synonym.config(text=dictionary.synonym(word.get()))
    antonym.config(text=dictionary.antonym(word.get()))

#adicionar label e buttons e frames
Label(root, text='Dicionário', font=("Helvetica 20 bold"), fg="Black").pack(pady=10)

#Frame 1 (Insira a palavra)
frame = Frame(root)
Label(frame, text='Digite a palavra', font=('Helvetica 15 bold'), fg="Green").pack(side=LEFT)
word = Entry(frame, font=('Hekvetica 15 bold'))
word.pack()
frame.pack(pady=10)

#Frame 2 (Siginficado)
frame1 = Frame(root)
Label(frame1, text='Significado:', font=('Helvetica 12 bold'),fg="Green").pack(side=LEFT)
meaning = Label(frame1, text="", font=('Hekvetica 10'))
meaning.pack()
frame1.pack(pady=10)

#Frame 3 (Sinonimo)
frame2 = Frame(root)
Label(frame2, text='Sinônimo:', font=('Helvetica 12 bold'), fg="Green").pack(side=LEFT)
synonym = Label(frame2, text="", font=('Hekvetica 10'))
synonym.pack()
frame2.pack(pady=10)

#Frame 4 (Antonimo)
frame3 = Frame(root)
Label(frame3, text='Antônimo:', font=('Helvetica 12 bold'),fg="Green").pack(side=LEFT)
antonym = Label(frame3, text="", font=('Hekvetica 10'))
antonym.pack()
frame3.pack(pady=10)

#button (pesquisar)
Button(root, text="Pesquisar", font=("Helvetica 15 bold"), command=dict).pack()

#executar
root.mainloop()
