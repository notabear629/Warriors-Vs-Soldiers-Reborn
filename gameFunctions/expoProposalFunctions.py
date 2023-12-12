import discord
from discord.ext import commands
import random
import asyncio


from gameObjects.Lobby import Lobby
from gameObjects.Player import Player
from gameObjects.Game import Game
from gameObjects.Role import Role

from gameFunctions.searchFunctions import searchFunctions
from gameFunctions.timerManager import timerManager

from dataFunctions.databaseManager import databaseManager

from embedBuilder import embedBuilder
from discordViewBuilder import discordViewBuilder
from discordViewBuilder import *

class expoProposalFunctions:
    async def getExpeditionSize(currentGame):
        if currentGame.currentRound == 1:
            expeditionNumber = 2
        elif currentGame.currentRound == 2:
            expeditionNumber = 3
        elif currentGame.currentRound > 2 and (len(currentGame.players) < 7):
            if (currentGame.currentRound == 3 and currentGame.players == 5):
                expeditionNumber = 2
            elif (currentGame.players == 5 and (currentGame.currentRound>3)) or (currentGame.players == 6 and currentGame.currentRound == 4):
                expeditionNumber = 3
            else:
                expeditionNumber = 4
        elif currentGame.currentRound > 2 and (len(currentGame.players) >= 7):
            dynamicOffset = currentGame.currentRoundWins
            if 1 in currentGame.passedRounds:
                dynamicOffset -= 1
            expeditionNumber = 3 + dynamicOffset
        if expeditionNumber > len(currentGame.livingSoldiers):
            expeditionNumber = len(currentGame.livingSoldiers)
        return expeditionNumber
    
    async def getExpeditionPrediction(currentGame):
        roundsToPredict = 5 - (currentGame.currentRound)
        if len(currentGame.players) == 5 or len(currentGame.players) == 6:
            roundNumbers = [2, 3, 2, 3, 3]
            if len(currentGame.players) == 6:
                roundNumbers = [2, 3, 4, 3, 4]
            while len(roundNumbers) > roundsToPredict:
                roundNumbers.pop(0)
            index = 0
            for round in roundNumbers:
                if roundNumbers[index] > len(currentGame.livingSoldiers):
                    roundNumbers[index] = len(currentGame.livingSoldiers)
                roundNumbers[index] = str(roundNumbers[index])
                index += 1
        else:
            sampleDict = {'low': 3, 'high': 5}
            roundNumbers = [2, 3, sampleDict, sampleDict, sampleDict]
            while len(roundNumbers) > roundsToPredict:
                roundNumbers.pop(0)
            index = 0
            for round in roundNumbers:
                roundPredicted = 5 - roundsToPredict + index + 1
                if type(round) == int:
                    if roundNumbers[index] > len(currentGame.livingSoldiers):
                        roundNumbers[index] = len(currentGame.livingSoldiers)
                    roundNumbers[index] = str(roundNumbers[index])
                else:
                    dynamicOffset = currentGame.currentRoundWins
                    if 1 in currentGame.passedRounds:
                        dynamicOffset -= 1
                    chancesRemaining = 3 - currentGame.currentRoundFails - 1
                    floor = currentGame.currentExpo.size + (roundPredicted - currentGame.currentRound) - chancesRemaining
                    if floor > len(currentGame.livingSoldiers):
                        floor = len(currentGame.livingSoldiers)
                    delaysRemaining = 3 - currentGame.currentRoundWins - 1
                    ceiling = currentGame.currentExpo.size + (roundPredicted - currentGame.currentRound) - delaysRemaining
                    if ceiling > len(currentGame.livingSoldiers):
                        ceiling = len(currentGame.livingSoldiers)
                    if floor == ceiling:
                        roundNumbers[index] = str(floor)
                    else:
                        roundNumbers[index] = f'({floor}-{ceiling})'
                index += 1

        return roundNumbers
    
    async def resetExpedition(currentGame, currentTheme, noMentions, home, prefix):
        currentGame.nextCommander()
        await expoProposalFunctions.showPlayers(currentGame, currentTheme, noMentions, home)
        commanderMessage = f'{currentGame.currentExpo.commander.user.mention}, you are now the {currentTheme.commanderName}! Use `{prefix}pick @mention` to pick your {currentTheme.expeditionTeamMembers} or use `{prefix}pass` to skirt your responsibility and allow the next player to propose a new {currentTheme.expeditionTeam}. You may empty your picks and start over by using `{prefix}clear`'
        await home.send(commanderMessage)
        timeout = await timerManager.setTimer(currentGame, 'Pick')
        if timeout == None:
            return
        elif timeout:
            await home.send(f'{currentGame.currentExpo.commander.user.mention}, you have failed to pick your {currentTheme.expeditionTeam} in time. The next {currentTheme.commanderName} will now have an opportunity to pick their {currentTheme.expeditionTeam}')
            await expoProposalFunctions.resetExpedition(currentGame, currentTheme, noMentions, home, prefix)
        else:
            if currentGame.currentExpo.passed:
                await home.send(f'You have passed the responsibility of choice to the next {currentTheme.commanderName}.')
                await expoProposalFunctions.resetExpedition(currentGame, currentTheme, noMentions, home, prefix)
            else:
                return

    async def showPlayers(currentGame, currentTheme, noMentions, home):
        embed = await embedBuilder.buildPlayers(currentGame, currentTheme)
        await home.send(embed=embed, allowed_mentions = noMentions)

    async def pick(ctx, currentGame, pickedPlayer, home, prefix, currentTheme):
        if home == ctx.message.channel and currentGame != None and currentGame.currentExpo.currentlyPicking and currentGame.currentExpo.commander.user == ctx.message.author:
            player = await searchFunctions.userToPlayer(currentGame, pickedPlayer)
            if player == None:
                await ctx.reply(f'You may only pick people playing the game for your {currentTheme.expeditionTeam}!')
            elif player in currentGame.currentExpo.expeditionMembers:
                await ctx.reply(f'This player is already in your {currentTheme.expeditionTeam}!')
            elif player not in currentGame.livingPlayers:
                await ctx.reply(f'This player is dead! You may only pick living players for your {currentTheme.expeditionTeam}')
            else:
                currentGame.currentExpo.addMember(player)
                embed = await embedBuilder.pickExpoMember(currentGame, currentTheme)
                await home.send(embed=embed)
                await home.send(f'{pickedPlayer.name} has been added to the {currentTheme.expeditionTeam}.')
                if len(currentGame.currentExpo.expeditionMembers) == currentGame.currentExpo.size:
                    await home.send(f'The {currentTheme.expeditionName} is now full. The time to vote on if it should be allowed to pass has come.')
                    await expoProposalFunctions.beginVoting(currentGame, home, prefix, currentTheme)

    async def passExpo(ctx, currentGame, home):
        if home == ctx.message.channel and currentGame != None and currentGame.currentExpo.currentlyPicking and currentGame.currentExpo.commander.user == ctx.message.author:
            currentGame.currentExpo.passExpo()

    async def clearExpo(ctx, currentGame, home, prefix, currentTheme):
        if home == ctx.message.channel and currentGame != None and currentGame.currentExpo.currentlyPicking and currentGame.currentExpo.commander.user == ctx.message.author:
            currentGame.currentExpo.clearExpedition()
            embed = await embedBuilder.pickExpoMember(currentGame, currentTheme)
            await home.send(embed=embed)
            await home.send(f'Your {currentTheme.expeditionTeam} proposal has been reset.')

    async def beginVoting(currentGame, home, prefix, currentTheme):
        currentGame.currentExpo.beginVoting(currentGame)
        discordView = await discordViewBuilder.expeditionVoteView()
        await home.send('THIS IS A TEST', view = discordView)






