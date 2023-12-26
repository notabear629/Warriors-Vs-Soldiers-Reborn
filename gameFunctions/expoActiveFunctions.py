from dataFunctions.databaseManager import databaseManager

from embedBuilder import embedBuilder

from discordViewBuilder import discordViewBuilder

from gameFunctions.timerManager import timerManager
from gameFunctions.webhookManager import webhookManager
from gameFunctions.searchFunctions import searchFunctions


import random

class expoActiveFunctions:
    async def activateExpedition(currentGame, currentTheme, home, client, prefix):
        currentGame.currentExpo.beginExpeditioning()
        await home.send(f'The {currentTheme.expeditionName} has begun! Players that are a part of the {currentTheme.expeditionTeam} should go to their personal channels and choose what they would like to do.')
        for player in currentGame.currentExpo.expeditionMembers:
            user = databaseManager.searchForUser(player.user)
            userChannel = client.get_channel(user['channelID'])
            embed = await embedBuilder.expeditionDM(currentGame, player, currentTheme)
            view = await discordViewBuilder.expeditionChoiceView(currentGame, currentTheme, player, client, home, expoActiveFunctions.chooseExpo)
            await userChannel.send(f'{player.user.mention}')
            await userChannel.send(view=view, embed=embed)
        timeout = await timerManager.setTimer(currentGame, home, currentTheme, 'Expo')
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

    async def chooseExpo(currentGame, player, client, currentTheme, home, choice):
        if currentGame.online and currentGame.currentExpo.currentlyExpeditioning and player in currentGame.currentExpo.expeditionMembers and player not in currentGame.currentExpo.expeditioned:
            if choice == 'Armin' and player.role.id == 'Armin' and player.role.abilityActive and currentGame.roundFails < 2:
                expoChoice = 'Armin'
            elif choice == 'LeviAttack' and player.role.id == 'Levi' and player.role.abilityActive and currentGame.roundFails < 2:
                expoChoice = 'LeviAttack'
            elif choice == 'LeviDefend' and player.role.id == 'Levi' and player.role.abilityActive:
                expoChoice = 'LeviDefend'
            elif choice == 'Daz' and player.role.id == 'Daz' and player.role.abilityActive:
                expoChoice = 'Daz'
            elif type(choice) == dict and 'Mikasa' in choice and player.role.id == 'Mikasa':
                expoChoice = choice
            elif choice == 'Sabotage' and player in currentGame.warriors:
                expoChoice = 'n'
            else:
                expoChoice = 'y'
            currentGame.currentExpo.actExpo(player, expoChoice)
            user = databaseManager.searchForUser(player.user)
            userChannel = client.get_channel(user['channelID'])
            await userChannel.send('Choice Received.')
            await currentGame.sendTemporaryMessage(currentTheme, home)


    async def results(ctx, currentGame, currentTheme, home, expoPredictFunction, client):
        if currentGame.online and currentGame.currentExpo.resultsAvailable and ctx.message.channel == home:
            if currentGame.currentExpo.dazActivated:
                await webhookManager.dazWebhook(currentGame, currentTheme, home, client)
                await home.send(currentTheme.dazMessageFollowUp)
                currentGame.refundAbilities()
            else:
                result = await expoActiveFunctions.getExpeditionResult(currentGame)
                await expoActiveFunctions.processResults(currentGame, currentTheme, result, home, expoPredictFunction)
                await webhookManager.processResultsWebhooks(currentGame, currentTheme, home, client)
                await expoActiveFunctions.processDeaths(currentGame, currentTheme, home, client)
            return True
        return False
            
            

    async def getExpeditionResult(currentGame):
        if currentGame.currentExpo.arminActivated:
            return 'Armin'
        elif len(currentGame.currentExpo.sabotagedExpedition) > 0 and currentGame.currentExpo.leviDefended == False:
            return 'n'
        return 'y'
    
    async def processResults(currentGame, currentTheme, result, home, expoPredictFunction):
        currentGame.processResult(result)
        embed = await embedBuilder.results(currentGame, currentTheme, result)
        await home.send(embed=embed)
        if result == 'y':
            await home.send(f'The {currentTheme.expeditionName} was a Success!')
        elif result == 'n' or result == 'Armin':
            failMessage = f'The {currentTheme.expeditionName} was a Failure!\n\n'
            if currentGame.roundFails == 1:
                failMessage += f'{currentTheme.wallMariaBreakMessage}'
            elif currentGame.roundFails == 2:
                failMessage += f'{currentTheme.wallRoseBreakMessage}'
            elif currentGame.roundFails == 3:
                failMessage += f'{currentTheme.wallSinaBreakMessage}'
            await home.send(failMessage)

    async def processDeaths(currentGame, currentTheme, home, client):
        deathFlags = {'Armin': False, 'Levi': False, 'Sasha': False}
        if currentGame.currentExpo.arminActivated:
            Armin = await searchFunctions.roleIDToPlayer(currentGame, 'Armin')
            if Armin != None:
                for player in currentGame.currentExpo.expeditionMembers:
                    if player.role.id != 'Armin':
                        currentGame.killPlayer(player, Armin, 'Armin')
                        deathFlags['Armin'] = True
        if currentGame.currentExpo.leviAttacked:
            Levi = await searchFunctions.roleIDToPlayer(currentGame, 'Levi')
            if Levi != None:
                for player in currentGame.currentExpo.sabotagedExpedition:
                    if player not in currentGame.deadPlayers:
                        currentGame.killPlayer(player, Levi, 'Levi')
                        deathFlags['Levi'] = True
        if currentGame.sashaTargeted != None:
            Sasha = await searchFunctions.roleIDToPlayer(currentGame, 'Sasha')
            if Sasha != None and currentGame.sashaTargeted in currentGame.currentExpo.expeditionMembers and Sasha not in currentGame.currentExpo.expeditionMembers and Sasha.role.abilityActive:
                if currentGame.sashaTarget not in currentGame.deadPlayers:
                    currentGame.killPlayer(currentGame.sashaTargeted, Sasha, 'Sasha')
                    deathFlags['Sasha'] = True
                    Sasha.role.disableAbility()
                    currentGame.currentExpo.activateSasha()


        await expoActiveFunctions.processDeathMessages(currentGame, currentTheme, home, deathFlags, client)

    async def processDeathMessages(currentGame, currentTheme, home, deathFlags, client):
        Mikasa = await searchFunctions.roleIDToPlayer(currentGame, 'Mikasa')
        Reiner = await searchFunctions.roleIDToPlayer(currentGame, 'Reiner')
        if type(currentGame.currentExpo.mikasaGuarded) == dict:
            await webhookManager.mikasaWebhook(currentGame, currentTheme, home, client)
        if type(currentGame.currentExpo.reinerBlocked) == dict:
            await webhookManager.reinerWebhook(currentGame, currentTheme, home, client)
        if deathFlags['Armin']:
            Armin = await searchFunctions.roleIDToPlayer(currentGame, 'Armin')
            arminMessage = currentTheme.getArminDeathMessages(currentGame, currentTheme, Armin, Mikasa, Reiner)
            await home.send(arminMessage)
        if deathFlags['Levi']:
            Levi = await searchFunctions.roleIDToPlayer(currentGame, 'Levi')
            leviMessage = currentTheme.getLeviDeathMessages(currentGame, currentTheme, Levi, Mikasa, Reiner)
            await home.send(leviMessage)
        if deathFlags['Sasha']:
            Sasha = await searchFunctions.roleIDToPlayer(currentGame, 'Sasha')
            sashaMessage = currentTheme.getSashaDeathMessages(currentGame, currentTheme, Sasha, Mikasa, Reiner)
            await home.send(sashaMessage)

        

