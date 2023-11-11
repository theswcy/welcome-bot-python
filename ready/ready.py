import discord
from discord.ext import commands

class ready(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot
    @commands.Cog.listener()
    async def on_ready(self):
        await self.bot.change_presence(
            status=discord.Status.online
            , activity=discord.Activity(type=discord.ActivityType.playing, name = "Hay!"))
# "Hay!" is the name of the activity that the bot will appear

# commands setup
def setup(bot: commands.Bot):
    bot.add_cog(ready(bot))