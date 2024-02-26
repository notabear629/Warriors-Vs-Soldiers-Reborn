import discord
from discord.ext import commands
from gameObjects.Lobby import Lobby
from embedBuilder import embedBuilder

from gameFunctions.searchFunctions import searchFunctions

from discordViewBuilder import discordViewBuilder

from helpBuilder import helpBuilder

from statBuilder import statBuilder

from dataFunctions.databaseManager import databaseManager

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


    async def profile(ctx, currentTheme, client, loadedRoles, input=None):
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
            profileEmbed = await statBuilder.profileEmbed(currentTheme, 'GLOBAL', loadedRoles, 'Main')
            profileView = await statBuilder.profileView(ctx.message.author, 'GLOBAL', currentTheme, loadedRoles)
        else:
            user = client.get_user(foundInput['userID'])
            profileEmbed = await statBuilder.profileEmbed(currentTheme, user, loadedRoles, 'Main')
            profileView = await statBuilder.profileView(ctx.message.author, user, currentTheme, loadedRoles)
        await ctx.reply(embed=profileEmbed, view=profileView)

        

