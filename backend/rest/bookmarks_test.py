from uuid import uuid4

import requests
import pytest


@pytest.mark.asyncio
@pytest.fixture()
def make_session():
    auth_url = 'http://localhost:8000/auth/signin'
    session = requests.session()
    resp = session.post(url=auth_url, json={'email': 'one@sonhador.ru', 'password': 'secret'}, allow_redirects=False)
    yield session
    del session


def test_create_bookmark(make_session):
    uuid = str(uuid4())
    new_book = {
        "title": f"New Bookmark {uuid}",
        'url': "http://somesite.com",
        "description": f'Description for {uuid}',
        'category': 'devops',
        'tags': 'somtag1, sometag2',
        'user_id': f'user_id_{uuid}'
    }
    crete_url = 'http://localhost:8000/bookmarks'
    resp2 = make_session.post(url=crete_url, json=new_book)
    assert resp2.status_code == 200


def test_get_bookmark(make_session):
    uuid = str(uuid4())
    new_book = {
        "title": f"New Bookmark {uuid}",
        'url': "http://somesite.com",
        "description": f'Description for {uuid}',
        'category': 'devops',
        'tags': 'somtag1, sometag2',
        'user_id': f'user_id_{uuid}'
    }
    crete_url = 'http://localhost:8000/bookmarks'
    resp1 = make_session.post(url=crete_url, json=new_book)
    resp2 = make_session.get(url=f'{crete_url}/{resp1.json()["id"]}')

    assert new_book['title'] == resp2.json()['title']
