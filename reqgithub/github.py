import requests
import xmltodict

xmltodict

print(xmltodict.unparse({'nome': 'Renzo'}))
resposta = requests.get('https://api.github.com/users/renzon')

print(resposta.text)