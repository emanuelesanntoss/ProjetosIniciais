import os

inscritos_recentes = ['Rebeca Duarte', 'Wiliam Nobrega', 'Falico porto', 'Paulo andou']

#criar arquivo com with
with open('inscritos.txt', 'w', newline = '') as file:
    for line in inscritos_recentes:
        file.write(line + os.linesep)

#tornar um executável (no terminal 'anaconda' passar o comando cxfreeze .\nomeArquivo.py)


