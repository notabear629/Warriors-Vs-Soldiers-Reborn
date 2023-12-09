#Requirement Imports
import discord
from discord.ext import commands
import os
from dotenv import load_dotenv

#Imports from other .py files

#Import Embed Builder Functions
from embedBuilder import embedBuilder

#Import the gameObjects
from gameObjects.Lobby import Lobby

from gameFunctions.lobbyFunctions import lobbyFunctions

intents = discord.Intents.all()
intents.members = True

load_dotenv()

BOT_TOKEN = os.getenv('BOT_TOKEN')
prefix = os.getenv('BOT_PREFIX')
HOME_ID = int(os.getenv('BOT_HOME_CHANNEL_ID'))

client = discord.Client(intents=intents)
client = commands.Bot(command_prefix = prefix, intents = intents, help_command = None, case_insensitive=True)

def resetFunction():
    global currentLobby
    if 'currentLobby' in globals():
        del currentLobby

@client.event
async def on_ready():
    global home
    global noMentions, withMentions
    home = client.get_channel(HOME_ID)
    noMentions = discord.AllowedMentions(everyone=False, users=False, roles=False, replied_user=False)
    withMentions = discord.AllowedMentions(everyone=True, users=True, roles=True, replied_user=True)
    print(f"Bot Online, watching Channel {home.name}")

@client.command('reset')
async def reset(ctx):
    if home == ctx.channel:
        if 'currentLobby' in globals():
            resetFunction()
            embed = await embedBuilder.buildReset(prefix)
            await home.send(embed=embed)
        else:
            await home.send('There is no lobby to reset.')

@client.command('host')
async def host(ctx):
    global currentLobby
    lobbyPassed = None
    if 'currentLobby' in globals():
        lobbyPassed = currentLobby
    functionCall = await lobbyFunctions.host(ctx, lobbyPassed, prefix, noMentions, home)
    if type(functionCall) == Lobby:
        currentLobby = functionCall

@client.command('join')
async def join(ctx):
    lobbyPassed = None
    if 'currentLobby' in globals():
        lobbyPassed = currentLobby
    await lobbyFunctions.join(ctx, lobbyPassed, prefix, noMentions, home)

@client.command('leave')
async def leave(ctx):
    lobbyPassed = None
    if 'currentLobby' in globals():
        lobbyPassed = currentLobby
    await lobbyFunctions.leave(ctx, lobbyPassed, prefix, noMentions, home)

@client.command('kick')
async def kick(ctx, kicked:discord.Member=None):
    lobbyPassed = None
    if 'currentLobby' in globals():
        lobbyPassed = currentLobby
    await lobbyFunctions.kick(ctx, lobbyPassed, prefix, noMentions, home, kicked)

@client.command('kickall')
async def kickall(ctx):
    lobbyPassed = None
    if 'currentLobby' in globals():
        lobbyPassed = currentLobby
    await lobbyFunctions.kickAll(ctx, lobbyPassed, prefix, noMentions, home)


client.run(BOT_TOKEN)
