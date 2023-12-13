import discord
from discord.ext import commands
from discord import ui
from discord.ui import *

from embedBuilder import embedBuilder

class discordViewBuilder:

    @staticmethod
    async def expeditionVoteView(currentTheme, currentGame, player, client, acceptFunction, rejectFunction, abstainFunction):
        returnedView = View()



        acceptButton = Button(label= 'Accept', emoji = currentTheme.emojiAcceptExpedition, style= discord.ButtonStyle.grey)
        async def processExpeditionAccept(interaction):
            await acceptFunction(currentGame, player, client)
            embed = await embedBuilder.voteDM(currentGame, player, currentTheme)
            await interaction.message.edit(embed=embed, view = None)
        acceptButton.callback = processExpeditionAccept

        rejectButton = Button(label = 'Reject', emoji = currentTheme.emojiRejectExpedition, style=discord.ButtonStyle.grey)
        async def processExpeditionReject(interaction):
            await rejectFunction(currentGame, player, client)
            embed = await embedBuilder.voteDM(currentGame, player, currentTheme)
            await interaction.message.edit(embed=embed, view = None)
        rejectButton.callback = processExpeditionReject
    

        abstainButton = Button(label = 'Abstain', emoji = currentTheme.emojiAbstainExpedition, style=discord.ButtonStyle.grey)
        async def processExpeditionAbstain(interaction):
            await abstainFunction(currentGame, player, client)
            embed = await embedBuilder.voteDM(currentGame, player, currentTheme)
            await interaction.message.edit(embed=embed, view = None)
        abstainButton.callback = processExpeditionAbstain

        returnedView.add_item(acceptButton)
        returnedView.add_item(rejectButton)
        returnedView.add_item(abstainButton)
        return returnedView
    