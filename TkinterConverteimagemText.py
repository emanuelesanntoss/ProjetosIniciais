#############################
#A lógica da caixa de diálogo de arquivo funcionará para que as imagens formatadas corretamente possam ser carregadas para o software.
#Após o upload bem-sucedido, o sistema está pronto para conversão e a função do módulo Pytesseract entra em ação.
#O módulo Pytesseract lê e extrai o texto da imagem e atualiza a área de texto com esse texto convertido.
#Além disso, a abordagem de manipulação de arquivos em python cria e anexa um arquivo de texto com o texto convertido e o armazenará no banco de dados local do nosso sistema.
#O arquivo armazenado pode ser acessado no futuro para fins de informação e verificação.
#############################

#importar bibliotecas
from tkinter import *
import tkinter.messagebox as tmsg     
from PIL import Image, ImageTk 
from tkinter import filedialog 
import pytesseract         
import os.path 
from tkinter import font

#criar uma interface, usando Tkinter (Label, Button, Frame e assim por diante)  
root = Tk() 
root.geometry('800x500')         
root.maxsize(1000, 500) 
root.minsize(600, 500) 
root.title('Conversor de imagem') 
def upload_file():         
    global filename 
    global start, last 
    filename = filedialog.askopenfilename( 
        initialdir='/Desktop', title = 'Selecione uma imagem', 
      filetypes=(('jpeg files', '*.jpg'), ('png files', '*.png'))) 

#Criando a funcionalidade principal - fazer o upload de um arquivo e depois convertê-lo.
    if filename == '': 
        t.delete(1.0, END) 
        t.insert(1.0, 'Você não forneceu nenhuma imagem para converter') 
        tmsg.showwarning( 
            title = 'Alert!', message = 'Por favor forneça uma imagem no formato PNG ou JPEG') 
        return
        
    else: 
        p_label_var.set('Imagem carregada com sucesso') 
        l.config(fg='#0CDD19') 
      
    if filename.endswith('.JPG') or filename.endswith('.JPEG') or filename.endswith('.jpg') or filename.endswith('.jpeg') or filename.endswith('.PNG') or filename.endswith('.png'): 
        filename_rev = filename[::-1] 
        last = filename.index('.') 
        start = len(filename) - filename_rev.index('/') - 1
def convert():         
    try: 
        c_label_var.set('Output...') 
        pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files (x86)\Tesseract-OCR\tesseract'
        text = pytesseract.image_to_string(filename) 
        t.delete(1.0, END) 
        t.insert(1.0, text) 
        root1 = Toplevel() 
        root1.title('Carregando imagem') 
        img1 = ImageTk.PhotoImage(Image.open(filename)) 
        Label(root1, image=img1).pack() 
        root1.mainloop() 
    except: 
        t.delete(1.0, END) 
        t.insert(1.0, 'Você ainda não forneceu nenhuma imagem para converter') 
        tmsg.showwarning( 
            title='Alert!', message='Por favor forneça uma imagem no formato PNG ou JPEG') 
        return
    f_name = filename[start+1:last]+'.txt'
    f_name = os.path.join(r'Database', f_name) 
    f = open(f_name, 'w') 
    f.write(text) 
    f.close() 
mainmenu = Menu(root) 
mainmenu.config(font = ('Times bold', 29)) 

#Menu - Ferramentas  
m1 = Menu(mainmenu, tearoff = 0) 
m1.add_command(label = 'Transformar imagens em texto',font = ('Times bold', 13)) 
root.config(menu = mainmenu) 
mainmenu.add_cascade(label = 'Ferramentas', menu = m1) 

 #Menu - Sobre 
m2 = Menu(mainmenu, tearoff = 0) 
m2.add_command(label = 'Develop Python',font = ('Times bold', 13)) 
m2.add_command(label = 'Interesse por Python', font = ('Times bold', 13)) 
mainmenu.add_cascade(label = 'Sobre', menu = m2) 
root.config(menu = mainmenu)

#Menu - Contato
m3 = Menu(mainmenu, tearoff=0) 
m3.add_command(label = 'E-mail: emanuelesanntoss@gmail.com',  
               font = ('Times bold', 13)) 
#m3.add_separator() 
m3.add_command(label = 'Telefone: +55-051997255283', font=('Times bold', 13)) 
#m3.add_separator() 
m3.add_command(label = 'GitHub: https://github.com/emanuelesanntoss/', 
               font = ('Times bold', 13)) 
root.config(menu = mainmenu) 
mainmenu.add_cascade(label = 'Contato', menu = m3) 

#banner  
Label(text = 'Leitor de imagem', bg = '#FAD2B8', 
      fg = '#39322D', font = ('Times bold', 18)).pack(fill = 'x') 
Label(text = 'Python ###', bg = '#FAD2B8', fg ='#39322D', font=( 
    'Times bold', 12, 'italic')).pack(fill='x') 
 
#frame 1 
f1 = Frame() 
f1.config(bg='white') 
Label(f1, text='Selecionar a imagem', width=20, 
      font=('Times bold', 15), bg='white').pack(side='left') 
Label(f1, text='format: png/jpeg', bg='white', 
      width=30).pack(side='right', padx=5) 
Button(f1, text='Upload', bg='#F58D4B', font=('Times bold', 15), 
       width=70, command=upload_file).pack(side='right') 
f1.pack(pady=10, fill='x') 
p_label_var = StringVar() 
p_label_var.set('Por favor carregue uma imagem') 
l = Label(textvariable=p_label_var, fg='red', bg='white') 
l.pack() 

#frame 2  
Label(text='©copyright 2021', bg='#433E3B', fg='white', 
      font=('Times bold', 10)).pack(side='bottom', fill='x') 
Label(text='Developer: Emanuele Santos', bg='#433E3B', fg='white', 
      font=('Times bold', 10, ' italic')).pack(side='bottom', fill='x') 
t = Text(root, height='9', font=('Times bold', 13)) 
t.pack(side='bottom', fill='x') 
t.insert(1.0, 'O texto da imagem convertida será exibido aqui...', END) 
c_label_var = StringVar() 
c_label_var.set('Pronto para conversão') 
c_label = Label(textvariable=c_label_var) 
c_label.pack(side='bottom', anchor='w') 
Button(root, text='Scan and Convert', bg='#F58D4B', font=('Times bold', 15), 
       width=70, command=convert).pack(pady='10', side='bottom') 

#executar
root.mainloop() 