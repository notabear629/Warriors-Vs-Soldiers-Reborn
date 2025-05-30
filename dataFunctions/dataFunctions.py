import discord
from discord.ext import commands

from dataFunctions.userInfoManager import userInfoManager

from helpBuilder import helpBuilder

class dataFunctions:

    async def displayDatatags(ctx, currentTheme):
        defaultStats = await userInfoManager.getDefaultStatistics()
        sortedTags = dict(sorted(defaultStats.items()))
        embeds = await helpBuilder.displayDataTags(currentTheme, sortedTags)
        for embed in embeds:
            await ctx.reply(embed=embed)