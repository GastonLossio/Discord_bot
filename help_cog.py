import discord
from discord.ext import commands

class help_cog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.help_message = """
```
General commands:
+help - Muestra los comandos disponibles
+p <keywords> - Reproduce la cancion de YouTube
+q - Despliega la cola de reproduccion
+skip - Salta la cancion actual
+clear - Borra la cola de reproduccion entera
+leave - Abandona el canal de voz
+pause - Pone pausa a la cancion 
+resume - Continua con la reproduccion de la cancion
```
"""
        self.text_channel_list = []

    #some debug info so that we know the bot has started
    @commands.Cog.listener()
    async def on_ready(self):
        for guild in self.bot.guilds:
            for channel in guild.text_channels:
                self.text_channel_list.append(channel)

        await self.send_to_all(self.help_message)

    @commands.command(name="help", help="Muestra los comandos disponibles")
    async def help(self, ctx):
        await ctx.send(self.help_message)

    async def send_to_all(self, msg):
        for text_channel in self.text_channel_list:
            await text_channel.send(msg)