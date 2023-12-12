import discord
from discord.ext import commands
import random


from gameObjects.Lobby import Lobby
from gameObjects.Player import Player
from gameObjects.Game import Game
from gameObjects.Role import Role
from gameObjects.Expedition import Expedition

from gameFunctions.expoProposalFunctions import expoProposalFunctions
from gameFunctions.lobbyFunctions import lobbyFunctions

from dataFunctions.databaseManager import databaseManager

from embedBuilder import embedBuilder

class midGameFunctions:
    async def showStatus(currentGame, currentTheme, home):
        futureExpoCounts = await expoProposalFunctions.getExpeditionPrediction(currentGame)
        embed = await embedBuilder.buildStatusEmbed(currentGame, currentTheme, futureExpoCounts)
        await home.send(embed=embed)

    async def status(ctx, currentLobby, currentGame, currentTheme, home, prefix, noMentions):
        if currentGame != None:
            await midGameFunctions.showStatus(currentGame, currentTheme, ctx.message.channel)
        else:
            if currentLobby == None:
                await ctx.reply(f'There is not currently a game being played, or an open lobby! Why not create one in <#{home.id}> using `{prefix}host`?')
            else:
                await lobbyFunctions.lobby(ctx, home, currentLobby, currentTheme, currentGame, prefix, noMentions)

    async def roles(ctx, currentGame, currentTheme, home):
        if currentGame != None:
            await midGameFunctions.showRoles(currentGame, currentTheme, ctx.message.channel)

    async def showRoles(currentGame, currentTheme, home):
        embed = await embedBuilder.buildCurrentRoles(currentGame, currentTheme)
        await home.send(embed=embed)

    async def showPlayers(currentGame, currentTheme, noMentions, home):
        embed = await embedBuilder.buildPlayers(currentGame, currentTheme)
        await home.send(embed=embed, allowed_mentions = noMentions)

    async def players(ctx, currentLobby, currentGame, currentTheme, noMentions, home, prefix):
        if currentGame != None:
            await midGameFunctions.showPlayers(currentGame, currentTheme, noMentions, ctx.message.channel)
        elif currentLobby != None:
            await lobbyFunctions.lobby(ctx, home, currentLobby, currentTheme, currentGame, prefix, noMentions)
        else:
            await ctx.reply(f'There is no active lobby! Why not start one in <#{home.id}> with `{prefix}host`?')