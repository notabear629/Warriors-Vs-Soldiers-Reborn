import discord
from discord.ext import commands
import random
import asyncio


from gameObjects.Lobby import Lobby
from gameObjects.Player import Player
from gameObjects.Game import Game
from gameObjects.Role import Role
from gameObjects.Expedition import Expedition
from gameObjects.Stats import Stats

from gameFunctions.searchFunctions import searchFunctions
from gameFunctions.timerManager import timerManager
from gameFunctions.expoActiveFunctions import expoActiveFunctions
from gameFunctions.webhookManager import webhookManager

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
            fiveManCounts = [2, 3, 2, 3, 3]
            sixManCounts = [2, 3, 4, 3, 4]
            if len(currentGame.players) == 5:
                expeditionNumber = fiveManCounts[currentGame.currentRound-1]
            else:
                expeditionNumber = sixManCounts[currentGame.currentRound-1]
        elif currentGame.currentRound > 2 and (len(currentGame.players) >= 7):
            dynamicOffset = currentGame.roundWins
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
                    if roundPredicted == 5:
                        if currentGame.currentRound == 1:
                            minimumFloor = 4
                            maximumCeiling = 5
                        elif 1 in currentGame.passedRounds:
                            minimumFloor = 4
                            maximumCeiling = 4
                        else:
                            minimumFloor = 5
                            maximumCeiling = 5
                    elif roundPredicted == 4:
                        if currentGame.currentRound == 1:
                            minimumFloor = 3
                            maximumCeiling = 5
                        elif currentGame.currentRound == 2 and 1 in currentGame.passedRounds:
                            minimumFloor = 3
                            maximumCeiling = 4
                        elif currentGame.currentRound == 2 and 1 in currentGame.failedRounds:
                            minimumFloor = 4
                            maximumCeiling = 5
                        elif currentGame.currentRound == 3:
                            minimumFloor = currentGame.currentExpo.size
                            maximumCeiling = currentGame.currentExpo.size
                            if currentGame.roundFails >= 2:
                                minimumFloor += 1
                            if currentGame.roundWins < 2:
                                maximumCeiling += 1
                    elif roundPredicted == 3:
                        minimumFloor = 3
                        maximumCeiling = 4
                    if minimumFloor > len(currentGame.livingSoldiers):
                        minimumFloor = len(currentGame.livingSoldiers)
                    if maximumCeiling > len(currentGame.livingSoldiers):
                        maximumCeiling = len(currentGame.livingSoldiers)
                    if minimumFloor == maximumCeiling:
                        roundNumbers[index] = str(minimumFloor)
                    else:
                        roundNumbers[index] = f'({minimumFloor}-{maximumCeiling})'                   
                index += 1
        currentGame.setExpoProjections(roundNumbers)
        return roundNumbers
    
    async def resetExpedition(currentGame, currentTheme, noMentions, home, prefix):
        if currentGame.currentExpo.erwinActivated:
            await expoProposalFunctions.erwinTakeover(currentGame, currentTheme, home, currentGame.client)
        else:
            currentGame.nextCommander()
        currentGame.currentExpo.resetExpo()
        await expoProposalFunctions.showPlayers(currentGame, currentTheme, noMentions, home)
        commanderMessage = f'{currentGame.currentExpo.commander.user.mention}, you are now the {currentTheme.commanderName}! Use `{prefix}pick @mention` to pick your {currentTheme.expeditionTeamMembers} or use `{prefix}pass` to skirt your responsibility and allow the next player to propose a new {currentTheme.expeditionTeam}. You may empty your picks and start over by using `{prefix}clear`'
        await home.send(commanderMessage)
        if len(currentGame.livingSoldiers) == len(currentGame.livingWarriors):
            await home.send(f'⚠️Warning! Voting Gridlock detected because the amount of living {currentTheme.soldierPlural} and {currentTheme.warriorPlural} are the same! In the case of a tied vote, instead of a reject, the commander\'s vote will play as the tiebreaker!⚠️')
        timeout = await timerManager.setTimer(currentGame, home, currentTheme, 'Pick')
        if timeout == None:
            return
        elif timeout:
            await home.send(f'{currentGame.currentExpo.commander.user.mention}, you have failed to pick your {currentTheme.expeditionTeam} in time. The next {currentTheme.commanderName} will now have an opportunity to pick their {currentTheme.expeditionTeam}')
            await expoProposalFunctions.resetExpedition(currentGame, currentTheme, noMentions, home, prefix)
        else:
            if currentGame.currentExpo.passed:
                await home.send(f'You have passed the responsibility of choice to the next {currentTheme.commanderName}.')
                await expoProposalFunctions.resetExpedition(currentGame, currentTheme, noMentions, home, prefix)
            elif currentGame.currentExpo.erwinActivated:
                await expoProposalFunctions.resetExpedition(currentGame, currentTheme, noMentions, home, prefix)
            elif currentGame.porcoGagged == currentGame.currentExpo.commander:
                await home.send(f'The {currentTheme.commanderName} is under a gag order and will be skipped!')
                await expoProposalFunctions.resetExpedition(currentGame, currentTheme, noMentions, home, prefix)
                Porco = await searchFunctions.roleIDToPlayer(currentGame, 'Porco')
                Porco.stats.gagSkip()
            else:
                return

    async def showPlayers(currentGame, currentTheme, noMentions, home):
        embed = await embedBuilder.buildPlayers(currentGame, currentTheme)
        await home.send(embed=embed, allowed_mentions = noMentions)

    async def pick(ctx, currentGame, pickedPlayer, home, prefix, currentTheme, client, noMentions):
        if home == ctx.message.channel and currentGame.online and currentGame.currentExpo.currentlyPicking and currentGame.currentExpo.commander.user == ctx.message.author:
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
                if len(currentGame.currentExpo.expeditionMembers) == currentGame.currentExpo.size and currentGame.currentExpo.filledUp == False:
                    currentGame.currentExpo.fillUp()
                    await home.send(f'The {currentTheme.expeditionName} is now full. The time to vote on if it should be allowed to pass has come.')
                    await expoProposalFunctions.beginVoting(currentGame, home, prefix, currentTheme, client, noMentions)

    async def passExpo(ctx, currentGame, home):
        if home == ctx.message.channel and currentGame.online and currentGame.currentExpo.currentlyPicking and currentGame.currentExpo.commander.user == ctx.message.author:
            currentGame.currentExpo.passExpo()

    async def clearExpo(ctx, currentGame, home, prefix, currentTheme):
        if home == ctx.message.channel and currentGame.online and currentGame.currentExpo.currentlyPicking and currentGame.currentExpo.commander.user == ctx.message.author:
            currentGame.currentExpo.clearExpedition()
            embed = await embedBuilder.pickExpoMember(currentGame, currentTheme)
            await home.send(embed=embed)
            await home.send(f'Your {currentTheme.expeditionTeam} proposal has been reset.')

    async def beginVoting(currentGame, home, prefix, currentTheme, client, noMentions):
        currentGame.currentExpo.beginVoting(currentGame)
        for player in currentGame.currentExpo.eligibleVoters:
            user = databaseManager.searchForUser(player.user)
            userChannel = client.get_channel(user['channelID'])
            embed = await embedBuilder.voteDM(currentGame, player, currentTheme)
            view = await discordViewBuilder.expeditionVoteView(currentTheme, currentGame, player, client, home, expoProposalFunctions.voteExpo)
            await userChannel.send(player.user.mention)
            await userChannel.send(embed=embed, view=view)
        timeout = await timerManager.setTimer(currentGame, home, currentTheme, 'Vote')
        if timeout == None:
            return
        elif timeout and currentGame.exposOver == False:
            await home.send(f'Time to vote on the {currentTheme.expeditionTeam} has run out. The remaining voters that did not vote will be marked as abstaining.')
            for player in currentGame.currentExpo.eligibleVoters:
                if player not in currentGame.currentExpo.voted:
                    currentGame.currentExpo.voteExpo(player, 'a')
        if currentGame.exposOver == False:
            await expoProposalFunctions.showVotingResults(currentGame, currentTheme, home, noMentions, prefix, client)

    
    async def voteExpo(currentGame, player, client, currentTheme, home, vote):
        if currentGame.online and currentGame.currentExpo.currentlyVoting and player in currentGame.currentExpo.eligibleVoters and player not in currentGame.currentExpo.voted:
            if vote == 'Accept':
                voteToProcess = 'y'
            elif vote == 'Reject':
                voteToProcess = 'n'
            elif vote == 'Secure' and player.role.id == 'Jean' and player.role.abilityActive:
                voteToProcess = 'Jean'
            elif 'Flip and Accept' in vote and player.role.id == 'Pieck' and player.role.abilityActive:
                voteToProcess = 'PieckAccept'
            elif 'Flip and Reject' in vote and player.role.id == 'Pieck' and player.role.abilityActive:
                voteToProcess = 'PieckReject'
            elif vote == 'Intercept' and player.role.id == 'Falco' and player.role.abilityActive:
                voteToProcess = 'Falco'
            else:
                voteToProcess = 'a'
            currentGame.currentExpo.voteExpo(player, voteToProcess)
            user = databaseManager.searchForUser(player.user)
            userChannel = client.get_channel(user['channelID'])
            await userChannel.send('Vote Received.')
            await currentGame.sendTemporaryMessage(currentTheme, home)

    async def getVotingResults(currentGame):
        if currentGame.currentExpo.jeanActivated:
            return True
        elif currentGame.currentExpo.pieckActivated:
            if len(currentGame.currentExpo.rejected) > len(currentGame.currentExpo.accepted):
                return True
            elif len(currentGame.livingSoldiers) == len(currentGame.livingWarriors) and currentGame.currentExpo.commander in currentGame.currentExpo.rejected and len(currentGame.currentExpo.rejected) == len(currentGame.currentExpo.accepted):
                return True
            return False
        elif len(currentGame.currentExpo.accepted) > len(currentGame.currentExpo.rejected):
            return True
        elif len(currentGame.livingSoldiers) == len(currentGame.livingWarriors) and len(currentGame.currentExpo.accepted) == len(currentGame.currentExpo.rejected) and currentGame.currentExpo.commander in currentGame.currentExpo.accepted:
            return True
        return False
    
    async def showVotingResults(currentGame, currentTheme, home, noMentions, prefix, client):
        if currentGame.currentExpo.falcoActivated:
            Falco = await searchFunctions.roleIDToPlayer(currentGame, 'Falco')
            currentGame.currentExpo.processFalco(Falco)
        voteResult = await expoProposalFunctions.getVotingResults(currentGame)
        await Stats.processVoteStats(currentGame, voteResult, searchFunctions)
        embed = await embedBuilder.showVotingResults(currentGame, currentTheme, voteResult)
        await home.send(embed=embed)
        await webhookManager.processExpoVoteWebhooks(currentGame, currentTheme, home, client)
        if voteResult:
            await home.send(f'The {currentTheme.expeditionName} Proposal has Passed!')
            await expoActiveFunctions.activateExpedition(currentGame, currentTheme, home, client, prefix)
        else:
            await home.send(f'The {currentTheme.expeditionName} Proposal has Failed!')
            await expoProposalFunctions.resetExpedition(currentGame, currentTheme, noMentions, home, prefix)

    async def advanceRound(currentGame, currentTheme, home, noMentions, prefix, client):
        currentGame.advanceRound()
        if currentGame.porcoGagged != None:
            for user in currentGame.gagRole.members:
                await user.remove_roles(currentGame.gagRole)
            currentGame.removeGag()
        expoSize = await expoProposalFunctions.getExpeditionSize(currentGame)
        expo = Expedition(currentGame.currentExpo.commander, expoSize, currentGame.players)
        currentGame.setExpedition(expo)
        futureExpoCounts = await expoProposalFunctions.getExpeditionPrediction(currentGame)
        embed = await embedBuilder.buildStatusEmbed(currentGame, currentTheme, futureExpoCounts)
        await home.send(embed=embed)
        await webhookManager.processNewRoundWebhooks(currentGame, currentTheme, home, client)
        await expoProposalFunctions.resetExpedition(currentGame, currentTheme, noMentions, home, prefix)


    async def flare(ctx, currentGame, client, gagRole):
        if currentGame.online:
            Erwin = await searchFunctions.roleIDToPlayer(currentGame, 'Erwin')
            user = databaseManager.searchForUser(Erwin.user)
            userChannel = client.get_channel(user['channelID'])
            if Erwin.user == ctx.message.author and Erwin.role.abilityActive and ctx.message.channel == userChannel and currentGame.currentExpo.currentlyPicking:
                if gagRole in Erwin.user.roles:
                    await Erwin.user.remove_roles(gagRole)
                    currentGame.removeGag()
                currentGame.currentExpo.activateErwin(Erwin)
                Erwin.stats.fireFlare()

    async def erwinTakeover(currentGame, currentTheme, home, client):
        await webhookManager.erwinWebhook(currentGame, currentTheme, home, client)
        Erwin = await searchFunctions.roleIDToPlayer(currentGame, 'Erwin')
        currentGame.erwinCommander(Erwin)

                










