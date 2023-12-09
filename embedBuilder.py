import discord
from discord.ext import commands

class embedBuilder:

    async def buildLobby(currentLobby, prefix):
        returnedEmbed = discord.Embed(title = 'The Lobby', description =f'The lobby has: **{len(currentLobby.users)}** players within it.\n\nUse `{prefix}help rules` for information on how to change the rules.', color = discord.Color.blue())
        playerList = ''
        for player in currentLobby.users:
            playerList += f'**{player.mention}**\n'
        returnedEmbed.add_field(name = 'Players', value = playerList, inline = False)
        return returnedEmbed
    
    async def buildReset(prefix):
        returnedEmbed = discord.Embed(title = 'The Game Lobby has been Reset.', description= f'Start a new lobby by using `{prefix}host`')
        return returnedEmbed