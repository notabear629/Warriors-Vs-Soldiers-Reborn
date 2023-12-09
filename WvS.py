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
    if home == ctx.channel:
        if 'currentLobby' in globals():     
            if ctx.message.author in currentLobby.users:
                if ctx.message.author == currentLobby.host:
                    await ctx.message.reply(f"You are already hosting a lobby. use `{prefix}reset` to close it to start a new one.")
                else:
                    await ctx.message.reply("Hey stinky, there's already a lobby! You're even in it!")
            else:
                await ctx.message.reply(f'There is already a lobby! Why not `{prefix}join` instead?')
        else:
            currentLobby = Lobby(ctx.message.author)
            embed = await embedBuilder.buildLobby(currentLobby, prefix)
            await home.send(embed=embed, allowed_mentions= noMentions)
            await home.send('Lobby Created.')

@client.command('join')
async def join(ctx):
    if home == ctx.channel:
        if 'currentLobby' in globals():
            if ctx.message.author in currentLobby.users:
                await ctx.message.reply('Hey stinky, you are already in the lobby!')
            else:
                currentLobby.addUser(user)
                embed = await embedBuilder.buildLobby(currentLobby, prefix)
                await home.send(embed=embed, allowed_mentions= noMentions)
                await home.send(f'**{ctx.message.author.name}** has joined the Lobby.')
        else:
            await ctx.message.reply(f'There is no active lobby. Why not create one using `{prefix}host`?')


client.run(BOT_TOKEN)
