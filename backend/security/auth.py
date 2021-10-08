from aiohttp_security.abc import AbstractAuthorizationPolicy


class AuthZ(AbstractAuthorizationPolicy):
    def __init__(self, storage):
        self.storage = storage

    async def permits(self, identity, permission, context=None):
        pass

    async def authorized_userid(self, identity):
        # вернуть инфу по юзеру из базы - identity - логин/первичный ключ
        pass
