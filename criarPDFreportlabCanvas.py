#install reportlab

#importar lib reportlab
from reportlab.pdfgen import canvas

#função
def GeneratePDF(lista):
    try:
        nome_pdf = input('Informe o nome do PDF:' + " ")
        pdf = canvas.Canvas('{}.pdf'.format(nome_pdf))
        x = 720
        for nome,idade in lista.items():
            x-=20
            pdf.drawString(247,x, '{} : {}'.format(nome,idade))
        pdf.setTitle(nome_pdf)
        pdf.setFont('Helvetica-oblique', 14)
        pdf.drawString(245,750, 'Lista de clientes')
        pdf.setFont('Helvetica-Bold', 12)
        pdf.drawString(245,724, 'Nome e idade')
#salvar arquivo
        pdf.salve()
#indica se pdf foi criado
        print('{}.pdf criado com sucesso!'.format(nome_pdf))
    except:
        print('Erro ao gerar{}'.format(nome_pdf))

lista = {'Felipe': '24', 'Jose': '42', 'Maria': '15'}
GeneratePDF(lista)