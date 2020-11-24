import discord
from discord.ext import commands
import requests
import json
import bot as main
import datetime
from datetime import datetime
import re

bot = discord.Client()
config = main.config


class status(commands.Cog):

    def __init__(self, bot):
        self.client = bot

    @commands.command(brief="`.status` Display server status and players online", aliases=['status'])
    @commands.has_role(int(config["member_role"]))
    async def status(self, ctx, server_name=''):
        server_name.lower()
        if server_name == '':
            await ctx.send('Available Options: survival, creative, mirror, total')
        else:

            # get_status def by iDarkLightning
            def get_status(server):
                try:
                    status = requests.get(f'https://api.mcsrvstat.us/2/ '
                                          f'{config["minecraft_servers"][server]["server_ip"]}')
                    json_data = status.json()
                except KeyError:
                    await ctx.send(server + 'is not a valid option')
                else:
                    online = json_data["online"]
                    if online:
                        embed = discord.Embed(
                            title=f'{ctx.message.guild} {server.upper()} Status', color=0x32CD32,
                            timestamp=datetime.utcnow())
                        online = 'Online'
                        online_players = json_data["players"]["online"]
                        max_players = json_data["players"]["max"]
                        embed.add_field(name="Status", value=online)
                        embed.add_field(name="Players Online",
                                        value=f'{online_players}/{max_players}')
                        if int(online_players) > 0:
                            players_online = re.sub(r'\s([?,!"](?:\s|$))', r'\1',
                                                    str(json_data["players"]["list"]).translate(
                                                        {ord(c): " " for c in "!@#$%^&*()[]{};:'./<>?\|`~-=+"}).replace(
                                                        "_", "\_"))
                            embed.add_field(name="Online Players", value=(
                                players_online), inline=False)
                        embed.set_thumbnail(url=f'{config["server_logo"]}')
                        embed.set_footer(text=f'{ctx.message.guild}')
                        await ctx.send(embed=embed)
                    if not online:
                        embed = discord.Embed(
                            title=f'{ctx.message.guild} {server.upper()} Status', color=0xFF0000,
                            timestamp=datetime.utcnow())
                        online = 'Offline'
                        embed.add_field(name="Status", value=(online))
                        embed.set_thumbnail(url=f'{config["server_logo"]}')
                        embed.set_footer(text=f'{ctx.message.guild}')
                        await ctx.send(embed=embed)

            if server_name == 'total':
                get_status('survival')
                get_status('creativebuild')
                get_status('creativereds')
                get_status('mirror')

            else:
                get_status(server_name)

def setup(bot):
    bot.add_cog(status(bot))
