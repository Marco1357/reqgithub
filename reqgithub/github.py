import json
import requests
import xmltodict

xmltodict


def github_user_to_xml(user):
    resposta = requests.get('https://api.github.com/users/%s' % user)
    dct = json.loads(resposta.text)
    xml = xmltodict.unparse({'user': dct}, pretty=True, newl='\n', indent='---')
    return xml


if __name__ == '__main__':
    github_user_to_xml('renzon')