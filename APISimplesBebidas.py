import requests

#enviando uma requisição GET e obtendo a resposta
response = requests.get(
    'https://www.thecocktaildb.com/api/json/v1/1/search.php?s=margarita'

)
print(response)

#tratando a resposta

#extraindo a lista de drinks
drinks = response.json() ['drinks']

#percorrendo os drinks "Margarita"
for drink in drinks:
    print(drink['strDrink']
    )
