import logging

import aiohttp_cors
import aioredis
from aiohttp import web
from aiohttp_security import setup as security_setup, SessionIdentityPolicy
from aiohttp_session import setup as session_setup
from aiohttp_session.redis_storage import RedisStorage

from data.mongo import MongoStorage
from rest.auth import AuthHandler
from rest.bookmarks import BookmarkHandler
from security.auth import AuthZ

logging.basicConfig(level=logging.DEBUG)

MONGO_URL = "mongodb://localhost"


async def create_app():
    redis_pool = await aioredis.create_pool('redis://127.0.0.1:6379')
    session_storage = RedisStorage(redis_pool)
    data_storage = MongoStorage(MONGO_URL, 'BookMark', 'bookmarks')
    app = web.Application()

    authHandler = AuthHandler(data_storage)
    bookMarkHandler = BookmarkHandler(data_storage)
    app.add_routes(
        [
            web.post('/auth/signin', authHandler.signin),
            web.get('/auth/signout', authHandler.signout),
            web.get('/api/bookmarks/{b_id:\w+}', bookMarkHandler.get),
            web.get('/api/bookmarks', bookMarkHandler.list),
            web.post('/api/bookmarks', bookMarkHandler.create),
            web.get('/sandbox', bookMarkHandler.sandbox)
        ]
    )

    session_setup(app, session_storage)
    security_setup(app, SessionIdentityPolicy(),
                   AuthZ(MongoStorage(MONGO_URL, 'BookMark', 'bookmarks')))

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
