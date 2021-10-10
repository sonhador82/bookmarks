from aiohttp_security.abc import AbstractAuthorizationPolicy


class AuthZ(AbstractAuthorizationPolicy):
    def __init__(self, storage):
        self.storage = storage

    async def permits(self, identity, permission, context=None):
        pass

    async def authorized_userid(self, identity):
        user_id = await self.storage.find_user_by_email(identity)
        if user_id:
            return user_id.email
