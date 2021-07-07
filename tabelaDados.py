from prettytable import PrettyTable
from prettytable import from_csv
from prettytable import from_html
from prettytable import MSWORD_FRIENDLY
from prettytable import PLAIN_COLUMNS


# Cria variavel e tabela
x = PrettyTable([ "Nome da cidade", "UF", "Populacao", "IDH-M", "Renda per Capita"])

# Todas o cabecalho da tabela em maiusculo
x.header_style = "upper"
x.horizontal_char = '_'
x.vertical_char = '!'
x.junction_char = '*'

# Alinha as colunas
x.align["Nome da cidade"] = "l"
x.align["UF"] = "l"
x.align["Populacao"] = "1"
x.align["IDH-M"] = "1"
x.align["Renda per Capita"] = "1"

# Deixa um espaco entre a borda das colunas e o conteudo (default)
x.padding_width = 3


# Adiciona dados a tabela
x.add_row(["Sao Paulo","SP", 12106920, 0.805, 54358]) 
x.add_row(["Rio de Janeiro","RJ", 6520266, 0.799, 49527]) 
x.add_row(["Belo Horizonte", "MG", 2523794, 0.810, 35187]) 
x.add_row(["Porto Alegre", "RS", 1484941, 0.805, 46122]) 
x.add_row(["Salvador", "BA", 2953986, 0.759, 19812]) 
x.add_row(["Recife", "PE", 1633697, 0.772, 29701]) 
x.add_row(["Brasilia", "DF", 3039444, 0.824, 73971])

# Style de tabela 1
#print(x.set_style (MSWORD_FRIENDLY))

# Stlyle de tabela 2
#print(x.set_style (PLAIN_COLUMNS))

# Ordenar por cidade
print(x.get_string(sortby="Nome da cidade"))






