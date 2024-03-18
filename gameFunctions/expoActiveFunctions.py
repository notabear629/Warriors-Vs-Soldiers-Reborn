from dataFunctions.databaseManager import databaseManager

from embedBuilder import embedBuilder

from discordViewBuilder import discordViewBuilder

from gameFunctions.timerManager import timerManager
from gameFunctions.webhookManager import webhookManager
from gameFunctions.searchFunctions import searchFunctions

from gameObjects.Stats import Stats
from gameObjects.Role import Role


import random
import asyncio

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
        elif timeout and currentGame.exposOver == False:
            await home.send(f'Time to act on the {currentTheme.expeditionName} has run out. The remaining players that did not act will have a random choice chosen for them.')
            for player in currentGame.currentExpo.expeditionMembers:
                if player not in currentGame.currentExpo.expeditioned:
                    if player in currentGame.warriors:
                        randomOption = random.choice(['y', 'n'])
                        currentGame.currentExpo.actExpo(player, randomOption)
                    else:
                        currentGame.currentExpo.actExpo(player, 'y')
        if currentGame.exposOver == False:
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
            elif choice == 'Bertholdt' and player.role.id == 'Bertholdt':
                expoChoice = 'Bertholdt'
            elif type(choice) == dict and 'Mikasa' in choice and player.role.id == 'Mikasa':
                expoChoice = choice
            elif type(choice) == dict and 'Annie' in choice and player.role.id == 'Annie':
                expoChoice = choice
            elif type(choice) == dict and 'Kenny' in choice and player.role.id == 'Kenny':
                expoChoice = choice
            elif choice == 'Sabotage' and (player in currentGame.warriors or (player.role.id == 'Frecklemir' and currentGame.frecklemirTeam == 'Warriors')):
                expoChoice = 'n'
            else:
                expoChoice = 'y'
            currentGame.currentExpo.actExpo(player, expoChoice)
            user = databaseManager.searchForUser(player.user)
            userChannel = client.get_channel(user['channelID'])
            await userChannel.send('Choice Received.')
            await currentGame.sendTemporaryMessage(currentTheme, home)


    async def results(ctx, currentGame, currentTheme, home, expoPredictFunction, client, homeServer, discord):
        if currentGame.online and currentGame.currentExpo.resultsAvailable and ctx.message.channel == home:
            if currentGame.currentExpo.dazActivated:
                await webhookManager.dazWebhook(currentGame, currentTheme, home, client)
                await home.send(currentTheme.dazMessageFollowUp)
                currentGame.refundAbilities()
            else:
                if currentGame.currentRules.rumbling:
                    rumblingCheck = await expoActiveFunctions.checkRumblingClause(currentGame)
                    if rumblingCheck:
                        await expoActiveFunctions.startRumbling(currentGame, currentTheme, home, client, homeServer, discord)
                        return True
                result = await expoActiveFunctions.getExpeditionResult(currentGame)
                await expoActiveFunctions.checkFrecklemir(currentGame, currentTheme, result, client)
                await expoActiveFunctions.checkPureTitan(currentGame, currentTheme, client)
                await expoActiveFunctions.processResults(currentGame, currentTheme, result, home, expoPredictFunction)
                await webhookManager.processResultsWebhooks(currentGame, currentTheme, home, client)
                await expoActiveFunctions.processDeaths(currentGame, currentTheme, home, client)
                await Stats.processResults(currentGame, result, searchFunctions)
                await expoActiveFunctions.processKeith(currentGame, currentTheme, result)
            return True
        return False
    
    async def processKeith(currentGame, currentTheme, result):
        Keith = await searchFunctions.roleIDToPlayer(currentGame, 'Keith')
        if Keith != None and currentGame.summonedRole != None and result == 'y':
            newRoleDict = getattr(currentTheme, currentGame.summonedRole)
            newRole = Role(newRoleDict)
            newRole.resolveEmojis(currentGame.client)
            Keith.changeRole(newRole)
            message = f'You are on the side of the **{currentTheme.soldierPlural}**.\n\n{currentTheme.soldierDefaultMessage}\n\n{Keith.role.roleMessage}'
            if Keith.role.id in Role.infoMessageRoles:
                functionCall = getattr(currentTheme, f'get{Keith.role.id}Info')
                message += functionCall(currentGame)
            embed = await embedBuilder.buildRoleMessageEmbed(Keith, message, currentTheme.soldierColor, currentTheme.soldierThumbnail)
            user = databaseManager.searchForUser(Keith.user)
            userChannel = currentGame.client.get_channel(user['channelID'])
            await userChannel.send(content = Keith.user.mention, embed=embed)
            Keith.stats.changeRole(Keith.role)
            await webhookManager.sendWebhook(currentGame, currentTheme, currentGame.home, currentTheme.keithMessage, 'Keith', currentGame.client, embed=None)
            await webhookManager.sendWebhook(currentGame, currentTheme, currentGame.home, f'{Keith.role.name} {currentTheme.keithMessage2}', Keith.role.id, currentGame.client, embed=None)
    
    async def checkPureTitan(currentGame, currentTheme, client):
        if currentGame.currentRules.wildcards:
            PureTitan = await searchFunctions.roleIDToPlayer(currentGame, 'PureTitan')
            if PureTitan != None and PureTitan in currentGame.currentExpo.expeditionMembers:
                priorityOne = []
                priorityTwo = []
                priorityThree = []
                priorityFour = []
                for player in currentGame.currentExpo.expeditionMembers:
                    if player == currentGame.currentExpo.mikasaGuarded or player.role.isTitan == False or player.role.id == 'Reiner' or player.role.id == 'PureTitan' or (player.role.id == 'Armin' and currentGame.currentExpo.arminActivated):
                        continue
                    elif player in currentGame.warriors and player.role.id != 'Zeke':
                        priorityOne.append(player)
                    elif player in currentGame.soldiers and player.role.id != 'Eren':
                        priorityTwo.append(player)
                    elif player.role.id == 'Zeke':
                        priorityThree.append(player)
                    elif player.role.id == 'Eren':
                        priorityFour.append(player)
                eatenPlayer = None
                if eatenPlayer == None and priorityOne != []:
                    eatenPlayer = random.choice(priorityOne)
                if eatenPlayer == None and priorityTwo != []:
                    eatenPlayer = random.choice(priorityTwo)
                if eatenPlayer == None and priorityThree != []:
                    eatenPlayer = random.choice(priorityThree)
                if eatenPlayer == None and priorityFour != []:
                    eatenPlayer = random.choice(priorityFour)
                if eatenPlayer == None:
                    return
                currentGame.eatPlayer(PureTitan, eatenPlayer, currentTheme, client)
                message = f'You have eaten a {currentTheme.titanSingle} and joined the side of the **{PureTitan.role.team}**\n\n{PureTitan.role.roleMessage}'
                if PureTitan.role.id in Role.infoMessageRoles:
                    if PureTitan.role.team == 'Warriors':
                        functionCall = getattr(currentTheme, f'getWarriorInfo')
                        message += functionCall(currentGame, player)
                    else:
                        functionCall = getattr(currentTheme, f'get{PureTitan.role.id}Info')
                        message += functionCall(currentGame)
                if PureTitan.role.team == 'Soldiers':
                    color = currentTheme.soldierColor
                    thumbnail = currentTheme.soldierThumbnail
                if PureTitan.role.team == 'Warriors':
                    color = currentTheme.warriorColor
                    thumbnail = currentTheme.warriorThumbnail
                embed = await embedBuilder.buildRoleMessageEmbed(PureTitan, message, color, thumbnail)
                user = databaseManager.searchForUser(PureTitan.user)
                userChannel = client.get_channel(user['channelID'])
                await userChannel.send(embed=embed, content=PureTitan.user.mention)
                message = f'You have been eaten by the {eatenPlayer.role.name} and are now the new {eatenPlayer.role.name}! You have joined the side of the **{eatenPlayer.role.team}**.\n\n{eatenPlayer.role.roleMessage}'
                embed = await embedBuilder.buildRoleMessageEmbed(eatenPlayer, message, currentTheme.wildcardColor, currentTheme.wildcardThumbnail)
                user = databaseManager.searchForUser(eatenPlayer.user)
                userChannel = client.get_channel(user['channelID'])
                await userChannel.send(embed=embed, content=eatenPlayer.user.mention)
            
    async def checkFrecklemir(currentGame, currentTheme, result, client):
        if currentGame.currentRules.wildcards:
            Frecklemir = await searchFunctions.roleIDToPlayer(currentGame, 'Frecklemir')
            if Frecklemir != None and Frecklemir in currentGame.currentExpo.expeditionMembers:
                if result == 'n' or result == 'Armin':
                    currentGame.setFrecklemirTeam('Warriors')
                    color = currentTheme.warriorColor
                    thumbnail = currentTheme.warriorThumbnail
                    message = f'You have decided to join the **{currentTheme.warriorPlural}**.\n\n{currentTheme.warriorDefaultMessage}'
                else:
                    currentGame.setFrecklemirTeam('Soldiers')
                    color = currentTheme.soldierColor
                    thumbnail = currentTheme.soldierThumbnail
                    message = f'You have decided to join the **{currentTheme.soldierPlural}**.\n\n{currentTheme.soldierDefaultMessage}'
                embed = await embedBuilder.buildRoleMessageEmbed(Frecklemir, message, color, thumbnail)
                user = databaseManager.searchForUser(Frecklemir.user)
                userChannel = client.get_channel(user['channelID'])
                await userChannel.send(embed=embed, content = Frecklemir.user.mention)
                Eren = await searchFunctions.roleIDToPlayer(currentGame, 'Eren')
                if Eren != None:
                    user = databaseManager.searchForUser(Eren.user)
                    erenChannel = client.get_channel(user['channelID'])
                    embed = await embedBuilder.erenFrecklemirEmbed(currentGame, currentTheme)
                    await webhookManager.erenFrecklemirWebhook(currentGame, currentTheme, erenChannel, Eren.user.mention, embed, client)

            

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
        deathFlags = {'Armin': False, 'Levi': False, 'Sasha': False, 'Kenny' : False, 'YmirRevival' : False, 'Gabi': False}
        if currentGame.currentExpo.arminActivated:
            Armin = await searchFunctions.roleIDToPlayer(currentGame, 'Armin')
            if Armin != None:
                for player in currentGame.currentExpo.expeditionMembers:
                    if player.role.id != 'Armin':
                        currentGame.killPlayer(player, Armin, 'Armin')
                        deathFlags['Armin'] = True
        if currentGame.currentExpo.leviAttacked:
            Levi = await searchFunctions.roleIDToPlayer(currentGame, 'Levi')
            if Levi != None and len(currentGame.currentExpo.sabotagedExpedition) > 0:
                for player in currentGame.currentExpo.sabotagedExpedition:
                    if player not in currentGame.deadPlayers:
                        currentGame.killPlayer(player, Levi, 'Levi')
                        deathFlags['Levi'] = True
                for player in currentGame.currentExpo.expeditionMembers:
                    if player not in currentGame.deadPlayers and player.role.id == 'PureTitan':
                        currentGame.killPlayer(player, Levi, 'Levi')
        if currentGame.currentExpo.kennyMurdered != None:
            Kenny = await searchFunctions.roleIDToPlayer(currentGame, 'Kenny')
            if Kenny != None:
                currentGame.killPlayer(currentGame.currentExpo.kennyMurdered, Kenny, 'Kenny')
                deathFlags['Kenny'] = True
        if currentGame.sashaTargeted != None:
            Sasha = await searchFunctions.roleIDToPlayer(currentGame, 'Sasha')
            if Sasha != None and currentGame.sashaTargeted in currentGame.currentExpo.expeditionMembers and Sasha not in currentGame.currentExpo.expeditionMembers and Sasha.role.abilityActive:
                if currentGame.sashaTargeted not in currentGame.deadPlayers:
                    currentGame.killPlayer(currentGame.sashaTargeted, Sasha, 'Sasha')
                    deathFlags['Sasha'] = True
                    Sasha.role.disableAbility()
                    currentGame.currentExpo.activateSasha()
        if currentGame.gabiTargeted != None:
            Gabi = await searchFunctions.roleIDToPlayer(currentGame, 'Gabi')
            if Gabi != None and currentGame.gabiTargeted in currentGame.livingPlayers and Gabi.role.abilityActive:
                if currentGame.gabiTargeted not in currentGame.deadPlayers:
                    currentGame.woundPlayer(currentGame.gabiTargeted)
                    deathFlags['Gabi'] = True
                    Gabi.role.disableAbility()
                    currentGame.currentExpo.activateGabi()
        if currentGame.currentExpo.gabiActivated == False:
            check = currentGame.healPlayers()
            if check:
                player = currentGame.healedPlayer
                await home.send(currentTheme.getHealMessage(player))
        if currentGame.ymirRevival != None and type(currentGame.ymirRevival) != dict:
            Ymir = await searchFunctions.roleIDToPlayer(currentGame, 'Ymir')
            if Ymir != None:
                currentGame.revivePlayer(currentGame.ymirRevival)
                deathFlags['YmirRevival'] = True


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
            if arminMessage != '':
                await home.send(arminMessage)
        if deathFlags['Levi']:
            Levi = await searchFunctions.roleIDToPlayer(currentGame, 'Levi')
            leviMessage = currentTheme.getLeviDeathMessages(currentGame, currentTheme, Levi, Mikasa, Reiner)
            if leviMessage != '':
                await home.send(leviMessage)
        if deathFlags['Kenny']:
            Kenny = await searchFunctions.roleIDToPlayer(currentGame, 'Kenny')
            kennyMessage = currentTheme.getKennyDeathMessages(currentGame, currentTheme, Kenny, Mikasa, Reiner)
            if kennyMessage != '':
                await home.send(kennyMessage)
        if deathFlags['Sasha']:
            Sasha = await searchFunctions.roleIDToPlayer(currentGame, 'Sasha')
            sashaMessage = currentTheme.getSashaDeathMessages(currentGame, currentTheme, Sasha, Mikasa, Reiner)
            if sashaMessage != '':
                await home.send(sashaMessage)
        if deathFlags['Gabi']:
            Gabi = await searchFunctions.roleIDToPlayer(currentGame, 'Gabi')
            gabiMessage = currentTheme.getGabiWoundMessage(currentGame, currentTheme, Gabi)
            if gabiMessage != '':
                await home.send(gabiMessage)
        if deathFlags['YmirRevival']:
            Ymir = await searchFunctions.roleIDToPlayer(currentGame, 'Ymir')
            ymirMessage = currentTheme.getYmirRevivalMessage(currentGame, currentTheme, Ymir)
            await webhookManager.ymirRevivalWebhook(currentGame, currentTheme, home, currentTheme.ymirRevivalMessage, client)
            await home.send(ymirMessage)

    async def checkRumblingClause(currentGame):
        if currentGame.currentRound >= 3:
            rolesInExpo = []
            for player in currentGame.currentExpo.expeditionMembers:
                rolesInExpo.append(player.role.id)
            if 'Eren' in rolesInExpo and 'Zeke' in rolesInExpo:
                for player in currentGame.currentExpo.expeditionMembers:
                    if player.role.rumblingTeam.startswith('alliance'):
                        return False
                return True
        return False
    
    async def startRumbling(currentGame, currentTheme, home, client, homeServer, discord):
        currentGame.activateRumbling()
        await home.set_permissions(homeServer.default_role, send_messages=False)
        standardStatusEmbed = await embedBuilder.buildStatusEmbed(currentGame, currentTheme, currentGame.expoProjections)
        standardRumblingEmbed = await embedBuilder.rumblingStatusEmbed(currentGame, currentTheme, currentGame.expoProjections)
        altRumblingEmbed = await embedBuilder.rumblingStatusEmbed(currentGame, currentTheme, currentGame.expoProjections, True)
        embedMessage = await home.send(embed = standardStatusEmbed)
        textMessage = await home.send(currentTheme.rumblingFirstMessage)
        attachmentMessage = await home.send(currentTheme.rumblingStartAttachment)
        await asyncio.sleep(currentTheme.rumblingTimerOne)
        await embedMessage.edit(embed = altRumblingEmbed)
        await textMessage.edit(content = currentTheme.rumblingSecondMessage)
        await asyncio.sleep(currentTheme.rumblingTimerTwo)
        await textMessage.edit(content = currentTheme.rumblingThirdMessage)
        await asyncio.sleep(currentTheme.rumblingTimerThree)
        await attachmentMessage.delete()
        await embedMessage.delete()
        await textMessage.delete()
        await home.send(currentTheme.rumblingIntroMessage)
        await home.send(embed=standardRumblingEmbed)
        rumblingRolesEmbed = await embedBuilder.rumblingRolesEmbed(currentGame, currentTheme)
        await home.send(embed=rumblingRolesEmbed)
        await home.set_permissions(homeServer.default_role, send_messages=True)

        


        

