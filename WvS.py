#Requirement Imports
import discord
from discord.ext import commands
import os
from dotenv import load_dotenv

#Imports from other .py files

#Import Embed Builder Functions
from embedBuilder import embedBuilder

from discordViewBuilder import discordViewBuilder

from statBuilder import statBuilder

#Import the gameObjects
from gameObjects.Lobby import Lobby
from gameObjects.Theme import Theme
from gameObjects.Game import Game
from gameObjects.Player import Player
from gameObjects.Rules import Rules
from gameObjects.Role import Role
from gameObjects.Badges import Badges

#Import the gameFunctions
from gameFunctions.lobbyFunctions import lobbyFunctions
from gameFunctions.gameStartFunctions import gameStartFunctions
from gameFunctions.midGameFunctions import midGameFunctions
from gameFunctions.expoProposalFunctions import expoProposalFunctions
from gameFunctions.expoActiveFunctions import expoActiveFunctions
from gameFunctions.endGameFunctions import endGameFunctions
from gameFunctions.rumblingFunctions import rumblingFunctions
from gameFunctions.infoFunctions import infoFunctions

from dataFunctions.databaseManager import databaseManager

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
GAG_ROLE_ID = int(os.getenv('BOT_WVS_GAG_ROLE_ID'))
ADMIN_ROLE_ID = int(os.getenv('ADMIN_ROLE_ID'))

client = discord.Client(intents=intents)
client = commands.Bot(command_prefix = prefix, intents = intents, help_command = None, case_insensitive=True)

async def resetFunction():
    global currentLobby, currentGame
    if currentLobby.online:
        currentLobby.turnOffline()
    if currentGame.online:
        currentGame.turnOffline()
    currentLobby = Lobby()
    currentGame = Game(client, homeServer, prefix, userCategory, home)
    for player in gagRole.members:
        await player.remove_roles(gagRole)

@client.event
async def on_ready():
    global home, homeServer, userCategory, gagRole, adminRole
    global noMentions, withMentions
    global currentTheme, currentRules, currentLobby, currentGame, loadedRoles, loadedBadges
    home = client.get_channel(HOME_ID)
    homeServer = client.get_guild(HOME_SERVER_ID)
    userCategory = client.get_channel(USER_CHANNEL_CATEGORY_ID)
    gagRole = homeServer.get_role(GAG_ROLE_ID)
    adminRole = homeServer.get_role(ADMIN_ROLE_ID)
    noMentions = discord.AllowedMentions(everyone=False, users=False, roles=False, replied_user=False)
    withMentions = discord.AllowedMentions(everyone=True, users=True, roles=True, replied_user=True)
    currentTheme = Theme()
    await currentTheme.resolveEmojis(client)
    currentRules = Rules()
    currentLobby = Lobby()
    currentGame = Game(client, homeServer, prefix, userCategory, home)
    loadedRoles = Role.loadRoles(currentTheme, client)
    loadedBadges = Badges(client)
    await userInfoManager.fixDatabase(None, homeServer, userCategory, currentTheme, prefix, loadedBadges)
    print(f"Bot Online\nOn Server {homeServer.name}\nHome Channel At {home.name}\nUser Category at {userCategory.name}")

@client.command('reset')
async def reset(ctx):
    if home == ctx.channel:
        if currentLobby.online:
            if currentGame.online and currentLobby.host != ctx.message.author:
                await home.send('Only the host may reset the game once the game has begun!')
            else:
                if currentGame.online and currentGame.commanderOrder[0].user == currentLobby.host and currentGame.currentExpo != None and currentGame.currentExpo.currentlyPicking:
                    await ctx.reply(f'...You didn\'t by chance mean to use `{prefix}clear`, did you? If you really want to reset, use `{prefix}pass` and then reset the game.')
                    return
                await resetFunction()
                embed = await embedBuilder.buildReset(prefix)
                await home.send(embed=embed)
        else:
            await home.send('There is no lobby to reset.')

@client.command('host')
async def host(ctx):
    await userInfoManager.userRegistration(ctx, ctx.message.author, homeServer, userCategory, currentTheme, prefix)
    await lobbyFunctions.host(ctx, currentLobby, currentGame, currentTheme, prefix, noMentions, home, currentRules, client, loadedRoles, adminRole)


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

@client.command('givehost')
async def givehost(ctx, newHost:discord.Member=None):
    await lobbyFunctions.giveHost(ctx, currentLobby, currentGame, currentTheme, prefix, noMentions, home, newHost)

@client.command('lobby')
async def lobby(ctx):
    await lobbyFunctions.lobby(ctx, home, currentLobby, currentTheme, currentGame, prefix, noMentions)

@client.command('options')
async def options(ctx):
    await lobbyFunctions.options(ctx, home, currentLobby, currentGame, currentTheme, prefix, noMentions, client, loadedRoles, adminRole)

@client.command('rules')
async def rules(ctx):
    await lobbyFunctions.options(ctx, home, currentLobby, currentGame, currentTheme, prefix, noMentions, client, loadedRoles, adminRole)

@client.command('settings')
async def settings(ctx):
    await lobbyFunctions.options(ctx, home, currentLobby, currentGame, currentTheme, prefix, noMentions, client, loadedRoles, adminRole)

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

@commands.max_concurrency(1, per=commands.BucketType.default, wait=False)
@client.command('start')
async def start(ctx):
    newGame = await gameStartFunctions.start(ctx, currentLobby, currentGame, home, prefix, currentTheme, client, currentRules, loadedRoles, gagRole, loadedBadges)
    if newGame:
        await midGameFunctions.showStatus(currentGame, currentTheme, home)
        await midGameFunctions.showRoles(currentGame, currentTheme, home)
        await expoProposalFunctions.resetExpedition(currentGame, currentTheme, noMentions, home, prefix)

@client.command('status')
async def status(ctx):
    await midGameFunctions.status(ctx, currentLobby, currentGame, currentTheme, home, prefix, noMentions)

@client.command('roles')
async def roles(ctx):
    await midGameFunctions.roles(ctx, currentGame, currentTheme, home, loadedRoles)

@client.command('players')
async def players(ctx):
    await midGameFunctions.players(ctx, currentLobby, currentGame, currentTheme, noMentions, home, prefix)

@client.command('pick')
async def pick(ctx, *, pickedUser:discord.Member):
    await expoProposalFunctions.pick(ctx, currentGame, pickedUser, home, prefix, currentTheme, client, noMentions)

@client.command('pass')
async def passExpo(ctx):
    await expoProposalFunctions.passExpo(ctx, currentGame, home)

@client.command('clear')
async def clear(ctx):
    await expoProposalFunctions.clearExpo(ctx, currentGame, home, prefix, currentTheme)


@commands.max_concurrency(1, per=commands.BucketType.default, wait=False)
@client.command('results')
async def results(ctx):
    resultsRead = await expoActiveFunctions.results(ctx, currentGame, currentTheme, home, expoProposalFunctions.getExpeditionPrediction, client, homeServer, discord)
    if resultsRead:
        if currentGame.currentExpo.dazActivated:
            await expoProposalFunctions.resetExpedition(currentGame, currentTheme, noMentions, home, prefix)
        else:
            if currentGame.online and currentGame.exposOver == False:
                await expoProposalFunctions.advanceRound(currentGame, currentTheme, home, noMentions, prefix, client)
            if currentGame.online and currentGame.exposOver:
                if currentGame.rumblingActivated:
                    await rumblingFunctions.rumblingStart(currentGame, currentTheme, home, client, prefix)
                else:
                    await endGameFunctions.processExpeditionEnd(currentGame, currentTheme, home)
            if currentGame.online and currentGame.winCondition != None:
                await resetFunction()

@client.command('kidnap')
async def kidnap(ctx, *, kidnappedUser:discord.Member):
    await endGameFunctions.kidnap(ctx, kidnappedUser, currentGame, currentTheme, home)

@client.command('attack')
async def attack(ctx, *, attackedUser:discord.Member):
    await rumblingFunctions.attack(ctx, attackedUser, currentGame, currentTheme, home)
    if currentGame.online and currentGame.winCondition != None:
        await resetFunction()

@client.command('retreat')
async def retreat(ctx):
    await endGameFunctions.skipToBasement(ctx, currentGame, currentTheme, home, client, gagRole)
    if currentGame.online and currentGame.winCondition != None:
        await resetFunction()

@client.command('target')
async def target(ctx):
    await midGameFunctions.target(ctx, currentGame, currentTheme, prefix, client)

@client.command('trial')
async def trial(ctx):
    await midGameFunctions.trial(ctx, currentGame, currentTheme, prefix, client)

@client.command('guard')
async def guard(ctx):
    await midGameFunctions.guard(ctx, currentGame, currentTheme, prefix, client)
    
@client.command('summon')
async def summon(ctx):
    await midGameFunctions.summon(ctx, currentGame, currentTheme)

@client.command('fire')
async def fire(ctx):
    await midGameFunctions.fire(ctx, currentGame, currentTheme)

@client.command('scream')
async def scream(ctx):
    await midGameFunctions.scream(ctx, currentGame, currentTheme)

@client.command('gag')
async def gag(ctx):
    await midGameFunctions.gag(ctx, currentGame, currentTheme, prefix, client, gagRole, midGameFunctions.executeGag)

@commands.max_concurrency(1, per=commands.BucketType.default, wait=True)
@client.command('check')
async def check(ctx, *, checkedPlayer:discord.Member):
    await midGameFunctions.check(ctx, checkedPlayer, currentGame, currentTheme)

@client.command('paths')
async def paths(ctx):
    await midGameFunctions.paths(ctx, currentGame, currentTheme, prefix, client)

@client.command('flare')
async def flare(ctx):
    await expoProposalFunctions.flare(ctx, currentGame, client, gagRole)

@client.command('rolelist')
async def rolelist(ctx):
    await infoFunctions.rolelist(ctx, loadedRoles, currentTheme)

@client.command('help')
async def help(ctx):
    await infoFunctions.help(ctx, currentTheme, loadedRoles, prefix)

@client.command('info')
async def info(ctx, *, input=None):
    await infoFunctions.info(ctx, currentTheme, loadedRoles, prefix, input)

@client.command('profile')
async def profile(ctx, *, input=None):
    await infoFunctions.profile(ctx, currentTheme, client, loadedRoles, homeServer, loadedBadges, input)

@client.command('stats')
async def stats(ctx, *, input=None):
    await infoFunctions.profile(ctx, currentTheme, client, loadedRoles, homeServer, loadedBadges, input)

@client.command('badges')
async def badges(ctx, *, input=None):
    await infoFunctions.badges(ctx, currentTheme, client, loadedBadges, input)

@client.command('lb')
async def lb(ctx, *, input=None):
    await infoFunctions.leaderboard(ctx, client, homeServer, loadedBadges, currentTheme, input)

@client.command('leaderboard')
async def leaderboard(ctx, *, input=None):
    await infoFunctions.leaderboard(ctx, client, homeServer, loadedBadges, currentTheme, input)

@client.command('advantage')
async def advantage(ctx):
    await infoFunctions.advantage(ctx, currentGame, currentTheme)

@client.command('admin')
async def admin(ctx):
    await userInfoManager.toggleAdmin(ctx, home, adminRole)

#test command only
@client.command('debug')
async def debug(ctx, *, var):
    if ctx.message.author.name == 'cerberus629':
        dotSeparators = var.split('.')
        rootVar = None
        for elem in dotSeparators:
            if '[' in elem or ']' in elem:
                leftSplit = elem.split('[')
                for elem2 in leftSplit:
                    if elem2 == leftSplit[0]:
                        dotSplit = elem2.split('.')
                        rootVar = getattr(rootVar, dotSplit[len(dotSplit)-1])
                        continue
                    rightSplit = elem2.split(']')
                    try:
                        index = int(rightSplit[0])
                        rootVar = rootVar[index]
                    except:
                        print(rightSplit[0])
                        rootVar=rootVar[rightSplit[0]]
            else:
                if elem == dotSeparators[0]:
                    rootVar = globals()[elem]
                else:
                    rootVar = getattr(rootVar, elem)
        if rootVar == None:
            await ctx.reply('None')
        else:
            await ctx.reply(rootVar)

#TEST COMMAND ONLY
@client.command('fill')
async def fill(ctx, *, arg=None):
    if ctx.message.author.name == 'cerberus629':
        bozos = [663576295682080789, 571823508909195265, 663577459647840259, 650144793296633887]
        bozoSeven = [650144793296633887, 663576295682080789, 663577459647840259, 663577459647840259, 571823508909195265, 571823508909195265]
        bozoUsers = []
        if str(arg) == '7':
            choiceGroup = bozoSeven
        else:
            choiceGroup = bozos
        for bozo in choiceGroup:
            user = homeServer.get_member(bozo)
            await userInfoManager.userRegistration(ctx, user, homeServer, userCategory, currentTheme, prefix)
            bozoUsers.append(user)
        await lobbyFunctions.forceJoin(ctx, bozoUsers, currentLobby, None, currentTheme, prefix, noMentions, home)


client.run(BOT_TOKEN)