import discord
from discord.ext import commands
import json
import os

with open("utils/config.json", "r", encoding = "UTF-8") as f:
  configData = json.load(f)

intents = discord.Intents.default()
intents.message_content = True
intents.members = True
bot = commands.Bot(intents = intents)

for filename in os.listdir("./ready"):
  if filename.endswith(".py") and not filename.startswith("__"):
    bot.load_extension("ready.{0}".format(filename[:-3]))
for filename in os.listdir("./commands"):
  if filename.endswith(".py") and not filename.startswith("__"):
    bot.load_extension("commands.{0}".format(filename[:-3]))
    
@bot.event
async def on_ready():
  print("bot ready!")