from dataFunctions.databaseManager import databaseManager

from embedBuilder import embedBuilder

from discordViewBuilder import discordViewBuilder

from gameFunctions.timerManager import timerManager
from gameFunctions.webhookManager import webhookManager
from gameFunctions.searchFunctions import searchFunctions

from gameObjects.Stats import Stats
from gameObjects.Role import Role
from gameObjects.Player import Player


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
            await userChannel.send(f'{player.user.mention}',view=view, embed=embed)
        Onyankpon = await searchFunctions.roleIDToPlayer(currentGame, 'Onyankopon')
        if Onyankpon != None and Onyankpon.role.abilityActive:
            user = databaseManager.searchForUser(Onyankpon.user)
            userChannel = client.get_channel(user['channelID'])
            view = await discordViewBuilder.onyankoponPilotView(currentGame, Onyankpon)
            await userChannel.send(f'{Onyankpon.user.mention}, Would you like to fly someone in?', view=view)
        timeout = await timerManager.setTimer(currentGame, home, currentTheme, 'Expo', [expoActiveFunctions.onyankoponFly])
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
            if choice == 'Armin' and (player.role.id == 'Armin' or player.role.id == 'Warhammer') and player.role.abilityActive and currentGame.roundFails < 2:
                expoChoice = 'Armin'
            elif choice == 'LeviAttack' and (player.role.id == 'Levi' or player.role.id == 'Warhammer') and player.role.abilityActive and currentGame.roundFails < 2:
                expoChoice = 'LeviAttack'
            elif choice == 'LeviDefend' and (player.role.id == 'Levi' or player.role.id == 'Warhammer') and player.role.abilityActive:
                expoChoice = 'LeviDefend'
            elif choice == 'Daz' and (player.role.id == 'Daz' or player.role.id == 'Warhammer') and player.role.abilityActive:
                expoChoice = 'Daz'
            elif choice == 'Rico' and player.role.id == 'Rico' and player.role.abilityActive:
                expoChoice = 'Rico'
            elif choice == 'Bertholdt' and player.role.id == 'Bertholdt':
                expoChoice = 'Bertholdt'
            elif choice == 'Ksaver' and player.role.id == 'Ksaver' and player.role.abilityActive:
                expoChoice = 'Ksaver'
            elif type(choice) == dict and 'Mikasa' in choice and player.role.id == 'Mikasa':
                expoChoice = choice
            elif type(choice) == dict and 'Petra' in choice and (player.role.id == 'Petra' or player.role.id == 'Warhammer'):
                expoChoice = choice
            elif type(choice) == dict and 'Frecklemir' in choice and (player.role.id == 'Frecklemir' or player.role.id == 'Warhammer'):
                expoChoice = choice
            elif type(choice) == dict and 'Hange' in choice and player.role.id == 'Hange':
                expoChoice = choice
            elif choice == 'Hannes' and (player.role.id == 'Hannes' or player.role.id == 'Warhammer') and player.role.abilityActive:
                expoChoice = 'Hannes'
            elif choice == 'Marco' and (player.role.id == 'Marco' or (player.role.id == 'Warhammer' and player.role.abilityActive)):
                expoChoice = 'Marco'
            elif type(choice) == dict and 'Willy' in choice and player.role.id == 'Willy':
                expoChoice = choice
            elif type(choice) == dict and 'Kenny' in choice and player.role.id == 'Kenny':
                expoChoice = choice
            elif choice == 'Sabotage' and player in currentGame.warriors:
                expoChoice = 'n'
            else:
                if player in currentGame.warriors and player == currentGame.friedaVowedPlayer:
                    expoChoice = 'n'
                else:
                    expoChoice = 'y'
            currentGame.currentExpo.actExpo(player, expoChoice)
            user = databaseManager.searchForUser(player.user)
            userChannel = client.get_channel(user['channelID'])
            await userChannel.send('Choice Received.')
            await currentGame.sendTemporaryMessage(currentTheme, home)
            if player == currentGame.hangeWiretapped:
                await webhookManager.processHangeWebhook(currentGame, currentTheme, choice)


    async def results(ctx, currentGame, currentTheme, home, expoPredictFunction, client, homeServer, discord):
        if currentGame.online and currentGame.currentExpo.resultsAvailable and ctx.message.channel == home:
            if currentGame.currentExpo.dazActivated or currentGame.currentExpo.warhammerActivated == 'Daz':
                await webhookManager.dazWebhook(currentGame, currentTheme, home, client)
                await home.send(currentTheme.dazMessageFollowUp)
                currentGame.refundAbilities()
            else:
                if currentGame.currentRules.rumbling:
                    rumblingCheck = await expoActiveFunctions.checkRumblingClause(currentGame)
                    if rumblingCheck:
                        await expoActiveFunctions.startRumbling(currentGame, currentTheme, home, client, homeServer, discord)
                        if currentGame.porcoGagged != None:
                            Marcel = await searchFunctions.roleIDToPlayer(currentGame, 'Marcel')
                            for user in currentGame.gagRole.members:
                                if Marcel == None or (Marcel != None and user not in currentGame.deadSoldiers):
                                    await user.remove_roles(currentGame.gagRole)
                            currentGame.removeGag()
                        return True
                Hannes = await searchFunctions.roleIDToPlayer(currentGame, 'Hannes')
                if Hannes != None and currentGame.currentExpo.hannesActivated == Hannes:
                    currentGame.currentExpo.ejectPlayer(Hannes)
                Warhammer = await searchFunctions.roleIDToPlayer(currentGame, 'Warhammer')
                if Warhammer != None and currentGame.currentExpo.warhammerActivated == 'Hannes':
                    currentGame.currentExpo.ejectPlayer(Warhammer)
                result = await expoActiveFunctions.getExpeditionResult(currentGame)
                await expoActiveFunctions.checkPureTitan(currentGame, currentTheme, client)
                await expoActiveFunctions.processResults(currentGame, currentTheme, result, home, expoPredictFunction)
                await webhookManager.processResultsWebhooks(currentGame, currentTheme, home, client)
                await expoActiveFunctions.processDeaths(currentGame, currentTheme, home, client)
                await Stats.processResults(currentGame, result, searchFunctions)
                await expoActiveFunctions.processKeith(currentGame, currentTheme, result)
                currentGame.updateExpoPlayers()
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


    async def getExpeditionResult(currentGame):
        if currentGame.currentExpo.arminActivated or currentGame.currentExpo.warhammerActivated == 'Armin':
            return 'Armin'
        elif len(currentGame.currentExpo.sabotagedExpedition) > 0 and (currentGame.currentExpo.leviDefended == False and currentGame.currentExpo.warhammerActivated != 'LeviDefend'):
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
        if currentGame.currentExpo.ksaverBlackout:
            currentGame.setBlackoutRound()

    async def processDeaths(currentGame, currentTheme, home, client):
        deathFlags = {'Armin': False, 'Levi': False, 'Sasha': False, 'Marco': False, 'Kenny' : False, 'YmirRevival' : False, 'Gabi': False, 'Petra':False, 'Rico':False, 'Frecklemir':False, 'Willy':False, 'WarhammerArmin':False, 'WarhammerLevi':False, 'WarhammerPetra':False, 'WarhammerMarco':False, 'WarhammerSasha':False, 'WarhammerRico':False, 'WarhammerFrecklemir':False}
        if currentGame.currentExpo.arminActivated:
            Armin = await searchFunctions.roleIDToPlayer(currentGame, 'Armin')
            if Armin != None:
                for player in currentGame.currentExpo.expeditionMembers:
                    if player.role.id != 'Armin':
                        await currentGame.killPlayer(player, Armin, 'Armin')
                        deathFlags['Armin'] = True
        if currentGame.currentExpo.warhammerActivated == 'Armin':
            Warhammer = await searchFunctions.roleIDToPlayer(currentGame, 'Warhammer')
            if Warhammer != None:
                for player in currentGame.currentExpo.expeditionMembers:
                    if player.role.id != 'Warhammer' and player in currentGame.warriors and player not in currentGame.deadPlayers:
                        await currentGame.killPlayer(player, Warhammer, 'Armin')
                        deathFlags['WarhammerArmin'] = True
        if currentGame.currentExpo.leviAttacked:
            Levi = await searchFunctions.roleIDToPlayer(currentGame, 'Levi')
            if Levi != None and len(currentGame.currentExpo.sabotagedExpedition) > 0:
                for player in currentGame.currentExpo.sabotagedExpedition:
                    if player not in currentGame.deadPlayers:
                        await currentGame.killPlayer(player, Levi, 'Levi')
                        deathFlags['Levi'] = True
                for player in currentGame.currentExpo.expeditionMembers:
                    if player not in currentGame.deadPlayers and player.role.id == 'PureTitan':
                        await currentGame.killPlayer(player, Levi, 'Levi')
        if currentGame.currentExpo.warhammerActivated == 'LeviAttack':
            Warhammer = await searchFunctions.roleIDToPlayer(currentGame, 'Warhammer')
            if Warhammer != None and len(currentGame.currentExpo.sabotagedExpedition) > 0:
                for player in currentGame.currentExpo.sabotagedExpedition:
                    if player not in currentGame.deadPlayers:
                        await currentGame.killPlayer(player, Warhammer, 'Levi')
                        deathFlags['WarhammerLevi'] = True
                for player in currentGame.currentExpo.expeditionMembers:
                    if player not in currentGame.deadPlayers and player.role.id == 'PureTitan':
                        await currentGame.killPlayer(player, Warhammer, 'Levi')
        if currentGame.ricoTargeted != None and currentGame.ricoFired and not currentGame.ricoTrapped:
            currentGame.ricoTrap()
            Rico = await searchFunctions.roleIDToPlayer(currentGame, 'Rico')
            if Rico != None and currentGame.ricoTargeted in currentGame.currentExpo.sabotagedExpedition:
                if currentGame.ricoTargeted not in currentGame.deadPlayers:
                    await currentGame.killPlayer(currentGame.ricoTargeted, Rico, 'Rico')
                    deathFlags['Rico'] = True
        if type(currentGame.warhammerAbility) == dict and 'Rico' in currentGame.warhammerAbility:
            Warhammer = await searchFunctions.roleIDToPlayer(currentGame, 'Warhammer')
            if Warhammer != None and currentGame.warhammerAbility['Rico'] in currentGame.currentExpo.sabotagedExpedition and Warhammer.role.abilityActive:
                if currentGame.warhammerAbility['Rico'] not in currentGame.deadPlayers:
                    await currentGame.killPlayer(currentGame.warhammerAbility['Rico'], Warhammer, 'Rico')
                    deathFlags['WarhammerRico'] = True
        if currentGame.currentExpo.petraWatched != None:
            Petra = await searchFunctions.roleIDToPlayer(currentGame, 'Petra')
            if Petra != None and currentGame.currentExpo.petraWatched in currentGame.currentExpo.sabotagedExpedition:
                if currentGame.currentExpo.petraWatched not in currentGame.deadPlayers:
                    await currentGame.killPlayer(currentGame.currentExpo.petraWatched, Petra, 'Petra')
                    deathFlags['Petra'] = True
        if type(currentGame.currentExpo.warhammerActivated) == dict and 'Petra' in currentGame.currentExpo.warhammerActivated:
            Warhammer = await searchFunctions.roleIDToPlayer(currentGame, 'Warhammer')
            if Warhammer != None and currentGame.currentExpo.warhammerActivated['Petra'] in currentGame.currentExpo.sabotagedExpedition and currentGame.currentExpo.warhammerActivated['Petra'] not in currentGame.deadPlayers:
                await currentGame.killPlayer(currentGame.currentExpo.warhammerActivated['Petra'], Warhammer, 'Petra')
                deathFlags['WarhammerPetra'] = True
        if currentGame.currentExpo.kennyMurdered != None and currentGame.currentExpo.kennyMurdered in currentGame.currentExpo.expeditionMembers:
            Kenny = await searchFunctions.roleIDToPlayer(currentGame, 'Kenny')
            if Kenny != None:
                await currentGame.killPlayer(currentGame.currentExpo.kennyMurdered, Kenny, 'Kenny')
                deathFlags['Kenny'] = True
        if currentGame.currentExpo.frecklemirMauled != None:
            Frecklemir = await searchFunctions.roleIDToPlayer(currentGame, 'Frecklemir')
            if Frecklemir != None and currentGame.currentExpo.frecklemirMauled in currentGame.currentExpo.expeditionMembers:
                if currentGame.currentExpo.frecklemirMauled not in currentGame.deadPlayers:
                    await currentGame.killPlayer(currentGame.currentExpo.frecklemirMauled, Frecklemir, 'Frecklemir')
                    deathFlags['Frecklemir'] = True
        if type(currentGame.currentExpo.warhammerActivated) == dict and 'Frecklemir' in currentGame.currentExpo.warhammerActivated:
            Warhammer = await searchFunctions.roleIDToPlayer(currentGame, 'Warhammer')
            if Warhammer != None and currentGame.currentExpo.warhammerActivated['Frecklemir'] in currentGame.currentExpo.expeditionMembers and currentGame.currentExpo.warhammerActivated['Frecklemir'] in currentGame.warriors:
                if currentGame.currentExpo.warhammerActivated['Frecklemir'] not in currentGame.deadPlayers:
                    await currentGame.killPlayer(currentGame.currentExpo.warhammerActivated['Frecklemir'], Warhammer, 'Frecklemir')
                    deathFlags['WarhammerFrecklemir'] = True
        if currentGame.currentExpo.willyBombed != None:
            Willy = await searchFunctions.roleIDToPlayer(currentGame, 'Willy')
            if Willy != None:
                await currentGame.killPlayer(Willy, Willy, 'Willy')
                deathFlags['Willy'] = True
                if currentGame.currentExpo.willyBombed in currentGame.currentExpo.expeditionMembers:
                    await currentGame.killPlayer(currentGame.currentExpo.willyBombed, Willy, 'Willy')
        if currentGame.sashaTargeted != None:
            Sasha = await searchFunctions.roleIDToPlayer(currentGame, 'Sasha')
            if Sasha != None and currentGame.sashaTargeted in currentGame.currentExpo.expeditionMembers and Sasha not in currentGame.currentExpo.expeditionMembers and Sasha.role.abilityActive:
                if currentGame.sashaTargeted not in currentGame.deadPlayers:
                    await currentGame.killPlayer(currentGame.sashaTargeted, Sasha, 'Sasha')
                    deathFlags['Sasha'] = True
                    Sasha.role.disableAbility()
                    currentGame.currentExpo.activateSasha()
        if type(currentGame.warhammerAbility) == dict and 'Sasha' in currentGame.warhammerAbility:
            Warhammer = await searchFunctions.roleIDToPlayer(currentGame, 'Warhammer')
            if Warhammer != None and currentGame.warhammerAbility['Sasha'] in currentGame.currentExpo.expeditionMembers and Warhammer not in currentGame.currentExpo.expeditionMembers and Warhammer.role.abilityActive:
                if currentGame.warhammerAbility['Sasha'] not in currentGame.deadPlayers:
                    await currentGame.killPlayer(currentGame.warhammerAbility['Sasha'], Warhammer, 'Sasha')
                    deathFlags['WarhammerSasha'] = True
                    Warhammer.role.disableAbility()
                    currentGame.currentExpo.changeWarhammerAbility('Sasha')
        if currentGame.currentExpo.marcoActivated:
            Marco = await searchFunctions.roleIDToPlayer(currentGame, 'Marco')
            if Marco not in currentGame.deadPlayers:
                await currentGame.killPlayer(Marco, Marco, 'Marco')
                deathFlags['Marco'] = True
        if currentGame.currentExpo.warhammerActivated == 'Marco':
            Warhammer = await searchFunctions.roleIDToPlayer(currentGame, 'Warhammer')
            if Warhammer not in currentGame.deadPlayers:
                await currentGame.killPlayer(Warhammer, Warhammer, 'Marco')
                deathFlags['WarhammerMarco'] = True
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
        Marlowe = await searchFunctions.roleIDToPlayer(currentGame, 'Marlowe')
        if Marlowe != None and Marlowe in currentGame.livingPlayers:
            marloweFlag = False
            for key, value in deathFlags.items():
                if value:
                    marloweFlag = True
                    break
            if marloweFlag:
                user = databaseManager.searchForUser(Marlowe.user)
                userChannel = client.get_channel(user['channelID'])
                embed = await embedBuilder.marloweMessageEmbed(currentGame, currentTheme)
                await webhookManager.sendWebhook(currentGame, currentTheme, userChannel, f'{Marlowe.user.mention}', 'Marlowe', client, embed)
                Marlowe.stats.processBodyID(currentGame)


        await expoActiveFunctions.processDeathMessages(currentGame, currentTheme, home, deathFlags, client)
        if type(currentGame.mikasaGuarded) == dict:
            Mikasa = await searchFunctions.roleIDToPlayer(currentGame, 'Mikasa')
            currentGame.guardPlayer(None)
            Mikasa.role.disableAbility()
            if currentGame.currentRules.casual == False:
                Mikasa.stats.guardPlayer()
        elif type(currentGame.mikasaGuarded) == Player:
            Mikasa = await searchFunctions.roleIDToPlayer(currentGame, 'Mikasa')
            if currentGame.currentRules.casual == False:
                Mikasa.stats.guardPlayer()
        await expoActiveFunctions.updateMarcelGag(currentGame.gagRole, currentGame)

    async def updateMarcelGag(gagRole, currentGame):
        Marcel = await searchFunctions.roleIDToPlayer(currentGame, 'Marcel')
        if Marcel != None:
            for player in currentGame.deadPlayers:
                if player in currentGame.soldiers:
                    if gagRole not in player.user.roles:
                        await player.user.add_roles(gagRole)

    async def onyankoponFly(currentGame):
        Onyankopon = await searchFunctions.roleIDToPlayer(currentGame, 'Onyankopon')
        await webhookManager.onyankoponWebhook(currentGame, currentGame.currentTheme, currentGame.home, currentGame.client)
        msg = currentGame.currentTheme.getPlaneMessage(currentGame, Onyankopon, currentGame.currentExpo.playerFlown)
        await currentGame.home.send(msg)
        currentGame.currentExpo.flyIn(currentGame.currentExpo.playerFlown)
        player = currentGame.currentExpo.playerFlown
        user = databaseManager.searchForUser(player.user)
        userChannel = currentGame.client.get_channel(user['channelID'])
        embed = await embedBuilder.expeditionDM(currentGame, player, currentGame.currentTheme)
        view = await discordViewBuilder.expeditionChoiceView(currentGame, currentGame.currentTheme, player, currentGame.client, currentGame.home, expoActiveFunctions.chooseExpo)
        await userChannel.send(f'{player.user.mention}',view=view, embed=embed)
        Hitch = await searchFunctions.roleIDToPlayer(currentGame, 'Hitch')
        if Hitch != None:
            hitchInfo = {'Onyankopon':Onyankopon}
            user = databaseManager.searchForUser(Hitch.user)
            userChannel = currentGame.client.get_channel(user['channelID'])
            hitchMessage = currentGame.currentTheme.getHitchInfo(currentGame, Hitch, hitchInfo)
            embed = await embedBuilder.infoUpdate(currentGame.currentTheme, Hitch, hitchMessage)
            await webhookManager.sendWebhook(currentGame, currentGame.currentTheme, userChannel, f'{Hitch.user.mention}', 'Hitch', currentGame.client)
            await webhookManager.sendWebhook(currentGame, currentGame.currentTheme, userChannel, '', 'Hitch', currentGame.client, embed)

                        

    async def processDeathMessages(currentGame, currentTheme, home, deathFlags, client):
        Mikasa = await searchFunctions.roleIDToPlayer(currentGame, 'Mikasa')
        Reiner = await searchFunctions.roleIDToPlayer(currentGame, 'Reiner')
        if type(currentGame.mikasaGuarded) == dict:
            await webhookManager.mikasaWebhook(currentGame, currentTheme, home, client)
        if type(currentGame.currentExpo.reinerBlocked) == dict:
            await webhookManager.reinerWebhook(currentGame, currentTheme, home, client)
        if deathFlags['Armin']:
            Armin = await searchFunctions.roleIDToPlayer(currentGame, 'Armin')
            arminMessage = currentTheme.getArminDeathMessages(currentGame, currentTheme, Armin, Mikasa, Reiner)
            if arminMessage != '':
                await home.send(arminMessage)
        if deathFlags['WarhammerArmin']:
            Warhammer = await searchFunctions.roleIDToPlayer(currentGame, 'Warhammer')
            warhammerMessage = currentTheme.getArminDeathMessages(currentGame, currentTheme, Warhammer, Mikasa, Reiner)
            if warhammerMessage != '':
                await home.send(warhammerMessage)
        if deathFlags['Levi']:
            Levi = await searchFunctions.roleIDToPlayer(currentGame, 'Levi')
            leviMessage = currentTheme.getLeviDeathMessages(currentGame, currentTheme, Levi, Mikasa, Reiner)
            if leviMessage != '':
                await home.send(leviMessage)
        if deathFlags['WarhammerLevi']:
            Warhammer = await searchFunctions.roleIDToPlayer(currentGame, 'Warhammer')
            warhammerMessage = currentTheme.getLeviDeathMessages(currentGame, currentTheme, Warhammer, Mikasa, Reiner)
            if warhammerMessage != '':
                await home.send(warhammerMessage)
        if deathFlags['Rico']:
            Rico = await searchFunctions.roleIDToPlayer(currentGame, 'Rico')
            ricoMessage = currentTheme.getRicoDeathMessages(currentGame, currentTheme, Rico, Mikasa, Reiner)
            if ricoMessage != '':
                await home.send(ricoMessage)
        if deathFlags['WarhammerRico']:
            Warhammer = await searchFunctions.roleIDToPlayer(currentGame, 'Warhammer')
            warhammerMessage = currentTheme.getRicoDeathMessages(currentGame, currentTheme, Warhammer, Mikasa, Reiner)
            if warhammerMessage != '':
                await home.send(warhammerMessage)
        if deathFlags['Petra']:
            Petra = await searchFunctions.roleIDToPlayer(currentGame, 'Petra')
            petraMessage = currentTheme.getPetraDeathMessages(currentGame, currentTheme, Petra, Mikasa, Reiner)
            if petraMessage != '':
                await home.send(petraMessage)
        if deathFlags['WarhammerPetra']:
            Warhammer = await searchFunctions.roleIDToPlayer(currentGame, 'Warhammer')
            warhammerMessage = currentTheme.getPetraDeathMessages(currentGame, currentTheme, Warhammer, Mikasa, Reiner)
            if warhammerMessage != '':
                await home.send(warhammerMessage)
        if deathFlags['Kenny']:
            Kenny = await searchFunctions.roleIDToPlayer(currentGame, 'Kenny')
            kennyMessage = currentTheme.getKennyDeathMessages(currentGame, currentTheme, Kenny, Mikasa, Reiner)
            if kennyMessage != '':
                await home.send(kennyMessage)
        if deathFlags['Frecklemir']:
            Frecklemir = await searchFunctions.roleIDToPlayer(currentGame, 'Frecklemir')
            frecklemirMessage = currentTheme.getFrecklemirDeathMessages(currentGame, currentTheme, Frecklemir, Mikasa, Reiner)
            if frecklemirMessage != '':
                await home.send(frecklemirMessage)
        if deathFlags['WarhammerFrecklemir']:
            Warhammer = await searchFunctions.roleIDToPlayer(currentGame, 'Warhammer')
            warhammerMessage = currentTheme.getFrecklemirDeathMessages(currentGame, currentTheme, Warhammer, Mikasa, Reiner)
            if warhammerMessage != '':
                await home.send(warhammerMessage)
        if deathFlags['Willy']:
            Willy = await searchFunctions.roleIDToPlayer(currentGame, 'Willy')
            willyMessage = currentTheme.getWillyDeathMessages(currentGame, currentTheme, Willy, Mikasa, Reiner)
            if willyMessage != '':
                await home.send(willyMessage)
        if deathFlags['Sasha']:
            Sasha = await searchFunctions.roleIDToPlayer(currentGame, 'Sasha')
            sashaMessage = currentTheme.getSashaDeathMessages(currentGame, currentTheme, Sasha, Mikasa, Reiner)
            if sashaMessage != '':
                await home.send(sashaMessage)
        if deathFlags['WarhammerSasha']:
            Warhammer = await searchFunctions.roleIDToPlayer(currentGame, 'Warhammer')
            Sasha = await searchFunctions.roleIDToRoleFromLoadedRoles(currentGame.loadedRoles, 'Sasha')
            warhammerMessage = currentTheme.getSashaDeathMessages(currentGame, currentTheme, Warhammer, Mikasa, Reiner, Sasha)
            if warhammerMessage != '':
                await home.send(warhammerMessage)
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
        if deathFlags['Marco']:
            Marco = await searchFunctions.roleIDToPlayer(currentGame, 'Marco')
            marcoMessage = currentTheme.getMarcoDeathMessages(currentGame, currentTheme, Marco)
            if marcoMessage != '':
                await webhookManager.marcoWebhook(currentGame, currentTheme, home, client)
                await home.send(marcoMessage)
        if deathFlags['WarhammerMarco']:
            Warhammer = await searchFunctions.roleIDToPlayer(currentGame, 'Warhammer')
            warhammerMessage = currentTheme.getMarcoDeathMessages(currentGame, currentTheme, Warhammer)
            if warhammerMessage != '':
                await home.send(warhammerMessage)

    async def checkRumblingClause(currentGame):
        if currentGame.currentRound >= 1:
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

        


        

