import discord
from discord.ext import commands
import bot as main

bot = discord.Client()
config = main.config

class techservers(commands.Cog):

    @commands.command(brief="`.techservers` Displays options for techservers commands", aliases=['techservers'])
    @commands.has_role(int(config["admin_role"]))
    async def techservers(self, ctx, option=''):
        if option == '':
            await ctx.send(discord.Embed(title='TechServers Options', description='display \n update\n',
                                         color=discord.Colour.orange()))
        else:

            def write_techservers():
                embed = discord.Embed(title='SMP Tech Servers', color=discord.Colour.orange())
                embed.set_thumbnail(url=config["logo"])
                embed.add_field(name=u'\u2063',
                                value='<:SciCraft:759730879400116225> [SciCraft](http://discord.gg/SciCraft)',
                                inline=True)
                embed.add_field(name=u'\u2063',
                                value='<:TIS:747821310863868015> [TIS](https://discord.gg/Qqy263x)',
                                inline=True)
                embed.add_field(name=u'\u2063',
                                value='<a:HammerSMP:747821029098782770> [Hammer](https://discord.gg/QMuwbqa)',
                                inline=True)
                embed.add_field(name=u'\u2063',
                                value='<:Hekate:747821039119106057> [Hekate](https://discord.gg/sfCkZDA)',
                                inline=True)
                embed.add_field(name=u'\u2063',
                                value='<a:Bismuth:759731751500251146> [Bismuth](https://discord.gg/za4ftxk)',
                                inline=True)
                embed.add_field(name=u'\u2063',
                                value='<:Dugged:747881134293254304> [Dugged](https://discord.gg/ah7Ftxd)',
                                inline=True)
                embed.add_field(name=u'\u2063',
                                value='<a:Hypnos:759731208007057428> [Hypnos](https://discord.gg/BKadJsM)',
                                inline=True)
                embed.add_field(name=u'\u2063',
                                value='<:Mechanists:747821180987244665> [Mechanists](https://discord.gg/c2DUWG8)',
                                inline=True)
                embed.add_field(name=u'\u2063',
                                value='<:EndTech:747821018281934878> [EndTech](https://discord.gg/admD8Qg)',
                                inline=True)
                embed.add_field(name=u'\u2063',
                                value='<:ProjectCBW:747821244845391956> [ProjectCBW](https://discord.gg/bR34wGa)',
                                inline=True)
                embed.add_field(name=u'\u2063',
                                value='<:TRC:747881134175551579> [TaiwanRC](https://discord.gg/q2TsYsD)',
                                inline=True)
                embed.add_field(name=u'\u2063',
                                value='<a:Techiberia:759730832469393408> [TechIberia](https://discord.gg/WrUy8RY)',
                                inline=True)
                embed.add_field(name=u'\u2063',
                                value='<a:MelonTech:747821193893118023> [MelonTech](https://discord.gg/99VW52r)',
                                inline=True)
                embed.add_field(name=u'\u2063',
                                value='<:Bobbycraft:747881134196654273> [BobbyCraft](https://discord.gg/W6tu4Vx)',
                                inline=True)
                embed.add_field(name=u'\u2063',
                                value='<:Lunaar:759730310618677269> [Lunaar](https://discord.gg/XTGKqah)',
                                inline=True)
                embed.add_field(name=u'\u2063',
                                value='<:LiteTech:764870963346669568> [LiteTech](https://discord.gg/3C7TYkp)',
                                inline=True)
                embed.add_field(name=u'\u2063',
                                value='<:CactusHug:764876943782182962> [CactusHug](https://discord.gg/8A8yEjm)',
                                inline=True)
                embed.add_field(name=u'\u2063',
                                value='<:Otium:764877010249842738> [Otium](https://discord.gg/cCYT9sj)',
                                inline=True)
                await ctx.send(embed=embed)

                embed = discord.Embed(title='Public Community Tech Servers', color=discord.Colour.orange())
                embed.set_thumbnail(url=config["logo"])
                embed.add_field(name=u'\u2063',
                                value='<:TMC:747821323094327397> [TMC](https://discord.gg/CM52CAH)',
                                inline=True)
                embed.add_field(name=u'\u2063',
                                value='<a:Monkeys:759727261049552897> [Monkeys](https://discord.gg/tmkV6zK)',
                                inline=True)
                embed.add_field(name=u'\u2063',
                                value='<:TechMCarchive:747821292794806344> [TechMCArchiv](https://discord.gg/V862pvq)',
                                inline=True)
                embed.add_field(name=u'\u2063',
                                value='<:EigenCraft:747820977618157669> [EigenCraft](https://discord.gg/qV4EsTp)',
                                inline=True)
                embed.add_field(name=u'\u2063',
                                value='<:Mojira:747821211094089799> [Mojira](https://discord.gg/rpCyfKV)',
                                inline=True)
                embed.add_field(name=u'\u2063',
                                value='<:JellySquid:759730061766295552> [JellySquid](https://discord.com/invite/dQkmETa)',
                                inline=True)
                embed.add_field(name=u'\u2063',
                                value='<:Ironlovers:747821132568199249> [IronLovers](https://discord.gg/gPecfY3)',
                                inline=True)
                embed.add_field(name=u'\u2063',
                                value='<:ORE:747821263334015039> [ORE](https://discord.com/invite/zjWRarN)',
                                inline=True)
                embed.add_field(name=u'\u2063',
                                value='<:StorageTech:759732443452014612> [StorageTech](https://discord.gg/JufJ6uf)',
                                inline=True)
                await ctx.send(embed=embed)

            if option == 'display':
                write_techservers()
            elif option == 'update':
                await ctx.channel.purge(limit=2)
                write_techservers()
            else:
                await ctx.send('Invalid option')

def setup(bot):
    bot.add_cog(techservers(bot))