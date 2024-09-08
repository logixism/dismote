import discord
from discord.ext import commands
from config import BOT_TOKEN, PREFIX


intents = discord.Intents.all()
bot = commands.Bot(command_prefix=PREFIX, intents=intents)


@bot.command()
async def stop_all(ctx):
    await bot.close()


@bot.event
async def on_ready():
    print(f"{bot.user.name} has connected to Discord!")

    await bot.load_extension("cogs.commands.media")
    await bot.load_extension("cogs.commands.power")
    await bot.load_extension("cogs.http")


bot.run(BOT_TOKEN)
