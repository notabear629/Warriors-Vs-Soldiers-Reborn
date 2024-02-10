import discord
from discord.ext import commands
from gameObjects.Lobby import Lobby
from embedBuilder import embedBuilder

from discordViewBuilder import discordViewBuilder

from helpBuilder import helpBuilder

class infoFunctions:
    async def rolelist(ctx, loadedRoles, currentTheme):
        roleListEmbed = await embedBuilder.rolelistEmbed(loadedRoles, currentTheme)
        await ctx.reply(embed=roleListEmbed)

    async def help(ctx, currentTheme, loadedRoles, prefix):
        mainEmbed = await helpBuilder.mainHelpEmbed(currentTheme)
        mainView = await helpBuilder.mainNavigatorView('Main', ctx.message.author, currentTheme, prefix, loadedRoles)
        await ctx.reply(embed=mainEmbed, view=mainView)

        

