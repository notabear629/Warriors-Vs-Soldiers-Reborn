import discord
from discord.ext import commands
from discord import ui
from discord.ui import *

from embedBuilder import embedBuilder

from gameObjects.Theme import Theme
from gameObjects.Role import Role

from gameFunctions.searchFunctions import searchFunctions
from gameFunctions.webhookManager import webhookManager

from dataFunctions.databaseManager import databaseManager

class discordViewBuilder:

    #This is a method that basically checks to make sure that who presses the button is the same person that the button was intended for.
    #If there is a line at the top that just says "return True" it's because I use it to exploit clicking the button for my alts when I debug.
    #The line should be deleted when actually seriously playing games.
    @staticmethod
    async def isInteractionIntended(player, interaction):
        #return True
        if player.user == interaction.user:
            return True
        return False

    @staticmethod
    async def expeditionVoteView(currentTheme, currentGame, player, client, home, voteExpoFunction):
        returnedView = View()

        acceptEmoji = currentTheme.emojiAcceptExpedition
        rejectEmoji = currentTheme.emojiRejectExpedition

        if player.role.id == 'Marco' and player in currentGame.deadPlayers:
            acceptEmoji = player.role.secondaryEmoji
            rejectEmoji = player.role.secondaryEmoji

        acceptButton = Button(label= 'Accept', emoji = acceptEmoji, style= discord.ButtonStyle.grey)
        async def processExpeditionAccept(interaction):
            if await discordViewBuilder.isInteractionIntended(player, interaction):
                await voteExpoFunction(currentGame, player, client, currentTheme, home, acceptButton.label)
                embed = await embedBuilder.voteDM(currentGame, player, currentTheme)
                await interaction.message.edit(embed=embed, view = None)
        acceptButton.callback = processExpeditionAccept

        rejectButton = Button(label = 'Reject', emoji = rejectEmoji, style=discord.ButtonStyle.grey)
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

        
        if (player.role.id == 'Zachary' or player.role.id == 'Warhammer') and player.role.abilityActive:
            zacharyButton = Button(label = 'Veto', emoji = player.role.emoji, style = discord.ButtonStyle.grey)
            async def processZacharyButton(interaction):
                if await discordViewBuilder.isInteractionIntended(player, interaction):
                    await voteExpoFunction(currentGame, player, client, currentTheme, home, zacharyButton.label)
                    embed = await embedBuilder.voteDM(currentGame, player, currentTheme)
                    await interaction.message.edit(embed=embed, view=None)
            zacharyButton.callback = processZacharyButton
            returnedView.add_item(zacharyButton)

        if (player.role.id == 'Samuel' or player.role.id == 'Warhammer') and player.role.abilityActive and currentGame.currentRound > 1:
            samuelButton = Button(label = 'Clownery', emoji = player.role.secondaryEmoji, style=discord.ButtonStyle.grey)
            async def processSamuelButton(interaction):
                if await discordViewBuilder.isInteractionIntended(player, interaction):
                    await voteExpoFunction(currentGame, player, client, currentTheme, home, samuelButton.label)
                    embed = await embedBuilder.voteDM(currentGame, player, currentTheme)
                    await interaction.message.edit(embed=embed, view=None)
            samuelButton.callback = processSamuelButton
            returnedView.add_item(samuelButton)

        if player.role.id == 'Falco' and player.role.abilityActive:
            falcoButton = Button(label = 'Intercept', emoji = player.role.emoji, style = discord.ButtonStyle.grey)
            async def processExpeditionFalco(interaction):
                if await discordViewBuilder.isInteractionIntended(player, interaction):
                    await voteExpoFunction(currentGame, player, client, currentTheme, home, falcoButton.label)
                    embed = await embedBuilder.voteDM(currentGame, player, currentTheme)
                    await interaction.message.edit(embed=embed, view = None)
            falcoButton.callback = processExpeditionFalco
            returnedView.add_item(falcoButton)

        if player.role.id == 'Magath' and player not in currentGame.currentExpo.expeditionMembers:
            magathButton = Button(label = 'Final Order', emoji = player.role.secondaryEmoji, style=discord.ButtonStyle.grey)
            async def processMagathVote(interaction):
                if await discordViewBuilder.isInteractionIntended(player, interaction):
                    await voteExpoFunction(currentGame, player, client, currentTheme, home, 'Final Order')
                    embed = await embedBuilder.voteDM(currentGame, player, currentTheme)
                    await interaction.message.edit(embed=embed, view=None)
            magathButton.callback = processMagathVote
            returnedView.add_item(magathButton)

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

        if player.role.id == 'Yelena' and player.role.abilityActive and len(currentGame.livingPlayers) > 1:
            yelenaSelect = Select(placeholder = 'Choose Vote to Steal')
            for voter in currentGame.currentExpo.eligibleVoters:
                if voter != player and ((voter.role.id == 'Marco' and voter in currentGame.deadPlayers) == False):
                    yelenaSelect.add_option(label = voter.user.name, emoji=player.role.emoji)
            async def processYelenaSelection(interaction):
                if await discordViewBuilder.isInteractionIntended(player, interaction):
                    for voter in currentGame.currentExpo.eligibleVoters:
                        if voter.user.name == str(yelenaSelect.values[0]):
                            stolenPlayer = voter
                    await voteExpoFunction(currentGame, player, client, currentTheme, home, {'Yelena':stolenPlayer})
                    embed = await embedBuilder.voteDM(currentGame, player, currentTheme)
                    await interaction.message.edit(embed=embed, view=None)
            yelenaSelect.callback = processYelenaSelection
            returnedView.add_item(yelenaSelect)

        return returnedView
    
    @staticmethod
    async def expeditionChoiceView(currentGame, currentTheme, player, client, home, chooseExpoFunction):
        returnedView = View()

        if not (player in currentGame.warriors and player == currentGame.friedaVowedPlayer):
            passButton = Button(label = 'Pass', emoji = currentTheme.emojiPassExpedition, style = discord.ButtonStyle.grey)
            async def processExpeditionPass(interaction):
                if await discordViewBuilder.isInteractionIntended(player, interaction):
                    await chooseExpoFunction(currentGame, player, client, currentTheme, home, passButton.label)
                    embed = await embedBuilder.expeditionDM(currentGame, player, currentTheme)
                    await interaction.message.edit(embed=embed, view = None)
            passButton.callback = processExpeditionPass
            returnedView.add_item(passButton)


        if player in currentGame.warriors:
            sabotageButton = Button(label = 'Sabotage', emoji = currentTheme.emojiSabotageExpedition, style=discord.ButtonStyle.grey)
            async def processExpeditionSabotage(interaction):
                if await discordViewBuilder.isInteractionIntended(player, interaction):
                    await chooseExpoFunction(currentGame, player, client, currentTheme, home, sabotageButton.label)
                    embed = await embedBuilder.expeditionDM(currentGame, player, currentTheme)
                    await interaction.message.edit(embed=embed, view = None)
            sabotageButton.callback = processExpeditionSabotage
            returnedView.add_item(sabotageButton)


        if (player.role.id == 'Armin' or player.role.id == 'Warhammer') and player.role.abilityActive and currentGame.roundFails < 2:
            nukeButton = Button(label = 'Nuke', emoji = currentTheme.emojiNuke, style=discord.ButtonStyle.grey)
            async def processExpeditionNuke(interaction):
                if await discordViewBuilder.isInteractionIntended(player, interaction):
                    await chooseExpoFunction(currentGame, player, client, currentTheme, home, 'Armin')
                    embed = await embedBuilder.expeditionDM(currentGame, player, currentTheme)
                    await interaction.message.edit(embed=embed, view = None)
            nukeButton.callback = processExpeditionNuke
            returnedView.add_item(nukeButton)

        if (player.role.id == 'Levi' or player.role.id == 'Warhammer') and player.role.abilityActive:
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

        if (player.role.id == 'Daz' or player.role.id == 'Warhammer')and player.role.abilityActive and player in currentGame.currentExpo.rejected:
            dazButton = Button(label = 'Chicken Out', emoji = player.role.secondaryEmoji, style=discord.ButtonStyle.grey)
            async def processDazButton(interaction):
                if await discordViewBuilder.isInteractionIntended(player, interaction):
                    await chooseExpoFunction(currentGame, player, client, currentTheme, home, 'Daz')
                    embed = await embedBuilder.expeditionDM(currentGame, player, currentTheme)
                    await interaction.message.edit(embed=embed, view = None)
            dazButton.callback = processDazButton
            returnedView.add_item(dazButton)

        if player.role.id == 'Rico' and player.role.abilityActive:
            ricoButton = Button(label= 'Prepare Trap', emoji=player.role.secondaryEmoji, style=discord.ButtonStyle.grey)
            async def processRicoButton(interaction):
                if await discordViewBuilder.isInteractionIntended(player, interaction):
                    await chooseExpoFunction(currentGame, player, client, currentTheme, home, 'Rico')
                    embed = await embedBuilder.expeditionDM(currentGame, player, currentTheme)
                    await interaction.message.edit(embed=embed, view=None)
            ricoButton.callback = processRicoButton
            returnedView.add_item(ricoButton)
        
        if (player.role.id == 'Petra' or player.role.id == 'Warhammer') and player.role.abilityActive and len(currentGame.currentExpo.expeditionMembers) > 1:
            petraSelect = Select(placeholder = f'Choose Player to Watch')
            for expeditioner in currentGame.currentExpo.expeditionMembers:
                if expeditioner != player:
                    petraSelect.add_option(label = expeditioner.user.name, emoji = player.role.emoji)
            async def processPetraSelection(interaction):
                if await discordViewBuilder.isInteractionIntended(player, interaction):
                    for expeditioner in currentGame.currentExpo.expeditionMembers:
                        if expeditioner.user.name == str(petraSelect.values[0]):
                            watchedPlayer = expeditioner
                            break
                    await chooseExpoFunction(currentGame, player, client, currentTheme, home, {'Petra':watchedPlayer})
                    embed = await embedBuilder.expeditionDM(currentGame, player, currentTheme)
                    await interaction.message.edit(embed=embed, view=None)
            petraSelect.callback = processPetraSelection
            returnedView.add_item(petraSelect)

        if ((player.role.id == 'Frecklemir') or (player.role.id == 'Warhammer' and player.role.abilityActive)) and len(currentGame.currentExpo.expeditionMembers) > 1:
            freckleSelect = Select(placeholder='Choose Player to Maul')
            warhammerValid = False
            for expeditioner in currentGame.currentExpo.expeditionMembers:
                if expeditioner != player:
                    if player.role.id == 'Frecklemir':
                        freckleSelect.add_option(label = expeditioner.user.name, emoji=player.role.secondaryEmoji)
                    if player.role.id == 'Warhammer' and expeditioner in currentGame.warriors:
                        warhammerValid = True
                        freckleSelect.add_option(label = expeditioner.user.name, emoji=player.role.secondaryEmoji)
            async def processFreckleSelection(interaction):
                if await discordViewBuilder.isInteractionIntended(player, interaction):
                    for expeditioner in currentGame.currentExpo.expeditionMembers:
                        if expeditioner.user.name == str(freckleSelect.values[0]):
                            selectedPlayer = expeditioner
                            break
                    await chooseExpoFunction(currentGame, player, client, currentTheme, home, {'Frecklemir':selectedPlayer})
                    embed = await embedBuilder.expeditionDM(currentGame, player, currentTheme)
                    await interaction.message.edit(embed=embed, view=None)
            if (player.role.id == 'Frecklemir') or (player.role.id == 'Warhammer' and warhammerValid):
                freckleSelect.callback = processFreckleSelection
                returnedView.add_item(freckleSelect)

        if player.role.id == 'Hange' and player.role.abilityActive and len(currentGame.currentExpo.expeditionMembers) > 1:
            hangeSelect = Select(placeholder = f'Choose Player to Wiretap')
            for expeditioner in currentGame.currentExpo.expeditionMembers:
                if expeditioner != player:
                    hangeSelect.add_option(label = expeditioner.user.name, emoji = player.role.secondaryEmoji)
            async def processHangeSelection(interaction):
                if await discordViewBuilder.isInteractionIntended(player, interaction):
                    for expeditioner in currentGame.currentExpo.expeditionMembers:
                        if expeditioner.user.name == str(hangeSelect.values[0]):
                            wiretappedPlayer = expeditioner
                    currentGame.wiretapPlayer(wiretappedPlayer)
                    await chooseExpoFunction(currentGame, player, client, currentTheme, home, {'Hange':wiretappedPlayer})
                    embed = await embedBuilder.expeditionDM(currentGame, player, currentTheme)
                    await interaction.message.edit(embed=embed, view=None)
            hangeSelect.callback = processHangeSelection
            returnedView.add_item(hangeSelect)

        if (player.role.id == 'Hannes' or player.role.id == 'Warhammer') and player.role.abilityActive:
            hannesButton = Button(label = 'Escape', emoji = player.role.emoji, style = discord.ButtonStyle.grey)
            async def processHannesButton(interaction):
                if await discordViewBuilder.isInteractionIntended(player, interaction):
                    await chooseExpoFunction(currentGame, player, client, currentTheme, home, 'Hannes')
                    embed = await embedBuilder.expeditionDM(currentGame, player, currentTheme)
                    await interaction.message.edit(embed=embed, view=None)
            hannesButton.callback = processHannesButton
            returnedView.add_item(hannesButton)

        if (player.role.id == 'Marco' or (player.role.id == 'Warhammer' and player.role.abilityActive)):
            marcoButton = Button(label = currentTheme.suicideLabel, emoji = currentTheme.emojiSuicide, style=discord.ButtonStyle.grey)
            async def processMarcoButton(interaction):
                if await discordViewBuilder.isInteractionIntended(player, interaction):
                    await chooseExpoFunction(currentGame, player, client, currentTheme, home, 'Marco')
                    embed = await embedBuilder.expeditionDM(currentGame, player, currentTheme)
                    await interaction.message.edit(embed=embed, view=None)
            marcoButton.callback = processMarcoButton
            returnedView.add_item(marcoButton)

        if player.role.id == 'Bertholdt':
            bertholdtButton = Button(label = 'Cloak', emoji = player.role.secondaryEmoji, style=discord.ButtonStyle.grey)
            async def processBertholdtButton(interaction):
                if await discordViewBuilder.isInteractionIntended(player, interaction):
                    await chooseExpoFunction(currentGame, player, client, currentTheme, home, 'Bertholdt')
                    embed = await embedBuilder.expeditionDM(currentGame, player, currentTheme)
                    await interaction.message.edit(embed=embed, view = None)
            bertholdtButton.callback = processBertholdtButton
            returnedView.add_item(bertholdtButton)

        if player.role.id == 'Willy' and player.role.abilityActive and len(currentGame.currentExpo.expeditionMembers) > 1:
            willySelect = Select(placeholder = 'Choose Player to Kamikaze')
            for expeditioner in currentGame.currentExpo.expeditionMembers:
                if expeditioner != player:
                    willySelect.add_option(label = expeditioner.user.name, emoji = player.role.emoji)
            async def processWillySelection(interaction):
                if await discordViewBuilder.isInteractionIntended(player, interaction):
                    for expeditioner in currentGame.currentExpo.expeditionMembers:
                        if expeditioner.user.name == str(willySelect.values[0]):
                            killedPlayer = expeditioner
                    await chooseExpoFunction(currentGame, player, client, currentTheme, home, {'Willy':killedPlayer})
                    embed = await embedBuilder.expeditionDM(currentGame, player, currentTheme)
                    await interaction.message.edit(embed=embed, view=None)
            willySelect.callback = processWillySelection
            returnedView.add_item(willySelect)

        if player.role.id == 'Kenny':
            kennySelect = Select(placeholder = 'Choose Player to Kill')
            for expeditioner in currentGame.currentExpo.expeditionMembers:
                kennySelect.add_option(label = expeditioner.user.name, emoji = player.role.secondaryEmoji)
            async def processKennySelection(interaction):
                if await discordViewBuilder.isInteractionIntended(player, interaction):
                    for expeditioner in currentGame.currentExpo.expeditionMembers:
                        if expeditioner.user.name == str(kennySelect.values[0]):
                            killedPlayer = expeditioner
                    await chooseExpoFunction(currentGame, player, client, currentTheme, home, {'Kenny':killedPlayer})
                    embed = await embedBuilder.expeditionDM(currentGame, player, currentTheme)
                    await interaction.message.edit(embed=embed, view = None)
            kennySelect.callback = processKennySelection
            returnedView.add_item(kennySelect)
        
        return returnedView
    
    @staticmethod
    async def sashaTargetView(currentGame, currentTheme, Sasha):
        returnedView = View()
        sashaTargetSelection = Select(placeholder= 'Choose who to target!', min_values=1, max_values=1)
        sashaTargetSelection.add_option(label = f'Remove Target')
        if Sasha.role.id == 'Sasha':
            for player in currentGame.livingPlayers:
                if player != Sasha:
                    sashaTargetSelection.add_option(label = f'{player.user.name}', emoji=Sasha.role.secondaryEmoji) 
        if Sasha.role.id == 'Warhammer':
            for player in currentGame.livingWarriors:
                if player != Sasha:
                    sashaTargetSelection.add_option(label = f'{player.user.name}', emoji=Sasha.role.secondaryEmoji) 
        async def processSashaSelection(interaction):
            if await discordViewBuilder.isInteractionIntended(Sasha, interaction):
                if currentGame.online and interaction.user == Sasha.user and Sasha.role.abilityActive and Sasha in currentGame.livingPlayers:
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
    async def onyankoponPilotView(currentGame, Onyankopon):
        returnedView = View()
        onionPilotSelection = Select(placeholder='Choose who to fly in!', min_values=1, max_values=1)
        for player in currentGame.livingPlayers:
            if player not in currentGame.currentExpo.expeditionMembers:
                onionPilotSelection.add_option(label = f'{player.user.name}', emoji=Onyankopon.role.secondaryEmoji)
        async def processOnionSelection(interaction):
            if await discordViewBuilder.isInteractionIntended(Onyankopon, interaction):
                if currentGame.online and interaction.user == Onyankopon.user and Onyankopon.role.abilityActive and Onyankopon in currentGame.livingPlayers and currentGame.currentExpo.playerFlown is None:
                    selection = str(onionPilotSelection.values[0])
                    for player in currentGame.livingPlayers:
                        if player.user.name == selection:
                            selectedPlayer = player
                            break
                    currentGame.currentExpo.fly(Onyankopon, selectedPlayer)
                    await interaction.message.edit(content=f'You have chosen to fly in: {player.user.name}', view=None)
                    await interaction.response.defer()
                    if Onyankopon == currentGame.hangeWiretapped:
                        await webhookManager.processHangeWebhook(currentGame, currentGame.currentTheme, 'midgame')
        onionPilotSelection.callback = processOnionSelection
        returnedView.add_item(onionPilotSelection)

        noButton = Button(label = 'Do Not Fly', emoji=str('❌'), style=discord.ButtonStyle.grey)
        async def processNoButton(interaction):
            if await discordViewBuilder.isInteractionIntended(Onyankopon, interaction):
                if currentGame.online and interaction.user == Onyankopon.user and Onyankopon.role.abilityActive and Onyankopon in currentGame.livingPlayers and currentGame.currentExpo.playerFlown is None:
                    currentGame.currentExpo.noFly()
                    await interaction.message.edit(content=f'You have chosen to fly nobody in.', view = None)
                    await interaction.response.defer()
                    if Onyankopon == currentGame.hangeWiretapped:
                        await webhookManager.processHangeWebhook(currentGame, currentGame.currentTheme, 'midgame')
        noButton.callback = processNoButton
        returnedView.add_item(noButton)

        return returnedView
    
        
    
    @staticmethod
    async def ricoTargetView(currentGame, currentTheme, Rico):
        returnedView = View()
        ricoTargetSelection = Select(placeholder='Choose who to target!', min_values=1, max_values=1)
        ricoTargetSelection.add_option(label = f'Remove Trap Target')
        for player in currentGame.livingPlayers:
            ricoTargetSelection.add_option(label = f'{player.user.name}', emoji=Rico.role.secondaryEmoji)
        async def processRicoSelection(interaction):
            if await discordViewBuilder.isInteractionIntended(Rico, interaction):
                if currentGame.online and interaction.user == Rico.user and Rico in currentGame.livingPlayers:
                    if (Rico.role.id == 'Rico' and not Rico.role.abilityActive and not currentGame.ricoFired) or (Rico.role.id == 'Warhammer' and Rico.role.abilityActive):
                        selection = str(ricoTargetSelection.values[0])
                        if selection == 'Remove Target':
                            currentGame.ricoTarget(Rico, None)
                            await interaction.message.edit(content = 'You are no longer targeting anybody.')
                            await interaction.response.defer()
                        else:
                            for player in currentGame.livingPlayers:
                                if player.user.name == selection:
                                    selectedPlayer = player
                                    break
                            currentGame.ricoTarget(Rico, selectedPlayer)
                            await interaction.message.edit(content=f'Your trap target has been updated to: {player.user.name}')
                            await interaction.response.defer()
        ricoTargetSelection.callback = processRicoSelection
        returnedView.add_item(ricoTargetSelection)
        return returnedView
    
    @staticmethod
    async def friedaVowView(currentGame, currentTheme, Frieda):
        returnedView = View()
        friedaVowSelection = Select(placeholder= 'Choose who to enforce a Vow on!', min_values=1, max_values=1)
        for player in currentGame.livingPlayers:
            friedaVowSelection.add_option(label=f'{player.user.name}', emoji=Frieda.role.secondaryEmoji)
        async def processFriedaVowSelection(interaction):
            if await discordViewBuilder.isInteractionIntended(Frieda, interaction):
                if currentGame.online and interaction.user == Frieda.user and Frieda.role.abilityActive and Frieda in currentGame.livingPlayers and currentGame.currentExpo.currentlyPicking:
                    selection = str(friedaVowSelection.values[0])
                    for player in currentGame.livingPlayers:
                        if player.user.name == selection:
                            selectedPlayer = player
                            break
                    currentGame.friedaVow(selectedPlayer)
                    if currentGame.currentRules.casual == False:
                        Frieda.stats.friedaVow(currentGame, selectedPlayer)
                    await webhookManager.friedaWebhook(currentGame, currentTheme, currentGame.home, currentGame.client)
                    await interaction.message.edit(content=f'You have enforced a vow on: {player.user.name}')
                    await interaction.response.defer()
        friedaVowSelection.callback = processFriedaVowSelection
        returnedView.add_item(friedaVowSelection)
        return returnedView
    
    @staticmethod
    async def moblitAnalyzeView(currentGame, currentTheme, Moblit):
        returnedView = View()

        moblitPlayerSelection = Select(placeholder= 'Choose who to analyze!', min_values=1, max_values=1)
        for player in currentGame.players:
            if player != Moblit:
                moblitPlayerSelection.add_option(label = f'{player.user.name}') 
        async def processMoblitPlayerSelection(interaction):
            if await discordViewBuilder.isInteractionIntended(Moblit, interaction):
                if currentGame.online and interaction.user == Moblit.user and Moblit.role.abilityActive and Moblit in currentGame.livingPlayers:
                    selection = str(moblitPlayerSelection.values[0])
                    for player in currentGame.livingPlayers:
                        if player.user.name == selection:
                            selectedPlayer = player
                            break
                    currentGame.setMoblitPlayer(selectedPlayer)
                    await interaction.response.defer()
        moblitPlayerSelection.callback = processMoblitPlayerSelection
        returnedView.add_item(moblitPlayerSelection)

        moblitRoleSelection = Select(placeholder= 'Choose which role to check!')
        gameRoles = []
        for player in currentGame.players:
            gameRoles.append(player.role.id)
        for role in currentGame.loadedRoles:
            if role.id in gameRoles and role.id != 'Eren' and role.id != 'Moblit' and role.id != 'Zeke':
                moblitRoleSelection.add_option(label = role.shortName, emoji=role.emoji)
        async def processMoblitRoleSelection(interaction):
            if await discordViewBuilder.isInteractionIntended(Moblit, interaction):
                if currentGame.online and interaction.user == Moblit.user and Moblit.role.abilityActive and Moblit in currentGame.livingPlayers:
                    selection = str(moblitRoleSelection.values[0])
                    for role in currentGame.loadedRoles:
                        if role.shortName == selection:
                            selectedRole = role
                            break
                    currentGame.setMoblitRole(selectedRole)
                    await interaction.response.defer()
        moblitRoleSelection.callback = processMoblitRoleSelection
        returnedView.add_item(moblitRoleSelection)

        analyzeButton = Button(label = 'Analyze', emoji = Moblit.role.secondaryEmoji, style=discord.ButtonStyle.grey)
        async def processAnalyzeButton(interaction):
            if await discordViewBuilder.isInteractionIntended(Moblit, interaction):
                if currentGame.online and interaction.user == Moblit.user and Moblit.role.abilityActive and Moblit in currentGame.livingPlayers:
                    if len(moblitPlayerSelection.values) > 0 and len(moblitRoleSelection.values) > 0:
                        Moblit.role.disableAbility()
                        if currentGame.currentRules.casual == False:
                            Moblit.stats.moblitAnalyze(currentGame.moblitPlayer.role.id == currentGame.moblitRole.id)
                        newEmbed = await embedBuilder.moblitResultsEmbed(currentGame)
                        await interaction.message.edit(embed=newEmbed, view=None)
                        await interaction.response.defer()
                        Hitch = await searchFunctions.roleIDToPlayer(currentGame, 'Hitch')
                        if Hitch != None:
                            hitchInfo = {}
                            if Moblit.role.id == 'Moblit':
                                hitchInfo['Moblit'] = Moblit
                        if Hitch != None and Hitch in currentGame.livingPlayers and hitchInfo != {}:
                            user = databaseManager.searchForUser(Hitch.user)
                            userChannel = currentGame.client.get_channel(user['channelID'])
                            hitchMessage = currentGame.currentTheme.getHitchInfo(currentGame, Hitch, hitchInfo)
                            embed = await embedBuilder.infoUpdate(currentGame.currentTheme, Hitch, hitchMessage)
                            await webhookManager.sendWebhook(currentGame, currentGame.currentTheme, userChannel, f'{Hitch.user.mention}', 'Hitch', currentGame.client)
                            await webhookManager.sendWebhook(currentGame, currentGame.currentTheme, userChannel, '', 'Hitch', currentGame.client, embed)

                    else:
                        await interaction.message.reply('Please ensure that you have selected both a player and role to analyze!')
                        await interaction.response.defer()
        analyzeButton.callback = processAnalyzeButton
        returnedView.add_item(analyzeButton)

        return returnedView
                    
            
    
    @staticmethod
    async def pyxisTrialView(currentGame, currentTheme, Pyxis):
        returnedView = View()
        pyxisTrialSelection = Select(placeholder = 'Choose Player to go on Trial')
        if Pyxis.role.id == 'Pyxis':
            for player in currentGame.playersOnExpos:
                if player in currentGame.livingPlayers:
                    pyxisTrialSelection.add_option(label = f'{player.user.name}', emoji = Pyxis.role.emoji)
        if Pyxis.role.id == 'Warhammer':
            for player in currentGame.playersOnExpos:
                if player in currentGame.livingWarriors:
                    pyxisTrialSelection.add_option(label = f'{player.user.name}', emoji = Pyxis.role.emoji)
        async def processPyxisSelection(interaction):
            if await discordViewBuilder.isInteractionIntended(Pyxis, interaction):
                if currentGame.online and interaction.user == Pyxis.user and Pyxis.role.abilityActive and Pyxis in currentGame.livingPlayers and currentGame.currentExpo.currentlyPicking:
                    selection = str(pyxisTrialSelection.values[0])
                    for player in currentGame.livingPlayers:
                        if player.user.name == selection:
                            selectedPlayer = player
                            break
                    Pyxis.role.disableAbility()
                    currentGame.currentExpo.trialPlayer(Pyxis, selectedPlayer)
                    await interaction.message.edit(content = f'You have chosen to bring **{player.user.name}** to trial.')
                    await interaction.response.defer()
        pyxisTrialSelection.callback = processPyxisSelection
        returnedView.add_item(pyxisTrialSelection)
        return returnedView
    
    @staticmethod
    async def mikasaGuardView(currentGame, currentTheme, Mikasa):
        returnedView = View()
        mikasaSelect = Select(placeholder=f'Choose Player to Guard')
        mikasaSelect.add_option(label = 'Cancel Guard', emoji = str('✖️'))
        for expeditioner in currentGame.livingPlayers:
            mikasaSelect.add_option(label = expeditioner.user.name, emoji= Mikasa.role.secondaryEmoji)
        async def processMikasaSelection(interaction):
            if await discordViewBuilder.isInteractionIntended(Mikasa, interaction):
                if str(mikasaSelect.values[0]) == 'Cancel Guard':
                    currentGame.guardPlayer(None)
                    msg = 'You have chosen to guard nobody.'
                else:
                    for expeditioner in currentGame.livingPlayers:
                        if expeditioner.user.name == str(mikasaSelect.values[0]):
                            guardedPlayer = expeditioner
                            msg = f'You have chosen to guard **{guardedPlayer.user.name}**.'
                    currentGame.guardPlayer(guardedPlayer)
                await interaction.message.edit(content=msg)
                await interaction.response.defer()
        mikasaSelect.callback = processMikasaSelection
        returnedView.add_item(mikasaSelect)
        return returnedView
    
    @staticmethod
    async def gabiFireView(currentGame, currentTheme, Gabi):
        returnedView = View()
        gabiTargetSelection = Select(placeholder = 'Choose who to fire at!')
        gabiTargetSelection.add_option(label = f'Stop Firing')
        for player in currentGame.livingPlayers:
            if player != Gabi:
                gabiTargetSelection.add_option(label = f'{player.user.name}', emoji=Gabi.role.secondaryEmoji)
        async def processGabiSelection(interaction):
            if await discordViewBuilder.isInteractionIntended(Gabi, interaction):
                if currentGame.online and interaction.user == Gabi.user and Gabi.role.abilityActive and Gabi in currentGame.livingPlayers:
                    selection = str(gabiTargetSelection.values[0])
                    if selection == 'Stop Firing':
                        currentGame.gabiFire(Gabi, None)
                        await interaction.message.edit(content = 'You will no longer fire upon anybody.')
                        await interaction.response.defer()
                    else:
                        for player in currentGame.livingPlayers:
                            if player.user.name == selection:
                                selectedPlayer = player
                                break
                        currentGame.gabiFire(Gabi, selectedPlayer)
                        await interaction.message.edit(content = f'You will fire upon: {player.user.name}')
                        await interaction.response.defer()
        gabiTargetSelection.callback = processGabiSelection
        returnedView.add_item(gabiTargetSelection)
        return returnedView
    
    @staticmethod
    async def annieView(currentGame, currentTheme, Annie):
        returnedView = View()
        if Annie.role.id == 'Annie' and Annie.role.abilityActive:
                annieButton = Button(label = 'Input Scream Message', emoji = Annie.role.secondaryEmoji, style=discord.ButtonStyle.grey)
                async def processAnnieButton(interaction):
                    if await discordViewBuilder.isInteractionIntended(Annie, interaction):
                        annieModal = Modal(title = 'Scream Message')
                        annieInput = TextInput(label='Type Scream Message Here', style=discord.TextStyle.paragraph)
                        annieModal.add_item(annieInput)
                        async def processAnnieInput(newInteraction):
                            if await discordViewBuilder.isInteractionIntended(Annie, newInteraction):
                                currentGame.changeAnnieMessage(annieInput.value)
                                await interaction.message.edit(content = 'Your Message has been set.')
                                await newInteraction.response.defer()
                        annieModal.on_submit = processAnnieInput
                        await interaction.response.send_modal(annieModal)
                annieButton.callback = processAnnieButton
                returnedView.add_item(annieButton)

                cancelButton = Button(label = 'Cancel Scream', emoji = str('✖️'), style=discord.ButtonStyle.grey)
                async def processCancelButton(interaction):
                    if await discordViewBuilder.isInteractionIntended(Annie, interaction):
                        currentGame.changeAnnieMessage(None)
                        await interaction.message.edit(content = 'You will no longer send a message.')
                        await interaction.response.defer()
                cancelButton.callback = processCancelButton
                returnedView.add_item(cancelButton)
        return returnedView
    
    @staticmethod
    async def keithSummonView(currentGame, Keith):
        returnedView = View()
        
        gameRoles = []
        keithRoles= []
        keithRoles2 = []
        for player in currentGame.players:
            gameRoles.append(player.role.id)
        for role in currentGame.loadedRoles:
            if role.id not in gameRoles and role.id != 'Eren' and role.team == 'Soldiers':
                if len(keithRoles) >= 25:
                    keithRoles2.append(role)
                else:
                    keithRoles.append(role)

        keithSummonSelection = Select(placeholder='Choose who to Summon!')
        for role in keithRoles:
            keithSummonSelection.add_option(label = role.shortName, emoji=role.emoji)
        async def processKeithSelection(interaction):
            if await discordViewBuilder.isInteractionIntended(Keith, interaction):
                if currentGame.online and interaction.user == Keith.user and Keith in currentGame.livingPlayers:
                    selection = str(keithSummonSelection.values[0])
                    if selection == 'Cancel Summon':
                        currentGame.keithSummon(None)
                        await interaction.message.edit(content = 'You will not summon anybody.')
                        await interaction.response.defer()
                    else:
                        for role in currentGame.loadedRoles:
                            if role.shortName == selection:
                                selectedRole = role
                                break
                        currentGame.keithSummon(selectedRole.id)
                        await interaction.message.edit(content = f'You will summon {selectedRole.name}')
                        await interaction.response.defer()
        keithSummonSelection.callback = processKeithSelection
        returnedView.add_item(keithSummonSelection)

        if len(keithRoles2) > 0:
            keithSummonSelection2 = Select(placeholder='Choose who to Summon!')
            for role in keithRoles2:
                keithSummonSelection2.add_option(label = role.shortName, emoji=role.emoji)
            async def processKeithSelection2(interaction):
                if await discordViewBuilder.isInteractionIntended(Keith, interaction):
                    if currentGame.online and interaction.user == Keith.user and Keith in currentGame.livingPlayers:
                        selection = str(keithSummonSelection2.values[0])
                        if selection == 'Cancel Summon':
                            currentGame.keithSummon(None)
                            await interaction.message.edit(content = 'You will not summon anybody.')
                            await interaction.response.defer()
                        else:
                            for role in currentGame.loadedRoles:
                                if role.shortName == selection:
                                    selectedRole = role
                                    break
                            currentGame.keithSummon(selectedRole.id)
                            await interaction.message.edit(content = f'You will summon {selectedRole.name}')
                            await interaction.response.defer()
            keithSummonSelection2.callback = processKeithSelection2
            returnedView.add_item(keithSummonSelection2)

        return returnedView
    
    @staticmethod
    async def ymirPathsView(currentGame, currentTheme, Ymir, client):
        returnedView = View()

        messageButton = Button(label = 'Send Message', emoji = str('🌌'), style=discord.ButtonStyle.grey)
        async def processMessageButton(interaction):
            if await discordViewBuilder.isInteractionIntended(Ymir, interaction):
                ymirModal = Modal(title = 'Send Message')
                ymirInput = TextInput(label='Type Message Content Here', style=discord.TextStyle.paragraph)
                ymirModal.add_item(ymirInput)
                async def processYmirInput(newInteraction):
                    if await discordViewBuilder.isInteractionIntended(Ymir, newInteraction):
                        msg = str(ymirInput.value)
                        embed = await embedBuilder.ymirMessageEmbed(currentGame, currentTheme, msg)
                        user = databaseManager.searchForUser(currentGame.ymirGuiding.user)
                        channel = client.get_channel(user['channelID'])
                        await webhookManager.ymirMessageWebhook(currentGame, currentTheme, channel, embed, client)
                        await interaction.message.reply('Message sent.')
                        await interaction.message.edit(view=None)
                        await newInteraction.response.defer()
                ymirModal.on_submit = processYmirInput
                await interaction.response.send_modal(ymirModal)
        messageButton.callback = processMessageButton
        returnedView.add_item(messageButton)

        if len(currentGame.deadPlayers) > 0 and Ymir.role.abilityActive:
            reviveSelect = Select(placeholder= 'Choose Player to Revive', min_values=1, max_values=1)
            for player in currentGame.deadPlayers:
                reviveSelect.add_option(label = f'{player.user.name}', emoji = currentTheme.emojiDead)
            async def processYmirRevive(interaction):
                if await discordViewBuilder.isInteractionIntended(Ymir, interaction):
                    if Ymir.role.abilityActive:
                        playerName = str(reviveSelect.values[0])
                        for player in currentGame.deadPlayers:
                            if player.user.name == playerName:
                                selectedPlayer = player
                                break
                        currentGame.ymirRevive(selectedPlayer)
                        Ymir.role.disableAbility()
                        await interaction.message.reply('Player will be revived upon the end of the next round.')
                        await interaction.message.edit(view = None)
                        await interaction.response.defer()
            reviveSelect.callback = processYmirRevive
            returnedView.add_item(reviveSelect)

        if Ymir.role.abilityActive:
            blessingSelect = Select(placeholder = 'Choose Player to Bless', min_values=1, max_values=1)
            #This part with addedPlayers is unironically just so I can test it in my server better
            addedPlayers = []
            for player in currentGame.livingPlayers:
                if player.user.name in addedPlayers or player.user.name == Ymir.user.name:
                    continue
                addedPlayers.append(player.user.name)
                blessingSelect.add_option(label = f'{player.user.name}', emoji = currentTheme.emojiPaths)
            async def processYmirBless(interaction):
                if await discordViewBuilder.isInteractionIntended(Ymir, interaction):
                    if Ymir.role.abilityActive:
                        playerName = str(blessingSelect.values[0])
                        for player in currentGame.livingPlayers:
                            if player.user.name == playerName:
                                selectedPlayer = player
                                break
                        currentGame.ymirBless(selectedPlayer)
                        Ymir.role.disableAbility()
                        await interaction.message.reply('Blessing Granted.')
                        await interaction.message.edit(view=None)
                        await interaction.response.defer()
                        await webhookManager.ymirBlessingGrantedWebook(currentGame, currentTheme, client)
            blessingSelect.callback = processYmirBless
            returnedView.add_item(blessingSelect)
                        
        return returnedView
    
    @staticmethod
    async def porcoTargetView(currentGame, currentTheme, Porco, gagRole, gagFunction, client):
        returnedView = View()

        porcoTargetSelection = Select(placeholder= 'Player Selection', min_values=1, max_values=1)
        for player in currentGame.livingPlayers:
            porcoTargetSelection.add_option(label = f'{player.user.name}', emoji=Porco.role.secondaryEmoji)
        
        async def processPorcoSelection(interaction):
            if await discordViewBuilder.isInteractionIntended(Porco, interaction):
                if currentGame.online and interaction.user == Porco.user and Porco.role.abilityActive and Porco in currentGame.livingPlayers and currentGame.exposOver == False:
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
    async def ankaDemoteView(currentGame, Anka, ankaFunction):
        returnedView = View()

        ankaDemoteSelection = Select(placeholder='Choose who to demote!', min_values=1, max_values=1)
        for player in currentGame.commanderOrder:
            ankaDemoteSelection.add_option(label = f'{player.user.name}', emoji=Anka.role.secondaryEmoji)
        
        async def processAnkaSelection(interaction):
            if await discordViewBuilder.isInteractionIntended(Anka, interaction):
                if currentGame.online and interaction.user == Anka.user and Anka.role.abilityActive and Anka in currentGame.livingPlayers and currentGame.currentExpo.currentlyPicking:
                    selection = str(ankaDemoteSelection.values[0])
                    for player in currentGame.livingPlayers:
                        if player.user.name == selection:
                            selectedPlayer = player
                            break
                    if Anka.role.id in ['Anka', 'Warhammer']:
                        await ankaFunction(currentGame, Anka, selectedPlayer)
                    await interaction.message.edit(content = f'You have chosen to demote: {player.user.name}', view=None)
                    await interaction.response.defer()
        
        ankaDemoteSelection.callback = processAnkaSelection
        returnedView.add_item(ankaDemoteSelection)


        return returnedView
    
    @staticmethod
    async def minaSmokeView(currentGame, Mina, minaFunction):
        returnedView = View()
        canReturn = False

        if (Mina.role.id == 'Mina' and not currentGame.greenFired) or (Mina.role.id == 'Warhammer' and Mina.role.abilityActive):
            canReturn = True
            greenSmokeButton = Button(label = 'Green Smoke', emoji=Mina.role.secondaryEmoji, style=discord.ButtonStyle.green)
            async def processGreenButton(interaction):
                if await discordViewBuilder.isInteractionIntended(Mina, interaction):
                    if currentGame.online and Mina in currentGame.livingPlayers:
                        await minaFunction(currentGame, Mina, 'Green')
                        newView = await discordViewBuilder.minaSmokeView(currentGame, Mina, minaFunction)
                        await interaction.message.edit(content = 'You have chosen to fire Green Smoke.', view=newView)
                        await interaction.response.defer()
            greenSmokeButton.callback = processGreenButton
            returnedView.add_item(greenSmokeButton)

        if (Mina.role.id == 'Mina' and not currentGame.redFired) or (Mina.role.id == 'Warhammer' and Mina.role.abilityActive):
            canReturn = True
            redSmokeButton = Button(label = 'Red Smoke', emoji=Mina.role.secondaryEmoji, style=discord.ButtonStyle.red)
            async def processRedButton(interaction):
                if await discordViewBuilder.isInteractionIntended(Mina, interaction):
                    if currentGame.online and Mina in currentGame.livingPlayers:
                        await minaFunction(currentGame, Mina, 'Red')
                        newView = await discordViewBuilder.minaSmokeView(currentGame, Mina, minaFunction)
                        await interaction.message.edit(content = 'You have chosen to fire Red Smoke.', view=newView)
                        await interaction.response.defer()
            redSmokeButton.callback = processRedButton
            returnedView.add_item(redSmokeButton)

        if (Mina.role.id == 'Mina' and not currentGame.blackFired) or (Mina.role.id == 'Warhammer' and Mina.role.abilityActive):
            canReturn = True
            blackSmokeButton = Button(label = 'Black Smoke', emoji=Mina.role.secondaryEmoji, style=discord.ButtonStyle.grey)
            async def processBlackButton(interaction):
                if await discordViewBuilder.isInteractionIntended(Mina, interaction):
                    if currentGame.online and Mina in currentGame.livingPlayers:
                        await minaFunction(currentGame, Mina, 'Black')
                        newView = await discordViewBuilder.minaSmokeView(currentGame, Mina, minaFunction)
                        await interaction.message.edit(content = 'You have chosen to fire Black Smoke.', view=newView)
                        await interaction.response.defer()
            blackSmokeButton.callback = processBlackButton
            returnedView.add_item(blackSmokeButton)

        if canReturn:
            return returnedView
        else:
            return None
    
    @staticmethod
    async def basicOptionsView(currentTheme, client, currentLobby, currentGame, prefix, loadedRoles, adminRole):
        returnedView = View()

        themeSelect = Select(placeholder= 'Choose Theme', min_values=1, max_values=1)

        for theme in Theme.loadedThemes:
            loadedTheme = Theme()
            loadedTheme.setTheme(theme)
            await loadedTheme.resolveEmojis(client)
            themeSelect.add_option(label = f'{theme.themeName}', emoji=loadedTheme.emojiTheme)

        async def processThemeSelect(interaction):
            themeName = str(themeSelect.values[0])
            if themeName != None and currentGame.online == False and currentLobby.online and (interaction.user == currentLobby.host or adminRole in interaction.user.roles):
                if themeName == currentTheme.themeName:
                    refreshedView = await discordViewBuilder.basicOptionsView(currentTheme, client, currentLobby, currentGame, prefix, loadedRoles, adminRole)
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
                    refreshedView = await discordViewBuilder.basicOptionsView(currentTheme, client, currentLobby, currentGame, prefix, loadedRoles, adminRole)
                    await interaction.message.edit(embed=embed, view=refreshedView)
                    await interaction.response.defer()

        themeSelect.callback = processThemeSelect

        returnedView.add_item(themeSelect)

        captainSelect = Select(placeholder = 'Team Captains', min_values=1, max_values=1)
        
        Eren = await searchFunctions.roleIDToRoleFromLoadedRoles(loadedRoles, 'Eren')
        Zeke = await searchFunctions.roleIDToRoleFromLoadedRoles(loadedRoles, 'Zeke')
        captainSelect.add_option(label = f'Coordinate and Warchief Enabled', emoji = str('✅'))
        captainSelect.add_option(label = f'Coordinate Only', emoji = str(Eren.emoji))
        captainSelect.add_option(label = f'Warchief Only', emoji = str(Zeke.emoji))
        captainSelect.add_option(label = f'Coordinate and Warchief Disabled', emoji = str('❌'))

        async def processCaptainSelect(interaction):
            option = str(captainSelect.values[0])
            if option != None and currentGame.online == False and currentLobby.online and (interaction.user == currentLobby.host or adminRole in interaction.user.roles):
                if option.startswith('Coordinate'):
                    if 'Enabled' in option:
                        currentLobby.currentRules.toggleCaptains(True, True)
                    elif 'Disabled' in option:
                        currentLobby.currentRules.toggleCaptains(False, False)
                    else:
                        currentLobby.currentRules.toggleCaptains(True, False)
                else:
                    currentLobby.currentRules.toggleCaptains(False, True)
                refreshedView = await discordViewBuilder.basicOptionsView(currentTheme, client, currentLobby, currentGame, prefix, loadedRoles, adminRole)
                embed = await embedBuilder.buildLobby(currentLobby, currentTheme, prefix)
                await interaction.message.edit(embed=embed, view=refreshedView)
                await interaction.response.defer()
        captainSelect.callback = processCaptainSelect
        returnedView.add_item(captainSelect)

        multiKidnapButton = Button(label = f'Toggle Multi-Kidnap', emoji = str('♾️'), style=discord.ButtonStyle.grey)
        async def processMultikidnapButton(interaction):
            if currentGame.online == False and currentLobby.online and (interaction.user == currentLobby.host or adminRole in interaction.user.roles):
                currentLobby.currentRules.toggleMultikidnap(not currentLobby.currentRules.multikidnap)
                refreshedView = await discordViewBuilder.basicOptionsView(currentTheme, client, currentLobby, currentGame, prefix, loadedRoles, adminRole)
                embed = await embedBuilder.buildLobby(currentLobby, currentTheme, prefix)
                await interaction.message.edit(embed=embed, view=refreshedView)
                await interaction.response.defer()
        multiKidnapButton.callback = processMultikidnapButton
        returnedView.add_item(multiKidnapButton)

        rumblingButton = Button(label = f'Toggle {currentTheme.rumblingName}', emoji = str(currentTheme.emojiRumbling), style = discord.ButtonStyle.grey)
        async def processRumblingButton(interaction):
            if currentGame.online == False and currentLobby.online and (interaction.user == currentLobby.host or adminRole in interaction.user.roles):
                currentLobby.currentRules.toggleRumbling(not currentLobby.currentRules.rumbling)
                refreshedView = await discordViewBuilder.basicOptionsView(currentTheme, client, currentLobby, currentGame, prefix, loadedRoles, adminRole)
                embed = await embedBuilder.buildLobby(currentLobby, currentTheme, prefix)
                await interaction.message.edit(embed=embed, view=refreshedView)
                await interaction.response.defer()
        rumblingButton.callback = processRumblingButton
        returnedView.add_item(rumblingButton)

        wildcardsButton = Button(label = f'Toggle Wildcards', emoji = str('🃏'), style=discord.ButtonStyle.grey)
        async def processWildcardsButton(interaction):
            if currentGame.online == False and currentLobby.online and (interaction.user == currentLobby.host or adminRole in interaction.user.roles):
                currentLobby.currentRules.toggleWildcards()
                refreshedView = await discordViewBuilder.basicOptionsView(currentTheme, client, currentLobby, currentGame, prefix, loadedRoles, adminRole)
                embed = await embedBuilder.buildLobby(currentLobby, currentTheme, prefix)
                await interaction.message.edit(embed=embed, view=refreshedView)
                await interaction.response.defer()
        wildcardsButton.callback = processWildcardsButton
        returnedView.add_item(wildcardsButton)

        casualButton = Button(label = 'Toggle Casual', emoji = str('🤙'), style=discord.ButtonStyle.grey)
        async def processCasualButton(interaction):
            if currentGame.online == False and currentLobby.online and (interaction.user == currentLobby.host or adminRole in interaction.user.roles):
                currentLobby.currentRules.toggleCasual(not currentLobby.currentRules.casual)
                refreshedView = await discordViewBuilder.basicOptionsView(currentTheme, client, currentLobby, currentGame, prefix, loadedRoles, adminRole)
                embed = await embedBuilder.buildLobby(currentLobby, currentTheme, prefix)
                await interaction.message.edit(embed=embed, view=refreshedView)
                await interaction.response.defer()
        casualButton.callback = processCasualButton
        returnedView.add_item(casualButton)

        intelligentButton = Button(label = 'Toggle Intelli-Roles', emoji = str('🧠'), style = discord.ButtonStyle.grey)
        async def processIntelligentButton(interaction):
            if currentGame.online == False and currentLobby.online and (interaction.user == currentLobby.host or adminRole in interaction.user.roles):
                currentLobby.currentRules.toggleIntelligentRoles()
                refreshedView = await discordViewBuilder.basicOptionsView(currentTheme, client, currentLobby, currentGame, prefix, loadedRoles, adminRole)
                embed = await embedBuilder.buildLobby(currentLobby, currentTheme, prefix)
                await interaction.message.edit(embed=embed, view=refreshedView)
                await interaction.response.defer()
        intelligentButton.callback = processIntelligentButton
        returnedView.add_item(intelligentButton)

        roleOptionSelect = Button(label = 'Go to Role Options', style=discord.ButtonStyle.grey)

        async def processRoleOptionSelect(interaction):
            if currentGame.online == False and currentLobby.online and (interaction.user == currentLobby.host or adminRole in interaction.user.roles):
                refreshedView = await discordViewBuilder.roleOptionsView(currentTheme, loadedRoles, currentLobby, currentGame, prefix, client, 'Soldiers', adminRole)
                refreshedEmbed = await embedBuilder.roleSelection(currentTheme, 'Soldiers', loadedRoles, currentLobby.currentRules)
                await interaction.message.edit(view=refreshedView, embed=refreshedEmbed)
                await interaction.response.defer()

        roleOptionSelect.callback = processRoleOptionSelect
        returnedView.add_item(roleOptionSelect)

        rulesetButton = Button(label = 'Go to your Saved Rulesets', style= discord.ButtonStyle.grey)
        async def processRulesetButton(interaction):
            if currentGame.online == False and currentLobby.online and (interaction.user == currentLobby.host or adminRole in interaction.user.roles):
                refreshedView = await discordViewBuilder.savedRulesetView(currentTheme, client, currentLobby, currentGame, prefix, loadedRoles, adminRole)
                refreshedEmbed = await embedBuilder.savedRulesets(currentTheme)
                await interaction.message.edit(view=refreshedView, embed=refreshedEmbed)
                await interaction.response.defer()
        rulesetButton.callback = processRulesetButton
        returnedView.add_item(rulesetButton)
      
        return returnedView
    
    @staticmethod
    async def roleOptionsView(currentTheme, loadedRoles, currentLobby, currentGame, prefix, client, team, adminRole, page=1):
        returnedView = View()

        if team == 'Soldiers':
            targetedGroup = Role.soldierGroupOptional
            teamName = currentTheme.soldierSingle
        elif team == 'Warriors':
            targetedGroup = Role.warriorGroupOptional
            teamName = currentTheme.warriorSingle
        elif team == 'Wildcards':
            targetedGroup = Role.wildcardRoles
            teamName = currentTheme.wildcardSingle

        x = 0
        focusedRoles = []
        for role in loadedRoles:
            if role.id in targetedGroup:
                if team == 'Soldiers':
                    if (page == 1 and x < 25) or (page == 2 and x > 24):
                        focusedRoles.append(role)
                    x += 1
                else:
                    focusedRoles.append(role)

        if team == 'Soldiers':
            pageSelect = Select(placeholder=f'Choose which Page to navigate to', min_values=1, max_values=1)
            pageSelect.add_option(label = 'Page 1')
            pageSelect.add_option(label = 'Page 2')
            async def handlePageChange(interaction):
                pageSelected = int(pageSelect.values[0].split(' ')[1])
                refreshedEmbed = await embedBuilder.roleSelection(currentTheme, team, loadedRoles, currentLobby.currentRules, pageSelected)
                refreshedView = await discordViewBuilder.roleOptionsView(currentTheme, loadedRoles, currentLobby, currentGame, prefix, client, team, adminRole, pageSelected)
                await interaction.message.edit(view=refreshedView, embed=refreshedEmbed)
                await interaction.response.defer()
            pageSelect.callback = handlePageChange
            returnedView.add_item(pageSelect)

        enableSelect = Select(placeholder= f'Choose to Enable {teamName} Roles', min_values=0, max_values=len(focusedRoles))
        for role in focusedRoles:
            enableSelect.add_option(label = role.shortName, emoji=role.emoji)
        async def enableRoles(interaction):
            changedRoles = await discordViewBuilder.getRoleRequest(enableSelect.values, loadedRoles) 
            await discordViewBuilder.changeRoleRules(currentGame, currentLobby, interaction, changedRoles, 'Enable', adminRole)
            refreshedEmbed = await embedBuilder.roleSelection(currentTheme, team, loadedRoles, currentLobby.currentRules, page)
            refreshedView = await discordViewBuilder.roleOptionsView(currentTheme, loadedRoles, currentLobby, currentGame, prefix, client, team, adminRole, page)
            await interaction.message.edit(view=refreshedView, embed=refreshedEmbed)
            await interaction.response.defer()
        enableSelect.callback = enableRoles
        returnedView.add_item(enableSelect)

        neutralSelect = Select(placeholder= f'Choose to Neutralize {teamName} Roles', min_values=0, max_values=len(focusedRoles))
        for role in focusedRoles:
            neutralSelect.add_option(label = role.shortName, emoji=role.emoji)
        async def neutralizeRoles(interaction):
            changedRoles = await discordViewBuilder.getRoleRequest(neutralSelect.values, loadedRoles)
            await discordViewBuilder.changeRoleRules(currentGame, currentLobby, interaction, changedRoles, 'Neutral', adminRole)
            refreshedEmbed = await embedBuilder.roleSelection(currentTheme, team, loadedRoles, currentLobby.currentRules, page)
            refreshedView = await discordViewBuilder.roleOptionsView(currentTheme, loadedRoles, currentLobby, currentGame, prefix, client, team, adminRole, page)
            await interaction.message.edit(view = refreshedView, embed = refreshedEmbed)
            await interaction.response.defer()
        neutralSelect.callback = neutralizeRoles
        returnedView.add_item(neutralSelect)

        disableSelect = Select(placeholder= f'Choose to Disable {teamName} Roles', min_values=0, max_values=len(focusedRoles))
        for role in focusedRoles:
            disableSelect.add_option(label = role.shortName, emoji=role.emoji)
        async def disableRoles(interaction):
            changedRoles = await discordViewBuilder.getRoleRequest(disableSelect.values, loadedRoles) 
            await discordViewBuilder.changeRoleRules(currentGame, currentLobby, interaction, changedRoles, 'Disable', adminRole)
            refreshedEmbed = await embedBuilder.roleSelection(currentTheme, team, loadedRoles, currentLobby.currentRules, page)
            refreshedView = await discordViewBuilder.roleOptionsView(currentTheme, loadedRoles, currentLobby, currentGame, prefix, client, team, adminRole, page)
            await interaction.message.edit(view=refreshedView, embed=refreshedEmbed)
            await interaction.response.defer()
        disableSelect.callback = disableRoles
        returnedView.add_item(disableSelect)

        backButton = Button(label = 'Go Back to Basic Options', emoji=currentTheme.emojiBackButton, style=discord.ButtonStyle.grey)

        async def processBackButton(interaction):
            embed = await embedBuilder.buildLobby(currentLobby, currentTheme, prefix)
            refreshedView = await discordViewBuilder.basicOptionsView(currentTheme, client, currentLobby, currentGame, prefix, loadedRoles, adminRole)
            await interaction.message.edit(embed=embed, view=refreshedView)
            await interaction.response.defer()

        backButton.callback = processBackButton
        returnedView.add_item(backButton)

        resetButton = Button(label = 'Reset Role Selection', emoji = str('🔄'), style=discord.ButtonStyle.grey)
        async def processResetButton(interaction):
            currentLobby.currentRules.clearRoles(team)
            refreshedEmbed = await embedBuilder.roleSelection(currentTheme, team, loadedRoles, currentLobby.currentRules, page)
            refreshedView = await discordViewBuilder.roleOptionsView(currentTheme, loadedRoles, currentLobby, currentGame, prefix, client, team, adminRole, page)
            await interaction.message.edit(view=refreshedView, embed=refreshedEmbed)
            await interaction.response.defer()
        resetButton.callback = processResetButton
        returnedView.add_item(resetButton)

        if team != 'Warriors':
            warriorButton = Button(label = f'Go to {currentTheme.warriorSingle} Role Options', emoji=currentTheme.emojiWarrior, style=discord.ButtonStyle.grey)
            async def processWarriorButton(interaction):
                refreshedEmbed = await embedBuilder.roleSelection(currentTheme, 'Warriors', loadedRoles, currentLobby.currentRules, page)
                refreshedView = await discordViewBuilder.roleOptionsView(currentTheme, loadedRoles, currentLobby, currentGame, prefix, client, 'Warriors', adminRole)
                await interaction.message.edit(view=refreshedView, embed=refreshedEmbed)
                await interaction.response.defer()
            warriorButton.callback = processWarriorButton
            returnedView.add_item(warriorButton)

        if team != 'Soldiers':
            soldierButton = Button(label = f'Go to {currentTheme.soldierSingle} Role Options', emoji=currentTheme.emojiSoldier, style=discord.ButtonStyle.grey)
            async def processSoldierButton(interaction):
                refreshedEmbed = await embedBuilder.roleSelection(currentTheme, 'Soldiers', loadedRoles, currentLobby.currentRules, page)
                refreshedView = await discordViewBuilder.roleOptionsView(currentTheme, loadedRoles, currentLobby, currentGame, prefix, client, 'Soldiers', adminRole)
                await interaction.message.edit(view=refreshedView, embed=refreshedEmbed)
                await interaction.response.defer()
            soldierButton.callback = processSoldierButton
            returnedView.add_item(soldierButton)

        if team != 'Wildcards':
            wildcardButton = Button(label = f'Go to {currentTheme.wildcardSingle} Role Options', emoji=currentTheme.emojiWildcard, style=discord.ButtonStyle.grey)
            async def processWildcardButton(interaction):
                refreshedEmbed = await embedBuilder.roleSelection(currentTheme, 'Wildcards', loadedRoles, currentLobby.currentRules, page)
                refreshedView = await discordViewBuilder.roleOptionsView(currentTheme, loadedRoles, currentLobby, currentGame, prefix, client, 'Wildcards', adminRole)
                await interaction.message.edit(view=refreshedView, embed=refreshedEmbed)
                await interaction.response.defer()
            wildcardButton.callback = processWildcardButton
            returnedView.add_item(wildcardButton)

        return returnedView
    
    @staticmethod
    async def savedRulesetView(currentTheme, client, currentLobby, currentGame, prefix, loadedRoles, adminRole):

        returnedView = View()
        player = databaseManager.searchForWvsPlayer(currentLobby.host)
        savedRulesets = player['savedRulesets']

        backButton = Button(label = 'Go Back to Basic Options', emoji=currentTheme.emojiBackButton, style=discord.ButtonStyle.grey)

        async def processBackButton(interaction):
            embed = await embedBuilder.buildLobby(currentLobby, currentTheme, prefix)
            refreshedView = await discordViewBuilder.basicOptionsView(currentTheme, client, currentLobby, currentGame, prefix, loadedRoles, adminRole)
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
                    refreshedView = await discordViewBuilder.savedRulesetView(currentTheme, client, currentLobby, currentGame, prefix, loadedRoles, adminRole)
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
            refreshedView = await discordViewBuilder.savedRulesetView(currentTheme, client, currentLobby, currentGame, prefix, loadedRoles, adminRole)
            await interaction.message.edit(view = refreshedView)
            await interaction.response.defer()

        saveSelect.callback = processSaveSelect
        loadSelect.callback = processLoadSelect
        returnedView.add_item(loadSelect)
        returnedView.add_item(saveSelect)
        return returnedView
        


    
    async def changeRoleRules(currentGame, currentLobby, interaction, changedRoles, enabledArg, adminRole):
        if currentGame.online == False and currentLobby.online and (interaction.user == currentLobby.host or adminRole in interaction.user.roles):
            currentLobby.currentRules.changeRoles(changedRoles, enabledArg)
    
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
        
