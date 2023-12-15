import discord
from discord.ext import commands
import random


from gameObjects.Lobby import Lobby
from gameObjects.Player import Player
from gameObjects.Game import Game
from gameObjects.Role import Role
from gameObjects.Expedition import Expedition

from gameFunctions.expoProposalFunctions import expoProposalFunctions

from dataFunctions.databaseManager import databaseManager

from embedBuilder import embedBuilder

class gameStartFunctions:
    async def start(ctx, currentLobby, currentGame, home, prefix, currentTheme, client, currentRules):
        if home == ctx.channel:
            if currentGame == None:
                if currentLobby != None:
                    if ctx.message.author == currentLobby.host:
                        await home.send(f'Starting game with **{len(currentLobby.users)}** Players...')
                        game = await gameStartFunctions.createGame(currentLobby, currentTheme, client, currentRules)
                        expoSize = await expoProposalFunctions.getExpeditionSize(game)
                        expo = Expedition(game.commanderOrder[0], expoSize, game.players)
                        game.setExpedition(expo)
                        await gameStartFunctions.sendRoleMessages(game, currentTheme, client)
                        return game
                    else:
                        await ctx.message.reply('Only the host may start the game!')
                else:
                    await ctx.message.reply(f'You may not start a game without an active lobby! Why not create one using `{prefix}host`?')
            else:
                await ctx.message.reply('There is already an active game!')

    async def createGame(currentLobby, currentTheme, client, currentRules):
        playerCounts = await gameStartFunctions.getPlayerCounts(currentLobby)
        roleList = []

        roleList += await gameStartFunctions.getSoldierRoles(playerCounts['soldierCount'], currentTheme, client)
        roleList += await gameStartFunctions.getWarriorRoles(playerCounts['warriorCount'], currentTheme, client)

        roleList = random.sample(roleList, len(roleList))
        players = []
        index = 0
        for user in currentLobby.users:
            newPlayer = Player(user, roleList[index])
            players.append(newPlayer)
            index += 1
        newGame = Game(currentLobby, players, currentRules)
        return newGame

    async def getPlayerCounts(currentLobby):
        playerCount = len(currentLobby.users)
        if playerCount % 2 == 0:
            soldierCount = playerCount/2 + 1
        else:
            soldierCount = playerCount/2 + .5
        warriorCount = playerCount-soldierCount
        return {'playerCount' : playerCount, 'soldierCount' : soldierCount, 'warriorCount' : warriorCount}

    async def getSoldierRoles(soldierCount, currentTheme, client):
        roleNames = ['Eren']
        optionalSoldierRoles = Role.soldierGroupOptional
        validSoldierRoles = optionalSoldierRoles.copy()
        sampleLimit = int(soldierCount - 1)
        if sampleLimit > len(validSoldierRoles):
            sampleLimit = len(validSoldierRoles)
        roleNames += random.sample(validSoldierRoles, sampleLimit)
        while len(roleNames) < soldierCount:
            roleNames.append('Soldier')
        
        returnedRoles = []
        for roleName in roleNames:
            roleInfo = getattr(currentTheme, roleName)
            if type(roleInfo['emoji']) == int:
                roleInfo['emoji'] = client.get_emoji(roleInfo['emoji'])
            returnedRoles.append(Role(roleInfo))
        return returnedRoles

    async def getWarriorRoles(warriorCount, currentTheme, client):
        roleNames = ['Zeke']
        optionalWarriorRoles = Role.warriorGroupOptional
        validWarriorRoles = optionalWarriorRoles.copy()
        sampleLimit = int(warriorCount - 1)
        if sampleLimit > len(validWarriorRoles):
            sampleLimit = len(validWarriorRoles)
        roleNames += random.sample(validWarriorRoles, sampleLimit)
        while len(roleNames) < warriorCount:
            roleNames.append('Warrior')
        
        returnedRoles = []
        for roleName in roleNames:
            roleInfo = getattr(currentTheme, roleName)
            if type(roleInfo['emoji']) == int:
                roleInfo['emoji'] = client.get_emoji(roleInfo['emoji'])
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


    


            