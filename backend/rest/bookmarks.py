from aiohttp import web
from aiohttp_security.api import check_authorized

from data.bookmark import BookmarkSchema
from data.mongo import Storage


class BookmarkHandler:
    def __init__(self, data_storage: Storage):
        self.storage = data_storage

    async def list(self, request: web.Request):
        user_id = await check_authorized(request)
        data = await self.storage.find_bookmarks_for_user(user_id)
        return web.json_response(BookmarkSchema(many=True).dump(data))

    async def get(self, request: web.Request):
        # TODO зарефачить чтобы только для определенного пользователя
        _ = await check_authorized(request)
        b_id = request.match_info['b_id']
        data = await self.storage.find_bookmark_by_id(b_id)
        return web.json_response(BookmarkSchema().dump(data))

    async def post(self, request):
        user_id = await check_authorized(request)
        data = await request.json()
        data['user_id'] = user_id
        #!TODO зарефачить наверное на фронте в tags str -> []
        tags = data['tags'].split(',')
        data['tags'] = tags
        result = await self.storage.insert_bookmark(BookmarkSchema().load(data))
        return web.json_response({"status": "ok", "id": result})

    async def sandbox(self, request):
        user_id = await check_authorized(request)
        return web.json_response({"user": user_id})
