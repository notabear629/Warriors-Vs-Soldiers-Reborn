import discord
from discord.ext import commands
from discord import ui
from discord.ui import *

from embedBuilder import embedBuilder

from gameObjects.Theme import Theme

class discordViewBuilder:

    #This is a method that basically checks to make sure that who presses the button is the same person that the button was intended for.
    #If there is a line at the top that just says "return True" it's because I use it to exploit clicking the button for my alts when I debug.
    #The line should be deleted when actually seriously playing games.
    @staticmethod
    async def isInteractionIntended(player, interaction):
        return True
        if player.user == interaction.user:
            return True
        return False

    @staticmethod
    async def expeditionVoteView(currentTheme, currentGame, player, client, home, voteExpoFunction):
        returnedView = View()


        acceptButton = Button(label= 'Accept', emoji = currentTheme.emojiAcceptExpedition, style= discord.ButtonStyle.grey)
        async def processExpeditionAccept(interaction):
            if await discordViewBuilder.isInteractionIntended(player, interaction):
                await voteExpoFunction(currentGame, player, client, currentTheme, home, acceptButton.label)
                embed = await embedBuilder.voteDM(currentGame, player, currentTheme)
                await interaction.message.edit(embed=embed, view = None)
        acceptButton.callback = processExpeditionAccept

        rejectButton = Button(label = 'Reject', emoji = currentTheme.emojiRejectExpedition, style=discord.ButtonStyle.grey)
        async def processExpeditionReject(interaction):
            if await discordViewBuilder.isInteractionIntended(player, interaction):
                await voteExpoFunction(currentGame, player, client, currentTheme, home, rejectButton.label)
                embed = await embedBuilder.voteDM(currentGame, player, currentTheme)
                await interaction.message.edit(embed=embed, view = None)
        rejectButton.callback = processExpeditionReject
    

        abstainButton = Button(label = 'Abstain', emoji = currentTheme.emojiAbstainExpedition, style=discord.ButtonStyle.grey)
        async def processExpeditionAbstain(interaction):
            if await discordViewBuilder.isInteractionIntended(player, interaction):
                await voteExpoFunction(currentGame, player, client, currentTheme, home, abstainButton.label)
                embed = await embedBuilder.voteDM(currentGame, player, currentTheme)
                await interaction.message.edit(embed=embed, view = None)
        abstainButton.callback = processExpeditionAbstain

        returnedView.add_item(acceptButton)
        returnedView.add_item(rejectButton)
        returnedView.add_item(abstainButton)

        if player.role.id == 'Jean' and player.role.abilityActive:
            jeanButton = Button(label = 'Secure', emoji = player.role.emoji, style = discord.ButtonStyle.grey)
            async def processExpeditionJean(interaction):
                if await discordViewBuilder.isInteractionIntended(player, interaction):
                    await voteExpoFunction(currentGame, player, client, currentTheme, home, jeanButton.label)
                    embed = await embedBuilder.voteDM(currentGame, player, currentTheme)
                    await interaction.message.edit(embed=embed, view = None)
            jeanButton.callback = processExpeditionJean
            returnedView.add_item(jeanButton)

        if player.role.id == 'Pieck' and player.role.abilityActive:
            pieckButtonAccept = Button(label = f'{currentTheme.emojiAcceptExpedition}Flip and Accept', emoji = player.role.emoji, style = discord.ButtonStyle.grey)
            async def processPieckAccept(interaction):
                if await discordViewBuilder.isInteractionIntended(player, interaction):
                    await voteExpoFunction(currentGame, player, client, currentTheme, home, pieckButtonAccept.label)
                    embed = await embedBuilder.voteDM(currentGame, player, currentTheme)
                    await interaction.message.edit(embed=embed, view = None)
            pieckButtonAccept.callback = processPieckAccept
            returnedView.add_item(pieckButtonAccept)

            pieckButtonReject = Button(label = f'{currentTheme.emojiRejectExpedition}Flip and Reject', emoji = player.role.emoji, style = discord.ButtonStyle.grey)
            async def processPieckReject(interaction):
                if await discordViewBuilder.isInteractionIntended(player, interaction):
                    await voteExpoFunction(currentGame, player, client, currentTheme, home, acceptButton.label, pieckButtonReject.label)
                    embed = await embedBuilder.voteDM(currentGame, player, currentTheme)
                    await interaction.message.edit(embed=embed, view = None)
            pieckButtonReject.callback = processPieckReject
            returnedView.add_item(pieckButtonReject)

        return returnedView
    
    @staticmethod
    async def expeditionChoiceView(currentGame, currentTheme, player, client, home, chooseExpoFunction):
        returnedView = View()

        passButton = Button(label = 'Pass', emoji = currentTheme.emojiPassExpedition, style = discord.ButtonStyle.grey)
        async def processExpeditionPass(interaction):
            await chooseExpoFunction(currentGame, player, client, currentTheme, home, passButton.label)
            embed = await embedBuilder.expeditionDM(currentGame, player, currentTheme)
            await interaction.message.edit(embed=embed, view = None)
        passButton.callback = processExpeditionPass

        sabotageButton = Button(label = 'Sabotage', emoji = currentTheme.emojiSabotageExpedition, style=discord.ButtonStyle.grey)
        async def processExpeditionSabotage(interaction):
            await chooseExpoFunction(currentGame, player, client, currentTheme, home, sabotageButton.label)
            embed = await embedBuilder.expeditionDM(currentGame, player, currentTheme)
            await interaction.message.edit(embed=embed, view = None)
        sabotageButton.callback = processExpeditionSabotage

        returnedView.add_item(passButton)
        if player in currentGame.warriors:
            returnedView.add_item(sabotageButton)
        return returnedView
    
    @staticmethod
    async def basicOptionsView(currentTheme, client, currentLobby, prefix):
        returnedView = View()

        themeSelect = Select(placeholder= 'Choose Theme', min_values=1, max_values=1)

        for theme in Theme.loadedThemes:
            if theme.themeName == currentTheme.themeName:
                isDefaultSelection = True
            else:
                isDefaultSelection = False
            loadedTheme = Theme()
            loadedTheme.setTheme(theme)
            await loadedTheme.resolveEmojis(client)
            themeSelect.add_option(label = f'Chosen Theme: {theme.themeName}', emoji=loadedTheme.emojiTheme, default=isDefaultSelection)

        async def processThemeSelect(interaction):
            themeName = discordViewBuilder.getThemeName(themeSelect.values)
            if themeName != currentTheme.themeName and themeName != None:
                theme = await discordViewBuilder.getThemeFromName(themeName, client)
                currentTheme.setTheme(theme)
                await currentTheme.resolveEmojis(client)
                embed = await embedBuilder.buildLobby(currentLobby, currentTheme, prefix)
                refreshedView = await discordViewBuilder.basicOptionsView(currentTheme, client, currentLobby, prefix)
                await interaction.message.edit(embed=embed, view=refreshedView)
                await interaction.response.defer()

        themeSelect.callback = processThemeSelect

        returnedView.add_item(themeSelect)

        roleOptionSelect = Button(label = 'Go to Role Options', style=discord.ButtonStyle.grey)

        async def processRoleOptionSelect(interaction):
            print(roleOptionSelect.label)
            await interaction.response.defer()

        roleOptionSelect.callback = processRoleOptionSelect
        returnedView.add_item(roleOptionSelect)

            
        return returnedView
    

    def getThemeName(themeValues):
        if themeValues == []:
            return None
        themeName = str(themeValues[0])
        return themeName[14:]
    
    async def getThemeFromName(themeName, client):
        selectedTheme = None
        for theme in Theme.loadedThemes:
            if theme.themeName == themeName:
                selectedTheme = theme
                break
        return selectedTheme
        
