import logging

import aioredis
from aiohttp import web, log
from aiohttp.web_request import Request
from aiohttp_session import get_session, setup as session_setup, session_middleware
from aiohttp_session.redis_storage import RedisStorage
from aiohttp_session import SimpleCookieStorage
from aiohttp_security import check_permission, remember, setup as security_setup, SessionIdentityPolicy
import aiohttp_cors


from data.mongo import MongoStorage
from data.bookmark import BookmarkSchema
from data.auth import check_credentials
from security.auth import AuthZ

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



### auth
async def login_handler(request: Request):
    session = await get_session(request)
    print(session)
    response = web.HTTPFound('/')
    data = await request.json()
    log.web_logger.debug(data)
    storage = MongoStorage(MONGO_URL, 'BookMark', 'bookmarks')
    if await check_credentials(storage, data['email'], data['password']):
        await remember(request, response, data['email'])
        return web.HTTPFound("/")
    return web.HTTPForbidden()


async def user_handler(request: Request):
    await check_permission(request, 'admin')
    return web.json_response(status=200, data={"created": "ok"})


async def sandbox_handler(request: Request):
    # session = await get_session(request)
    # session["puss"] = "test"
    storage = MongoStorage(MONGO_URL, 'BookMark', 'bookmarks')
    response = web.HTTPOk()
    data = await request.json()

    if await check_credentials(storage, data['email'], data['password']):
        await remember(request, response, data['email'])
        return web.HTTPFound("/")

    return web.Response(text="hello world")
    #return web.json_response(status=200, data={"status": "ok", "session": session.__dict__})


async def create_app():
    redis_pool = await aioredis.create_pool('redis://127.0.0.1:6379')
    session_storage = RedisStorage(redis_pool)

    app = web.Application()
    app.add_routes(
        [
            web.post('/bookmark', bookmark_handler),
            web.post('/auth/login', login_handler),
            web.post('/auth/user', user_handler),
            web.get('/sandbox', sandbox_handler),
            web.post('/sandbox', sandbox_handler)
        ]
    )

    # fernet_key = fernet.Fernet.generate_key()
    # secret_key = base64.urlsafe_b64decode(fernet_key)
    # session_setup(app, EncryptedCookieStorage(secret_key))

    session_setup(app, session_storage)
    security_setup(app, SessionIdentityPolicy(), AuthZ(MongoStorage(MONGO_URL, 'BookMark', 'bookmarks')))

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
    web.run_app(create_app())