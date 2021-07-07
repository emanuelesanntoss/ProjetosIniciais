import random

minusculas = "abcdefghijklmnopqrstuvxyz"
maiusculas = minusculas.upper()
numeros = "123456789"
simbolos = "=[]()*&;/_-@+"

tudo = minusculas + maiusculas + numeros + simbolos
qtdigitos = 5
senha = "".join(random.sample(tudo,qtdigitos))
print(senha)