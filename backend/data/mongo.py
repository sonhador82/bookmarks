import abc
import asyncio
import json
import math

from motor.motor_asyncio import AsyncIOMotorClient, AsyncIOMotorCollection, AsyncIOMotorCursor
from bson import json_util, ObjectId

from .bookmark import Bookmark, BookmarkSchema
from .auth import User, UserJsonEncoder


class Storage(abc.ABC):
    @abc.abstractmethod
    async def find_bookmark_by_id(self, b_id: str):
        pass

    @abc.abstractmethod
    async def insert_bookmark(self, bookmark: Bookmark) -> str:
        pass


class MongoStorage(Storage):
    def __init__(self, mongo_url: str, database: str, collection: str):
        self.client: AsyncIOMotorClient = AsyncIOMotorClient(mongo_url)
        self.db = getattr(self.client, database)
        self.collection: AsyncIOMotorCollection = getattr(self.db, collection)
        self.bookmarks: AsyncIOMotorCollection = getattr(self.db, "bookmarks")
        self.users: AsyncIOMotorCollection = getattr(self.db, "users")

    async def insert_bookmark(self, bookmark: Bookmark) -> str:
        data = BookmarkSchema().dump(bookmark)
        result = await self.bookmarks.insert_one(data)
        return str(result.inserted_id)

    async def find_bookmark_by_id(self, b_id) -> Bookmark:
        data = await self.bookmarks.find_one({'_id': ObjectId(b_id)})
        #!TODO убрать этот позор! должно быть что-то типа #return BookmarkSchema().load(data)
        return Bookmark(data['title'], data['url'], data['description'], data['category'], data['tags'], str(data['_id']))


    #!TODO создавать индекс
    #self.users.create_index({"email"}, {"unique": True})

    async def getCursor(self) -> AsyncIOMotorCursor:
        return self.collection.find()

    async def getItems(self, page_num: int, limit: int):
        count = await self.collection.estimated_document_count()
        pages = math.ceil(count / limit)
        skip = page_num*limit
        cursor = self.collection.find()
        cursor.skip(skip)
        cursor.limit(limit)

        items = json_util.dumps(await cursor.to_list(None))

        return json.dumps({"pages": pages, "page": page_num, "items": json.loads(items)})


## User managment
    async def insert_user(self, user: User) -> str:
        data = json.loads(json.dumps(user, cls=UserJsonEncoder))
        result = await self.users.insert_one(data)
        return str(result.inserted_id)

    async def find_user_by_email(self, user_email) -> User:
        data = await self.users.find_one({'email': user_email})
        if not data:
            raise Exception("User not found")
        return User(data['email'], data['full_name'], data['password'], data['is_admin'])
