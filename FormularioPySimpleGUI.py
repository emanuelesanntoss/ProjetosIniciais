import PySimpleGUI as sg

class TelaPython:
    def __init__(self):
        #tema da tela de layout
        sg.change_look_and_feel('DarkEmber')
        #layout
        layout =[
            [sg.Text('Nome', size=(5,0)),sg.Input(size=(15,0),key='nome')],
            [sg.Text('Idade', size=(5,0)),sg.Input(size=(15,0),key='idade')],
            [sg.Text('Quais provedores de e-mails são aceitos?')],
            [sg.Checkbox('Gmail',key='gmail'),sg.Checkbox('Outlook',key='outlook'),sg.Checkbox('Yahoo',key='yahoo')],
            [sg.Text('Aceita cartão')],
            [sg.Radio('Sim','cartoes', key='aceitaCartao'),sg.Radio('Não','cartoes',key='naoAceitaCartao')],
            [sg.Slider(range=(0,255),default_value=0,orientation='h',size=(15,20),key='sliderVelocidade')],
            [sg.Button('Enviar dados')],
            [sg.Output(size=(30,20))]
        ]
        #janela
        # propriedade self faz com que a janela fique sempre aberta (não feche após enviar os dados)
        self.janela = sg.Window('Dados do usuario').layout(layout)
        #Identificar pelos nomes inseridos no Key   
    def Iniciar(self):
        # while indica para a janela permanecer aberta (loop)
        while True:
            #extrair os dados da tela (todas as variaveis ficam identadas junto com o self)
            self.button, self.values = self.janela.Read()

            nome = self.values['nome']
            idade = self.values['idade']
            aceita_gmail = self.values['gmail']
            aceita_outlook = self.values['outlook']
            aceita_yahoo = self.values['yahoo']
            aceita_cartao = self.values['aceitaCartao']
            nao_aceita_cartao = self.values['naoAceitaCartao']
            velocidade_script = self.values['sliderVelocidade']
            #Exibe na tela
            print(f'nome:{nome}')
            print(f'idade:{idade}')
            print(f'Aceita gmail:{aceita_gmail}')
            print(f'Aceita outlook:{aceita_outlook}')
            print(f'Aceita yahoo:{aceita_yahoo}')
            print(f'Aceita cartao:{aceita_cartao}')
            print(f'Nao aceita cartao:{nao_aceita_cartao}')
            print(f'Velocidade script:{velocidade_script}')


tela = TelaPython()
tela.Iniciar()