import discord
from discord.ext import commands
from discord import ui
from discord.ui import *

from embedBuilder import embedBuilder

from gameObjects.Theme import Theme
from gameObjects.Role import Role

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
                    await voteExpoFunction(currentGame, player, client, currentTheme, home, pieckButtonReject.label)
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

        if player.role.id == 'Armin' and player.role.abilityActive and currentGame.roundFails < 2:
            nukeButton = Button(label = 'Nuke', emoji = player.role.secondaryEmoji, style=discord.ButtonStyle.grey)
            async def processExpeditionNuke(interaction):
                await chooseExpoFunction(currentGame, player, client, currentTheme, home, 'Armin')
                embed = await embedBuilder.expeditionDM(currentGame, player, currentTheme)
                await interaction.message.edit(embed=embed, view = None)
            nukeButton.callback = processExpeditionNuke
            returnedView.add_item(nukeButton)

        if player.role.id == 'Levi' and player.role.abilityActive:
            if currentGame.roundFails < 2:
                leviAttackButton = Button(label = 'Attack', emoji = player.role.secondaryEmoji, style=discord.ButtonStyle.grey)
                async def processLeviAttack(interaction):
                    await chooseExpoFunction(currentGame, player, client, currentTheme, home, 'LeviAttack')
                    embed = await embedBuilder.expeditionDM(currentGame, player, currentTheme)
                    await interaction.message.edit(embed=embed, view = None)
                leviAttackButton.callback = processLeviAttack
                returnedView.add_item(leviAttackButton)
            leviDefendButton = Button(label = 'Defend', emoji = player.role.emoji, style=discord.ButtonStyle.grey)
            async def processLeviDefend(interaction):
                await chooseExpoFunction(currentGame, player, client, currentTheme, home, 'LeviDefend')
                embed = await embedBuilder.expeditionDM(currentGame, player, currentTheme)
                await interaction.message.edit(embed=embed, view = None)
            leviDefendButton.callback = processLeviDefend
            returnedView.add_item(leviDefendButton)
        
        return returnedView
    
    @staticmethod
    async def basicOptionsView(currentTheme, client, currentLobby, currentGame, prefix, loadedRoles):
        returnedView = View()

        themeSelect = Select(placeholder= 'Choose Theme', min_values=1, max_values=1)

        for theme in Theme.loadedThemes:
            loadedTheme = Theme()
            loadedTheme.setTheme(theme)
            await loadedTheme.resolveEmojis(client)
            themeSelect.add_option(label = f'{theme.themeName}', emoji=loadedTheme.emojiTheme)

        async def processThemeSelect(interaction):
            themeName = str(themeSelect.values[0])
            if themeName != None and currentGame.online == False and currentLobby.online and interaction.user == currentLobby.host:
                if themeName == currentTheme.themeName:
                    refreshedView = await discordViewBuilder.basicOptionsView(currentTheme, client, currentLobby, currentGame, prefix, loadedRoles)
                    embed = await embedBuilder.buildLobby(currentLobby, currentTheme, prefix)
                    await interaction.message.edit(embed=embed, view=refreshedView)
                    await interaction.response.defer()
                else:
                    theme = await discordViewBuilder.getThemeFromName(themeName, client)
                    currentTheme.setTheme(theme)
                    await currentTheme.resolveEmojis(client)
                    for role in loadedRoles:
                        role.update(currentTheme, client)
                    embed = await embedBuilder.buildLobby(currentLobby, currentTheme, prefix)
                    refreshedView = await discordViewBuilder.basicOptionsView(currentTheme, client, currentLobby, currentGame, prefix, loadedRoles)
                    await interaction.message.edit(embed=embed, view=refreshedView)
                    await interaction.response.defer()

        themeSelect.callback = processThemeSelect

        returnedView.add_item(themeSelect)

        roleOptionSelect = Button(label = 'Go to Role Options', style=discord.ButtonStyle.grey)

        async def processRoleOptionSelect(interaction):
            if currentGame.online == False and currentLobby.online and interaction.user == currentLobby.host:
                refreshedView = await discordViewBuilder.roleOptionsView(currentTheme, loadedRoles, currentLobby, currentGame, prefix, client, 'Soldiers')
                refreshedEmbed = await embedBuilder.roleSelection(currentTheme, 'Soldiers', loadedRoles, currentLobby.currentRules)
                await interaction.message.edit(view=refreshedView, embed=refreshedEmbed)
                await interaction.response.defer()

        roleOptionSelect.callback = processRoleOptionSelect
        returnedView.add_item(roleOptionSelect)
      
        return returnedView
    
    @staticmethod
    async def roleOptionsView(currentTheme, loadedRoles, currentLobby, currentGame, prefix, client, team):
        returnedView = View()

        if team == 'Soldiers':
            targetedGroup = Role.soldierGroupOptional
            teamName = currentTheme.soldierSingle
        elif team == 'Warriors':
            targetedGroup = Role.warriorGroupOptional
            teamName = currentTheme.warriorSingle


        focusedRoles = []
        for role in loadedRoles:
            if role.id in targetedGroup:
                focusedRoles.append(role)

        enableSelect = Select(placeholder= f'Choose to Enable {teamName} Roles', min_values=1, max_values=len(focusedRoles))
        for role in focusedRoles:
            enableSelect.add_option(label = role.shortName, emoji=role.emoji)
        async def enableRoles(interaction):
            changedRoles = await discordViewBuilder.getRoleRequest(enableSelect.values, loadedRoles) 
            await discordViewBuilder.changeRoleRules(currentGame, currentLobby, interaction, changedRoles, True)
            refreshedEmbed = await embedBuilder.roleSelection(currentTheme, team, loadedRoles, currentLobby.currentRules)
            refreshedView = await discordViewBuilder.roleOptionsView(currentTheme, loadedRoles, currentLobby, currentGame, prefix, client, team)
            await interaction.message.edit(view=refreshedView, embed=refreshedEmbed)
            await interaction.response.defer()
        enableSelect.callback = enableRoles
        returnedView.add_item(enableSelect)

        disableSelect = Select(placeholder= f'Choose to Disable {teamName} Roles', min_values=1, max_values=len(focusedRoles))
        for role in focusedRoles:
            disableSelect.add_option(label = role.shortName, emoji=role.emoji)
        async def disableRoles(interaction):
            changedRoles = await discordViewBuilder.getRoleRequest(disableSelect.values, loadedRoles) 
            await discordViewBuilder.changeRoleRules(currentGame, currentLobby, interaction, changedRoles, False)
            refreshedEmbed = await embedBuilder.roleSelection(currentTheme, team, loadedRoles, currentLobby.currentRules)
            refreshedView = await discordViewBuilder.roleOptionsView(currentTheme, loadedRoles, currentLobby, currentGame, prefix, client, team)
            await interaction.message.edit(view=refreshedView, embed=refreshedEmbed)
            await interaction.response.defer()
        disableSelect.callback = disableRoles
        returnedView.add_item(disableSelect)

        backButton = Button(label = 'Go Back to Basic Options', emoji=currentTheme.emojiBackButton, style=discord.ButtonStyle.grey)

        async def processBackButton(interaction):
            embed = await embedBuilder.buildLobby(currentLobby, currentTheme, prefix)
            refreshedView = await discordViewBuilder.basicOptionsView(currentTheme, client, currentLobby, currentGame, prefix, loadedRoles)
            await interaction.message.edit(embed=embed, view=refreshedView)
            await interaction.response.defer()

        backButton.callback = processBackButton
        returnedView.add_item(backButton)

        if team != 'Warriors':
            warriorButton = Button(label = f'Go to {currentTheme.warriorSingle} Role Options', emoji=currentTheme.emojiWarrior, style=discord.ButtonStyle.grey)
            async def processWarriorButton(interaction):
                refreshedEmbed = await embedBuilder.roleSelection(currentTheme, 'Warriors', loadedRoles, currentLobby.currentRules)
                refreshedView = await discordViewBuilder.roleOptionsView(currentTheme, loadedRoles, currentLobby, currentGame, prefix, client, 'Warriors')
                await interaction.message.edit(view=refreshedView, embed=refreshedEmbed)
                await interaction.response.defer()
            warriorButton.callback = processWarriorButton
            returnedView.add_item(warriorButton)

        elif team != 'Soldiers':
            soldierButton = Button(label = f'Go to {currentTheme.soldierSingle} Role Options', emoji=currentTheme.emojiSoldier, style=discord.ButtonStyle.grey)
            async def processSoldierButton(interaction):
                refreshedEmbed = await embedBuilder.roleSelection(currentTheme, 'Soldiers', loadedRoles, currentLobby.currentRules)
                refreshedView = await discordViewBuilder.roleOptionsView(currentTheme, loadedRoles, currentLobby, currentGame, prefix, client, 'Soldiers')
                await interaction.message.edit(view=refreshedView, embed=refreshedEmbed)
                await interaction.response.defer()
            soldierButton.callback = processSoldierButton
            returnedView.add_item(soldierButton)

        return returnedView
    
    async def changeRoleRules(currentGame, currentLobby, interaction, changedRoles, isEnabled):
        if currentGame.online == False and currentLobby.online and interaction.user == currentLobby.host:
            currentLobby.currentRules.changeRoles(changedRoles, isEnabled)
    
    async def getThemeFromName(themeName, client):
        selectedTheme = None
        for theme in Theme.loadedThemes:
            if theme.themeName == themeName:
                selectedTheme = theme
                break
        return selectedTheme
    
    async def getRoleRequest(shortNames, loadedRoles):
        roleRequest = []
        for shortName in shortNames:
            for role in loadedRoles:
                if role.shortName == shortName:
                    roleRequest.append(role.id)
                    break
        return roleRequest
        
