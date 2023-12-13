import discord
from discord.ext import commands

from gameFunctions.expoProposalFunctions import expoProposalFunctions

from embedBuilder import embedBuilder

class endGameFunctions:
    async def processExpeditionEnd(currentGame, currentTheme, home):
        futureExpoCounts = await expoProposalFunctions.getExpeditionPrediction(currentGame)
        embed = await embedBuilder.buildStatusEmbed(currentGame, currentTheme, futureExpoCounts)
        await home.send(embed=embed)
        if currentGame.roundFails == 3:
            await endGameFunctions.breakAllWalls(currentGame, currentTheme, home)
        elif currentGame.roundWins == 3:
            await endGameFunctions.reachBasement(currentGame, currentTheme, home)
            

    async def breakAllWalls(currentGame, currentTheme, home):
        await home.send(currentTheme.wallBreakMessage)

    async def reachBasement(currentGame, currentTheme, home):
        await home.send(currentTheme.basementMessage)
    