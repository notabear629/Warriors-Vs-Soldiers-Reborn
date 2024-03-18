import discord
from discord.ext import commands
from themeData.defaultGameTheme import *
from gameObjects.Role import Role

from gameFunctions.searchFunctions import searchFunctions

from dataFunctions.databaseManager import databaseManager

class embedBuilder:

    async def buildLobby(currentLobby, currentTheme, prefix):
        returnedEmbed = discord.Embed(title = f'{currentTheme.gameName} Lobby', description =f'The lobby has: **{len(currentLobby.users)}** players within it.\n\nUse `{prefix}help` for help and info about the game. Use `{prefix}options` or `{prefix}rules` as the host to change the game rules.', color = currentTheme.lobbyEmbedColor)
        playerList = ''
        for player in currentLobby.users:
            playerList += f'**{player.mention}**\n'
        returnedEmbed.add_field(name = 'Players', value = playerList, inline = False)
        returnedEmbed.add_field(name = 'Current Theme', value = f'{currentTheme.emojiTheme}`{currentTheme.themeName}`', inline = False)
        if currentLobby.currentRules.noCoordinate and currentLobby.currentRules.noWarchief:
            captainEmoji = str('❌')
            captainChoice = 'Coordinate and Warchief Disabled'
        elif currentLobby.currentRules.noCoordinate and currentLobby.currentRules.noWarchief == False:
            captainEmoji = str('🦹‍♂️')
            captainChoice = 'Only Warchief Enabled'
        elif currentLobby.currentRules.noCoordinate == False and currentLobby.currentRules.noWarchief:
            captainEmoji = str('🗺️')
            captainChoice = 'Only Coordinate Enabled'
        else:
            captainEmoji = str('✅')
            captainChoice = 'Coordinate and Warchief Enabled'
        returnedEmbed.add_field(name = f'Team Captains', value = f'{captainEmoji}`{captainChoice}`', inline=False)
        if currentLobby.currentRules.enabledSoldiers == [] and currentLobby.currentRules.disabledSoldiers == [] and currentLobby.currentRules.enabledWarriors == [] and currentLobby.currentRules.disabledWarriors == [] and currentLobby.currentRules.enabledWildcards == [] and currentLobby.currentRules.disabledWildcards == []:
            customEmoji = str('🎲')
            customChoice = 'Completely Random'
        else:
            customEmoji = str('🎭')
            customChoice = 'Role Selection Active'
        returnedEmbed.add_field(name = 'Roleset Rules', value = f'{customEmoji}`{customChoice}`', inline=False)
        if currentLobby.currentRules.multikidnap:
            kidnapEmoji = str('♾️')
            kidnapVal = 'Multi-kidnap'
        else:
            kidnapEmoji = str('🌐')
            kidnapVal = 'Standard Rules'
        returnedEmbed.add_field(name = 'Kidnap Rules', value = f'{kidnapEmoji}`{kidnapVal}`', inline = False)
        if currentLobby.currentRules.rumbling:
            rumblingEmoji = currentTheme.emojiRumbling
            rumblingVal = 'Enabled'
        else:
            rumblingEmoji = str('❌')
            rumblingVal = 'Disabled'
        returnedEmbed.add_field(name = f'{currentTheme.rumblingName}', value = f'{rumblingEmoji}`{rumblingVal}`', inline = False)
        if currentLobby.currentRules.wildcards:
            wildcardEmoji = currentTheme.emojiWildcard
            wildcardVal = 'Enabled'
        else:
            wildcardEmoji = str('❌')
            wildcardVal = 'Disabled'
        returnedEmbed.add_field(name = 'Wildcards', value = f'{wildcardEmoji}`{wildcardVal}`', inline=False)
        if currentLobby.currentRules.casual:
            rankedEmoji = currentTheme.emojiCasual
            rankedChoice = 'Casual'
        else:
            rankedEmoji = currentTheme.emojiRanked
            rankedChoice = 'Ranked'
        returnedEmbed.add_field(name = 'Ranked Status', value = f'{rankedEmoji}`{rankedChoice}`', inline= False)
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
        if len(currentGame.wildcards) > 0:
            buildDescription += f' with **{len(currentGame.wildcards)}** {currentTheme.wildcardPlural}'
            if len(currentGame.deadWildcards) > 0:
                buildDescription += f' (**{len(currentGame.livingWildcards)}** Alive)'
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
                if currentGame.currentRules.noCoordinate:
                    soldierList += str('❓\n')
                    continue
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

        if len(currentGame.wildcards) > 0:
            wildcardList = ''
            for role in Role.wildcardRoles:
                search = await searchFunctions.roleIDToPlayer(currentGame, role)
                if search != None:
                    if type(search) == list:
                        for player in search:
                            wildcardList += f'{player.role.emoji}{player.role.name}{player.role.emoji}\n'
                    else:
                        wildcardList += f'{search.role.emoji}{search.role.name}{search.role.emoji}\n'
            returnedEmbed.add_field(name = f'{currentTheme.emojiWildcard}{currentTheme.wildcardPlural}{currentTheme.emojiWildcard}', value = wildcardList, inline = False)

        if currentGame.deadPlayers != []:
            deadList = ''
            for player in currentGame.deadPlayers:
                if player in currentGame.deadSoldiers:
                    roleEmoji = currentTheme.emojiSoldier
                elif player in currentGame.deadWarriors:
                    roleEmoji = currentTheme.emojiWarrior
                elif player in currentGame.deadWildcards:
                    roleEmoji = currentTheme.emojiWildcard
                deadList += f'{roleEmoji}{player.user.name}{roleEmoji}\n'
            returnedEmbed.add_field(name = f'{currentTheme.emojiDead}Dead Players{currentTheme.emojiDead}', value=deadList, inline=False)
            
        return returnedEmbed
    
    async def soldierRoleDM(currentGame, currentTheme):
        soldierList = ''
        for role in Role.soldierRoles:
            search = await searchFunctions.roleIDToPlayer(currentGame, role)
            if search != None:
                if type(search) == list:
                    for player in search:
                        soldierList += f'{player.role.emoji}{player.role.name}{player.role.emoji}\n'
                else:
                    soldierList += f'{search.role.emoji}{search.role.name}{search.role.emoji}\n'
        returnedEmbed = discord.Embed(title = f'{currentTheme.emojiSoldier}List of {currentTheme.soldierSingle} Roles{currentTheme.emojiSoldier}', description= soldierList, color = currentTheme.warriorColor)
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
        titansSmelled = 0
        for expeditioner in currentGame.currentExpo.expeditionMembers:
            playerList += f'**{expeditioner.user.name}**'
            if (expeditioner in currentGame.warriors and player in currentGame.warriors and player.role.id != 'Magath' and expeditioner.role.id != 'Magath') or (player.role.id == 'Eren' and (expeditioner in currentGame.warriors or (expeditioner.role.id == 'Frecklemir' and currentGame.frecklemirTeam == 'Warriors')) and expeditioner.role.id != 'Zeke'):
                playerList += f'{currentTheme.emojiWarrior}'
            elif (expeditioner in currentGame.warriors and player in currentGame.warriors and (player.role.id == 'Magath' or expeditioner.role.id == 'Magath')):
                playerList += f'{currentTheme.emojiWarrior}{expeditioner.role.emoji}'
            playerList += '\n'
            if expeditioner.role.isTitan:
                titansSmelled += 1
        if player.role.id == 'Mike' and player in currentGame.currentExpo.expeditionMembers:
            titanName = currentTheme.titanPlural
            if titansSmelled == 1:
                titanName = currentTheme.titanSingle
            playerList += f'\n{player.role.secondaryEmoji}You {currentTheme.mikeSmell} **{titansSmelled}** {titanName}!{player.role.secondaryEmoji}'
        if player.role.id == 'Floch' and player in currentGame.currentExpo.expeditionMembers:
            Eren = await searchFunctions.roleIDToPlayer(currentGame, 'Eren')
            erenEmoji = Eren.role.emoji
            playerList += '\n'
            if Eren in currentGame.currentExpo.expeditionMembers:
                playerList += f'{erenEmoji}{currentTheme.flochMessageEren}{erenEmoji}'
            else:
                playerList += f'{currentTheme.emojiNoEren}{currentTheme.flochMessageNoEren}{currentTheme.emojiNoEren}'
        returnedEmbed = discord.Embed(title = f'{currentTheme.expeditionName} Approval', description = playerList, color=currentTheme.voteDMColor)
        if player.role.id == 'Jean' and currentGame.currentExpo.jeanActivated:
            voteDesc = f'You have voted to secure this {currentTheme.expeditionTeam}.'
        elif player.role.id == 'Pieck' and currentGame.currentExpo.pieckActivated and player in currentGame.currentExpo.rejected:
            voteDesc = f'You have chosen to flip and accept this {currentTheme.expeditionTeam}.'
        elif player.role.id == 'Pieck' and currentGame.currentExpo.pieckActivated and player in currentGame.currentExpo.accepted:
            voteDesc = f'You have chosen to flip and accept this {currentTheme.expeditionTeam}.'
        elif player.role.id == 'Falco' and currentGame.currentExpo.falcoActivated and player in currentGame.currentExpo.voted:
            voteDesc = f'You have chosen to intercept the votes on this {currentTheme.expeditionTeam}.'
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
            if player.role.id == 'Falco' and player.role.abilityActive:
                voteDesc += f'\n{player.role.emoji} Click the Intercept Button to Intercept the {currentTheme.expeditionTeam} votes, which will turn to an accept ONLY IF it will pass.'
            elif player.role.id == 'Pieck' and player.role.abilityActive:
                voteDesc += f'\n{player.role.secondaryEmoji}{currentTheme.emojiAcceptExpedition} Click the Flip and Accept Button to Flip the votes, and **AFTER FLIPPING** accept the {currentTheme.expeditionTeam}. Click this if you want to stay accepted after flip.'
                voteDesc += f'\n{player.role.secondaryEmoji}{currentTheme.emojiRejectExpedition} Click the Flip and Reject Button to Flip the votes, and **AFTER FLIPPING** reject the {currentTheme.expeditionTeam}. Click this if you want to stay rejected after flip.'
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
            if (expeditioner in currentGame.warriors and player in currentGame.warriors and player.role.id != 'Magath' and expeditioner.role.id != 'Magath') or (player.role.id == 'Eren' and expeditioner in currentGame.warriors and expeditioner.role.id != 'Zeke'):
                playerList += f'{currentTheme.emojiWarrior}'
            elif (expeditioner in currentGame.warriors and player in currentGame.warriors and (player.role.id == 'Magath' or expeditioner.role.id == 'Magath')):
                playerList += f'{currentTheme.emojiWarrior}{expeditioner.role.emoji}'
            playerList += '\n'
        playerList += '\n'
        playerList += f'{currentTheme.emojiPassExpedition} Select Pass to Pass this {currentTheme.expeditionName} normally\n'
        if player in currentGame.warriors:
            playerList += f'{currentTheme.emojiSabotageExpedition} Select Sabotage to Sabotage this {currentTheme.expeditionName}\n'
        if player.role.id == 'Armin' and player.role.abilityActive and currentGame.roundFails < 2:
            playerList += f'{currentTheme.emojiNuke} Select Nuke to fail this {currentTheme.expeditionName}, and take its {currentTheme.expeditionTeamMembers} with it.\n'
        if player.role.id == 'Levi' and player.role.abilityActive and currentGame.roundFails < 2:
            playerList += f'{player.role.secondaryEmoji} Select Attack to kill any {currentTheme.warriorPlural} that try to attack, but not defend the {currentTheme.expeditionName}\n'
        if player.role.id == 'Levi' and player.role.abilityActive:
            playerList += f'{player.role.emoji} Select Defend to defend the {currentTheme.expeditionName} and guarantee its success, but let any attackers survive.\n'
        if player.role.id == 'Daz' and player.role.abilityActive and player in currentGame.currentExpo.rejected:
            playerList += f'{player.role.secondaryEmoji} Select Chicken Out to cancel this {currentTheme.expeditionName} and go back to the picking phase.\n'
        if player.role.id == 'Mikasa':
            playerList += f'{player.role.emoji} Select a player from the "Choose Player to Guard to Pass this {currentTheme.expeditionName}, and guard that player.\n'
        if player.role.id == 'Bertholdt':
            playerList += f'{player.role.secondaryEmoji} Select Cloak to Sabotage this {currentTheme.expeditionName} and hide how many saboteurs were present.\n'
        if player.role.id == 'Annie' and player.role.abilityActive:
            playerList += f'{player.role.secondaryEmoji} Select Input Scream Message to sabotage this {currentTheme.expeditionName} and then pass a secret message to your fellow {currentTheme.warriorPlural}.\n'
        if player.role.id == 'Kenny':
            playerList += f'{player.role.secondaryEmoji} Select a player to Kill to kill them and pass this {currentTheme.expeditionName}.\n'

        if player.role.id == 'Armin' and currentGame.currentExpo.arminActivated:
            decisionString = f'You have chosen to nuke this {currentTheme.expeditionName}.'
        elif player.role.id == 'Levi' and currentGame.currentExpo.leviAttacked:
            decisionString = f'You have chosen to attack all {currentTheme.warriorPlural} that dare to challenge you.'
        elif player.role.id == 'Levi' and currentGame.currentExpo.leviDefended:
            decisionString = f'You have chosen to defend this {currentTheme.expeditionName}.'
        elif player.role.id == 'Daz' and currentGame.currentExpo.dazActivated:
            decisionString = f'You have chosen to chicken out from going on this {currentTheme.expeditionName}.'
        elif player.role.id == 'Mikasa' and currentGame.currentExpo.mikasaGuarded != None and type(currentGame.currentExpo.mikasaGuarded) != dict:
            decisionString = f'You have chosen to pass the expedition while guarding **{currentGame.currentExpo.mikasaGuarded.user.name}**.'
        elif player.role.id == 'Bertholdt' and currentGame.currentExpo.bertholdtCloaked:
            decisionString = f'You have chosen to cloak and sabotage this {currentTheme.expeditionName}.'
        elif player.role.id == 'Annie' and currentGame.currentExpo.annieMessage != None:
            decisionString = f'You have chosen to sabotage the {currentTheme.expeditionName} and send a secret message to your fellow {currentTheme.warriorPlural}'
        elif player.role.id == 'Kenny' and currentGame.currentExpo.kennyMurdered != None:
            decisionString = f'You have chosen to Kill {currentGame.currentExpo.kennyMurdered.user.name}.'
        elif player in currentGame.currentExpo.passedExpedition:
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
        elif currentGame.currentlyKidnapping and currentGame.currentRules.multikidnap:
            returnedEmbed = discord.Embed(title = f'Kidnap Decision', description= f'{len(currentGame.multikidnapRecord)}/{len(currentGame.warriors)}', color = currentTheme.temporaryMessageColor)
            return returnedEmbed
        
    async def results(currentGame, currentTheme, result):
        if result == 'y':
            if currentGame.currentExpo.leviDefended and len(currentGame.currentExpo.sabotagedExpedition) > 0:
                resultColor = currentTheme.expoSecuredColor
            else:
                resultColor = currentTheme.expoPassedColor
        elif result == 'n':
            resultColor = currentTheme.expoSabotagedColor
        elif result == 'Armin':
            resultColor = currentTheme.arminNukeColor
        outcomeList = ''
        if currentGame.currentExpo.arminActivated:
            for player in currentGame.currentExpo.expeditionMembers:
                outcomeList += f'{currentTheme.emojiNuke}\n'
        elif currentGame.currentExpo.leviDefended:
            if len(currentGame.currentExpo.sabotagedExpedition) > 0:
                for player in currentGame.currentExpo.expeditionMembers:
                    outcomeList += f'{currentTheme.emojiSecuredExpedition}\n'
            else:
                for player in currentGame.currentExpo.expeditionMembers:
                    outcomeList += f'{currentTheme.emojiPassExpedition}\n'
        elif currentGame.currentExpo.bertholdtCloaked:
            for player in currentGame.currentExpo.expeditionMembers:
                if player.role.id == 'Bertholdt':
                    Bertholdt = player
                    break
            for player in currentGame.currentExpo.expeditionMembers:
                outcomeList += f'{Bertholdt.role.secondaryEmoji}\n'
        else:
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
    
    async def scoreboard(currentGame, currentTheme):

        returnedEmbed = discord.Embed(title = f'Scoreboard', color= currentTheme.endgameCardColor)
        for role in Role.allRoles:
            search = await searchFunctions.roleIDToPlayer(currentGame, role)
            if search != None:
                if type(search) == list:
                    for player in search:
                        if player == currentGame.MVP:
                            addedEmoji = currentTheme.emojiMVP
                        elif player in currentGame.winners:
                            addedEmoji = currentTheme.emojiWinner
                        else:
                            addedEmoji = currentTheme.emojiLoser
                        returnedEmbed.add_field(name = f'{addedEmoji}{player.user.name}{addedEmoji}', value=f'MVP Points: {player.mvpPoints}', inline=True)
                else:
                    if search == currentGame.MVP:
                        addedEmoji = currentTheme.emojiMVP
                    elif search in currentGame.winners:
                        addedEmoji = currentTheme.emojiWinner
                    else:
                        addedEmoji = currentTheme.emojiLoser
                    returnedEmbed.add_field(name = f'{addedEmoji}{search.user.name}{addedEmoji}', value=f'MVP Points: {search.mvpPoints}', inline=True)

        return returnedEmbed
    
    async def pointsBoard(currentGame, currentTheme):
        updateValue = ''
        for player in currentGame.players:
            db = databaseManager.getWvsPlayerByID(player.user.id)
            differential = db['points']['LegacyPoints'] - player.oldLegacyPoints
            if differential < 0:
                difVal = str(differential)
            else:
                difVal = f'+{differential}'
            updateValue += f'{player.user.name}: **{player.oldLegacyPoints}** --> **{db['points']['LegacyPoints']}** ({difVal})\n'
        returnedEmbed = discord.Embed(title = 'Legacy Points Update', description = updateValue, color = currentTheme.endgameCardColor)
        return returnedEmbed
    
    async def savedRulesets(currentTheme):
        returnedEmbed = discord.Embed(title = 'Loaded Rulesets', description='This is a place to load in rulesets you have already saved. Use the load option to choose to load a ruleset you have previously saved. Use save and choose a slot to save a new ruleset, or overwrite an older ruleset to that slot.', color= currentTheme.lobbyEmbedColor)
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
        elif team == 'Wildcards':
            selectedPlural = currentTheme.wildcardPlural
            selectedColor = currentTheme.wildcardColor
            selectedThumbnail = currentTheme.wildcardThumbnail
            selectedSubgroup = Role.wildcardRoles
            enabledGroup = currentRules.enabledWildcards
            disabledGroup = currentRules.disabledWildcards
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
    
    async def infoUpdate(currentTheme, player, infoMessage):
        if player.role.team == 'Soldiers':
            selectedColor = currentTheme.soldierColor
        elif player.role.team == 'Warriors':
            selectedColor = currentTheme.warriorColor
        returnedEmbed = discord.Embed(title= f'{player.role.name} Information Update', description=infoMessage, color = selectedColor)
        return returnedEmbed

    async def rumblingStatusEmbed(currentGame, currentTheme, futureExpoCounts, altCase = None):
        buildDescription = f'Number of Players: **{len(currentGame.players)}**'
        if len(currentGame.deadPlayers) > 0:
            buildDescription += f' (**{len(currentGame.livingPlayers)}** Alive)'
        buildDescription += '\n'
        if altCase == None:
            buildDescription += f'**{len(currentGame.yeagerists)}** {currentTheme.yeageristPlural}'
            if len(currentGame.deadYeagerists) > 0:
                buildDescription += f' (**{len(currentGame.livingYeagerists)}** Alive)'
            buildDescription += f' vs **{len(currentGame.alliance)}** {currentTheme.alliancePlural}'
            if len(currentGame.deadAlliance) > 0:
                buildDescription += f' (**{len(currentGame.livingAlliance)}** Alive)'
            selectedColor = currentTheme.rumblingStatusColor
        else:
            buildDescription += '????? vs ?????'
            selectedColor = currentTheme.rumblingAltStatusColor
        returnedEmbed = discord.Embed(title = 'Current Game Status', description= buildDescription, color= selectedColor)
        spaceEmoji = f'{currentTheme.emojiSpacer}'
        spacer = spaceEmoji + spaceEmoji
        bigSpacer = spacer + spacer
        progressString = ''
        for i in range(3):
            progressString += bigSpacer + currentTheme.emojiRoundVictoryMarker
            if i != 2:
                progressString += '\n'
            else:
                progressString += currentTheme.emojiVictoryMarker
        returnedEmbed.add_field(name = 'Progress to Annhilation', value=progressString, inline=True)
        brokenWall = f'{currentTheme.emojiRumblingWallExterior}{currentTheme.emojiRumblingWallInterior}{currentTheme.emojiRumblingWallExterior}'
        wallStatusString = ''
        for i in range(3):
            wallStatusString += spacer + brokenWall
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
        if altCase == None:
            allianceVal = ''
            for allianceMember in currentGame.allianceFighters:
                if allianceMember in currentGame.deadPlayers:
                    allianceVal += f'{currentTheme.emojiDead}{allianceMember.user.name}{currentTheme.emojiDead}'
                elif allianceMember in currentGame.livingPlayers:
                    allianceVal += f'{allianceMember.role.emoji}{allianceMember.role.shortName}{allianceMember.role.emoji}'
                allianceVal += '\n'
            returnedEmbed.add_field(name = f'{currentTheme.allianceTeam} Fighters', value=allianceVal, inline= False)
            yeageristVal = ''
            for yeagerist in currentGame.yeageristFighters:
                if yeagerist in currentGame.deadPlayers:
                    yeageristVal += f'{currentTheme.emojiDead}{yeagerist.user.name}{currentTheme.emojiDead}'
                elif yeagerist in currentGame.livingPlayers:
                    yeageristVal += f'{yeagerist.role.emoji}{yeagerist.role.shortName}{yeagerist.role.emoji}'
                yeageristVal += '\n'
            returnedEmbed.add_field(name = f'{currentTheme.yeageristTeam} Fighters', value=yeageristVal, inline= False)
        return returnedEmbed
    
    async def rumblingRolesEmbed(currentGame, currentTheme):
        returnedEmbed = discord.Embed(title = 'Current list of roles in game', color = currentTheme.rolesEmbedColor)
        
        altYeagerList = currentGame.yeagerists.copy()
        altYeagerList.reverse()
        Eren = altYeagerList[0]
        Zeke = altYeagerList[1]

        if len(currentGame.yeageristFighters) > 0:
            teamYeageristFighters = await embedBuilder.getTeamList(currentGame.yeageristFighters, currentGame, currentTheme)
            returnedEmbed.add_field(name = f'{Eren.role.secondaryEmoji}{currentTheme.yeageristTeam} Fighters{Zeke.role.secondaryEmoji}', value = teamYeageristFighters, inline = False)
            for fighter in currentGame.yeageristFighters:
                print(fighter.user.name)

        if len(currentGame.yeageristBench) > 0:
            teamYeageristBench = await embedBuilder.getTeamList(currentGame.yeageristBench, currentGame, currentTheme)
            returnedEmbed.add_field(name = f'{Eren.role.secondaryEmoji}{currentTheme.yeageristTeam} Bench{Zeke.role.secondaryEmoji}', value = teamYeageristBench, inline = False)

        if len(currentGame.allianceFighters) > 0:
            teamAllianceFighters = await embedBuilder.getTeamList(currentGame.allianceFighters, currentGame, currentTheme)
            returnedEmbed.add_field(name = f'{currentGame.livingAlliance[0].role.emoji}{currentTheme.allianceTeam} Fighters{currentGame.livingAlliance[0].role.emoji}', value = teamAllianceFighters, inline = False)

        if len(currentGame.allianceBench) > 0:
            teamAllianceBench = await embedBuilder.getTeamList(currentGame.allianceBench, currentGame, currentTheme)
            returnedEmbed.add_field(name = f'{currentGame.livingAlliance[0].role.emoji}{currentTheme.allianceTeam} Bench{currentGame.livingAlliance[0].role.emoji}', value = teamAllianceBench, inline = False)

        if currentGame.deadPlayers != []:
            deadList = ''
            for player in currentGame.deadPlayers:
                if player in currentGame.deadYeagerists:
                    deadList += f'{Eren.role.secondaryEmoji}{player.user.name}{Zeke.role.secondaryEmoji}\n'
                elif player in currentGame.deadAlliance:
                    roleEmoji = currentTheme.emojiWarrior
                    deadList += f'{currentGame.livingAlliance[0].role.emoji}{player.user.name}{currentGame.livingAlliance[0].role.emoji}\n'
            returnedEmbed.add_field(name = f'{currentTheme.emojiDead}Dead Players{currentTheme.emojiDead}', value=deadList, inline=False)
            
        return returnedEmbed
    
    async def getTeamList(team, currentGame, currentTheme):
            teamList = ''
            for member in team:
                if member in currentGame.livingPlayers:
                    teamList += f'{member.role.emoji}{member.role.name}{member.role.emoji}'
                else:
                    teamList += f'{currentTheme.emojiDead}{member.role.name}{currentTheme.emojiDead}'
                if member in currentGame.yeagerists:
                    teamList += f'({member.user.name})'
                teamList += '\n'
            return teamList
    
    async def rolelistEmbed(loadedRoles, currentTheme):
        soldierRoles = []
        warriorRoles = []
        wildcardRoles = []
        for role in loadedRoles:
            if role.team == 'Soldiers':
                soldierRoles.append(role)
            elif role.team == 'Warriors':
                warriorRoles.append(role)
            elif role.team == 'Wildcards':
                wildcardRoles.append(role)
        returnedEmbed = discord.Embed(title = 'Roles Implemented into the Game', color = currentTheme.rolesEmbedColor)
        soldierList = ''
        for role in soldierRoles:
            soldierList += f'{role.emoji}{role.name}{role.emoji}\n'
        warriorList = ''
        for role in warriorRoles:
            warriorList += f'{role.emoji}{role.name}{role.emoji}\n'
        wildcardList = ''
        for role in wildcardRoles:
            wildcardList += f'{role.emoji}{role.name}{role.emoji}\n'
        returnedEmbed.add_field(name = f'{currentTheme.emojiSoldier}{currentTheme.soldierPlural}{currentTheme.emojiSoldier}', value = f'{soldierList}', inline=True)
        returnedEmbed.add_field(name = f'{currentTheme.emojiWarrior}{currentTheme.warriorPlural}{currentTheme.emojiWarrior}', value = f'{warriorList}', inline=True)
        returnedEmbed.add_field(name = f'{currentTheme.emojiWildcard}{currentTheme.wildcardPlural}{currentTheme.emojiWildcard}', value = f'{wildcardList}', inline=True)
        return returnedEmbed
    
    async def erenFrecklemirEmbed(currentGame, currentTheme):
        Frecklemir = await searchFunctions.roleIDToRoleFromLoadedRoles(currentGame.loadedRoles, 'Frecklemir')
        desc = f'{Frecklemir.name} has chosen to fight on the side of the '
        if currentGame.frecklemirTeam == 'Soldiers':
            desc += f'**{currentTheme.emojiSoldier}{currentTheme.soldierPlural}{currentTheme.emojiSoldier}**.'
        else:
            desc += f'**{currentTheme.emojiWarrior}{currentTheme.warriorPlural}{currentTheme.emojiWarrior}**.\n\nTheir identity has been revealed as **'
            realFreckles = await searchFunctions.roleIDToPlayer(currentGame, 'Frecklemir')
            desc += f'{realFreckles.user.name}**.'
        returnedEmbed = discord.Embed(title = f'{Frecklemir.name} has picked a Side!', description= desc, color = currentTheme.soldierColor)
        return returnedEmbed
    
    async def ymirEmbed(currentGame, currentTheme):
        desc = currentTheme.ymirMessage
        returnedEmbed = discord.Embed(title = '??????????', description = desc, color = currentTheme.wildcardColor)
        returnedEmbed.set_thumbnail(url = currentTheme.emojiPaths.url)
        return returnedEmbed
    
    async def pathsEmbed(currentGame, currentTheme):
        desc = 'The following is a list of choices for you to make. Message can be used as many times as you want per game, whereas ONLY A SINGLE ONE of the other abilities can be used ONCE. Abilities include:\n`Message`: Passes a message to the player you are guiding\n`Revive`: Revives any dead player, if one exists, the next time there is an expo is complete.\n`Bless`: Blesses any one player, which grants them the ability to check another player\'s team'
        returnedEmbed = discord.Embed(title = 'PATHS', description=desc, color = currentTheme.wildcardColor)
        returnedEmbed.set_thumbnail(url = currentTheme.emojiPaths.url)
        return returnedEmbed
    
    async def ymirMessageEmbed(currentGame, currentTheme, msg):
        Ymir = await searchFunctions.roleIDToRoleFromLoadedRoles(currentGame.loadedRoles, 'Ymir')
        returnedEmbed = discord.Embed(title = f'Message From {Ymir.name}', description=msg, color = currentTheme.wildcardColor)
        returnedEmbed.set_thumbnail(url = currentTheme.emojiPaths.url)
        return returnedEmbed

    async def blessingEmbed(currentGame, currentTheme, checkedPlayer):
        if checkedPlayer in currentGame.soldiers or (checkedPlayer.role.id == 'Frecklemir' and currentGame.frecklemirTeam == 'Soldiers'):
            color = currentTheme.soldierColor
            team = currentTheme.soldierPlural
            thumbnail = currentTheme.soldierThumbnail
        elif checkedPlayer in currentGame.warriors or (checkedPlayer.role.id == 'Frecklemir' and currentGame.frecklemirTeam == 'Warriors'):
            color = currentTheme.warriorColor
            team = currentTheme.warriorPlural
            thumbnail = currentTheme.warriorThumbnail
        elif checkedPlayer in currentGame.wildcards:
            color = currentTheme.wildcardColor
            team = currentTheme.wildcardPlural
            thumbnail = currentTheme.wildcardThumbnail
        desc = f'{checkedPlayer.user.name} is fighting for the **{team}**.'
        returnedEmbed = discord.Embed(title = f'{checkedPlayer.user.name}\'s Allegiance...', description = desc, color = color)
        returnedEmbed.set_thumbnail(url = thumbnail)
        return returnedEmbed

