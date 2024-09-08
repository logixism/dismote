import asyncio
from discord.ext import commands
from functions import media, power
from config import DEVICES
from quart import Quart, request, Response

app = Quart(__name__)

missing_req_arg = Response(
    status=400,
    content_type="application/json",
    response="Missing required argument.",
)


@app.route("/")
async def index():
    return "Hello World!"


@app.post("/power/shutdown")
async def shutdown():
    data = await request.get_json() or {}
    delay = data.get("delay", 0)
    power.shutdown(delay)

    return {"success": True}


@app.post("/power/restart")
async def restart():
    data = await request.get_json() or {}
    delay = data.get("delay", 0)
    power.restart(delay)

    return {"success": True}


@app.post("/power/lock")
async def lock():
    power.lock()

    return {"success": True}


@app.post("/power/rs_cancel")
async def rs_cancel():
    power.rs_cancel()

    return {"success": True}


@app.get("/media/volume")
async def get_volume():
    return {"success": True, "data": {"volume": media.get_volume()}}


@app.patch("/media/volume")
async def set_volume():
    data = await request.get_json() or {}
    volume = data.get("volume", None)
    if volume is None:
        return missing_req_arg
    media.set_volume(volume)

    return {"success": True}


@app.get("/media/sources/active")
async def get_active_source():
    return {"success": True, "data": media.get_active_device_data()}


@app.patch("/media/sources/active")
async def set_active_source():
    data = await request.get_json() or {}
    source = data.get("source", None)
    if source is None:
        return {"error": "No source provided"}
    if source not in DEVICES:
        return {"error": "Source not found"}
    media.set_active_device(DEVICES[source])

    return {"success": True}


class Http(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.bot.loop.create_task(self.run())

    async def run(self):
        await app.run_task(host="0.0.0.0", port=80)


async def setup(bot):
    await bot.add_cog(Http(bot))
