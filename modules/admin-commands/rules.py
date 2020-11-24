import discord
from discord.ext import commands
import bot as main

bot = discord.Client()
config = main.config

class rules(commands.Cog):

    @commands.command(brief="`.rules` Displays options for rules commands", aliases=['rules'])
    @commands.has_role(int(config["admin_role"]))
    async def techservers(self, ctx, option=''):
        if option == '':
            await ctx.send(discord.Embed(title='Rules Options', description='display \n update\n',
                                         color=discord.Colour.orange()))
        else:

            def write_rules():

                # Spanish Rules
                embed = discord.Embed(
                    title='Normas del Servidor de Discord',
                    description="- No se tolerará el comportamiento tóxico entre las personas y hacia otros. (Esto incluye insultos, difamación, discriminación, críticas destructivas, etc).\n"
                                "- No está permitido solicitar roles.\n"
                                "- Cualquier tipo de Spam no será permitido.\n"
                                "- La acción de pingear a otras personas no estará permitida, exceptuando que estés en una conversación con esa persona.\n"
                                "- En #👤en-general (Inglés) o #👤es-general(Español), solo se hablará en el idioma que corresponde a ese canal.\n"
                                "- No está permitido hablar de temas que puedan generar controversia (Política, deporte, etc...).\n"
                                "- No estará permitido divulgar contenido que pueda dañar la sensibilidad de los otros. (Explicito, Gore, etc...).\n"
                                "- Insistir a los administradores una vez enviado el formulario no se permitirá.\n"
                                "- Si tienes alguna duda/problema abre un ticket en el canal de: #📨apply\n"
                                "\n"
                                "Dependiendo de la gravedad y la intensidad de la norma incumplida se verá que tipo de sanciones se aplicara en ese caso, entre los que se encuentran desde una simple advertencia al kickeo o baneo del usuario.\n",
                    color=discord.Colour.orange()
                )
                embed.set_thumbnail(url=config["logo"])
                await ctx.send(embed=embed)

                # English Rules
                embed = discord.Embed(
                    title='Discord Server Rules',
                    description="- Any toxic behaviour to someone or between people won't be allowed. (This includes insults, defamation, discrimation, etc...).\n"
                                "- Request roles is not allowed.\n"
                                "- Any kind of spam won't be allowed.\n"
                                "- Pinging someone is not allowed, except if you're talking with him/her.\n"
                                "- On #👤en-general (English) or #👤es-general(Spanish), you'll only talk with their respective languages.\n"
                                "- Talk about topics (Polític, sports, etc...) that could generate controversy is not allowed.\n"
                                "- Share content that could hurt other people sensibility (Like explicit, gore, etc...) is not allowed.\n"
                                "- Insist admins after you sent the application form won't be allowed.\n"
                                "- If you have any doubt/problem you can send a ticket in the channel: #📨apply.\n"
                                "\n"
                                "Depending on the severity or the intensity of the infringed rule, it will be the kind of punishment that will apply. It goes from a simple warning to a kick or ban of the user.",
                    color=discord.Colour.orange()
                )
                embed.set_thumbnail(url=config["logo"])
                await ctx.send(embed=embed)

            if option == 'display':
                write_rules()
            elif option == 'update':
                await ctx.channel.purge(limit=2)
                write_rules()
            else:
                await ctx.send('Invalid option')

def setup(bot):
    bot.add_cog(rules(bot))
