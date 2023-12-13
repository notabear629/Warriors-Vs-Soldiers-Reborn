from dataFunctions.databaseManager import databaseManager

from embedBuilder import embedBuilder

from discordViewBuilder import discordViewBuilder

from gameFunctions.timerManager import timerManager

import random

class expoActiveFunctions:
    async def activateExpedition(currentGame, currentTheme, home, client, prefix):
        currentGame.currentExpo.beginExpeditioning()
        await home.send(f'The {currentTheme.expeditionName} has begun! Players that are a part of the {currentTheme.expeditionTeam} should go to their personal channels and choose what they would like to do.')
        for player in currentGame.currentExpo.expeditionMembers:
            user = databaseManager.searchForUser(player.user)
            userChannel = client.get_channel(user['channelID'])
            embed = await embedBuilder.expeditionDM(currentGame, player, currentTheme)
            view = await discordViewBuilder.expeditionChoiceView(currentGame, currentTheme, player, client, home, expoActiveFunctions.passExpo, expoActiveFunctions.sabotageExpo)
            await userChannel.send(f'{player.user.mention}')
            await userChannel.send(view=view, embed=embed)
        timeout = await timerManager.setTimer(currentGame, 'Expo')
        if timeout == None:
            return
        elif timeout:
            await home.send(f'Time to act on the {currentTheme.expeditionName} has run out. The remaining players that did not act will have a random choice chosen for them.')
            for player in currentGame.currentExpo.expeditionMembers:
                if player not in currentGame.currentExpo.expeditioned:
                    if player in currentGame.warriors:
                        randomOption = random.choice(['y', 'n'])
                        currentGame.currentExpo.actExpo(player, randomOption)
                    else:
                        currentGame.currentExpo.actExpo(player, 'y')
        await home.send(f'The {currentTheme.expeditionName} results are in! Use `{prefix}results` to view them!')

    async def passExpo(currentGame, player, client, currentTheme, home):
        if currentGame != None and currentGame.currentExpo.currentlyExpeditioning and player in currentGame.currentExpo.expeditionMembers and player not in currentGame.currentExpo.expeditioned:
            currentGame.currentExpo.actExpo(player, 'y')
            user = databaseManager.searchForUser(player.user)
            userChannel = client.get_channel(user['channelID'])
            await userChannel.send('Choice Received.')
            await currentGame.sendTemporaryMessage(currentTheme, home)

    async def sabotageExpo(currentGame, player, client, currentTheme, home):
        if currentGame != None and currentGame.currentExpo.currentlyExpeditioning and player in currentGame.currentExpo.expeditionMembers and player not in currentGame.currentExpo.expeditioned:
            currentGame.currentExpo.actExpo(player, 'n')
            user = databaseManager.searchForUser(player.user)
            userChannel = client.get_channel(user['channelID'])
            await userChannel.send('Choice Received.')
            await currentGame.sendTemporaryMessage(currentTheme, home)

    async def results(ctx, currentGame, currentTheme, home, expoPredictFunction):
        if currentGame != None and currentGame.currentExpo.resultsAvailable and ctx.message.channel == home:
            result = await expoActiveFunctions.getExpeditionResult(currentGame)
            embed = await embedBuilder.results(currentGame, currentTheme, result)
            await expoActiveFunctions.processResults(currentGame, currentTheme, result, home, expoPredictFunction)
            

    async def getExpeditionResult(currentGame):
        if len(currentGame.currentExpo.sabotagedExpedition) > 0:
            return 'n'
        return 'y'
    
    async def processResults(currentGame, currentTheme, result, home, expoPredictFunction):
        currentGame.processResult(result)
        embed = await embedBuilder.results(currentGame, currentTheme, result)
        await home.send(embed=embed)
        if result == 'y':
            await home.send(f'The {currentTheme.expeditionName} was a Success!')
        elif result == 'n':
            failMessage = f'The {currentTheme.expeditionName} was a Failure!\n\n'
            if currentGame.roundFails == 1:
                failMessage += f'{currentTheme.wallMariaBreakMessage}'
            elif currentGame.roundFails == 2:
                failMessage += f'{currentTheme.wallRoseBreakMessage}'
            elif currentGame.roundFails == 3:
                failMessage += f'{currentTheme.wallSinaBreakMessage}'
            await home.send(failMessage)

