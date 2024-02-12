import discord
from discord.ext import commands
from discord import ui
from discord.ui import *

from embedBuilder import embedBuilder

from gameObjects.Theme import Theme
from gameObjects.Role import Role

from dataFunctions.databaseManager import databaseManager

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

        if player.role.id == 'Falco' and player.role.abilityActive:
            falcoButton = Button(label = 'Intercept', emoji = player.role.emoji, style = discord.ButtonStyle.grey)
            async def processExpeditionFalco(interaction):
                if await discordViewBuilder.isInteractionIntended(player, interaction):
                    await voteExpoFunction(currentGame, player, client, currentTheme, home, falcoButton.label)
                    embed = await embedBuilder.voteDM(currentGame, player, currentTheme)
                    await interaction.message.edit(embed=embed, view = None)
            falcoButton.callback = processExpeditionFalco
            returnedView.add_item(falcoButton)

        if player.role.id == 'Pieck' and player.role.abilityActive:
            pieckButtonAccept = Button(label = f'{currentTheme.emojiAcceptExpedition}Flip and Accept', emoji = player.role.secondaryEmoji, style = discord.ButtonStyle.grey)
            async def processPieckAccept(interaction):
                if await discordViewBuilder.isInteractionIntended(player, interaction):
                    await voteExpoFunction(currentGame, player, client, currentTheme, home, pieckButtonAccept.label)
                    embed = await embedBuilder.voteDM(currentGame, player, currentTheme)
                    await interaction.message.edit(embed=embed, view = None)
            pieckButtonAccept.callback = processPieckAccept
            returnedView.add_item(pieckButtonAccept)

            pieckButtonReject = Button(label = f'{currentTheme.emojiRejectExpedition}Flip and Reject', emoji = player.role.secondaryEmoji, style = discord.ButtonStyle.grey)
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
            if await discordViewBuilder.isInteractionIntended(player, interaction):
                await chooseExpoFunction(currentGame, player, client, currentTheme, home, passButton.label)
                embed = await embedBuilder.expeditionDM(currentGame, player, currentTheme)
                await interaction.message.edit(embed=embed, view = None)
        passButton.callback = processExpeditionPass

        sabotageButton = Button(label = 'Sabotage', emoji = currentTheme.emojiSabotageExpedition, style=discord.ButtonStyle.grey)
        async def processExpeditionSabotage(interaction):
            if await discordViewBuilder.isInteractionIntended(player, interaction):
                await chooseExpoFunction(currentGame, player, client, currentTheme, home, sabotageButton.label)
                embed = await embedBuilder.expeditionDM(currentGame, player, currentTheme)
                await interaction.message.edit(embed=embed, view = None)
        sabotageButton.callback = processExpeditionSabotage

        returnedView.add_item(passButton)
        if player in currentGame.warriors:
            returnedView.add_item(sabotageButton)

        if player.role.id == 'Armin' and player.role.abilityActive and currentGame.roundFails < 2:
            nukeButton = Button(label = 'Nuke', emoji = currentTheme.emojiNuke, style=discord.ButtonStyle.grey)
            async def processExpeditionNuke(interaction):
                if await discordViewBuilder.isInteractionIntended(player, interaction):
                    await chooseExpoFunction(currentGame, player, client, currentTheme, home, 'Armin')
                    embed = await embedBuilder.expeditionDM(currentGame, player, currentTheme)
                    await interaction.message.edit(embed=embed, view = None)
            nukeButton.callback = processExpeditionNuke
            returnedView.add_item(nukeButton)

        if player.role.id == 'Levi' and player.role.abilityActive:
            if currentGame.roundFails < 2:
                leviAttackButton = Button(label = 'Attack', emoji = player.role.secondaryEmoji, style=discord.ButtonStyle.grey)
                async def processLeviAttack(interaction):
                    if await discordViewBuilder.isInteractionIntended(player, interaction):
                        await chooseExpoFunction(currentGame, player, client, currentTheme, home, 'LeviAttack')
                        embed = await embedBuilder.expeditionDM(currentGame, player, currentTheme)
                        await interaction.message.edit(embed=embed, view = None)
                leviAttackButton.callback = processLeviAttack
                returnedView.add_item(leviAttackButton)
            leviDefendButton = Button(label = 'Defend', emoji = player.role.emoji, style=discord.ButtonStyle.grey)
            async def processLeviDefend(interaction):
                if await discordViewBuilder.isInteractionIntended(player, interaction):
                    await chooseExpoFunction(currentGame, player, client, currentTheme, home, 'LeviDefend')
                    embed = await embedBuilder.expeditionDM(currentGame, player, currentTheme)
                    await interaction.message.edit(embed=embed, view = None)
            leviDefendButton.callback = processLeviDefend
            returnedView.add_item(leviDefendButton)

        if player.role.id == 'Daz' and player.role.abilityActive and player in currentGame.currentExpo.rejected:
            dazButton = Button(label = 'Chicken Out', emoji = player.role.secondaryEmoji, style=discord.ButtonStyle.grey)
            async def processDazButton(interaction):
                if await discordViewBuilder.isInteractionIntended(player, interaction):
                    await chooseExpoFunction(currentGame, player, client, currentTheme, home, 'Daz')
                    embed = await embedBuilder.expeditionDM(currentGame, player, currentTheme)
                    await interaction.message.edit(embed=embed, view = None)
            dazButton.callback = processDazButton
            returnedView.add_item(dazButton)

        if player.role.id == 'Mikasa':
            mikasaSelect = Select(placeholder=f'Choose Player to Guard')
            for expeditioner in currentGame.currentExpo.expeditionMembers:
                mikasaSelect.add_option(label = expeditioner.user.name, emoji= player.role.secondaryEmoji)
            async def processMikasaSelection(interaction):
                if await discordViewBuilder.isInteractionIntended(player, interaction):
                    for expeditioner in currentGame.currentExpo.expeditionMembers:
                        if expeditioner.user.name == str(mikasaSelect.values[0]):
                            guardedPlayer = expeditioner
                    await chooseExpoFunction(currentGame, player, client, currentTheme, home, {'Mikasa':guardedPlayer})
                    embed = await embedBuilder.expeditionDM(currentGame, player, currentTheme)
                    await interaction.message.edit(embed=embed, view = None)
            mikasaSelect.callback = processMikasaSelection
            returnedView.add_item(mikasaSelect)

        if player.role.id == 'Bertholdt':
            bertholdtButton = Button(label = 'Cloak', emoji = player.role.secondaryEmoji, style=discord.ButtonStyle.grey)
            async def processBertholdtButton(interaction):
                if await discordViewBuilder.isInteractionIntended(player, interaction):
                    await chooseExpoFunction(currentGame, player, client, currentTheme, home, 'Bertholdt')
                    embed = await embedBuilder.expeditionDM(currentGame, player, currentTheme)
                    await interaction.message.edit(embed=embed, view = None)
            bertholdtButton.callback = processBertholdtButton
            returnedView.add_item(bertholdtButton)

        if player.role.id == 'Annie':
            annieButton = Button(label = 'Input Scream Message', emoji = player.role.secondaryEmoji, style=discord.ButtonStyle.grey)
            async def processAnnieButton(interaction):
                if await discordViewBuilder.isInteractionIntended(player, interaction):
                    annieModal = Modal(title = 'Scream Message')
                    annieInput = TextInput(label='Type Scream Message Here', style=discord.TextStyle.paragraph)
                    annieModal.add_item(annieInput)
                    async def processAnnieInput(newInteraction):
                        if await discordViewBuilder.isInteractionIntended(player, newInteraction):
                            await chooseExpoFunction(currentGame, player, client, currentTheme, home, {'Annie':str(annieInput.value)})
                            embed = await embedBuilder.expeditionDM(currentGame, player, currentTheme)
                            await interaction.message.edit(embed=embed, view = None)
                            await newInteraction.response.defer()
                    annieModal.on_submit = processAnnieInput
                    await interaction.response.send_modal(annieModal)
                    
            annieButton.callback = processAnnieButton
            returnedView.add_item(annieButton)
        
        return returnedView
    
    @staticmethod
    async def sashaTargetView(currentGame, currentTheme, Sasha):
        returnedView = View()

        sashaTargetSelection = Select(placeholder= 'Choose who to target!', min_values=1, max_values=1)
        sashaTargetSelection.add_option(label = f'Remove Target')
        for player in currentGame.livingPlayers:
            if player != Sasha:
                sashaTargetSelection.add_option(label = f'{player.user.name}', emoji=Sasha.role.secondaryEmoji)
        
        async def processSashaSelection(interaction):
            if await discordViewBuilder.isInteractionIntended(Sasha, interaction):
                if currentGame.online and interaction.user == Sasha.user and Sasha.role.abilityActive:
                    selection = str(sashaTargetSelection.values[0])
                    if selection == 'Remove Target':
                        currentGame.sashaTarget(Sasha, None)
                        await interaction.message.edit(content='You are no longer targeting anybody.')
                        await interaction.response.defer()
                    else:
                        for player in currentGame.livingPlayers:
                            if player.user.name == selection:
                                selectedPlayer = player
                                break
                        currentGame.sashaTarget(Sasha, selectedPlayer)
                        await interaction.message.edit(content=f'Your target has been updated to: {player.user.name}')
                        await interaction.response.defer()

        sashaTargetSelection.callback = processSashaSelection

        returnedView.add_item(sashaTargetSelection)

        return returnedView
    
    @staticmethod
    async def porcoTargetView(currentGame, currentTheme, Porco, gagRole, gagFunction, client):
        returnedView = View()

        porcoTargetSelection = Select(placeholder= 'Player Selection', min_values=1, max_values=1)
        for player in currentGame.livingPlayers:
            porcoTargetSelection.add_option(label = f'{player.user.name}', emoji=Porco.role.secondaryEmoji)
        
        async def processPorcoSelection(interaction):
            if await discordViewBuilder.isInteractionIntended(Porco, interaction):
                if currentGame.online and interaction.user == Porco.user and Porco.role.abilityActive:
                    selection = str(porcoTargetSelection.values[0])
                    for player in currentGame.livingPlayers:
                        if player.user.name == selection:
                            selectedPlayer = player
                            break
                    await gagFunction(Porco, gagRole, selectedPlayer, currentGame, client)
                    await interaction.message.edit(content=f'You have set out a gag order for: {player.user.name}', view=None)
                    await interaction.response.defer()

        porcoTargetSelection.callback = processPorcoSelection

        returnedView.add_item(porcoTargetSelection)

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

        multikidnapSelect = Select(placeholder = 'Kidnap Rules', min_values=1, max_values=1)

        multikidnapSelect.add_option(label = f'Standard Rules', emoji = str('🌐'))
        multikidnapSelect.add_option(label = f'Multi-Kidnap', emoji = str('♾️'))

        async def processMultikidnapSelect(interaction):
            option = str(multikidnapSelect.values[0])
            if option != None and currentGame.online == False and currentLobby.online and interaction.user == currentLobby.host:
                if option.startswith('Multi'):
                    currentLobby.currentRules.toggleMultikidnap(True)
                else:
                    currentLobby.currentRules.toggleMultikidnap(False)
                refreshedView = await discordViewBuilder.basicOptionsView(currentTheme, client, currentLobby, currentGame, prefix, loadedRoles)
                embed = await embedBuilder.buildLobby(currentLobby, currentTheme, prefix)
                await interaction.message.edit(embed=embed, view=refreshedView)
                await interaction.response.defer()
        multikidnapSelect.callback = processMultikidnapSelect
        returnedView.add_item(multikidnapSelect)

        rumblingSelect = Select(placeholder = 'Rumbling Settings', min_values=1, max_values=1)

        rumblingSelect.add_option(label = f'{currentTheme.rumblingName} Enabled', emoji = currentTheme.emojiRumbling)
        rumblingSelect.add_option(label = f'{currentTheme.rumblingName} Disabled', emoji = str('❌'))

        async def processRumblingSelect(interaction):
            option = str(rumblingSelect.values[0])
            if option != None and currentGame.online == False and currentLobby.online and interaction.user == currentLobby.host:
                if option.endswith(' Enabled'):
                    currentLobby.currentRules.toggleRumbling(True)
                else:
                    currentLobby.currentRules.toggleRumbling(False)
                refreshedView = await discordViewBuilder.basicOptionsView(currentTheme, client, currentLobby, currentGame, prefix, loadedRoles)
                embed = await embedBuilder.buildLobby(currentLobby, currentTheme, prefix)
                await interaction.message.edit(embed=embed, view=refreshedView)
                await interaction.response.defer()
        rumblingSelect.callback = processRumblingSelect
        returnedView.add_item(rumblingSelect)

        roleOptionSelect = Button(label = 'Go to Role Options', style=discord.ButtonStyle.grey)

        async def processRoleOptionSelect(interaction):
            if currentGame.online == False and currentLobby.online and interaction.user == currentLobby.host:
                refreshedView = await discordViewBuilder.roleOptionsView(currentTheme, loadedRoles, currentLobby, currentGame, prefix, client, 'Soldiers')
                refreshedEmbed = await embedBuilder.roleSelection(currentTheme, 'Soldiers', loadedRoles, currentLobby.currentRules)
                await interaction.message.edit(view=refreshedView, embed=refreshedEmbed)
                await interaction.response.defer()

        roleOptionSelect.callback = processRoleOptionSelect
        returnedView.add_item(roleOptionSelect)

        rulesetButton = Button(label = 'Go to your Saved Rulesets', style= discord.ButtonStyle.grey)
        async def processRulesetButton(interaction):
            if currentGame.online == False and currentLobby.online and interaction.user == currentLobby.host:
                refreshedView = await discordViewBuilder.savedRulesetView(currentTheme, client, currentLobby, currentGame, prefix, loadedRoles)
                refreshedEmbed = await embedBuilder.savedRulesets(currentTheme)
                await interaction.message.edit(view=refreshedView, embed=refreshedEmbed)
                await interaction.response.defer()
        rulesetButton.callback = processRulesetButton
        returnedView.add_item(rulesetButton)
      
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

        enableSelect = Select(placeholder= f'Choose to Enable {teamName} Roles', min_values=0, max_values=len(focusedRoles))
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

        disableSelect = Select(placeholder= f'Choose to Disable {teamName} Roles', min_values=0, max_values=len(focusedRoles))
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

        resetButton = Button(label = 'Reset Role Selection', emoji = str('🔄'), style=discord.ButtonStyle.grey)
        async def processResetButton(interaction):
            currentLobby.currentRules.clearRoles(team)
            refreshedEmbed = await embedBuilder.roleSelection(currentTheme, team, loadedRoles, currentLobby.currentRules)
            refreshedView = await discordViewBuilder.roleOptionsView(currentTheme, loadedRoles, currentLobby, currentGame, prefix, client, team)
            await interaction.message.edit(view=refreshedView, embed=refreshedEmbed)
            await interaction.response.defer()
        resetButton.callback = processResetButton
        returnedView.add_item(resetButton)

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
    
    @staticmethod
    async def savedRulesetView(currentTheme, client, currentLobby, currentGame, prefix, loadedRoles):

        returnedView = View()
        player = databaseManager.searchForWvsPlayer(currentLobby.host)
        savedRulesets = player['savedRulesets']

        backButton = Button(label = 'Go Back to Basic Options', emoji=currentTheme.emojiBackButton, style=discord.ButtonStyle.grey)

        async def processBackButton(interaction):
            embed = await embedBuilder.buildLobby(currentLobby, currentTheme, prefix)
            refreshedView = await discordViewBuilder.basicOptionsView(currentTheme, client, currentLobby, currentGame, prefix, loadedRoles)
            await interaction.message.edit(embed=embed, view=refreshedView)
            await interaction.response.defer()

        backButton.callback = processBackButton
        returnedView.add_item(backButton)

        loadSelect = Select(placeholder = '🔃Load Saved Ruleset', min_values=1, max_values=1)

        saveSelect = Select(placeholder = '💾Save/Overwrite Ruleset', min_values=1, max_values=1)

        index = 1
        for ruleset in savedRulesets:
            if ruleset != None:
                newName = f'{index} -  {ruleset['name']}'
                loadSelect.add_option(label = newName, emoji= str('✅'))
                saveSelect.add_option(label = newName, emoji= str('✅'))
            else:
                newName = f'{index} - EMPTY'
                loadSelect.add_option(label = newName, emoji= str('❌'))
                saveSelect.add_option(label = newName, emoji= str('❌'))
            index += 1

        async def processSaveSelect(interaction):
            indexSaved = int(saveSelect.values[0][0]) - 1
            rulesetModal = Modal(title = f'Choose Name for Ruleset {indexSaved + 1}')
            nameInput = TextInput(label='Type Name Here', style=discord.TextStyle.short)
            rulesetModal.add_item(nameInput)
            async def processNameInput(newInteraction):
                    name = str(nameInput.value)
                    rules = {}
                    for key, value in vars(currentLobby.currentRules).items():
                        if key.startswith('__'):
                            continue
                        else:
                            rules[key] = value
                    ruleset = {'name': name, 'rules':rules}
                    savedRulesets[indexSaved] = ruleset
                    databaseManager.updateRuleset(currentLobby.host.id, savedRulesets)
                    refreshedView = await discordViewBuilder.savedRulesetView(currentTheme, client, currentLobby, currentGame, prefix, loadedRoles)
                    await interaction.message.edit(view = refreshedView)
                    await newInteraction.response.defer()
                    
            rulesetModal.on_submit = processNameInput
            await interaction.response.send_modal(rulesetModal)

        async def processLoadSelect(interaction):
            indexSelected = int(loadSelect.values[0][0]) - 1
            ruleset = savedRulesets[indexSelected]
            if ruleset == None:
                rules = {}
            else:
                rules = ruleset['rules']
            currentLobby.currentRules.loadRules(rules)
            refreshedView = await discordViewBuilder.savedRulesetView(currentTheme, client, currentLobby, currentGame, prefix, loadedRoles)
            await interaction.message.edit(view = refreshedView)
            await interaction.response.defer()

        saveSelect.callback = processSaveSelect
        loadSelect.callback = processLoadSelect
        returnedView.add_item(loadSelect)
        returnedView.add_item(saveSelect)
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
        
