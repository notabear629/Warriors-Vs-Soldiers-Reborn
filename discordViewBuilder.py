import discord
from discord.ext import commands
from discord import ui
from discord.ui import *

from embedBuilder import embedBuilder

class discordViewBuilder:

    @staticmethod
    async def expeditionVoteView(currentTheme, currentGame, player, client, home, acceptFunction, rejectFunction, abstainFunction):
        returnedView = View()



        acceptButton = Button(label= 'Accept', emoji = currentTheme.emojiAcceptExpedition, style= discord.ButtonStyle.grey)
        async def processExpeditionAccept(interaction):
            await acceptFunction(currentGame, player, client, currentTheme, home)
            embed = await embedBuilder.voteDM(currentGame, player, currentTheme)
            await interaction.message.edit(embed=embed, view = None)
        acceptButton.callback = processExpeditionAccept

        rejectButton = Button(label = 'Reject', emoji = currentTheme.emojiRejectExpedition, style=discord.ButtonStyle.grey)
        async def processExpeditionReject(interaction):
            await rejectFunction(currentGame, player, client, currentTheme, home)
            embed = await embedBuilder.voteDM(currentGame, player, currentTheme)
            await interaction.message.edit(embed=embed, view = None)
        rejectButton.callback = processExpeditionReject
    

        abstainButton = Button(label = 'Abstain', emoji = currentTheme.emojiAbstainExpedition, style=discord.ButtonStyle.grey)
        async def processExpeditionAbstain(interaction):
            await abstainFunction(currentGame, player, client, currentTheme, home)
            embed = await embedBuilder.voteDM(currentGame, player, currentTheme)
            await interaction.message.edit(embed=embed, view = None)
        abstainButton.callback = processExpeditionAbstain

        returnedView.add_item(acceptButton)
        returnedView.add_item(rejectButton)
        returnedView.add_item(abstainButton)
        return returnedView
    
    @staticmethod
    async def expeditionChoiceView(currentGame, currentTheme, player, client, home, passFunction, sabotageFunction):
        returnedView = View()

        passButton = Button(label = 'Pass', emoji = currentTheme.emojiPassExpedition, style = discord.ButtonStyle.grey)
        async def processExpeditionPass(interaction):
            await passFunction(currentGame, player, client, currentTheme, home)
            embed = await embedBuilder.expeditionDM(currentGame, player, currentTheme)
            await interaction.message.edit(embed=embed, view = None)
        passButton.callback = processExpeditionPass

        sabotageButton = Button(label = 'Sabotage', emoji = currentTheme.emojiSabotageExpedition, style=discord.ButtonStyle.grey)
        async def processExpeditionSabotage(interaction):
            await sabotageFunction(currentGame, player, client, currentTheme, home)
            embed = await embedBuilder.expeditionDM(currentGame, player, currentTheme)
            await interaction.message.edit(embed=embed, view = None)
        sabotageButton.callback = processExpeditionSabotage

        returnedView.add_item(passButton)
        if player in currentGame.warriors:
            returnedView.add_item(sabotageButton)
        return returnedView
    