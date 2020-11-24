from discord.ext import commands
from googletrans import Translator

translator = Translator()

class autotranslator(commands.Cog):

    def __init__(self, bot):
        self.client = bot

    @commands.Cog.listener()
    async def on_message(self, ctx):
        msg = str(ctx.content)[2:]
        translation = translator.detect(msg)

        if translation.lang == 'en':
            spanishtrans = translator.translate(msg, dest='es')
            await ctx.send(spanishtrans)

        else:
            englishtrans = translator.translate(msg, dest='en')
            await ctx.send(englishtrans)

def setup(bot):
    bot.add_cog(autotranslator(bot))