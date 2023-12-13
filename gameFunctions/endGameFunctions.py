import discord
from discord.ext import commands

from gameFunctions.expoProposalFunctions import expoProposalFunctions
from gameFunctions.timerManager import timerManager
from gameFunctions.searchFunctions import searchFunctions

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
        currentGame.setWinCondition('wallBreaks')
        await endGameFunctions.processEndgame(currentGame, currentTheme, home)

    async def reachBasement(currentGame, currentTheme, home):
        currentGame.activateKidnap()
        await home.send(currentTheme.basementMessage)
        timeout = await timerManager.setTimer(currentGame, 'Kidnap')
        if timeout == None:
            return
        elif timeout:
            await endGameFunctions.kidnapTimeout(currentGame, currentTheme, home)     
        else:
            await endGameFunctions.processKidnap(currentGame, currentTheme, home)

    async def kidnapTimeout(currentGame, currentTheme, home):
        await home.send(f'{currentTheme.kidnapTimeoutMessage}')
        currentGame.setWinCondition('kidnapTimeout')
        await endGameFunctions.processEndgame(currentGame, currentTheme, home)

    async def kidnap(ctx, kidnappedUser, currentGame, currentTheme, home):
        if ctx.message.channel == home and currentGame != None and currentGame.deleted == False and currentGame.currentlyKidnapping and currentGame.kidnappedPlayer == None:
            kidnapper = await searchFunctions.userToPlayer(currentGame, ctx.message.author)
            if kidnapper == None:
                await ctx.reply(f'Only someone playing the game can choose who to kidnap!')
            elif kidnapper not in currentGame.warriors:
                await ctx.reply(f'Only the {currentTheme.warriorPlural} may choose who to kidnap!')
            else:
                kidnappedPlayer = await searchFunctions.userToPlayer(currentGame, kidnappedUser)
                if kidnappedPlayer == None:
                    await ctx.reply(f'You can only kidnap somebody playing the game!')
                else:
                    currentGame.kidnapPlayer(kidnappedPlayer)



    async def processKidnap(currentGame, currentTheme, home):
        Eren = await searchFunctions.roleIDToPlayer(currentGame, 'Eren')
        if currentGame.kidnappedPlayer == Eren:
            await endGameFunctions.kidnapSuccess(currentGame, currentTheme, home)
        else:
            await endGameFunctions.kidnapFail(currentGame, currentTheme, home)

    async def kidnapSuccess(currentGame, currentTheme, home):
        await home.send(currentTheme.kidnapSuccessMessage)
        currentGame.setWinCondition('kidnapSuccess')
        await endGameFunctions.processEndgame(currentGame, currentTheme, home)

    async def kidnapFail(currentGame, currentTheme, home):
        await home.send(currentTheme.kidnapFailMessage)
        currentGame.setWinCondition('kidnapFail')
        await endGameFunctions.processEndgame(currentGame, currentTheme, home)

    async def processEndgame(currentGame, currentTheme, home):
        currentGame.processWinners()
        embed = await embedBuilder.endgame(currentGame, currentTheme)
        await home.send(embed=embed)

    