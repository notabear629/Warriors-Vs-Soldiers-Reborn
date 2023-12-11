#Requirement Imports
import discord
from discord.ext import commands
import os
from dotenv import load_dotenv
from scipy.special import comb

#Imports from other .py files

#Import Embed Builder Functions
from embedBuilder import embedBuilder

#Import the gameObjects
from gameObjects.Lobby import Lobby
from gameObjects.Theme import Theme
from gameObjects.Game import Game
from gameObjects.Player import Player

#Import the gameFunctions
from gameFunctions.lobbyFunctions import lobbyFunctions
from gameFunctions.gameStartFunctions import gameStartFunctions
from gameFunctions.midGameFunctions import midGameFunctions

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
    global currentLobby, currentGame
    if 'currentLobby' in globals():
        del currentLobby
    if 'currentGame' in globals():
        del currentGame

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
    await currentTheme.resolveEmojis(client)
    print(f"Bot Online\nOn Server {homeServer.name}\nHome Channel At {home.name}\nUser Category at {userCategory.name}")

@client.command('reset')
async def reset(ctx):
    if home == ctx.channel:
        if 'currentLobby' in globals():
            if 'currentGame' in globals() and currentLobby.host != ctx.message.author:
                await home.send('Only the host may reset the game once the game has begun!')
            else:
                resetFunction()
                embed = await embedBuilder.buildReset(prefix)
                await home.send(embed=embed)
        else:
            await home.send('There is no lobby to reset.')

@client.command('host')
async def host(ctx):
    global currentLobby
    lobbyPassed = None
    gamePassed = None
    if 'currentLobby' in globals():
        lobbyPassed = currentLobby
    if 'currentGame' in globals():
        gamePassed = currentGame
    await userInfoManager.userRegistration(ctx, ctx.message.author, homeServer, userCategory, currentTheme, prefix)
    functionCall = await lobbyFunctions.host(ctx, lobbyPassed, gamePassed, currentTheme, prefix, noMentions, home)
    if type(functionCall) == Lobby:
        currentLobby = functionCall

@client.command('join')
async def join(ctx):
    lobbyPassed = None
    gamePassed = None
    if 'currentLobby' in globals():
        lobbyPassed = currentLobby
    if 'currentGame' in globals():
        gamePassed = currentGame
    await userInfoManager.userRegistration(ctx, ctx.message.author, homeServer, userCategory, currentTheme, prefix)
    await lobbyFunctions.join(ctx, lobbyPassed, gamePassed, currentTheme, prefix, noMentions, home)

@client.command('leave')
async def leave(ctx):
    lobbyPassed = None
    gamePassed = None
    if 'currentLobby' in globals():
        lobbyPassed = currentLobby
    if 'currentGame' in globals():
        gamePassed = currentGame
    await lobbyFunctions.leave(ctx, lobbyPassed, gamePassed, currentTheme, prefix, noMentions, home)

@client.command('kick')
async def kick(ctx, kicked:discord.Member=None):
    lobbyPassed = None
    gamePassed = None
    if 'currentLobby' in globals():
        lobbyPassed = currentLobby
    if 'currentGame' in globals():
        gamePassed = currentGame
    await lobbyFunctions.kick(ctx, lobbyPassed, gamePassed, currentTheme, prefix, noMentions, home, kicked)

@client.command('kickall')
async def kickall(ctx):
    lobbyPassed = None
    gamePassed = None
    if 'currentLobby' in globals():
        lobbyPassed = currentLobby
    if 'currentGame' in globals():
        gamePassed = currentGame
    await lobbyFunctions.kickAll(ctx, lobbyPassed, gamePassed, currentTheme, prefix, noMentions, home)

@client.command('lobby')
async def lobby(ctx):
    lobbyPassed = None
    gamePassed = None
    if 'currentLobby' in globals():
        lobbyPassed = currentLobby
    if 'currentGame' in globals():
        gamePassed = currentGame
    await lobbyFunctions.lobby(ctx, home, lobbyPassed, currentTheme, gamePassed, prefix, noMentions)

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

@client.command('start')
async def start(ctx):
    global currentGame
    passedLobby = None
    passedGame = None
    if 'currentLobby' in globals():
        passedLobby = currentLobby
    if 'currentGame' in globals():
        passedGame = currentGame
    newGame = await gameStartFunctions.start(ctx, passedLobby, passedGame, home, prefix, currentTheme, client)
    if newGame != None:
        currentGame = newGame
        await midGameFunctions.showStatus(currentGame, currentTheme, home)
        await midGameFunctions.showRoles(currentGame, currentTheme, home)
        await midGameFunctions.showPlayers(currentGame, currentTheme, noMentions, home)

@client.command('status')
async def status(ctx):
    passedLobby = None
    passedGame = None
    if 'currentLobby' in globals():
        passedLobby = currentLobby
    if 'currentGame' in globals():
        passedGame = currentGame
    await midGameFunctions.status(ctx, passedLobby, passedGame, currentTheme, home, prefix, noMentions)

@client.command('roles')
async def roles(ctx):
    passedGame = None
    if 'currentGame' in globals():
        passedGame = currentGame
    await midGameFunctions.roles(ctx, passedGame, currentTheme, home)

@client.command('players')
async def players(ctx):
    passedLobby = None
    passedGame = None
    if 'currentLobby' in globals():
        passedLobby = currentLobby
    if 'currentGame' in globals():
        passedGame = currentGame
    await midGameFunctions.players(ctx, passedLobby, passedGame, currentTheme, noMentions, home, prefix)


#TEST COMMAND ONLY
@client.command('fill')
async def fill(ctx):
    bozos = [663576295682080789, 685709582118551552, 663577459647840259, 650144793296633887]
    bozoUsers = []
    for bozo in bozos:
        user = homeServer.get_member(bozo)
        await userInfoManager.userRegistration(ctx, user, homeServer, userCategory, currentTheme, prefix)
        bozoUsers.append(user)
    await lobbyFunctions.forceJoin(ctx, bozoUsers, currentLobby, None, currentTheme, prefix, noMentions, home)


client.run(BOT_TOKEN)
