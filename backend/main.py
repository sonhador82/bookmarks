from aiohttp import web
from aiohttp.web_request import Request
import aiohttp_cors

import motor.motor_asyncio

client = motor.motor_asyncio.AsyncIOMotorClient()
db = client.sandbox
collection = db.bookmarks


async def bookmark_handler(request: Request):
    global collection
    data = await request.json()
    tags = data['tags'].split(',')
    data['tags'] = tags
    await collection.insert_one(data)
    return web.json_response({"status": "ok"})

app = web.Application()


cors = aiohttp_cors.setup(app)
resource = cors.add(app.router.add_resource("/bookmark"))

route = cors.add(
    resource.add_route("POST", bookmark_handler),
    {
        "*": aiohttp_cors.ResourceOptions(
            allow_credentials=True,
            allow_headers="*",
            expose_headers="*"
        )
    }
)


if __name__ == '__main__':
    web.run_app(app)