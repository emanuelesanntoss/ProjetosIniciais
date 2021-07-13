import requests
import json
import win32com.client as win32

# esse link pode mudar se os donos da API mudarem
cotacoes = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL")
cotacoes_dic = cotacoes.json()
cotacao_dolar = cotacoes_dic['USDBRL']['bid']
print(cotacao_dolar)
cotacao_btc = cotacoes_dic['BTCBRL']['bid']
print(cotacao_btc)

# enviar um email com o relatório
outlook = win32.Dispatch('outlook.application')
mail = outlook.CreateItem(0)
mail.To = 'emanuelesanntoss@gmail.com'
mail.Subject = 'Cotação atualizada dólar/biticoin'
mail.HTMLBody = f'''
<p>Prezados (as),</p>

<p>Segue cotação atualizada dólar/biticon.</p>

<p>Dólar:</p>
A cotação nesse momento: ${cotacao_dolar}
<p>Bitcoin:</p>
A cotação nesse momento: R${cotacao_btc}

<p>Qualquer dúvida estou à disposição.</p>

<p>Att.,</p>
<p>Emanuele Santos</p>
'''

mail.Send()

print('Email Enviado')
