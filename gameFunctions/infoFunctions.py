import discord
from discord.ext import commands
from gameObjects.Lobby import Lobby
from embedBuilder import embedBuilder

from gameFunctions.searchFunctions import searchFunctions

from discordViewBuilder import discordViewBuilder

from helpBuilder import helpBuilder

from statBuilder import statBuilder

from dataFunctions.databaseManager import databaseManager
from dataFunctions.userInfoManager import userInfoManager

class infoFunctions:
    async def rolelist(ctx, loadedRoles, currentTheme):
        roleListEmbed = await embedBuilder.rolelistEmbed(loadedRoles, currentTheme)
        await ctx.reply(embed=roleListEmbed)

    async def help(ctx, currentTheme, loadedRoles, prefix):
        mainEmbed = await helpBuilder.mainHelpEmbed(currentTheme)
        mainView = await helpBuilder.mainNavigatorView('Main', ctx.message.author, currentTheme, prefix, loadedRoles)
        await ctx.reply(embed=mainEmbed, view=mainView)

    async def info(ctx, currentTheme, loadedRoles, prefix, input=None):
        foundRole = None
        if input != None:
            foundRole = await searchFunctions.stringToRole(loadedRoles, input)
        if foundRole != None:
            infoEmbed = await helpBuilder.specificRoleInfoEmbed(currentTheme, foundRole)
        else:
            infoEmbed = await helpBuilder.roleInfoHelpEmbed(currentTheme)
        infoView = await helpBuilder.mainNavigatorView('Role Info', ctx.message.author, currentTheme, prefix, loadedRoles)
        await ctx.reply(embed=infoEmbed, view = infoView)


    async def profile(ctx, currentTheme, client, loadedRoles, homeServer, loadedBadges, input=None):
        foundInput = None
        if len(ctx.message.mentions) > 0:
            foundInput = databaseManager.searchForUser(ctx.message.mentions[0])
        if input == None and foundInput == None:
            foundInput = databaseManager.searchForUser(ctx.message.author)
            if foundInput == None:
                foundInput = 'GLOBAL'
                await ctx.reply('You have not yet registered in the game! As such, you have no profile and you will be shown the global stats.')
        if foundInput == None:
            if input.lower() == 'global':
                foundInput = 'GLOBAL'
            else:
                foundInput = databaseManager.searchForUserByName(input)
                if foundInput == None:
                    foundInput == 'GLOBAL'
        if foundInput == None:
            foundInput = 'GLOBAL'
        if foundInput == 'GLOBAL':
            profileEmbed = await statBuilder.profileEmbed(currentTheme, 'GLOBAL', loadedRoles, currentTheme.helpEmbedColor, loadedBadges,'Main')
            profileView = await statBuilder.profileView(ctx.message.author, 'GLOBAL', currentTheme, loadedRoles, currentTheme.helpEmbedColor, loadedBadges)
        else:
            user = client.get_user(foundInput['userID'])
            role = homeServer.get_role(foundInput['roleID'])
            if role.color == discord.Color.default():
                color = currentTheme.helpEmbedColor
            else:
                color = role.color
            profileEmbed = await statBuilder.profileEmbed(currentTheme, user, loadedRoles, color, loadedBadges, 'Main')
            profileView = await statBuilder.profileView(ctx.message.author, user, currentTheme, loadedRoles, color, loadedBadges)
        await ctx.reply(embed=profileEmbed, view=profileView)

    async def badges(ctx, currentTheme, client, loadedBadges, input=None):
        foundInput = None
        if len(ctx.message.mentions) > 0:
            foundInput = databaseManager.searchForUser(ctx.message.mentions[0])
        if input == None and foundInput == None:
            foundInput = databaseManager.searchForUser(ctx.message.author)
            if foundInput == None:
                await ctx.reply('You have not yet registered in the game! As such, you have no badge screen.')
        if foundInput == None:
            foundInput = databaseManager.searchForUserByName(input)
            if foundInput == None:
                await ctx.reply('No user found with such a name!')
        if foundInput != None:
            user = client.get_user(foundInput['userID'])
            badgesEmbed = await statBuilder.badgesEmbed(user, currentTheme, loadedBadges)
            await ctx.reply(embed=badgesEmbed)

    async def leaderboard(ctx, client, homeServer, loadedBadges, currentTheme, input):
        if input != None:
            argSplit = input.split(' ')
        else:
            argSplit = []
        finalInput = None
        if input != None and len(argSplit) == 1:
            defaultStats = await userInfoManager.getDefaultStatistics()
            for stat, value in defaultStats.items():
                if stat.lower() == input.lower():
                    finalInput = stat
                    break
        if input != None and len(argSplit) == 3:
            specialArgs = ['%', '/', '-']
            finalInput = [None, None, None]
            if argSplit[1] not in specialArgs:
                finalInput = None
            else:
                finalInput[1] = argSplit[1]
                defaultStats = await userInfoManager.getDefaultStatistics()
                for stat, value in defaultStats.items():
                    if stat.lower() == argSplit[0].lower():
                        finalInput[0] = stat
                    if stat.lower() == argSplit[2].lower():
                        finalInput[2] = stat
                    if None not in finalInput:
                        break
        if finalInput != None and len(argSplit) == 1:
            lbView = await statBuilder.leaderboardAltView(ctx.message.author, client, homeServer, loadedBadges, currentTheme, finalInput, 1)
            lbEmbed = await statBuilder.leaderboardEmbed(client, homeServer, loadedBadges, currentTheme, finalInput, 1)
        elif finalInput != None and len(argSplit) == 3:
            lbView = await statBuilder.leaderboardAltView(ctx.message.author, client, homeServer, loadedBadges, currentTheme, finalInput, 1)
            lbEmbed = await statBuilder.leaderboardEmbed(client, homeServer, loadedBadges, currentTheme, finalInput, 1)
        else:
            lbView = await statBuilder.leaderboardView(ctx.message.author, client, homeServer, loadedBadges, currentTheme, 'LegacyPoints', 1)
            lbEmbed = await statBuilder.leaderboardEmbed(client, homeServer, loadedBadges, currentTheme, 'LegacyPoints', 1)
        await ctx.send(embed=lbEmbed, view=lbView)

    async def advantage(ctx, currentGame, currentTheme):
        if currentGame.online:
            embed = await statBuilder.advantageEmbed(currentGame, currentTheme)
            await ctx.reply(embed=embed)

        

