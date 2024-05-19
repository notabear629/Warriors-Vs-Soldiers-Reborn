import discord
from discord.ext import commands
import random


from gameObjects.Lobby import Lobby
from gameObjects.Player import Player
from gameObjects.Game import Game
from gameObjects.Role import Role
from gameObjects.Expedition import Expedition

from gameFunctions.expoProposalFunctions import expoProposalFunctions
from gameFunctions.searchFunctions import searchFunctions
from gameFunctions.webhookManager import webhookManager

from dataFunctions.databaseManager import databaseManager
from dataFunctions.userInfoManager import userInfoManager

from embedBuilder import embedBuilder

class gameStartFunctions:
    async def start(ctx, currentLobby, currentGame, home, prefix, currentTheme, client, currentRules, loadedRoles, gagRole, loadedBadges):
        if home == ctx.channel:
            if currentGame.online == False:
                if currentLobby.online:
                    if ctx.message.author == currentLobby.host:
                        if len(currentLobby.users) >= 5:
                            illegalRules = await gameStartFunctions.checkIllegalRules(currentLobby, currentTheme)
                            if illegalRules == '':
                                currentGame.turnOnline()
                                await home.send(f'Starting game with **{len(currentLobby.users)}** Players...')
                                await gameStartFunctions.createGame(currentGame, currentLobby, currentTheme, client, currentRules, loadedRoles, gagRole, loadedBadges)
                                expoSize = await expoProposalFunctions.getExpeditionSize(currentGame)
                                expo = Expedition(currentGame.commanderOrder[0], expoSize, currentGame.players)
                                currentGame.setExpedition(expo)
                                await gameStartFunctions.sendRoleMessages(currentGame, currentTheme, client)
                                await gameStartFunctions.processYmir(currentGame, currentTheme, client)
                                return True
                            else:
                                await ctx.message.reply(f'⚠️Illegal Rule Configuration detected!⚠️\nGame cannot be started until following issues are resolved:\n{illegalRules}')
                        else:
                            await ctx.message.reply('A minimum of **5** Players is required to start the game!') 
                    else:
                        await ctx.message.reply('Only the host may start the game!')
                else:
                    await ctx.message.reply(f'You may not start a game without an active lobby! Why not create one using `{prefix}host`?')
            else:
                await ctx.message.reply('There is already an active game!')

    async def createGame(currentGame, currentLobby, currentTheme, client, currentRules, loadedRoles, gagRole, loadedBadges):
        playerCounts = await gameStartFunctions.getPlayerCounts(currentLobby)
        roleList = await gameStartFunctions.getRoles(playerCounts['soldierCount'], playerCounts['warriorCount'], playerCounts['wildcardCount'], currentTheme, client, currentLobby)
        roleList = random.sample(roleList, len(roleList))
        players = []
        index = 0
        for user in currentLobby.users:
            newPlayer = Player(user, roleList[index])
            players.append(newPlayer)
            index += 1
        currentGame.start(currentLobby, players, currentRules, loadedRoles, gagRole, loadedBadges)

    async def getPlayerCounts(currentLobby):
        playerCount = len(currentLobby.users)
        if currentLobby.currentRules.wildcards:
            if playerCount % 2 == 0:
                soldierCount = playerCount/2 + 1
            else:
                soldierCount = playerCount/2 + .5
            wildcardCount = (playerCount-7)//5 + 1
            warriorCount = playerCount - soldierCount - wildcardCount
        else:
            if playerCount % 2 == 0:
                soldierCount = playerCount/2 + 1
            else:
                soldierCount = playerCount/2 + .5
            warriorCount = playerCount-soldierCount
            wildcardCount = 0
        return {'playerCount' : playerCount, 'soldierCount' : soldierCount, 'warriorCount' : warriorCount, 'wildcardCount': wildcardCount}
    

    async def getRoles(soldierCount, warriorCount, wildcardCount, currentTheme, client, currentLobby):
        roleNames = []
        soldierRoleNames = []
        warriorRoleNames = []
        wildcardRoleNames = []
        bannedRoles = currentLobby.currentRules.disabledSoldiers + currentLobby.currentRules.disabledWarriors + currentLobby.currentRules.disabledWildcards
        if currentLobby.currentRules.noCoordinate == False:
            roleNames.append('Eren')
            soldierRoleNames.append('Eren')
            for role in Role.soldierBannedNoEren:
                if role not in bannedRoles:
                    bannedRoles.append(role)
        if currentLobby.currentRules.noWarchief == False:
            roleNames.append('Zeke')
            warriorRoleNames.append('Zeke')
            for role in Role.soldierBannedNoZeke:
                if role not in bannedRoles:
                    bannedRoles.append(role)

        if wildcardCount > 0:
            bannedWildcards = []
            for role in bannedRoles:
                if role in Role.wildcardRoles:
                    bannedWildcards.append(role)
            while wildcardCount > len(Role.wildcardRoles) - len(bannedWildcards):
                wildcardCount -= 1
                if soldierCount - warriorCount - (len(Role.wildcardRoles) - len(bannedWildcards)) >= 2:
                    warriorCount += 1
                else:
                    soldierCount += 1
        
        forcedSoldiers = currentLobby.currentRules.enabledSoldiers.copy()
        while len(soldierRoleNames) < soldierCount and len(forcedSoldiers) > 0:
            soldierChoice = random.choice(forcedSoldiers)
            forcedSoldiers.remove(soldierChoice)
            roleNames.append(soldierChoice)
            soldierRoleNames.append(soldierChoice)

        forcedWarriors = currentLobby.currentRules.enabledWarriors.copy()
        while len(warriorRoleNames) < warriorCount and len(forcedWarriors) > 0:
            warriorChoice = random.choice(forcedWarriors)
            forcedWarriors.remove(warriorChoice)
            roleNames.append(warriorChoice)
            warriorRoleNames.append(warriorChoice)

        forcedWildcards = currentLobby.currentRules.enabledWildcards.copy()
        while len(wildcardRoleNames) < wildcardCount and len(forcedWildcards) > 0:
            wildcardChoice = random.choice(forcedWildcards)
            forcedWildcards.remove(wildcardChoice)
            roleNames.append(wildcardChoice)
            wildcardRoleNames.append(wildcardChoice)

        validSoldiers = []
        validWarriors = []
        validWildcards = []
        if currentLobby.currentRules.intelligentRoles:
            roleRoot = Role.primeRoles.copy()
        else:
            roleRoot = Role.allRoles.copy()

        for role in roleRoot:
            if role in Role.soldierGroupOptional and role not in bannedRoles and role not in soldierRoleNames:
                validSoldiers.append(role)
            if role in Role.warriorGroupOptional and role not in bannedRoles and role not in warriorRoleNames:
                validWarriors.append(role)

        for role in Role.wildcardRoles:
            if role not in bannedRoles and role not in wildcardRoleNames:
                validWildcards.append(role)
        
        if currentLobby.currentRules.intelligentRoles:
            updateCall = await gameStartFunctions.updateIntelligentRoles(soldierRoleNames, warriorRoleNames, validSoldiers, validWarriors, soldierCount, warriorCount, bannedRoles)
            validSoldiers = updateCall[0]
            validWarriors = updateCall[1]

        while len(soldierRoleNames) < soldierCount:
            if currentLobby.currentRules.intelligentRoles:
                updateCall = await gameStartFunctions.updateIntelligentRoles(soldierRoleNames, warriorRoleNames, validSoldiers, validWarriors, soldierCount, warriorCount, bannedRoles)
                validSoldiers = updateCall[0]
                validWarriors = updateCall[1]
            if len(validSoldiers) == 0:
                soldierRoleNames.append('Soldier')
                roleNames.append('Soldier')
            else:
                soldierChoice = random.choice(validSoldiers)
                validSoldiers.remove(soldierChoice)
                soldierRoleNames.append(soldierChoice)
                roleNames.append(soldierChoice)

        while len(warriorRoleNames) < warriorCount:
            if len(validWarriors) == 0:
                warriorRoleNames.append('Warrior')
                roleNames.append('Warrior')
            else:
                warriorChoice = random.choice(validWarriors)
                validWarriors.remove(warriorChoice)
                warriorRoleNames.append(warriorChoice)
                roleNames.append(warriorChoice)

        
        while len(wildcardRoleNames) < wildcardCount:
            wildcardChoice = random.choice(validWildcards)
            validWildcards.remove(wildcardChoice)
            wildcardRoleNames.append(wildcardChoice)
            roleNames.append(wildcardChoice)

        returnedRoles = []
        for roleName in roleNames:
            roleInfo = getattr(currentTheme, roleName)
            if type(roleInfo['emoji']) == int:
                roleInfo['emoji'] = client.get_emoji(roleInfo['emoji'])
            if type(roleInfo['secondaryEmoji']) == int:
                roleInfo['secondaryEmoji'] = client.get_emoji(roleInfo['secondaryEmoji'])
            returnedRoles.append(Role(roleInfo))

        return returnedRoles
    
    async def updateIntelligentRoles(soldierRoleNames, warriorRoleNames, validSoldiers, validWarriors, soldierCount, warriorCount, bannedRoles):
        for role, dependencies in Role.roleDependencies.items():
            if role in bannedRoles or role in validSoldiers or role in validWarriors or role in soldierRoleNames or role in warriorRoleNames:
                continue
            for dependency, condition in dependencies.items():
                if dependency == 'soldierCount' and soldierCount >= condition and role in Role.soldierGroupOptional:
                    validSoldiers.append(role)
                    break
                if dependency == 'warriorCount' and warriorCount >= condition and role in Role.warriorGroupOptional:
                    validWarriors.append(role)
                    break
                if dependency == 'requiredRoles':
                    for conditionalRole in condition:
                        if conditionalRole in soldierRoleNames or conditionalRole in warriorRoleNames:
                            if role in Role.soldierGroupOptional:
                                validSoldiers.append(role)
                            if role in Role.warriorGroupOptional:
                                validWarriors.append(role)
                            break
        return (validSoldiers, validWarriors)

    async def getSoldierRoles(soldierCount, currentTheme, client, currentLobby, existingRoles=None):
        if currentLobby.currentRules.noCoordinate or existingRoles != None:
            roleNames = []
        else:
            roleNames = [random.choice(Role.soldierGroupCoordinate)]
        enabledRoles = currentLobby.currentRules.enabledSoldiers
        scrambleIndex = len(enabledRoles)
        if scrambleIndex < 0:
            scrambleIndex = 0
        enabledRoles = random.sample(enabledRoles, scrambleIndex)

        
        index = 0
        while (len(roleNames) < soldierCount and index < len(enabledRoles)):
            if currentLobby.currentRules.noCoordinate and enabledRoles[index] in Role.soldierBannedNoEren:
                continue
            roleNames.append(enabledRoles[index])
            index += 1

        sampleLimit = int(soldierCount - len(roleNames))
        if sampleLimit > 0:
            validRoles = Role.soldierGroupOptional.copy()
            for role in roleNames:
                if role in validRoles:
                    validRoles.remove(role)
            for role in currentLobby.currentRules.disabledSoldiers:
                if role in validRoles:
                    validRoles.remove(role)
            if currentLobby.currentRules.noCoordinate:
                for role in Role.soldierGroupOptional:
                    if role in Role.soldierBannedNoEren and role in validRoles:
                        if role in validRoles:
                            validRoles.remove(role)
            if currentLobby.currentRules.noWarchief:
                for role in Role.soldierGroupOptional:
                    if role in Role.soldierBannedNoZeke and role in validRoles:
                        if role in validRoles:
                            validRoles.remove(role)
            if existingRoles != None:
                for role in existingRoles:
                    if role.id in validRoles:
                        validRoles.remove(role.id)
            if sampleLimit > len(validRoles):
                sampleLimit = len(validRoles)
            roleNames += random.sample(validRoles, sampleLimit)
            while len(roleNames) < soldierCount:
                roleNames.append('Soldier')
        
        returnedRoles = []
        for roleName in roleNames:
            roleInfo = getattr(currentTheme, roleName)
            if type(roleInfo['emoji']) == int:
                roleInfo['emoji'] = client.get_emoji(roleInfo['emoji'])
            if type(roleInfo['secondaryEmoji']) == int:
                roleInfo['secondaryEmoji'] = client.get_emoji(roleInfo['secondaryEmoji'])
            returnedRoles.append(Role(roleInfo))
        return returnedRoles

    async def getWarriorRoles(warriorCount, currentTheme, client, currentLobby, existingRoles=None):
        if currentLobby.currentRules.noWarchief or existingRoles != None:
            roleNames = []
        else:
            roleNames = [random.choice(Role.warriorGroupWarchief)]
        enabledRoles = currentLobby.currentRules.enabledWarriors
        scrambleIndex = len(enabledRoles)
        if scrambleIndex < 0:
            scrambleIndex = 0
        enabledRoles = random.sample(enabledRoles, scrambleIndex)
        index = 0
        while (len(roleNames) < warriorCount and index < len(enabledRoles)):
            roleNames.append(enabledRoles[index])
            index += 1

        sampleLimit = int(warriorCount - len(roleNames))
        if sampleLimit > 0:
            validRoles = Role.warriorGroupOptional.copy()
            for role in roleNames:
                if role in validRoles:
                    validRoles.remove(role)
            for role in currentLobby.currentRules.disabledWarriors:
                if role in validRoles:
                    validRoles.remove(role)
            if existingRoles != None:
                for role in existingRoles:
                    if role.id in validRoles:
                        validRoles.remove(role.id)
            if sampleLimit > len(validRoles):
                sampleLimit = len(validRoles)
            roleNames += random.sample(validRoles, sampleLimit)
            while len(roleNames) < warriorCount:
                roleNames.append('Warrior')
        
        returnedRoles = []
        for roleName in roleNames:
            roleInfo = getattr(currentTheme, roleName)
            if type(roleInfo['emoji']) == int:
                roleInfo['emoji'] = client.get_emoji(roleInfo['emoji'])
            if type(roleInfo['secondaryEmoji']) == int:
                roleInfo['secondaryEmoji'] = client.get_emoji(roleInfo['secondaryEmoji'])
            returnedRoles.append(Role(roleInfo))
        return returnedRoles
    
    async def getWildcardRoles(wildcardCount, currentTheme, client, currentLobby):
        enabledRoles = currentLobby.currentRules.enabledWildcards
        scrambleIndex = len(enabledRoles)
        if scrambleIndex < 0:
            scrambleIndex = 0
        enabledRoles = random.sample(enabledRoles, scrambleIndex)
        roleNames = []
        index = 0
        while index < len(enabledRoles) and len(roleNames) < wildcardCount:
            roleNames.append(enabledRoles[index])
            index += 1
        sampleLimit = int(wildcardCount - len(roleNames))

        if sampleLimit > 0:
            validRoles = Role.wildcardRoles.copy()
            for role in roleNames:
                if role in validRoles:
                    validRoles.remove(role)
            for role in currentLobby.currentRules.disabledWildcards:
                if role in validRoles:
                    validRoles.remove(role)
            if sampleLimit > len(validRoles):
                sampleLimit = len(validRoles)
            roleNames += random.sample(validRoles, sampleLimit)
        returnedRoles = []
        for roleName in roleNames:
            roleInfo = getattr(currentTheme, roleName)
            if type(roleInfo['emoji']) == int:
                roleInfo['emoji'] = client.get_emoji(roleInfo['emoji'])
            if type(roleInfo['secondaryEmoji']) == int:
                roleInfo['secondaryEmoji'] = client.get_emoji(roleInfo['secondaryEmoji'])
            returnedRoles.append(Role(roleInfo))
        return returnedRoles
    
    async def sendRoleMessages(currentGame, currentTheme, client):
        for player in currentGame.players:
            await gameStartFunctions.sendRoleMessage(currentGame, currentTheme, player, client)
            defaultStats = await userInfoManager.getDefaultStatistics()
            player.addStats(player.role, defaultStats)
            

    async def sendRoleMessage(currentGame, currentTheme, player, client):
        if player.role.team == 'Soldiers':
            messageColor = currentTheme.soldierColor
            messageThumbnail = currentTheme.soldierThumbnail
            messageDefault = currentTheme.soldierDefaultMessage
            teamName = currentTheme.soldierPlural
        elif player.role.team == 'Warriors':
            messageColor = currentTheme.warriorColor
            messageThumbnail = currentTheme.warriorThumbnail
            messageDefault = currentTheme.warriorDefaultMessage
            teamName = currentTheme.warriorPlural
        elif player.role.team == 'Wildcards':
            messageColor = currentTheme.wildcardColor
            messageThumbnail = currentTheme.wildcardThumbnail
            messageDefault = currentTheme.wildcardDefaultMessage
            teamName = 'Wildcard'
        
        roleMessage = f'You are **{player.role.name}**\n\n'
        if player.role.id in Role.soldierGroupCoordinate or player.role.id in Role.warriorGroupWarchief:
            roleMessage += f'You are the Team Captain of the '
        elif player.role.team != 'Wildcards':
            roleMessage += f'You are on the side of the '
        else:
            roleMessage += f'You are a '
        roleMessage += f'**{teamName}**.\n\n'
        roleMessage += messageDefault + '\n\n'
        roleMessage += player.role.roleMessage +'\n\n'

        if player.role.id in Role.infoMessageRoles:
            if player.role.team == 'Warriors':
                functionCall = getattr(currentTheme, f'getWarriorInfo')
                roleMessage += functionCall(currentGame, player)
            else:
                functionCall = getattr(currentTheme, f'get{player.role.id}Info')
                roleMessage += functionCall(currentGame)
        
        embed = await embedBuilder.buildRoleMessageEmbed(player, roleMessage, messageColor, messageThumbnail)
        
        user = databaseManager.searchForUser(player.user)
        userChannel = client.get_channel(user['channelID'])
        await userChannel.send(player.user.mention, embed=embed)

        if player.role.team == 'Warriors' and currentGame.currentRules.noCoordinate:
            embed = await embedBuilder.soldierRoleDM(currentGame, currentTheme)
            await userChannel.send(embed=embed)

    async def processYmir(currentGame, currentTheme, client):
        Ymir = await searchFunctions.roleIDToPlayer(currentGame, 'Ymir')
        if Ymir != None:
            ymirSimped = currentGame.ymirGuiding
            user = databaseManager.searchForUser(ymirSimped.user)
            userChannel = client.get_channel(user['channelID'])
            embed = await embedBuilder.ymirEmbed(currentGame, currentTheme)
            await webhookManager.ymirWebhook(currentGame, currentTheme, userChannel, ymirSimped.user.mention, embed, client)


    async def checkIllegalRules(currentLobby, currentTheme):
        illegalRules = ''
        if currentLobby.currentRules.casual == False and currentLobby.currentRules.rumbling:
            illegalRules += f'{currentTheme.rumblingName} can only be enabled if the lobby is set to casual!\n'
        if currentLobby.currentRules.rumbling and len(currentLobby.users) < 7:
            illegalRules += f'{currentTheme.rumblingName} can only be enabled if there are 7 or more players!\n'
        if currentLobby.currentRules.casual == False and (currentLobby.currentRules.noCoordinate or currentLobby.currentRules.noWarchief):
            illegalRules += f'Ranked games must have both the Coordinate and the Warchief!\n'
        if currentLobby.currentRules.rumbling and (currentLobby.currentRules.noCoordinate or currentLobby.currentRules.noWarchief):
            illegalRules += f'{currentTheme.rumblingName} can only be enabled if both the Coordinate and Warchief are enabled!\n'
        if currentLobby.currentRules.wildcards and currentLobby.currentRules.casual == False:
            illegalRules += 'Wildcards are only supported in casual games!\n'
        if currentLobby.currentRules.wildcards and len(currentLobby.users) < 7:
            illegalRules += f'Wildcards are only supported in games with 7 or more players!\n'

        return illegalRules

    


            