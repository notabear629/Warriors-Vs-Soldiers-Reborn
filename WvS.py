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
from gameObjects.Theme import Theme

#Import the gameFunctions
from gameFunctions.lobbyFunctions import lobbyFunctions

#Import the dataFunctions
from dataFunctions.userInfoManager import userInfoManager

intents = discord.Intents.all()
intents.members = True

load_dotenv()

BOT_TOKEN = os.getenv('BOT_TOKEN')
prefix = os.getenv('BOT_PREFIX')
HOME_ID = int(os.getenv('BOT_HOME_CHANNEL_ID'))
HOME_SERVER_ID = int(os.getenv('BOT_HOME_SERVER_ID'))
USER_CHANNEL_CATEGORY_ID = int(os.getenv('BOT_USER_CHANNEL_CATEGORY_ID'))

client = discord.Client(intents=intents)
client = commands.Bot(command_prefix = prefix, intents = intents, help_command = None, case_insensitive=True)

def resetFunction():
    global currentLobby
    if 'currentLobby' in globals():
        del currentLobby

@client.event
async def on_ready():
    global home, homeServer, userCategory
    global noMentions, withMentions
    global currentTheme
    home = client.get_channel(HOME_ID)
    homeServer = client.get_guild(HOME_SERVER_ID)
    userCategory = client.get_channel(USER_CHANNEL_CATEGORY_ID)
    noMentions = discord.AllowedMentions(everyone=False, users=False, roles=False, replied_user=False)
    withMentions = discord.AllowedMentions(everyone=True, users=True, roles=True, replied_user=True)
    currentTheme = Theme()
    print(f"Bot Online\nOn Server {homeServer.name}\nHome Channel At {home.name}\nUser Category at {userCategory.name}")

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
    await userInfoManager.userRegistration(ctx, ctx.message.author, homeServer, userCategory, currentTheme, prefix)
    functionCall = await lobbyFunctions.host(ctx, lobbyPassed, currentTheme, prefix, noMentions, home)
    if type(functionCall) == Lobby:
        currentLobby = functionCall

@client.command('join')
async def join(ctx):
    lobbyPassed = None
    if 'currentLobby' in globals():
        lobbyPassed = currentLobby
    await userInfoManager.userRegistration(ctx, ctx.message.author, homeServer, userCategory, currentTheme, prefix)
    await lobbyFunctions.join(ctx, lobbyPassed, currentTheme, prefix, noMentions, home)

@client.command('leave')
async def leave(ctx):
    lobbyPassed = None
    if 'currentLobby' in globals():
        lobbyPassed = currentLobby
    await lobbyFunctions.leave(ctx, lobbyPassed, currentTheme, prefix, noMentions, home)

@client.command('kick')
async def kick(ctx, kicked:discord.Member=None):
    lobbyPassed = None
    if 'currentLobby' in globals():
        lobbyPassed = currentLobby
    await lobbyFunctions.kick(ctx, lobbyPassed, currentTheme, prefix, noMentions, home, kicked)

@client.command('kickall')
async def kickall(ctx):
    lobbyPassed = None
    if 'currentLobby' in globals():
        lobbyPassed = currentLobby
    await lobbyFunctions.kickAll(ctx, lobbyPassed, currentTheme, prefix, noMentions, home)

@client.command('lobby')
async def lobby(ctx):
    if 'currentGame' in globals():
        pass
    else:
        if 'currentLobby' in globals():
            embed = await embedBuilder.buildLobby(currentLobby, currentTheme, prefix)
            await home.send(embed=embed, allowed_mentions=noMentions)
        else:
            await ctx.send(f'There is no lobby! Use `{prefix}host` from within <#{home.id}> to create one.')

@client.command('color')
async def color(ctx, *, colorInput=None):
    await userInfoManager.userRegistration(ctx, ctx.message.author, homeServer, userCategory, currentTheme, prefix)
    await userInfoManager.changeColor(ctx, ctx.message.author, homeServer, colorInput)

@client.command('colour')
async def colour(ctx, *, colorInput=None):
    await userInfoManager.userRegistration(ctx, ctx.message.author, homeServer, userCategory, currentTheme, prefix)
    await userInfoManager.changeColor(ctx, ctx.message.author, homeServer, colorInput)

@client.command('renamechannel')
async def renamechannel(ctx, *, channelName=None):
    await userInfoManager.userRegistration(ctx, ctx.message.author, homeServer, userCategory, currentTheme, prefix)
    await userInfoManager.changeChannelName(ctx, client, ctx.message.author, homeServer, channelName)

@client.command('renamerole')
async def renamerole(ctx, *, roleName=None):
    await userInfoManager.userRegistration(ctx, ctx.message.author, homeServer, userCategory, currentTheme, prefix)
    await userInfoManager.changeRoleName(ctx, ctx.message.author, homeServer, roleName)

@client.command('fixme')
async def fixme(ctx):
    await userInfoManager.userRegistration(ctx, ctx.message.author, homeServer, userCategory, currentTheme, prefix)
    await userInfoManager.fixUser(ctx, client, ctx.message.author, homeServer, userCategory, currentTheme, prefix)


client.run(BOT_TOKEN)
