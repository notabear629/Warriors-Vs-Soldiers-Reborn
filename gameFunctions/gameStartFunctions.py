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

from dataFunctions.databaseManager import databaseManager

from embedBuilder import embedBuilder

class gameStartFunctions:
    async def start(ctx, currentLobby, currentGame, home, prefix, currentTheme, client, currentRules, loadedRoles, gagRole):
        if home == ctx.channel:
            if currentGame.online == False:
                if currentLobby.online:
                    if ctx.message.author == currentLobby.host:
                        await home.send(f'Starting game with **{len(currentLobby.users)}** Players...')
                        await gameStartFunctions.createGame(currentGame, currentLobby, currentTheme, client, currentRules, loadedRoles, gagRole)
                        expoSize = await expoProposalFunctions.getExpeditionSize(currentGame)
                        expo = Expedition(currentGame.commanderOrder[0], expoSize, currentGame.players)
                        currentGame.setExpedition(expo)
                        await gameStartFunctions.sendRoleMessages(currentGame, currentTheme, client)
                        return True
                    else:
                        await ctx.message.reply('Only the host may start the game!')
                else:
                    await ctx.message.reply(f'You may not start a game without an active lobby! Why not create one using `{prefix}host`?')
            else:
                await ctx.message.reply('There is already an active game!')

    async def createGame(currentGame, currentLobby, currentTheme, client, currentRules, loadedRoles, gagRole):
        playerCounts = await gameStartFunctions.getPlayerCounts(currentLobby)
        roleList = []

        roleList += await gameStartFunctions.getSoldierRoles(playerCounts['soldierCount'], currentTheme, client, currentLobby)
        roleList += await gameStartFunctions.getWarriorRoles(playerCounts['warriorCount'], currentTheme, client, currentLobby)

        roleList = random.sample(roleList, len(roleList))
        players = []
        index = 0
        for user in currentLobby.users:
            newPlayer = Player(user, roleList[index])
            players.append(newPlayer)
            index += 1
        currentGame.start(currentLobby, players, currentRules, loadedRoles, gagRole)
        search = await searchFunctions.roleIDToPlayer(currentGame, 'Hange')
        if search != None:
            await search.role.startHange(currentGame, search)

    async def getPlayerCounts(currentLobby):
        playerCount = len(currentLobby.users)
        if playerCount % 2 == 0:
            soldierCount = playerCount/2 + 1
        else:
            soldierCount = playerCount/2 + .5
        warriorCount = playerCount-soldierCount
        return {'playerCount' : playerCount, 'soldierCount' : soldierCount, 'warriorCount' : warriorCount}

    async def getSoldierRoles(soldierCount, currentTheme, client, currentLobby):
        roleNames = [random.choice(Role.soldierGroupCoordinate)]
        enabledRoles = currentLobby.currentRules.enabledSoldiers
        scrambleIndex = len(enabledRoles)
        if scrambleIndex < 0:
            scrambleIndex = 0
        enabledRoles = random.sample(enabledRoles, scrambleIndex)

        
        index = 0
        while (len(roleNames) < soldierCount and index < len(enabledRoles)):
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

    async def getWarriorRoles(warriorCount, currentTheme, client, currentLobby):
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
    
    async def sendRoleMessages(currentGame, currentTheme, client):
        for player in currentGame.players:
            await gameStartFunctions.sendRoleMessage(currentGame, currentTheme, player, client)

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
            messageDefault = currentTheme.wildcardMessage
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
        await userChannel.send(player.user.mention)
        await userChannel.send(embed=embed)


    


            