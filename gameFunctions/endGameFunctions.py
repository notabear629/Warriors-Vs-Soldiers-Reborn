import discord
from discord.ext import commands

from gameObjects.Stats import Stats

from gameFunctions.expoProposalFunctions import expoProposalFunctions
from gameFunctions.timerManager import timerManager
from gameFunctions.searchFunctions import searchFunctions
from gameFunctions.webhookManager import webhookManager

from dataFunctions.userInfoManager import userInfoManager
from dataFunctions.databaseManager import databaseManager

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

        for player in currentGame.gagRole.members:
            await player.remove_roles(currentGame.gagRole)

        if currentGame.currentRules.noCoordinate:
            await endGameFunctions.noCoordinateWin(currentGame, currentTheme, home)
            return
        
        if currentGame.currentExpo != None and currentGame.roundWins == 3:
            currentGame.expeditionHistory.append(currentGame.currentExpo)
            currentGame.previousExpeditionCounts.append(currentGame.currentExpo.size)

        currentGame.activateKidnap()
        await home.send(currentTheme.basementMessage)
        await home.send(await endGameFunctions.getWarriorList(currentGame, currentTheme))
        if currentGame.currentRules.multikidnap:
            await home.send(f'Multikidnap is currently active! Each {currentTheme.warriorSingle} should select a candidate to kidnap to continue.')
            timeout = await timerManager.setTimer(currentGame, home, currentTheme, 'Multikidnap')
            if timeout == None:
                return
            elif timeout:
                await endGameFunctions.multikidnapTimeout(currentGame, currentTheme, home)     
            else:
                await endGameFunctions.processMultikidnap(currentGame, currentTheme, home)
        else:
            timeout = await timerManager.setTimer(currentGame, home, currentTheme, 'Kidnap')
            if timeout == None:
                return
            elif timeout:
                await endGameFunctions.kidnapTimeout(currentGame, currentTheme, home)     
            else:
                await endGameFunctions.processKidnap(currentGame, currentTheme, home)

    async def getWarriorList(currentGame, currentTheme):
        warriorList = f'The {currentTheme.warriorPlural} are:\n'
        for warrior in currentGame.warriors:
            warriorList += f'**{warrior.user.name}**\n'
        if currentGame.niccoloDecoy != None:
            Niccolo = await searchFunctions.roleIDToPlayer(currentGame, 'Niccolo')
            warriorList += f'The Decoy planted by **{Niccolo.role.shortName}** was **{currentGame.niccoloDecoy.user.name}**'
        return warriorList

    async def kidnapTimeout(currentGame, currentTheme, home):
        await home.send(f'{currentTheme.kidnapTimeoutMessage}')
        currentGame.setWinCondition('kidnapTimeout')
        await endGameFunctions.processEndgame(currentGame, currentTheme, home)

    async def multikidnapTimeout(currentGame, currentTheme, home):
        await home.send(f'{currentTheme.multikidnapTimeoutMessage}')
        await endGameFunctions.processMultikidnap(currentGame, currentTheme, home)
        

    async def kidnap(ctx, kidnappedUser, currentGame, currentTheme, home):
        if ctx.message.channel == home and currentGame.online and currentGame.currentlyKidnapping and currentGame.kidnappedPlayer == None:
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
                    if currentGame.currentRules.multikidnap:
                        if kidnapper in currentGame.multikidnapRecord:
                            await ctx.reply('You have already made your choice!')
                        else:
                            currentGame.multikidnapPlayer(kidnapper, kidnappedPlayer)
                            await currentGame.sendTemporaryMessage(currentTheme, home)
                    else:
                        currentGame.kidnapPlayer(kidnappedPlayer)

    async def processKidnap(currentGame, currentTheme, home):
        Eren = await searchFunctions.roleIDToPlayer(currentGame, 'Eren')
        if currentGame.kidnappedPlayer == Eren:
            await endGameFunctions.kidnapSuccess(currentGame, currentTheme, home)
        else:
            await endGameFunctions.kidnapFail(currentGame, currentTheme, home)

    async def processMultikidnap(currentGame, currentTheme, home):
        kidnapCounts = {}
        for player in currentGame.players:
            kidnapCounts[player] = 0
        for warrior, kidnapped in currentGame.multikidnapRecord.items():
            kidnapCounts[kidnapped] += 1
        topCandidates = []
        highestNumber = 0
        for player, count in kidnapCounts.items():
            if count == highestNumber:
                topCandidates.append(player)
            if count > highestNumber:
                highestNumber = count
                topCandidates = [player]
        if len(topCandidates) == 1:
            if topCandidates[0].role.id == 'Eren':
                await endGameFunctions.multikidnapSuccess(currentGame, currentTheme, home)
            else:
                await endGameFunctions.multikidnapFail(currentGame, currentTheme, home)
        else:
            await endGameFunctions.multikidnapFail(currentGame, currentTheme, home)
            


    async def kidnapSuccess(currentGame, currentTheme, home):
        await home.send(currentTheme.kidnapSuccessMessage)
        currentGame.setWinCondition('kidnapSuccess')
        await endGameFunctions.processEndgame(currentGame, currentTheme, home)

    async def kidnapFail(currentGame, currentTheme, home):
        await home.send(currentTheme.kidnapFailMessage)
        currentGame.setWinCondition('kidnapFail')
        await endGameFunctions.processEndgame(currentGame, currentTheme, home)

    async def multikidnapSuccess(currentGame, currentTheme, home):
        await home.send(currentTheme.multikidnapSuccessMessage)
        currentGame.setWinCondition('multikidnapSuccess')
        await endGameFunctions.processEndgame(currentGame, currentTheme, home)

    async def multikidnapFail(currentGame, currentTheme, home):
        await home.send(currentTheme.multikidnapFailMessage)
        currentGame.setWinCondition('multikidnapFail')
        await endGameFunctions.processEndgame(currentGame, currentTheme, home)

    async def sendMultikidnapWarriorWinners(currentGame, currentTheme, home):
        warriorWinMessage = currentTheme.getVictoriousWarriors(currentGame, currentTheme)
        if warriorWinMessage != None:
            await home.send(warriorWinMessage)

    async def noCoordinateWin(currentGame, currentTheme, home):
        await home.send(currentTheme.noCordSuccessMessage)
        currentGame.setWinCondition('noCoordinateWin')
        await endGameFunctions.processEndgame(currentGame, currentTheme, home)

    async def processEndgame(currentGame, currentTheme, home):
        await currentGame.processWinners()
        await Stats.processMVP(currentGame)
        await endGameFunctions.processEndgameStats(currentGame)
        if currentGame.winCondition == 'multikidnapSuccess' or currentGame.winCondition == 'multikidnapFail':
            await endGameFunctions.sendMultikidnapWarriorWinners(currentGame, currentTheme, home)
        embed = await embedBuilder.endgame(currentGame, currentTheme)
        await home.send(embed=embed)
        if currentGame.currentRules.casual == False:
            embed = await embedBuilder.scoreboard(currentGame, currentTheme)
            await home.send(embed=embed)
            if len(currentGame.MVP) == 1:
                await home.send(f'{currentTheme.emojiMVP}{currentGame.MVP[0].user.mention} has won Match MVP with **{currentGame.MVP[0].mvpPoints}** MVP Points!{currentTheme.emojiMVP}')
            else:
                await home.send(f'{currentTheme.emojiMVP} Multiple players won Match MVP with **{currentGame.MVP[0].mvpPoints}** MVP Points!{currentTheme.emojiMVP}')
        if currentGame.currentRules.casual == False:
            await endGameFunctions.saveStats(currentGame)
            await endGameFunctions.notifyBadges(currentGame, home)
            await userInfoManager.fixDatabase(None, currentGame.homeServer, currentGame.userCategory, currentTheme, currentGame.prefix, currentGame.badges)
            await endGameFunctions.notifyTitles(currentGame, home)
            embed = await embedBuilder.pointsBoard(currentGame, currentTheme)
            await home.send(embed=embed)
            

    async def processEndgameStats(currentGame):
        for player in currentGame.players:
            player.stats.processEndgame(player, currentGame)
        await Stats.processELO(currentGame)

    async def notifyBadges(currentGame, home):
        badgeUpdates = await endGameFunctions.checkUserBadges(currentGame)
        for badgeUpdate in badgeUpdates:
            if badgeUpdate != "":
                await home.send(badgeUpdate)

    async def notifyTitles(currentGame, home):
        titleUpdates = await endGameFunctions.checkUserTitles(currentGame)
        for titleUpdate in titleUpdates:
            if titleUpdate != "":
                await home.send(titleUpdate)

    async def checkUserBadges(currentGame):
        badgeStrings = []
        for player in currentGame.players:
            badgeString = ""
            loadedBadges = currentGame.badges
            for badgeType, value in loadedBadges.badgeTitles.items():
                wvsPlayer = databaseManager.getWvsPlayerByID(player.user.id)
                badgeInfo = loadedBadges.getBadgeOutput(badgeType, wvsPlayer['stats'][badgeType])
                if badgeInfo['badge'] != wvsPlayer['badges'][badgeType]:
                    if badgeString != "":
                        badgeString += '\n\n'
                    badgeString += f'{badgeInfo['emoji']}{player.user.mention} has earned the **{badgeInfo['badge']}** badge for {badgeInfo['title']}! (+**{badgeInfo['points']}**BP)'
            totalRank = loadedBadges.getTotalBadgeOutput(wvsPlayer)
            if wvsPlayer['badges']['Rank'] != totalRank['badge']:
                if badgeString != "":
                    badgeString += '\n\n'
                badgeString += f'{totalRank['emoji']}{player.user.mention} has leveled up to the **{totalRank['badge']}** Badge Rank!'
            badgeStrings.append(badgeString)
        return badgeStrings
    
    async def checkUserTitles(currentGame):
        titleStrings = []
        for player in currentGame.players:
            titleString = ""
            loadedBadges = currentGame.badges
            db = databaseManager.getWvsPlayerByID(player.user.id)
            for title in db['titles']:
                if title not in player.oldTitles:
                    if titleString != "":
                        titleString += '\n\n'
                    titleString += f'{getattr(loadedBadges, f'emoji{title}')}{player.user.mention} has earned the title of **{getattr(loadedBadges, 'titleAnnouncements')[title]}**!'
            titleStrings.append(titleString)
        return titleStrings

    async def saveStats(currentGame):
        for player in currentGame.players:
            statDict = {}
            for key, value in vars(player.stats).items():
                if key.startswith('__'):
                    continue
                else:
                    statDict[key] = value
            databaseManager.tallyStatsByID(player.user.id, statDict)
            

    async def skipToBasement(ctx, currentGame, currentTheme, home, client, gagRole):
        if currentGame.online and currentGame.exposOver == False:
            Zeke = await searchFunctions.roleIDToPlayer(currentGame, 'Zeke')
            user = databaseManager.searchForUser(Zeke.user)
            zekeChannel = client.get_channel(user['channelID'])
            if ctx.message.author == Zeke.user and ctx.message.channel == zekeChannel:
                if currentGame.currentRules.noCoordinate:
                    await ctx.reply('There is no Coordinate! You cannot retreat!')
                    return
                currentGame.skipExpos()
                await ctx.reply('Retreat Confirmed!')
                if currentGame.porcoGagged != None:
                    for user in currentGame.gagRole.members:
                        await user.remove_roles(currentGame.gagRole)
                    currentGame.removeGag()
                futureExpoCounts = await expoProposalFunctions.getExpeditionPrediction(currentGame)
                embed = await embedBuilder.buildStatusEmbed(currentGame, currentTheme, futureExpoCounts)
                await home.send(embed=embed)
                await webhookManager.basementSkipWebhook(currentGame, currentTheme, home, client)
                await endGameFunctions.reachBasement(currentGame, currentTheme, home)

    