from uuid import uuid4
import requests


def test_create_bookmark():
    auth_url = 'http://localhost:8000/auth/signin'
    session = requests.session()
    resp = session.post(url=auth_url, json={'email': 'one@sonhador.ru', 'password': 'secret'}, allow_redirects=False)

    uuid = str(uuid4())
    new_book = {
        "title": f"New Bookmark {uuid}",
        'url': "http://somesite.com",
        "description": f'Description for {uuid}',
        'category': 'devops',
        'tags': 'somtag1, sometag2',
        'user_id': f'user_id_{uuid}'
    }
    crete_url = 'http://localhost:8000/bookmark'
    resp2 = session.post(url=crete_url, json=new_book)
    assert resp2.status_code == 200
