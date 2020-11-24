import discord
from discord.ext import commands
import json
import os

# Author: LegendNightt
# Special thanks to iDarkLightning, and his LiteBot code

with open("config.json") as json_file:
    config = json.load(json_file)

bot = commands.Bot(command_prefix=config["prefix"])


@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Game(name='.help'))
    channel = bot.get_channel(config["bot_channel"])
    await channel.send('DiscordBot ON!')
    print(bot.user.name + ' initiated correctly :D')


for filename in os.listdir('sys'):
    if os.path.isfile(f'sys/{filename}') and filename.endswith('.py'):
        bot.load_extension(f'sys.{filename[:-3]}')

for filename in os.listdir('modules'):
    if os.path.isfile(f'modules/{filename}') and filename.endswith('.py'):
        bot.load_extension(f'modules.{filename[:-3]}')


@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CheckFailure):
        await ctx.send("Insufficient permissions for executing this command")
    elif isinstance(error, commands.CommandInvokeError):
        await ctx.send("This command wasn't used correctly")
    else:
        raise error


bot.run(config["token"])
