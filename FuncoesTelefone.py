import phonenumbers

# ajuste telefone
telefone = '+5551997255283'
telefone_ajustado = phonenumbers.parse(telefone)
# tem a opcao de passar a pais que é o telefone que ajusta o formato
#telefone = '51997255283'
#telefone_ajustado = phonenumbers.parse(telefone, 'BR')
print(telefone_ajustado)

# descobrir a localizacao do telefone
from phonenumbers import geocoder
local = geocoder.description_for_number(telefone_ajustado, 'pt-br')
print(local)

# formatar telefone
telefone_formulario = '51997255283'
telefone_formulario_ajustado = phonenumbers.parse(telefone_formulario, 'BR')
telefone_formatado = phonenumbers.format_number(telefone_formulario_ajustado, phonenumbers.PhoneNumberFormat.NATIONAL)
print(telefone_formatado)

# descobrir a operadora
from phonenumbers import carrier
operadora = carrier.name_for_number(telefone_ajustado, 'pt-br')
print (operadora)

# retirar um telefone de um texto
corpo_email = """
Prezados(as),

Quando tiverem uma resposta da proposta, favor entrar em contato.

Atenciosamente;
Emanuele Santos - Analista de sistema
(21)99999-9999"""
for telefone in phonenumbers.PhoneNumberMatcher(corpo_email, 'BR'):
   print (telefone)

# Observacoes
    # quando texto em mais várias linhas usar """ (tres aspas no inicio e tres aspas no final do texto)
    # quando na linha anterior o método terminar com : logo o próximo comando tem que está identado.