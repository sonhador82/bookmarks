import json

import pytest

from .mongo import MongoStorage
from .auth import User, UserJsonEncoder


@pytest.mark.asyncio
@pytest.fixture
async def mongo_test():
    m = MongoStorage("mongodb://localhost", "tests", "users")
    await m.users.create_index("email", unique=True)
    yield m
    await m.users.drop()

# @pytest.fixture
# def prepdb():
#
#     yield user
#     admin_client.delete_user(user)


@pytest.mark.asyncio
async def test_user_creation(mongo_test):
    email = "test@test.com"
    user = User(email, "Gagarin the best", "SomeHashedSecret")
    result = await mongo_test.insert_user(user)
    find_user: User = await mongo_test.find_user_by_email(email)
    assert user == find_user
