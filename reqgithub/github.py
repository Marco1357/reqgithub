import json
import requests
import xmltodict

xmltodict

print(xmltodict.unparse({'nome': 'Renzo'}))
resposta = requests.get('https://api.github.com/users/renzon')
dct = json.loads(resposta.text)
xml = xmltodict.unparse({'user': dct}, pretty=True, newl='\n', indent='---')
print(xml)
print(resposta.text)