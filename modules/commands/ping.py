import discord
from discord.ext import commands

bot = discord.Client()

class ping(commands.Cog):

    @commands.command(brief="`.ping` Returns the bot's latency to discord", aliases=['ping'])
    async def ping(self, ctx):
        await ctx.send(f'pong {round(bot.latency * 1000)}ms')

def setup(bot):
    bot.add_cog(ping(bot))
