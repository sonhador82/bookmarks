
from aiohttp import web, log
from aiohttp_security import remember, forget

from data.auth import check_credentials
from data.mongo import MongoStorage


class AuthHandler:
    def __init__(self, data_storage: MongoStorage):
        self.storage = data_storage

    async def signin(self, request: web.Request):
        response = web.HTTPFound('/')
        data = await request.json()
        log.web_logger.debug(data)
        if await check_credentials(self.storage, data['email'], data['password']):
            await remember(request, response, data['email'])
            return web.HTTPFound("/")
        return web.HTTPForbidden()

    async def signout(self, request: web.Request):
        resp = web.Response()
        await forget(request, resp)
        return resp
