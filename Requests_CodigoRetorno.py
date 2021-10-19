# Http Status Codes APIs

cod = '200'
match cod:

#########################################################################################################################

# Respostas de sucesso (2XX)

# 200 – Success
# Pode ser usado em GET, PUT, POST, DELETE.
    case '200':
        print('A requisição foi processada com sucesso')
# 201 - Created
# somente faz sentido para POST.
    case '201':
        print('A requisição foi processada com sucesso e uma entidade foi criada.')
# 202 – Accepted
# Faz sentido para POST, PUT, DELETE.
# Usado em comunicação assíncrona. O cliente não espera o processamento. Apenas é notificado de que ele será iniciado.
    case '202':
        print('A requisição foi recebida com sucesso e será processada posteriormente.')
# 204 – No Content
# Pode ser usado em POST, PUT, DELETE, ...
# Para GET, não faz sentido. Se não há dados a retornar, considerar 404 ou 410.
    case '204':
        print('A requisição foi processada com sucesso e o retorno (body) não contém dados.')

#########################################################################################################################

# Mensagens de redirecionamento (3XX)

# 302 – Found
# O header da resposta deve conter o campo Location indicando a URL a ser consultada.
# Navegadores obedecem automaticamente ao 302, sem envolvimento do código Javascript.
# Significava originalmente que o recurso solicitado foi temporariamente movido para outro endereço. Na prática, porém, é utilizado de uma forma geral para forçar o redirecionamento do cliente para outra URL.
    case '302':
        print(' A requisição será redireciona para outra URL.')

#########################################################################################################################

# Respostas de erro do cliente (4XX)

# 400 - Bad Request
# Exemplo: parâmetro na URL com grafia incorreta ou JSON no corpo da requisição com estrutura incorreta/inesperada.
# Reparar na diferença para o 422.
    case '400':
        print('A requisição falhou porque o cliente não obedeceu à sintaxe esperada.')
# 401 – Unauthorized
# Exemplos: usuário não fez login, portanto não tem cookie de sessão; token ausente; token presente porém inválido.
# Reparar na diferença para o 403.
    case '401':
        print('A requisição não está autenticada.')
# 403 – Forbidden
# Exemplo: usuário tem perfil que não lhe permite aquela transação.
# Reparar na diferença para o 401.
    case '403':
        print('A requisição está autenticada porém a operação não é permitida.')
# 404 – Not found
# Pode ser retornado quando foi consultada uma rota que não existe. Ou uma rota válida, porém não existe a entidade com o ID especificado, por exemplo.
# Reparar na diferença para o 410.
    case '404':
        print('O recurso requisitado não foi encontrado.')
# 409 – Conflict
# É uma opção para os casos de tentativa de inclusão de registro duplicado, por exemplo, ou registro que viola alguma consistência.
# Reparar na diferença para o 422 (são facilmente confundidos).
    case '409':
        print('Sintaxe e semântica estão OK, porém a requisição encontrou algum conflito. Típico de quando alguma regra de negócio não foi obedecida.')
# 410 – Gone
# Parecido com o 404, porém deixa claro que a entidade um dia existiu. Foi excluída, não está mais disponível.
    case '410':
        print('O recurso requisitado não foi encontrado, embora previamente estivesse presente.')
# 422 - Unprocessable Entity
# Indica que o servidor entende o tipo de conteúdo da entidade da requisição, e a sintaxe da requisição está correta, mas não foi possível processar as instruções presentes.
# Reparar na diferença para o 400 e para o 409.
    case '422':
        print('A requisição falhou porque o cliente não obedeceu à semântica esperada.')

#########################################################################################################################

# Respostas de erro do servidor (5XX)

# 500 – Internal server error
# Típico de exceção tratada mas sem saída de contorno, sem fallback. O IIS e outros servidores web também costumam devolver erro 500 quando a aplicação não tratou alguma exceção.
    case '500':
        print('O servidor encontrou um erro inesperado, um erro com o qual não sabe lidar.')
# 510 – Not implemented
# É útil quando o serviço ainda está em desenvolvimento. Criam-se todas as rotas inicialmente sem implementação. Depois, implementa-se uma a uma.
    case '510':
        print('A operação ainda não foi implementada.')

#########################################################################################################################

# quando o código de retorno não é nenhum informado
    case outro_cod:
        print('Erro não encontrado')








