from aiohttp import web
from data.bookmark import BookmarkSchema
from data.mongo import Storage


class BookmarkHandler:
    def __init__(self, data_storage: Storage):
        self.storage = data_storage

    async def list(self, request: web.Request):
        return web.HTTPOk(text="Show all bookmarks")

    async def get(self, request: web.Request):
        b_id = request.match_info['b_id']
        data = await self.storage.find_bookmark_by_id(b_id)
        return web.json_response(BookmarkSchema().dump(data))

    async def post(self, request):
        data = await request.json()
        #!TODO зарефачить наверное на фронте в tags str -> []
        tags = data['tags'].split(',')
        data['tags'] = tags
        result = await self.storage.insert_bookmark(BookmarkSchema().load(data))
        return web.json_response({"status": "ok", "id": result})
