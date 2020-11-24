import discord
from discord.ext import commands
import bot as main

bot = discord.Client()
config = main.config

class member_join(commands.Cog):

    def __init__(self, bot):
        self.client = bot

    @commands.Cog.listener()
    async def on_member_join(self, member):
        embed = discord.Embed(title='FractalSMP', color=discord.Colour.orange())
        embed.set_thumbnail(url=(config["logo"]))
        embed.add_field(name='What are we?',
                        value='FractalSMP is a Technical and Decorative Minecraft Server.',
                        inline=False)
        embed.add_field(name='What are we searching for?',
                        value='We are working to reach a high level in the Minecraft Technical Community.',
                        inline=False)
        embed.add_field(name='What players are we looking for?',
                        value='We are looking for players who know about Technical or Decorative Minecraft, or just want '
                              'to spend a lot of time in the server crafting, farming, ...',
                        inline=False)
        embed.add_field(name='How can I enter?',
                        value='You need to send an access form, you can find it below.',
                        inline=False)
        embed.add_field(name='Bot commands help',
                        value='For bot commands help just type .help in #random',
                        inline=False)
        embed.add_field(name='Access Form: ',
                        value='https://bit.ly/fractalform',
                        inline=False)
        embed.add_field(name='Web:',
                        value='https://fractalsmp.com',
                        inline=False)
        embed.add_field(name='Twitter:',
                        value='https://twitter.com/fractalsmp',
                        inline=False)
        embed.add_field(name='Youtube: ',
                        value='https://bit.ly/YTFractal',
                        inline=False)
        await member.send(embed=embed)

    canal = bot.get_channel(config["join_channel"])
    await canal.send(
        'Welcome to FractalSMP ' + member.mention + ' we hope you will have a good time here! :smile: :partying_face: **check your '
                                                    'private messages for more information.** '
                                                    ':envelope_with_arrow: ')

def setup(bot):
    bot.add_cog(member_join(bot))
