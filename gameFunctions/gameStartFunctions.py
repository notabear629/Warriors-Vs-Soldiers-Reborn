import discord
from discord.ext import commands
import random


from gameObjects.Lobby import Lobby
from gameObjects.Player import Player
from gameObjects.Game import Game
from gameObjects.Role import Role


from embedBuilder import embedBuilder

class gameStartFunctions:
    async def start(ctx, currentLobby, currentGame, home, prefix, currentTheme, client):
        if home == ctx.channel:
            if currentGame == None:
                if currentLobby != None:
                    if ctx.message.author == currentLobby.host:
                        game = await gameStartFunctions.createGame(currentLobby, currentTheme, client)
                        return game
                    else:
                        await ctx.message.reply('Only the host may start the game!')
                else:
                    await ctx.message.reply(f'You may not start a game without an active lobby! Why not create one using `{prefix}host`?')
            else:
                await ctx.message.reply('There is already an active game!')

    async def createGame(currentLobby, currentTheme, client):
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
        newGame = Game(currentLobby, players)
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
        sampleLimit = soldierCount - 1
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
        sampleLimit = warriorCount - 1
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

    


            