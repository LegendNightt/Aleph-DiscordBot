import discord
from discord.ext import commands
import bot as main

bot = discord.Client()
config = main.config

for command in config["simplecommands"]:

    class command(commands.Cog):

        @commands.command(aliases=[command])
        async def command(self, ctx):
            await ctx.send(config["simplecommands"][command])

    def setup(bot):
        bot.add_cog(command(bot))