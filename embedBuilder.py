import discord
from discord.ext import commands
from themeData.defaultGameTheme import *
from gameObjects.Role import Role

from gameFunctions.searchFunctions import searchFunctions

class embedBuilder:

    async def buildLobby(currentLobby, currentTheme, prefix):
        returnedEmbed = discord.Embed(title = f'{currentTheme.gameName} Lobby', description =f'The lobby has: **{len(currentLobby.users)}** players within it.\n\nUse `{prefix}help rules` for information on how to change the rules.', color = currentTheme.lobbyEmbedColor)
        playerList = ''
        for player in currentLobby.users:
            playerList += f'**{player.mention}**\n'
        returnedEmbed.add_field(name = 'Players', value = playerList, inline = False)
        returnedEmbed.add_field(name = 'Current Theme', value = f'{currentTheme.emojiTheme}`{currentTheme.themeName}`', inline = False)
        return returnedEmbed
    
    async def buildReset(prefix):
        returnedEmbed = discord.Embed(title = 'The Game Lobby has been Reset.', description= f'Start a new lobby by using `{prefix}host`')
        return returnedEmbed
    
    async def buildRegistrationWelcome(user, homeServer, currentTheme, prefix):
        returnedEmbed = discord.Embed(title = f'Welcome to {homeServer.name}\'s Game Bot!', description=f'{user.mention}, This game is originally built on Entropi\'s Warriors vs Soldiers. notabear629 remastered it in the form of "Warriors vs Soldiers Reborn" with customizable themes. The current game theme is: **{currentTheme.gameName}** Due to part of the game\'s functionality, the bot no longer uses DMs, and instead this channel will be your new personal headquarters! A role has been given to you that gives you exclusive access to this channel. Please review the commands below to personalize your experience!')
        returnedEmbed.add_field(name= f'`{prefix}color`', value=f'This command will change your color to match the desired 6 digit hex code provided. You may also use `{prefix}colour` if you\'re a heathen like that. Example usage: `{prefix}color ff0000` will change your color to Red.', inline=True)
        returnedEmbed.add_field(name= f'`{prefix}renamechannel`', value = f'This command will allow you to rename your channel to your desired name. Usage: `{prefix}renamechannel The Dungeon` will change your channel\'s name to "The Dungeon". You may also use `{prefix}renamechannel` by itself to reset the channel name back to blank. PLEASE NOTE: DISCORD HAS A RATE LIMIT FOR BOTS OF 2 CHANNEL NAME CHANGES PER 10 MINUTES. THIS IS UNAVOIDABLE AND I CANNOT CHANGE IT. TRYING TO MAKE MORE THAN 2 IN A 10 MINUTE SPAN WILL SEVERELY DELAY THE RENAME OPERATION.', inline=True)
        returnedEmbed.add_field(name = f'`{prefix}renamerole`', value = f'This command is essentially the same as the above command, except for renames your role. Usage: `{prefix}renamerole King of WvS` will change your role name to "King of WvS". You may also use `{prefix}renamerole` by itself to reset its name back to the default name.', inline=True)
        returnedEmbed.add_field(name = f'`{prefix}fixme`', value = f'This command will fix your user information. If you lose your role, your role or channel gets deleted, or any other number of issues, you can simply use the command: `{prefix}fixme` and the bot will attempt to fix your user information.', inline=True)
        return returnedEmbed
    
    async def buildRoleMessageEmbed(player, message, color, thumbnail):
        returnedEmbed = discord.Embed(title = f'**{player.role.emoji}{player.role.name}{player.role.emoji}**', description=message, color=color)
        returnedEmbed.set_thumbnail(url = thumbnail)
        return returnedEmbed
    
    async def buildStatusEmbed(currentGame, currentTheme, futureExpoCounts):
        buildDescription = f'Number of Players: **{len(currentGame.players)}**'
        if len(currentGame.deadPlayers) > 0:
            buildDescription += f' (**{len(currentGame.livingPlayers)}** Alive)'
        buildDescription += '\n'
        buildDescription += f'**{len(currentGame.soldiers)}** {currentTheme.soldierPlural}'
        if len(currentGame.deadSoldiers) > 0:
            buildDescription += f' (**{len(currentGame.livingSoldiers)}** Alive)'
        buildDescription += f' vs **{len(currentGame.warriors)}** {currentTheme.warriorPlural}'
        if len(currentGame.deadWarriors) > 0:
            buildDescription += f' (**{len(currentGame.livingWarriors)}** Alive)'
        if currentGame.roundFails == 3:
            selectedColor = currentTheme.lostColor
        elif currentGame.roundFails > currentGame.roundWins:
            selectedColor = currentTheme.losingColor
        elif currentGame.roundFails == currentGame.roundWins:
            selectedColor = currentTheme.neutralColor
        else:
            selectedColor = currentTheme.winningColor
        returnedEmbed = discord.Embed(title = 'Current Game Status', description= buildDescription, color= selectedColor)
        spaceEmoji = f'{currentTheme.emojiSpacer}'
        spacer = spaceEmoji + spaceEmoji
        bigSpacer = spacer + spacer
        progressString = ''
        progressMarkerEmotes = [currentTheme.emojiWinMarkerOne, currentTheme.emojiWinMarkerTwo, currentTheme.emojiWinMarkerThree]
        for i in range(3):
            if currentGame.roundWins > i:
                progressString += bigSpacer + currentTheme.emojiRoundVictoryMarker
            else:
                progressString += bigSpacer + progressMarkerEmotes[i]
            if i != 2:
                progressString += '\n'
            else:
                progressString += currentTheme.emojiVictoryMarker
        returnedEmbed.add_field(name = currentTheme.statusProgress, value=progressString, inline=True)
        wallMaria = f'{currentTheme.emojiMariaExterior}{currentTheme.emojiMariaInterior}{currentTheme.emojiMariaExterior}'
        wallRose = f'{currentTheme.emojiRoseExterior}{currentTheme.emojiRoseInterior}{currentTheme.emojiRoseExterior}'
        wallSina = f'{currentTheme.emojiSinaExterior}{currentTheme.emojiSinaInterior}{currentTheme.emojiSinaExterior}'
        walls = [wallMaria, wallRose, wallSina]
        wallStatusString = ''
        for i in range(3):
            if currentGame.roundFails > i:
                wallStatusString += f'{spacer}{currentTheme.emojiBrokenExterior}{currentTheme.emojiBrokenInterior}{currentTheme.emojiBrokenExterior}'
            else:
                wallStatusString += spacer + walls[i]
            if i != 2:
                wallStatusString += '\n'
        returnedEmbed.add_field(name = currentTheme.statusWalls, value = wallStatusString, inline = True)
        previousExpoCounts = currentGame.previousExpeditionCounts
        index = 0
        for expo in previousExpoCounts:
            previousExpoCounts[index] = str(previousExpoCounts[index])
            index += 1
        currentExpoCount = [str(currentGame.currentExpo.size)]
        expoCounts = previousExpoCounts + currentExpoCount + futureExpoCounts
        expeditionString = ''
        for i in range(5):
            currentRound =  i + 1
            statusMarker = ''
            if currentRound in currentGame.failedRounds:
                statusMarker = f'{currentTheme.emojiFailMarker}'
            elif currentRound in currentGame.passedRounds:
                statusMarker = f'{currentTheme.emojiWinMarker}'
            elif currentRound == currentGame.currentRound:
                statusMarker = f'{currentTheme.emojiCurrentMarker}' 
            expeditionString += f'{currentTheme.expeditionName} {currentRound}: **{expoCounts[i]}** {currentTheme.expoMembersName} {statusMarker}'
            if i != 4:
                expeditionString += '\n'
        returnedEmbed.add_field(name = currentTheme.statusExpeditions, value = expeditionString, inline = False)
        return returnedEmbed
    
    async def buildCurrentRoles(currentGame, currentTheme):
        returnedEmbed = discord.Embed(title = 'Current list of roles in game', color = currentTheme.rolesEmbedColor)
        soldierList = ''
        for role in Role.soldierRoles:
            search = await searchFunctions.roleIDToPlayer(currentGame, role)
            if search != None:
                if type(search) == list:
                    for player in search:
                        soldierList += f'{player.role.emoji}{player.role.name}{player.role.emoji}\n'
                else:
                    soldierList += f'{search.role.emoji}{search.role.name}{search.role.emoji}\n'
        returnedEmbed.add_field(name = f'{currentTheme.emojiSoldier}{currentTheme.soldierPlural}{currentTheme.emojiSoldier}', value = soldierList, inline = False)
        warriorList = ''
        for role in Role.warriorRoles:
            search = await searchFunctions.roleIDToPlayer(currentGame, role)
            if search != None:
                if type(search) == list:
                    for player in search:
                        warriorList += f'{player.role.emoji}{player.role.name}{player.role.emoji}\n'
                else:
                    warriorList += f'{search.role.emoji}{search.role.name}{search.role.emoji}\n'
        returnedEmbed.add_field(name = f'{currentTheme.emojiWarrior}{currentTheme.warriorPlural}{currentTheme.emojiWarrior}', value = warriorList, inline = False)
        return returnedEmbed
    
    async def buildPlayers(currentGame, currentTheme):
        playerList = ''
        for player in currentGame.commanderOrder:
            playerList += f'{player.user.mention}'
            if player == currentGame.commanderOrder[0]:
                playerList += f'{currentTheme.emojiCommanderMarker}'
            playerList += '\n'
        returnedEmbed = discord.Embed(title = f'List of players (in queue to become {currentTheme.commanderName})', description = playerList, color = currentTheme.playersEmbedColor)
        return returnedEmbed
    
    async def pickExpoMember(currentGame, currentTheme):
        playerList = ''
        for player in currentGame.currentExpo.expeditionMembers:
            playerList += f'**{player.user.name}**\n'
        returnedEmbed = discord.Embed(title = f'{len(currentGame.currentExpo.expeditionMembers)}/{currentGame.currentExpo.size} players in {currentTheme.expeditionTeam}', description=playerList, color=currentTheme.pickColor)
        return returnedEmbed
    
    async def voteDM(currentGame, player, currentTheme):
        playerList = f'The current {currentTheme.expeditionTeam}:\n'
        for expeditioner in currentGame.currentExpo.expeditionMembers:
            playerList += f'**{expeditioner.user.name}**'
            if (expeditioner in currentGame.warriors and player in currentGame.warriors) or (player.role.id == 'Eren' and expeditioner in currentGame.warriors and expeditioner.role.id != 'Zeke'):
                playerList += f'{currentTheme.emojiWarrior}'
            playerList += '\n'
        returnedEmbed = discord.Embed(title = f'{currentTheme.expeditionName} Approval', description = playerList, color=currentTheme.voteDMColor)
        if player.role.id == 'Jean' and currentGame.currentExpo.jeanActivated:
            voteDesc = f'You have voted to secure this {currentTheme.expeditionTeam}.'
        elif player.role.id == 'Pieck' and currentGame.currentExpo.pieckActivated and player in currentGame.currentExpo.rejected:
            voteDesc = f'You have chosen to flip and accept this {currentTheme.expeditionTeam}.'
        elif player.role.id == 'Pieck' and currentGame.currentExpo.pieckActivated and player in currentGame.currentExpo.accepted:
            voteDesc = f'You have chosen to flip and accept this {currentTheme.expeditionTeam}.'
        elif player in currentGame.currentExpo.accepted:
            voteDesc = f'You have voted to accept this {currentTheme.expeditionTeam}.'
        elif player in currentGame.currentExpo.rejected:
            voteDesc = f'You have voted to reject this {currentTheme.expeditionTeam}.'
        elif player in currentGame.currentExpo.abstained:
            voteDesc = f'You have abstained from voting on this {currentTheme.expeditionTeam}.'
        else:
            voteDesc = f'You have not yet voted on this {currentTheme.expeditionTeam}.\n\n{currentTheme.emojiAcceptExpedition} Click the Accept Button to Accept the {currentTheme.expeditionTeam}\n{currentTheme.emojiRejectExpedition} Click the Reject Button to Reject the {currentTheme.expeditionTeam}\n{currentTheme.emojiAbstainExpedition} Click the Abstain Button to Abstain from voting on the {currentTheme.expeditionTeam}'
            if player.role.id == 'Jean' and player.role.abilityActive:
                voteDesc += f'\n{player.role.emoji} Click the Secure Button to Secure the {currentTheme.expeditionTeam}.'
            elif player.role.id == 'Pieck' and player.role.abilityActive:
                voteDesc += f'\n{player.role.emoji}{currentTheme.emojiAcceptExpedition} Click the Flip and Accept Button to Flip the votes, and **AFTER FLIPPING** accept the {currentTheme.expeditionTeam}. Click this if you want to stay accepted after flip.'
                voteDesc += f'\n{player.role.emoji}{currentTheme.emojiRejectExpedition} Click the Flip and Reject Button to Flip the votes, and **AFTER FLIPPING** reject the {currentTheme.expeditionTeam}. Click this if you want to stay rejected after flip.'
        returnedEmbed.add_field(name = f'Your Vote', value=voteDesc)
        return returnedEmbed
    
    async def showVotingResults(currentGame, currentTheme, expeditionPassed):
        if currentGame.currentExpo.jeanActivated:
            playerList = ''
            for voter in currentGame.currentExpo.eligibleVoters:
                playerList += f'**{voter.user.name}**'
                playerList += f'{currentTheme.emojiAcceptExpedition}\n'
        else:
            playerList = ''
            displayAccept = f'{currentTheme.emojiAcceptExpedition}'
            displayReject = f'{currentTheme.emojiRejectExpedition}'
            if currentGame.currentExpo.pieckActivated:
                displayReject = f'{currentTheme.emojiAcceptExpedition}'
                displayAccept = f'{currentTheme.emojiRejectExpedition}'
            for voter in currentGame.currentExpo.eligibleVoters:
                playerList += f'**{voter.user.name}**'
                if voter in currentGame.currentExpo.accepted:
                    playerList += displayAccept
                elif voter in currentGame.currentExpo.rejected:
                    playerList += displayReject
                elif voter in currentGame.currentExpo.abstained:
                    playerList += f'{currentTheme.emojiAbstainExpedition}'
                playerList += '\n'
        if currentGame.currentExpo.jeanActivated:
            embedColor = currentTheme.jeanedExpeditionColor
        elif expeditionPassed:
            embedColor = currentTheme.acceptedExpeditionColor
        elif expeditionPassed == False:
            embedColor = currentTheme.rejectedExpeditionColor
        returnedEmbed = discord.Embed(title = f'{currentTheme.expeditionName} Voting Results', description= playerList, color = embedColor)
        return returnedEmbed
    
    async def expeditionDM(currentGame, player, currentTheme):
        playerList = f'The current {currentTheme.expeditionTeam}:\n'
        for expeditioner in currentGame.currentExpo.expeditionMembers:
            playerList += f'**{expeditioner.user.name}**'
            if (expeditioner in currentGame.warriors and player in currentGame.warriors) or (player.role.id == 'Eren' and expeditioner in currentGame.warriors and expeditioner.role.id != 'Zeke'):
                playerList += f'{currentTheme.emojiWarrior}'
            playerList += '\n'

        if player in currentGame.currentExpo.passedExpedition:
            decisionString = f'You have chosen to pass this {currentTheme.expeditionName}.'
        elif player in currentGame.currentExpo.sabotagedExpedition:
            decisionString = f'You have chosen to sabotage this {currentTheme.expeditionName}.'
        else:
            decisionString = f'You have not yet made a decision on what to do on this {currentTheme.expeditionName}.'

        returnedEmbed = discord.Embed(title = f'{currentTheme.expeditionName} Decision', description=playerList, color = currentTheme.expeditionDMColor)
        returnedEmbed.add_field(name = f'Your Decision', value = decisionString, inline=False)

        return returnedEmbed
    
    async def temporaryMessage(currentGame, currentTheme):
        if currentGame.currentExpo.currentlyVoting:
            returnedEmbed = discord.Embed(title = f'{currentTheme.expeditionName} Voters', description= f'{len(currentGame.currentExpo.voted)}/{len(currentGame.currentExpo.eligibleVoters)}', color = currentTheme.temporaryMessageColor)
            return returnedEmbed
        elif currentGame.currentExpo.currentlyExpeditioning:
            returnedEmbed = discord.Embed(title = f'{currentTheme.expeditionTeamMembers}', description= f'{len(currentGame.currentExpo.expeditioned)}/{len(currentGame.currentExpo.expeditionMembers)}', color = currentTheme.temporaryMessageColor)
            return returnedEmbed
        
    async def results(currentGame, currentTheme, result):
        if result == 'y':
            resultColor = currentTheme.expoPassedColor
        elif result == 'n':
            resultColor = currentTheme.expoSabotagedColor
        outcomeList = ''
        for passer in currentGame.currentExpo.passedExpedition:
            outcomeList += f'{currentTheme.emojiPassExpedition}\n'
        for sabotager in currentGame.currentExpo.sabotagedExpedition:
            outcomeList += f'{currentTheme.emojiSabotageExpedition}\n'
        returnedEmbed = discord.Embed(title = f'{currentTheme.expeditionName} Results', description=outcomeList, color = resultColor)

        return returnedEmbed
    
    async def endgame(currentGame, currentTheme):
        
        buildDescription = f'Number of Players: **{len(currentGame.players)}**'
        buildDescription += '\n'
        buildDescription += f'**{len(currentGame.soldiers)}** {currentTheme.soldierPlural}'
        buildDescription += f' vs **{len(currentGame.warriors)}** {currentTheme.warriorPlural}'

        returnedEmbed = discord.Embed(title = f'Game Summary', description=buildDescription, color= currentTheme.endgameCardColor)
        for role in Role.allRoles:
            search = await searchFunctions.roleIDToPlayer(currentGame, role)
            if search != None:
                if type(search) == list:
                    newTitle = f'{search[0].role.emoji}{search[0].role.name}{search[0].role.emoji}'
                    newDesc = ''
                    for player in search:
                        newDesc += f'{player.user.name}'
                        if player in currentGame.winners:
                            newDesc += f'{currentTheme.emojiWinner}'
                        else:
                            newDesc += f'{currentTheme.emojiLoser}'
                        if player != search[len(search)-1]:
                            newDesc += '\n'
                    returnedEmbed.add_field(name=newTitle, value = newDesc, inline= True)
                else:
                    if search in currentGame.winners:
                        addedEmoji = currentTheme.emojiWinner
                    else:
                        addedEmoji = currentTheme.emojiLoser
                    returnedEmbed.add_field(name=f'{search.role.emoji}{search.role.name}{search.role.emoji}', value=f'{search.user.name}{addedEmoji}', inline=True)
        return returnedEmbed
    
    async def roleSelection(currentTheme, team, loadedRoles, currentRules):
        if team == 'Soldiers':
            selectedPlural = currentTheme.soldierPlural
            selectedColor = currentTheme.soldierColor
            selectedThumbnail = currentTheme.soldierThumbnail
            selectedSubgroup = Role.soldierGroupOptional
            enabledGroup = currentRules.enabledSoldiers
            disabledGroup = currentRules.disabledSoldiers
        elif team == 'Warriors':
            selectedPlural = currentTheme.warriorPlural
            selectedColor = currentTheme.warriorColor
            selectedThumbnail = currentTheme.warriorThumbnail
            selectedSubgroup = Role.warriorGroupOptional
            enabledGroup = currentRules.enabledWarriors
            disabledGroup = currentRules.disabledWarriors
        returnedEmbed = discord.Embed(title = f'Options for {selectedPlural} Roles', color = selectedColor)
        returnedEmbed.set_thumbnail(url = selectedThumbnail)

        for role in loadedRoles:
            if role.id in selectedSubgroup:
                if role.id in enabledGroup:
                    selectedValue = f'{currentTheme.emojiRoleEnabled}`Enabled`'
                elif role.id in disabledGroup:
                    selectedValue = f'{currentTheme.emojiRoleDisabled}`Disabled`'
                else:
                    selectedValue = f'{currentTheme.emojiRoleDefault}`Default`'
                returnedEmbed.add_field(name = f'{role.emoji}{role.shortName}{role.emoji}', value=selectedValue, inline=True)

        return returnedEmbed
    

