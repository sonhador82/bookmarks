
from aiohttp import web, log
from aiohttp_session import get_session
from aiohttp_security import remember

from data.mongo import MongoStorage
from data.auth import check_credentials


class AuthHandler:
    def __init__(self, data_storage: MongoStorage):
        self.storage = data_storage

    async def signin(self, request: web.Request):
        # session = await get_session(request)
        # print(session)
        response = web.HTTPFound('/')
        data = await request.json()
        log.web_logger.debug(data)
        if await check_credentials(self.storage, data['email'], data['password']):
            await remember(request, response, data['email'])
            return web.HTTPFound("/")
        return web.HTTPForbidden()


    # def signout(self, request: web.Request):
    #     pass
    #
    # async def signup_handler(request: Request):
    #     await check_permission(request, 'admin')
    #     return web.json_response(status=200, data={"created": "ok"})
