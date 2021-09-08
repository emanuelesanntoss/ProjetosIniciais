"""Função normal para retornar valor do imposto
preco = 5000
def calcularImposto(preco):
    return preco * 0.3
print(calcularImposto(preco))
"""
"""Função lambda para retornar valor do imposto
x = 1000
calcularImposto = lambda x: x*0.3
print(calcularImposto(x))
"""
#Função lambda, usando map (funcao dentro de funcao)
valores = [1000,500,50]
imposto = list(map(lambda x:x*0.3, valores))
print(imposto)