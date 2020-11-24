import discord
from discord.ext import commands
import bot as main

bot = discord.Client()
config = main.config

class poll(commands.Cog):

    @commands.command(brief="`.poll` Create a simple discord poll", aliases=['poll'])
    @commands.has_role(int(config["member_role"]))
    async def poll(self, ctx, message='', option1='', option2=''):
        if message == '':
            await ctx.send('Please, specify a theme')

        elif (option1 != '') and (option2 == ''):
            await ctx.send('Please, specify option 2')

        elif (option2 != '') and (option1 == ''):
            await ctx.send('Please, specify option 1')

        elif (option1 != '') and (option2 != ''):
            lines = '▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔'
            embed = discord.Embed(title='Question:\n' + message + '\n' + lines, color=discord.Colour.gold())
            embed.add_field(name='1º option', value='1\u20e3 ' + option1, inline=False)
            embed.add_field(name='2º option', value='2\u20e3 ' + option2, inline=False)
            sent = await ctx.send(embed=embed)
            await sent.add_reaction('1\u20e3')
            await sent.add_reaction('2\u20e3')

        else:
            lines = '▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔'
            embed = discord.Embed(title='Question:\n' + message + '\n' + lines, color=discord.Colour.gold())
            embed.add_field(name='1º option', value=(config["poll"]["yes_emote"]) + ' Yes', inline=False)
            embed.add_field(name='2º option', value=(config["poll"]["no_emote"]) + ' No', inline=False)
            sent = await ctx.send(embed=embed)
            await sent.add_reaction(config["poll"]["yes_emote"])
            await sent.add_reaction(config["poll"]["no_emote"])

def setup(bot):
    bot.add_cog(poll(bot))
