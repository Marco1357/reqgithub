from unittest import TestCase
from unittest.mock import Mock
from reqgithub import github

json_str = '''{
  "login": "renzon",
  "id": 3457115,
  "avatar_url": "https://avatars.githubusercontent.com/u/3457115?v=3",
  "gravatar_id": "",
  "url": "https://api.github.com/users/renzon",
  "html_url": "https://github.com/renzon",
  "followers_url": "https://api.github.com/users/renzon/followers",
  "following_url": "https://api.github.com/users/renzon/following{/other_user}",
  "gists_url": "https://api.github.com/users/renzon/gists{/gist_id}",
  "starred_url": "https://api.github.com/users/renzon/starred{/owner}{/repo}",
  "subscriptions_url": "https://api.github.com/users/renzon/subscriptions",
  "organizations_url": "https://api.github.com/users/renzon/orgs",
  "repos_url": "https://api.github.com/users/renzon/repos",
  "events_url": "https://api.github.com/users/renzon/events{/privacy}",
  "received_events_url": "https://api.github.com/users/renzon/received_events",
  "type": "User",
  "site_admin": false,
  "name": "Renzo Nuccitelli",
  "company": "Python Pro",
  "blog": "https://adm.python.pro.br",
  "location": "Brazil",
  "email": "renzo@python.pro.br",
  "hireable": false,
  "bio": null,
  "public_repos": 59,
  "public_gists": 9,
  "followers": 130,
  "following": 3,
  "created_at": "2013-02-02T14:15:53Z",
  "updated_at": "2015-03-07T21:40:06Z"
}'''


class ToXMLTests(TestCase):
    def setUp(self):
        print('Inicializando')

    def tearDown(self):
        print('Finalizando')

    def test_sucesso(self):
        resposta = Mock()
        resposta.text = json_str
        get = github.requests.get
        github.requests.get = Mock(return_value=resposta)
        xml = github.github_user_to_xml('renzon')
        self.assertTrue(xml.startswith('<?xml version="1.0" encoding="utf-8"?>'))
        github.requests.get.assert_called_once_with('https://api.github.com/users/renzon')
        github.requests.get = get

    def test_blah(self):
        # print(github.github_user_to_xml('edimar'))
        raise NotImplementedError