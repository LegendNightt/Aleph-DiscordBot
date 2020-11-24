import discord
from discord.ext import commands
import os
import sys
import bot as main

bot = discord.Client()
config = main.config

class reload(commands.Cog):

    @commands.command(brief="`.reload` Restarts discord bot", aliases=['reload'])
    @commands.has_role(int(config["admin_role"]))
    async def reload(self, ctx):
        await ctx.send('Restarting...')
        python = sys.executable
        os.execl(python, python, *sys.argv)

def setup(bot):
    bot.add_cog(reload(bot))