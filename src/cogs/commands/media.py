import discord
from config import DEVICES
from discord.ext import commands
from functions.media import get_volume, set_volume, set_active_device, get_active_device_data

class Media(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    

    # /// Volume commands /// #

    @commands.group(name="volume")
    async def volume(self, ctx: commands.Context):
        pass

    @volume.command(name="get")
    async def volume_get(self, ctx: commands.Context):
        await ctx.send(
            embed = discord.Embed(
                title = "Volume",
                description = f"Current volume is {get_volume()}%",
                color = discord.Color.blurple()
            )
        )

    @volume.command(name="set")
    async def volume_set(self, ctx: commands.Context, volume: float):
        set_volume(volume)
    

    # /// Sources commands /// #

    @commands.group(name = "sources")
    async def sources(self, ctx: commands.Context):
        pass

    @sources.command(name = "get_active_data")
    async def sources_get_active_data(self, ctx: commands.Context):
        embed = discord.Embed(title = "Current audio device", color = discord.Color.blurple())

        for key, value in get_active_device_data().items():
            embed.add_field(name=key,value=value,inline=False)

        await ctx.send(embed=embed)

    @sources.command(name = "set_active")
    async def sources_set_active(self, ctx: commands.Context, device: str):
        device_id = DEVICES.get(device.lower(), None)
        if not device_id:
            await ctx.send('device not found')
            return
        
        set_active_device(device_id)

        embed = discord.Embed(title = "Audio device set", description = f"Device set to {device}", color = discord.Color.blurple())
        await ctx.send(embed=embed)


async def setup(bot):
    await bot.add_cog(Media(bot))
