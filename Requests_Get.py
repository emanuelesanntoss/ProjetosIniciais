import requests

# Pegar informacao - GET
# Firebase - Base de dados - https://console.firebase.google.com/u/0/project/teste-58ce0/database/teste-58ce0-default-rtdb/data


requisicao = requests.get("https://teste-58ce0-default-rtdb.firebaseio.com/.json")
print(requisicao)
print(requisicao.json())