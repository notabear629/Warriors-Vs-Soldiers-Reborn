#Requirement Imports
import discord
from discord.ext import commands
import os
from dotenv import load_dotenv

#Imports from other .py files

#Import Embed Builder Functions
from embedBuilder import embedBuilder

from discordViewBuilder import discordViewBuilder

#Import the gameObjects
from gameObjects.Lobby import Lobby
from gameObjects.Theme import Theme
from gameObjects.Game import Game
from gameObjects.Player import Player
from gameObjects.Rules import Rules
from gameObjects.Role import Role

#Import the gameFunctions
from gameFunctions.lobbyFunctions import lobbyFunctions
from gameFunctions.gameStartFunctions import gameStartFunctions
from gameFunctions.midGameFunctions import midGameFunctions
from gameFunctions.expoProposalFunctions import expoProposalFunctions
from gameFunctions.expoActiveFunctions import expoActiveFunctions
from gameFunctions.endGameFunctions import endGameFunctions

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
    if currentLobby.online:
        currentLobby.turnOffline()
    if currentGame.online:
        currentGame.turnOffline()
    currentLobby = Lobby()
    currentGame = Game(client)

@client.event
async def on_ready():
    global home, homeServer, userCategory
    global noMentions, withMentions
    global currentTheme, currentRules, currentLobby, currentGame, loadedRoles
    home = client.get_channel(HOME_ID)
    homeServer = client.get_guild(HOME_SERVER_ID)
    userCategory = client.get_channel(USER_CHANNEL_CATEGORY_ID)
    noMentions = discord.AllowedMentions(everyone=False, users=False, roles=False, replied_user=False)
    withMentions = discord.AllowedMentions(everyone=True, users=True, roles=True, replied_user=True)
    currentTheme = Theme()
    await currentTheme.resolveEmojis(client)
    currentRules = Rules()
    currentLobby = Lobby()
    currentGame = Game(client)
    loadedRoles = Role.loadRoles(currentTheme, client)
    print(f"Bot Online\nOn Server {homeServer.name}\nHome Channel At {home.name}\nUser Category at {userCategory.name}")

@client.command('reset')
async def reset(ctx):
    if home == ctx.channel:
        if currentLobby.online:
            if currentGame.online and currentLobby.host != ctx.message.author:
                await home.send('Only the host may reset the game once the game has begun!')
            else:
                resetFunction()
                embed = await embedBuilder.buildReset(prefix)
                await home.send(embed=embed)
        else:
            await home.send('There is no lobby to reset.')

@client.command('host')
async def host(ctx):
    await userInfoManager.userRegistration(ctx, ctx.message.author, homeServer, userCategory, currentTheme, prefix)
    await lobbyFunctions.host(ctx, currentLobby, currentGame, currentTheme, prefix, noMentions, home, currentRules)


@client.command('join')
async def join(ctx):
    await userInfoManager.userRegistration(ctx, ctx.message.author, homeServer, userCategory, currentTheme, prefix)
    await lobbyFunctions.join(ctx, currentLobby, currentGame, currentTheme, prefix, noMentions, home)

@client.command('leave')
async def leave(ctx):
    await lobbyFunctions.leave(ctx, currentLobby, currentGame, currentTheme, prefix, noMentions, home)

@client.command('kick')
async def kick(ctx, kicked:discord.Member=None):
    await lobbyFunctions.kick(ctx, currentLobby, currentGame, currentTheme, prefix, noMentions, home, kicked)

@client.command('kickall')
async def kickall(ctx):
    await lobbyFunctions.kickAll(ctx, currentLobby, currentGame, currentTheme, prefix, noMentions, home)

@client.command('lobby')
async def lobby(ctx):
    await lobbyFunctions.lobby(ctx, home, currentLobby, currentTheme, currentGame, prefix, noMentions)

@client.command('options')
async def options(ctx):
    await lobbyFunctions.options(ctx, home, currentLobby, currentGame, currentTheme, prefix, noMentions, client, loadedRoles)

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
    newGame = await gameStartFunctions.start(ctx, currentLobby, currentGame, home, prefix, currentTheme, client, currentRules, loadedRoles)
    if newGame:
        await midGameFunctions.showStatus(currentGame, currentTheme, home)
        await midGameFunctions.showRoles(currentGame, currentTheme, home)
        await expoProposalFunctions.resetExpedition(currentGame, currentTheme, noMentions, home, prefix)

@client.command('status')
async def status(ctx):
    await midGameFunctions.status(ctx, currentLobby, currentGame, currentTheme, home, prefix, noMentions)

@client.command('roles')
async def roles(ctx):
    await midGameFunctions.roles(ctx, currentGame, currentTheme, home)

@client.command('players')
async def players(ctx):
    await midGameFunctions.players(ctx, currentLobby, currentGame, currentTheme, noMentions, home, prefix)

@client.command('pick')
async def pick(ctx, *, pickedUser:discord.Member):
    await expoProposalFunctions.pick(ctx, currentGame, pickedUser, home, prefix, currentTheme, client, noMentions)

@client.command('pass')
async def passExpo(ctx):
    await expoProposalFunctions.passExpo(ctx, currentGame, home, prefix, currentTheme)

@client.command('clear')
async def clear(ctx):
    await expoProposalFunctions.clearExpo(ctx, currentGame, home, prefix, currentTheme)
        
@client.command('results')
async def results(ctx):
    resultsRead = await expoActiveFunctions.results(ctx, currentGame, currentTheme, home, expoProposalFunctions.getExpeditionPrediction, client)
    if resultsRead:
        if currentGame.currentExpo.dazActivated:
            await expoProposalFunctions.resetExpedition(currentGame, currentTheme, noMentions, home, prefix)
        else:
            if currentGame.online and currentGame.exposOver == False:
                await expoProposalFunctions.advanceRound(currentGame, currentTheme, home, noMentions, prefix, client)
            if currentGame.online and currentGame.exposOver:
                await endGameFunctions.processExpeditionEnd(currentGame, currentTheme, home)
            if currentGame.online and currentGame.winCondition != None:
                resetFunction()

@client.command('kidnap')
async def kidnap(ctx, *, kidnappedUser:discord.Member):
    await endGameFunctions.kidnap(ctx, kidnappedUser, currentGame, currentTheme, home)

@client.command('target')
async def target(ctx):
    await midGameFunctions.target(ctx, currentGame, currentTheme, prefix, client)

@client.command('flare')
async def flare(ctx):
    await expoProposalFunctions.flare(ctx, currentGame, client)



#TEST COMMAND ONLY
@client.command('fill')
async def fill(ctx):
    bozos = [663576295682080789, 571823508909195265, 663577459647840259, 650144793296633887]
    bozoUsers = []
    for bozo in bozos:
        user = homeServer.get_member(bozo)
        await userInfoManager.userRegistration(ctx, user, homeServer, userCategory, currentTheme, prefix)
        bozoUsers.append(user)
    await lobbyFunctions.forceJoin(ctx, bozoUsers, currentLobby, None, currentTheme, prefix, noMentions, home)

#TEST COMMAND ONLY
@client.command('test')
async def test(ctx):
    view = await discordViewBuilder.roleOptionsView(loadedRoles)
    await ctx.send(view=view)


client.run(BOT_TOKEN)
