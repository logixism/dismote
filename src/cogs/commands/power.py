import discord
from discord.ext import commands
from functions.power import shutdown, restart, lock, rs_cancel

class Power(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command(name="shutdown")
    async def shutdown(self, ctx, delay: int = 0):
        result = shutdown(delay)
        embed = discord.Embed(title = "Shutdown", description = f"Shutting down in {delay} seconds", color = discord.Color.blurple())
        embed.set_footer(text = f"Return code {result.returncode}")
        await ctx.send(embed=embed)

    @commands.command(name="restart")
    async def restart(self, ctx, delay: int = 0):
        result = restart(delay)
        embed = discord.Embed(title = "Restart", description = f"Restarting in {delay} seconds", color = discord.Color.blurple())
        embed.set_footer(text = f"Return code {result.returncode}")
        await ctx.send(embed=embed)

    @commands.command(name="lock")
    async def lock(self, ctx):
        lock()
        embed = discord.Embed(title = "Lock", description = "Computer locked!", color = discord.Color.blurple())
        embed.set_footer(text = f"Return code 0")
        await ctx.send(embed=embed)

    @commands.command(name="rs_cancel")
    async def rs_cancel(self, ctx):
        result = rs_cancel()
        embed = discord.Embed(title = "Shutdown/restart", description = "Shutdown/restart cancelled", color = discord.Color.blurple())
        embed.set_footer(text = f"Return code {result.returncode}")
        await ctx.send(embed=embed)
    

async def setup(bot):
    await bot.add_cog(Power(bot))
