import discord
from discord.ext import commands
import requests

bot = discord.Client()

class avatar(commands.Cog):

    @commands.command(brief="`.avatar` Gets the pfp from a discord user", aliases=['avatar'])
    async def avatar(self, ctx):
        with requests.get(ctx.message.mention.avatar_url) as r:
            img_data = r.content
        with open('image_name.jpg', 'wb') as handler:
            handler.write(img_data)

def setup(bot):
    bot.add_cog(avatar(bot))