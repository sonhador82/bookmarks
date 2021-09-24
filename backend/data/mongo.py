import asyncio
from motor.motor_asyncio import AsyncIOMotorClient, AsyncIOMotorCollection

from .bookmark import Bookmark, BookmarkSchema


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


#todo refactor to test
async def main():
    m = MongoStorage("mongodb://localhost", "bookmarks")
    b = Bookmark("My Title", "https://ya.ru", "Dummy decs", "devops", ["devops", "ci/cd"])
    result = await m.insertBookmark(b)
    print(result)
    print(f'result id: {result}')
    result2 = await m.findBookmarkById(result)
    print(f'result2: {result2}')


if __name__ == '__main__':
    asyncio.run(main(), debug=True)
