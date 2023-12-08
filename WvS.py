import discord
from discord.ext import commands
import os
from dotenv import load_dotenv

intents = discord.Intents.all()
intents.members = True

load_dotenv()

BOT_TOKEN = os.getenv('BOT_TOKEN')
PREFIX = os.getenv('BOT_PREFIX')

client = discord.Client(intents=intents)
client = commands.Bot(command_prefix = PREFIX, intents = intents, help_command = None, case_insensitive=True)

@client.event
async def on_ready():
    print('Bot Online')

client.run(BOT_TOKEN)
