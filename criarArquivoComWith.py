# usando para abrir arquivos

# com with
# cria o arquivo (é necessário dar um alias para o arquivo)
with open('alunoArquivoWith.txt', 'w') as arq:

#  passa o alias e escreve no arquivo
    arq.write('Boas vindas aos alunos: ' + 'Marqueti - Julieti - Pauleti')
# nesse caso não é necessário fechar o arquivo (com a função with já fecha o arquivo)

