import discord
from discord.ext import commands
from themeData.defaultGameTheme import *

class embedBuilder:

    async def buildLobby(currentLobby, currentTheme, prefix):
        returnedEmbed = discord.Embed(title = f'{currentTheme.gameName} Lobby', description =f'The lobby has: **{len(currentLobby.users)}** players within it.\n\nUse `{prefix}help rules` for information on how to change the rules.', color = discord.Color.blue())
        playerList = ''
        for player in currentLobby.users:
            playerList += f'**{player.mention}**\n'
        returnedEmbed.add_field(name = 'Players', value = playerList, inline = False)
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
                wallStatusString += f'{spacer}{currentTheme.brokenExterior}{currentTheme.brokenInterior}{currentTheme.brokenExterior}'
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
            elif currentRound == currentGame.currentRound:
                statusMarker = f'{currentTheme.emojiCurrentMarker}'
            elif currentRound in currentGame.passedRounds:
                statusMarker = f'{currentTheme.emojiWinMarker}'
            expeditionString += f'{currentTheme.expeditionName} {currentRound}: **{expoCounts[i]}** {currentTheme.expoMembersName} {statusMarker}'
            if i != 4:
                expeditionString += '\n'
        returnedEmbed.add_field(name = currentTheme.statusExpeditions, value = expeditionString, inline = False)
        return returnedEmbed
