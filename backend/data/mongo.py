import asyncio
import json
import math

from motor.motor_asyncio import AsyncIOMotorClient, AsyncIOMotorCollection, AsyncIOMotorCursor
from bson import json_util

from bookmark import Bookmark, BookmarkSchema


class MongoStorage:
    def __init__(self, mongo_url: str, database: str, collection: str):
        self.client: AsyncIOMotorClient = AsyncIOMotorClient(mongo_url)
        self.db = getattr(self.client, database)
        self.collection: AsyncIOMotorCollection = getattr(self.db, collection)

    async def insertBookmark(self, bookmark: Bookmark) -> str:
        data = BookmarkSchema().dump(bookmark)
        result = await self.collection.insert_one(data)
        return str(result.inserted_id)

    async def findBookmarkById(self, b_id) -> Bookmark:
        data = await self.collection.find_one({'_id': b_id})
        return BookmarkSchema().load(data)

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


#todo refactor to test
async def main():
    m = MongoStorage("mongodb://localhost", "BookMark", "bookmarks")
    print(await m.getItems(2, 10))


    # cur: AsyncIOMotorCursor = await m.getCursor()
    # print((await cur.to_list(None))[0:2])
    # cur.rewind()
    # cur.limit(5)
    # cur.skip(0)
    # print(await cur.to_list(None))

    # b = Bookmark("My Title", "https://ya.ru", "Dummy decs", "devops", ["devops", "ci/cd"])
    # result = await m.insertBookmark(b)
    # print(result)
    # print(f'result id: {result}')
    # result2 = await m.findBookmarkById(result)
    # print(f'result2: {result2}')


if __name__ == '__main__':
    asyncio.run(main(), debug=True)
