import discord
from discord.ext import commands
import random


from gameObjects.Lobby import Lobby
from gameObjects.Player import Player
from gameObjects.Game import Game
from gameObjects.Role import Role
from gameObjects.Expedition import Expedition

from gameFunctions.expoProposalFunctions import expoProposalFunctions
from gameFunctions.lobbyFunctions import lobbyFunctions
from gameFunctions.searchFunctions import searchFunctions

from dataFunctions.databaseManager import databaseManager

from embedBuilder import embedBuilder
from discordViewBuilder import discordViewBuilder

class midGameFunctions:
    async def showStatus(currentGame, currentTheme, home):
        futureExpoCounts = await expoProposalFunctions.getExpeditionPrediction(currentGame)
        if currentGame.rumblingActivated:
            embed = await embedBuilder.rumblingStatusEmbed(currentGame, currentTheme, futureExpoCounts)
        else:
            embed = await embedBuilder.buildStatusEmbed(currentGame, currentTheme, futureExpoCounts)
        await home.send(embed=embed)

    async def status(ctx, currentLobby, currentGame, currentTheme, home, prefix, noMentions):
        if currentGame.online:
            await midGameFunctions.showStatus(currentGame, currentTheme, ctx.message.channel)
        else:
            if currentLobby.online == False:
                await ctx.reply(f'There is not currently a game being played, or an open lobby! Why not create one in <#{home.id}> using `{prefix}host`?')
            else:
                await lobbyFunctions.lobby(ctx, home, currentLobby, currentTheme, currentGame, prefix, noMentions)

    async def roles(ctx, currentGame, currentTheme, home):
        if currentGame.online:
            await midGameFunctions.showRoles(currentGame, currentTheme, ctx.message.channel)

    async def showRoles(currentGame, currentTheme, home):
        if currentGame.rumblingActivated:
            embed = await embedBuilder.rumblingRolesEmbed(currentGame, currentTheme)
        else:
            embed = await embedBuilder.buildCurrentRoles(currentGame, currentTheme)
        await home.send(embed=embed)

    async def showPlayers(currentGame, currentTheme, noMentions, home):
        embed = await embedBuilder.buildPlayers(currentGame, currentTheme)
        await home.send(embed=embed, allowed_mentions = noMentions)

    async def players(ctx, currentLobby, currentGame, currentTheme, noMentions, home, prefix):
        if currentGame.online:
            await midGameFunctions.showPlayers(currentGame, currentTheme, noMentions, ctx.message.channel)
        elif currentLobby.online:
            await lobbyFunctions.lobby(ctx, home, currentLobby, currentTheme, currentGame, prefix, noMentions)
        else:
            await ctx.reply(f'There is no active lobby! Why not start one in <#{home.id}> with `{prefix}host`?')

    async def target(ctx, currentGame, currentTheme, prefix, client):
        if currentGame.online:
            Sasha = await searchFunctions.roleIDToPlayer(currentGame, 'Sasha')
            user = databaseManager.searchForUser(Sasha.user)
            userChannel = client.get_channel(user['channelID'])
            if Sasha != None and Sasha.user == ctx.message.author and Sasha.role.abilityActive and ctx.message.channel == userChannel:
                view = await discordViewBuilder.sashaTargetView(currentGame, currentTheme, Sasha)
                await userChannel.send('Choose who to target!', view=view)

    async def gag(ctx, currentGame, currentTheme, prefix, client, gagRole, gagFunction):
        if currentGame.online:
            Porco = await searchFunctions.roleIDToPlayer(currentGame, 'Porco')
            user = databaseManager.searchForUser(Porco.user)
            userChannel = client.get_channel(user['channelID'])
            if Porco != None and Porco.user == ctx.message.author and Porco.role.abilityActive and ctx.message.channel == userChannel:
                view = await discordViewBuilder.porcoTargetView(currentGame, currentTheme, Porco, gagRole, gagFunction, client)
                await userChannel.send('Choose who to gag!', view=view)

    async def executeGag(Porco, gagRole, gaggedPlayer, currentGame, client):
        if Porco.role.abilityActive:
            if gaggedPlayer.role.id == 'Erwin' and (currentGame.currentExpo.erwinActivated or gaggedPlayer.role.abilityActive == False):
                user = databaseManager.searchForUser(Porco.user)
                userChannel = client.get_channel(user['channelID'])
                await userChannel.send(f'{Porco.user.mention}, You cannot gag a player who fired a flare!')
            else:
                if gagRole not in gaggedPlayer.user.roles:
                    await gaggedPlayer.user.add_roles(gagRole)
                    user = databaseManager.searchForUser(Porco.user)
                    userChannel = client.get_channel(user['channelID'])
                    await userChannel.send(f'{Porco.user.mention}, You have successfully carried out a gag order.')
                    Porco.role.disableAbility()
                    currentGame.porcoGag(gaggedPlayer)
