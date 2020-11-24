import discord
from discord.ext import commands
from googletrans import Translator

translator = Translator()

class disctranslator(commands.Cog):

    def __init__(self, bot):
        self.client = bot

    @commands.Cog.listener()
    async def on_message(self, ctx):
        if str(ctx.content).startswith('t '):
            msg = str(ctx.content)[2:]
            translation = translator.detect(msg)

            if translation.lang == 'en':
                spanishtrans = translator.translate(msg, dest='es')

                embed = discord.Embed(title='Spanish Translator', color=discord.Colour.green())
                embed.add_field(name='english', value=msg, inline=True)
                embed.add_field(name='spanish', value=spanishtrans.text, inline=True)
                await ctx.channel.send(embed=embed)

            else:
                englishtrans = translator.translate(msg, dest='en')

                embed = discord.Embed(title='English Translator', color=discord.Colour.green())
                embed.add_field(name='spanish', value=msg, inline=True)
                embed.add_field(name='english', value=englishtrans.text, inline=True)
                await ctx.channel.send(embed=embed)

def setup(bot):
    bot.add_cog(disctranslator(bot))
