import discord
from discord.ext import commands
from utils.bot import bot

class welcome(commands.Cog):
    def __init__(self, baby: commands.Bot) -> None:
        self.baby = baby

    @bot.event
    async def on_member_join(member):
# "CHANNEL_ID" is the id of channel that the bot will send message.
        channel_id = "CHANNEL_ID"
        channel = bot.get_channel(channel_id)
# "{member.mention}" is the mention of the new member."
        embed = discord.Embed(
            title = "Title", # This is the title of the embed.
            description = f"Description" # This is the description of the embed.
            )
        # This is the field that will appear in the embed. If you don´t want this, just remove it.
        embed.add_field(
            name = "Name", # This is the title of the field.
            value = "Description", # This is the description of the field.
            inline = False
            )
        embed.set_footer(
            text = "Text" # This is the text that will appear on the embed. If your don´t want this, just remove it.
            )
        embed.set_thumbnail(
            url = member.avatar # URL of the member's icon. If you want to use your server´s icon, just change the (member.avatar) to ("YOUR_SERVER_ICON_URL").
            )
        embed.color = discord.Color(
            int(
                'ffffff', 16 # "ffffff" is the color WHITE, the color that will appear in the embed message. Use HEXA COLORS to change the color.
                )
            )
        await channel.send(
            content = f"Welcome {member.mention}!", # This is the non-embed message that the bot will send with the embed.
            embed = embed
            )

# [ WARNING ] this is the DELETE WELCOME MESSAGE EVENT, If you don't want this command, just delete it.
    @bot.event
    async def on_member_remove(member):
# "CHANNEL_ID" is the id of channel that the bot will delete message.
        channel_id = "CHANNEL_ID"
        channel = bot.get_channel(channel_id)
        messages = await channel.history().flatten()
        for message in messages:
            if message.author == bot.user and f'Welcome {member.mention}!' in message.content:
                await message.delete()

# command setup
def setup(bot: commands.Bot):
    bot.add_cog(welcome(bot))