import logging

import aioredis
from aiohttp import web, log
from aiohttp.web_request import Request
from aiohttp_session import get_session, setup as session_setup
from aiohttp_session.redis_storage import RedisStorage
from aiohttp_session import SimpleCookieStorage
import aiohttp_cors

from data.mongo import MongoStorage
from data.bookmark import BookmarkSchema

logging.basicConfig(level=logging.DEBUG)

MONGO_URL="mongodb://localhost"

async def bookmark_handler(request: Request):
    data = await request.json()
    tags = data['tags'].split(',')
    data['tags'] = tags
    storage = MongoStorage(MONGO_URL, 'BookMark', 'bookmarks')
    result = await storage.insertBookmark(BookmarkSchema().load(data))
    print(result)
    return web.json_response({"status": "ok", "id": result})


async def show_bookmarks(request: Request):
    session = await get_session(request)
    log.web_logger.debug(session)
    if 'isAuth' in session:
        if session['isAuth']:
            log.web_logger.debug("ACCESS GRANTED, show bookmarks")
            return web.json_response({"bookmarks": ["1"]})
    raise web.HTTPForbidden()


    # global collection
    # cursor = collection.find()
    # print(await collection.count_documents(filter={}))
    # async for doc in cursor:
    #     print(doc)


async def login_handler(request: Request):
    data = await request.json()
    log.web_logger.debug(data)
    if data['username'] == 'one@sonhador.ru' and data['password'] == '123':
        session = await get_session(request)
        session['isAuth'] = True
        return web.json_response({"status": "ok"})
    return web.json_response(status=403)


async def make_app():
    app = web.Application()
    app.add_routes(
        [
            web.post('/bookmark', bookmark_handler),
            web.post('/login', login_handler)
        ]
    )

    # fernet_key = fernet.Fernet.generate_key()
    # secret_key = base64.urlsafe_b64decode(fernet_key)
    # session_setup(app, EncryptedCookieStorage(secret_key))
    redis_pool = await aioredis.create_pool('redis://127.0.0.1:6379')
    session_setup(app, RedisStorage(redis_pool))

    cors = aiohttp_cors.setup(app, defaults={
        "*": aiohttp_cors.ResourceOptions(
            allow_credentials=True,
            expose_headers="*",
            allow_headers="*"
        )
    })
    for route in list(app.router.routes()):
        cors.add(route)
    return app


if __name__ == '__main__':
    web.run_app(make_app())