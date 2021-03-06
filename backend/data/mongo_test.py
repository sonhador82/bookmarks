import pytest

from .mongo import MongoStorage
from .bookmark import Bookmark, BookmarkSchema
from .auth import User, check_credentials


@pytest.mark.asyncio
@pytest.fixture()
async def mongo_test():
    m = MongoStorage("mongodb://localhost", "tests", "users")
    await m.users.create_index("email", unique=True)
    yield m
    await m.users.drop()


@pytest.mark.asyncio
async def test_user_creation(mongo_test):
    email = "test@test.com"
    user = User(email, "Gagarin the best", "SomeHashedSecret")
    result = await mongo_test.insert_user(user)
    find_user: User = await mongo_test.find_user_by_email(email)
    assert user == find_user


@pytest.mark.asyncio
async def test_check_creds(mongo_test):
    email = "test@test.com"
    password = "SomeHashedSecret"
    user = User(email, "Gagarin the best", "SomeHashedSecret")
    await mongo_test.insert_user(user)
    assert await check_credentials(mongo_test, email, password) is True


@pytest.mark.asyncio
async def test_create_bookmark(mongo_test):
    data = {
        "title": "Bookmark Title",
        "url": "http://somedomain.com",
        "description": "Some description",
        "category": "devops",
        "tags": ("Tag1", "Tag2"),
        "user_id": "one@sonhador.ru"
    }
    b1 = BookmarkSchema().load(data)
    result_id = await mongo_test.insert_bookmark(b1)
    b1._id = result_id
    b2 = await mongo_test.find_bookmark_by_id(data['user_id'], result_id)
    assert b1 == b2
