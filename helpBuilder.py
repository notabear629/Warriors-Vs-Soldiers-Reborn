import discord
from discord.ext import commands
from discord import ui
from discord.ui import *

from gameObjects.Theme import Theme
from gameObjects.Role import Role

from gameFunctions.searchFunctions import searchFunctions

class helpBuilder:
    async def mainHelpEmbed(currentTheme):
        helpDesc = f'Welcome to {currentTheme.gameName}! This is a Game Based on Warriors Vs. Soldiers by Entropi, which itself is based on a board game called The Resistance: Avalon. This game has the ability to be re-skinned, so the game name and theme may or may not be entirely different, but at its core it is a Warriors Vs. Soldiers successor! This game was NOT made by Entropi and is not directly affiliated with Entropi, but we give her tremendous credit for the creation of the original and thanks for all the joy it has brought us! This version of the game was made by notabear629, but the source code is open and available for modifications, so if you aren\'t seeing this on a server ran by me, it may have been modified by somebody else! I greatly encourage this, and would like to ask you to write your own name in the list here in order to track the incremental modifications made all the way from Entropi\'s core idea to you!\n\nFor help on the game, please select a menu to navigate to from the options listed below.'
        returnedEmbed = discord.Embed(title = f'About {currentTheme.gameName}', description= helpDesc, color = currentTheme.helpEmbedColor)
        returnedEmbed.add_field(name = '📝`User Info`', value = 'This game does not use DMs at all! The game automatically gives you a personal channel and role on the server it is hosted on. For more information on this, and commands associated with this, choose this option.', inline=True)
        returnedEmbed.add_field(name = '🎮`Starting a Game`', value = 'Commands used for starting a game', inline= True)
        returnedEmbed.add_field(name = '⚙️`Game Options and Rules`', value = 'Information on the various Game Options and Rules', inline= True)
        returnedEmbed.add_field(name = '🕹️`How to Play`', value = 'Basic information on the game and how to play it', inline=True)
        returnedEmbed.add_field(name = '👥`Role Information`', value = 'A menu that allows you to bring up a help screen for every individual role', inline=True)
        returnedEmbed.add_field(name = '❓`Help Commands`', value = 'Commands used for getting help/info about the game', inline=True)
        returnedEmbed.add_field(name = '📊`Statistics and Awards`', value = 'A collection of commands and information about stats and awards that can be earned in-game', inline=True)
        return returnedEmbed
    
    async def userInfoEmbed(currentTheme, prefix):
        returnedEmbed = discord.Embed(title = 'User Info and Registration', description= 'As mentioned previously, DMs are NOT used by this bot! Instead, everything takes place on the host server it is configured to. As soon as you host or join a game for the first time, you will be registered into the game. Registered players get their own personal channels within the server, and their own personal roles. When you play the game, messages such as those asking you to make a decision on voting on expeditions will take place in your personal channel. This is because this game has some functionalities that are not supported in DMs. In addition, it gives you a little home base to interact with the game with. There are some commands you can execute related to this, they are listed below.', color = currentTheme.helpEmbedColor)
        returnedEmbed.add_field(name = f'`{prefix}color`', value = f'This command allows you to change your color to any hex code that you like. a hex code is a 6 digit color code that specifies a specific RGB value color. You can get values for hex codes online to get the exact color you like. This command can be used like this: `{prefix}color FF0000`. This example will give you a pure red color.', inline=True)
        returnedEmbed.add_field(name = f'`{prefix}colour`', value = 'This command is exactly identical to the color command. It just lets you use the British spelling instead of the American if you are CRINGE!', inline= True)
        returnedEmbed.add_field(name = f'`{prefix}renamechannel`', value = f'When you first get your channel, it is by default named "#channel-yourusername". This command allows you to customize your channel name. It is used like so: `{prefix}renamechannel The Dungeon`', inline=True)
        returnedEmbed.add_field(name = f'`{prefix}renamerole`', value = f'Much like with the personal channels, your role also has a default name. The default name is "role-yourusername". If you wish to change it, you can change it like so: `{prefix}renamerole Wvs Legend`', inline=True)
        returnedEmbed.add_field(name = f'`{prefix}fixme`', value=f'This command can be called in case you lose your role or channel or it\'s broken in some way shape or form. Some bug checking will be done and the bot will automatically try to fix your issues. Usage: `{prefix}fixme`', inline=True)
        return returnedEmbed
    
    async def lobbyInfoEmbed(currentTheme, prefix):
        returnedEmbed = discord.Embed(title = 'Creating a Lobby', description = 'This section teaches you the commands used to successfully open a lobby', color = currentTheme.helpEmbedColor)
        returnedEmbed.add_field(name = f'`{prefix}host`', value = 'Simply call this command to host a game! It opens a lobby with you as the host.', inline=True)
        returnedEmbed.add_field(name = f'`{prefix}join`', value = 'If there is already a lobby, and you are not in the lobby, you may use this command to join it.', inline= True)
        returnedEmbed.add_field(name = f'`{prefix}leave`', value = 'If you are already in a lobby and decide you no longer want to be in it, you may use this command to leave the lobby.', inline=True)
        returnedEmbed.add_field(name = f'`{prefix}kick`', value = f'If you are the host of a lobby, you can use this command to remove a particular player from the lobby. Usage: `{prefix}kick @player`', inline=True)
        returnedEmbed.add_field(name = f'`{prefix}kickall`', value= f'If you are the host of the lobby, you may simply call this command to remove all players except for you. Kicking all other players as the name implies.', inline=True)
        returnedEmbed.add_field(name = f'`{prefix}lobby`', value = 'Calling this command will display the current status of the lobby, including its rules and players within it.', inline=True)
        returnedEmbed.add_field(name=f'`{prefix}options`', value = 'If you are the host of a lobby, you can call this command to bring up the menu to change its options and rules. The rules from the immediately previously played game are saved if the bot stood online, so if you wish to play with the same rules multiple games in a row, you will only have to configure this once.', inline=True)
        returnedEmbed.add_field(name = f'`{prefix}rules`', value= 'Does the same thing as options, what you use is personal preference.', inline=True)
        returnedEmbed.add_field(name = f'`{prefix}settings`', value= 'Does the same thing as options, what you use is personal preference.', inline=True)
        returnedEmbed.add_field(name = f'`{prefix}reset`', value= 'This command can be used to close a lobby. If a game is ongoing, the host can use this command to cancel it. If the gag role is enabled on a player after a game during a bug, you may call this command to fix it.', inline=True)
        returnedEmbed.add_field(name = f'`{prefix}start`', value = 'This command is used by the host to start the game once the players have joined and the rules and options have been set.', inline=True)
        return returnedEmbed
    
    async def optionsAndRulesEmbed(currentTheme):
        returnedEmbed = discord.Embed(title = 'Game Options and Rules', description='This section is a collection of information regarding the various options and rules configurable to the game. Select the option you wish to know more about.', color = currentTheme.helpEmbedColor)
        returnedEmbed.add_field(name = '🎭`Game Themes`', value = 'This section teaches you more about Game Themes, the ability to re-skin the game!', inline= True)
        returnedEmbed.add_field(name = '👨‍✈️`Team Captains`', value = 'This section teaches you more about the Team Captains, and the rule options you can select.', inline=True)
        returnedEmbed.add_field(name = '🥷`Kidnap Rules`', value = 'This section teaches you more about the various rules regarding the kidnap phase of the game!', inline=True)
        returnedEmbed.add_field(name = f'{currentTheme.emojiRumbling}`{currentTheme.rumblingName}`', value = 'This section teaches you more about the optional rule to play with new ways to win and find new endings! In the default theme, based off "The Rumbling" in Attack on Titan\'s final season.', inline=True)
        returnedEmbed.add_field(name = f'{currentTheme.emojiWildcard}`{currentTheme.wildcardPlural}`', value = f'This section explains everything to know about the 3rd team the {currentTheme.wildcardPlural}!', inline=True)
        returnedEmbed.add_field(name = f'{currentTheme.emojiRanked}`Ranked Status`', value = 'This section explains what setting the game to Ranked or Casual does', inline=True)
        returnedEmbed.add_field(name = f'👥`Role Options`', value = 'This section explains how to properly configure the Role Options based on what you want', inline=True)
        returnedEmbed.add_field(name = f'💾`Saved Rulesets`', value= 'This section explains how to quickly save and load particular rulesets', inline=True)
        return returnedEmbed
    
    async def gameThemesEmbed(currentTheme):
        returnedEmbed = discord.Embed(title = 'Game Themes', description = 'This game has a feature called themes! Themes allow you to re-skin the game without changing any of its functionality. For example, the default for this game is an Attack on Titan based skin entitled Warriors vs Soldiers. This does not have to be the case! Users are allowed, and enocuraged, to create their own themes with very powerful re-skin abilities. For example, it is possible to create a Danganronpa-themed game entitled "Hopes vs Despairs". The Soldiers/Warriors name is configurable, the roles could all be re-named and re-emoji\'d to Danganronpa characters, even the expedition name could be re-named to "Class Trials". Essentially everything is customizeable in this game, and the options are limitless! Selecting your theme does not change the gameplay at all, but does change how it looks and the aesthetics of the game.', color = currentTheme.helpEmbedColor)
        return returnedEmbed
    
    async def teamCaptainsEmbed(currentTheme, loadedRoles):
        Eren = await searchFunctions.roleIDToRoleFromLoadedRoles(loadedRoles, 'Eren')
        Zeke = await searchFunctions.roleIDToRoleFromLoadedRoles(loadedRoles, 'Zeke')
        Mike = await searchFunctions.roleIDToRoleFromLoadedRoles(loadedRoles, 'Mike')
        Historia = await searchFunctions.roleIDToRoleFromLoadedRoles(loadedRoles, 'Historia')
        Floch = await searchFunctions.roleIDToRoleFromLoadedRoles(loadedRoles, 'Floch')
        Keith = await searchFunctions.roleIDToRoleFromLoadedRoles(loadedRoles, 'Keith')
        returnedEmbed = discord.Embed(title = 'Team Captains', description = 'An explanation of all of the various rules available for Team Captains', color = currentTheme.helpEmbedColor)
        returnedEmbed.add_field(name = f'✅`Coordinate and Warchief Enabled`', value = f'This option means that {Eren.shortName} and {Zeke.shortName} will be present in every single game, no matter what.', inline=True)
        returnedEmbed.add_field(name = f'{Eren.emoji}`Coordinate Only`', value = f'This option means that {Zeke.shortName} will be disabled and will not appear in the game. {Historia.shortName} and {Keith.shortName} are also banned.', inline=True)
        returnedEmbed.add_field(name = f'{Zeke.emoji}`Warchief Only`', value = f'This option means that {Eren.shortName} will be disabled and will not appear in the game. There will be no kidnapping phase, and reaching the basement is an instant win for the soldiers. The soldier roles that are present in the game will be hidden, and the Warriors will be DM\'d the soldier roles present so they can choose to pretend to be players that another player isn\'t already. In this gamemode, {Floch.shortName}, {Historia.shortName}, {Keith.shortName} and {Mike.shortName} will also be banned.', inline=True)
        returnedEmbed.add_field(name = f'❌`Coordinate and Warchief Disabled`', value = 'This option means that consequences for both of the captains being disabled will apply, and neither will appear in the game.', inline=True)
        return returnedEmbed
    
    async def kidnapRulesEmbed(currentTheme):
        returnedEmbed = discord.Embed(title = 'Kidnap Rules', description = f'Typically at the end of the game, the {currentTheme.warriorPlural} have a final chance to win by identifying the Coordinate. That is still implemented into this game, however there are two options for rules!', color = currentTheme.helpEmbedColor)
        returnedEmbed.add_field(name = '🌐`Standard Rules`', value = f'This is the classic Warriors vs Soldiers ruleset. The {currentTheme.warriorPlural} get ONE chance as a team to identify the Coordinate. ONE person will make the decision for the whole team.', inline=True)
        returnedEmbed.add_field(name = '♾️`Multikidnap`', value = f'This is a ruleset newly implemented in this game! Instead of one {currentTheme.warriorSingle} making the decision for the whole team, EACH {currentTheme.warriorSingle} will get to choose who they believe to be the Coordinate. The {currentTheme.warriorPlural} will no longer win or lose as a team. To put it simply, you will win if you guessed who to kidnap correctly, and you will lose if you guessed who to kidnap incorrectly. Very simple. It does not matter what your teammates choose. For the {currentTheme.soldierPlural}, it is a bit more complicated. They will lose IF and ONLY IF there is a most popular choice for Coordinate among the {currentTheme.warriorPlural} AND if that choice is the correct answer. They will win otherwise. As an example, if there are 6 {currentTheme.warriorPlural} in a game, 3 chose to kidnap correctly, 2 chose an incorrect candidate, and 1 chose a different incorrect candidate, since the correct candidate was the most popular choice, the {currentTheme.soldierPlural} would lose, and the 3 {currentTheme.warriorPlural} that kidnapped correctly would win. The {currentTheme.warriorPlural} that kidnapped incorrectly would lose, despite their teammates winning.', inline=True)
        return returnedEmbed
    
    async def rumblingInfoEmbed(currentTheme):
        returnedEmbed = discord.Embed(title = f'{currentTheme.rumblingName}', description = 'An option originally based on The Rumbling from Attack on Titan! In order so you can better understand, the information regarding this setting will be written as if the current theme is set to the default Attack on Titan so it\'s easier to relate concepts to the show.', color=currentTheme.helpEmbedColor)
        returnedEmbed.add_field(name = '`What is the Rumbling?`', value = 'The Rumbling in this game is something that can be triggered if the setting is enabled. If the conditions to activate the rumbling are met, the current game context of the Warriors vs Soldiers game will cease entirely and a new game with different gameplay will be formulated based on the struggle between Yeagerists and Alliance Members.', inline=True)
        returnedEmbed.add_field(name = '`How are the Teams Constructed?`', value = 'The teams are constructed based on the theme data an individual person entered. In the original default Attack on Titan theme, I put the characters into teams based on both where they would go according to the series and choices made for game balancing purposes. There are two teams: Yeagerists and Alliance members. In addition, there are two categories, those that will fight in the new game, and those that will NOT fight in the new game, but will win or lose based on if their team wins. The info help screen for a role will tell you their allegiance.', inline=True)
        returnedEmbed.add_field(name = '`How can I trigger the Rumbling?`', value = 'In order to trigger the Rumbling, some conditions must be met. First of all, it will be triggered only after an expedition is complete, once you look at the results of the expedition, if the conditions within that expedition were met, the Rumbling will start. The conditions are as follows:\n1. The Round MUST be round 3 or later. The Rumbling cannot start in the first 2 rounds.\n2. Eren and Zeke must BOTH be in the expedition. They are the two characters that ultimately activate the rumbling.\n3. NO character that has an allegiance to the Alliance can be present in the expedition. It must be full of only Yeagerists.', inline= True)
        returnedEmbed.add_field(name = '`How is the Rumbling fought?`', value = 'The game works like this. All of the Yeagerist fighters and the Alliance fighters will form in to two teams. The Yeagerists will be the ones playing the game, in a fashion very similar to kidnapping. The Alliance fighters will have a specific order that is scrambled and randomized, the Yeagerist fighters will be semi-randomized except Eren will always be last and Zeke will be second to last. The game begins with the First Yeagerist being told the Role of the First Alliance Member, but NOT their identity. The first Yeagerist must select who they believe has this role, if they get it right, they kill the Alliance Member and the next Alliance Member steps up to fight that particular Yeagerist. If they get it wrong, the Yeagerist themselves is killed and that Alliance Member moves forward to fight the next Yeagerist. The game continues until one side is completely wiped out.', inline= True)
        returnedEmbed.add_field(name = '`How do I get different Endings?`', value= 'The Rumbling has multiple possible different endings. First, there is a default victory for both the Yeagerists and the Alliance. Next, there is something called "Domination Victories". This happens when a particular yeagerist kills every single alliance member by themselves, without another yeagerist getting a single kill. Each fighting yeagerist role has their own domination victory. In addition, if the yeagerists cannot identify a single alliance member correctly and every alliance member makes it through, the ALLIANCE has their own domination victory.', inline= True)
        return returnedEmbed
    
    async def wildcardEmbed(currentTheme, loadedRoles):
        returnedEmbed = discord.Embed(title = currentTheme.wildcardPlural, description= f'Enabling this special team introduces a 3rd faction to the game, one not necessarily that is inline with the {currentTheme.soldierPlural} or the {currentTheme.warriorPlural}, but instead has their own unique objectives. This gamemode requires 7. This tends to be the most chaotic setting in the game.', color = currentTheme.wildcardColor)
        returnedEmbed.set_thumbnail(url = currentTheme.wildcardThumbnail)
        return returnedEmbed
    
    async def rankedEmbed(currentTheme):
        returnedEmbed = discord.Embed(title = 'Ranked Status', description= 'This setting determines if certain stats are tracked throughout the game for ranked leaderboard purposes or if the results of the game are kept off-record.', color = currentTheme.helpEmbedColor)
        returnedEmbed.add_field(name = f'{currentTheme.emojiRanked}`Ranked`', value = 'Selecting this option means that the stats of the game will be tracked and saved. A game MVP will be rewarded at the end of the match.', inline=True)
        returnedEmbed.add_field(name = f'{currentTheme.emojiCasual}`Casual`', value = 'Selecting this value means that the results of this game will not be tracked. In addition, it will allow for some of the whackier rules to be played.', inline=True)
        return returnedEmbed
    
    async def roleOptionsInfoEmbed(currentTheme):
        returnedEmbed = discord.Embed(title = 'Role Options', description= 'By default, the game will give you a completely random list of roles. Generating specific roles unless there are more players than roles, then which generic roles will be given out, akin to the generic Warrior/Soldier in the original Warriors vs Soldiers game. However, on a per-team basis, you can configure certain roles to be enabled or disabled.', color= currentTheme.helpEmbedColor)
        returnedEmbed.add_field(name = '✅`Role Enabling`', value = 'You can select certain roles to enable in the options menu. By doing this, you will GUARANTEE that a particular role shows up in the pool, and that role WILL appear in your game, unless you enabled more roles than there are players for that particular team. Roles that are not enabled will not be disbarred from being added. If you play with 5 players and you enable a particular role, the soldier roles will always consist of The Coordinate, the role you enabled, and another random role from the list.', inline=True)
        returnedEmbed.add_field(name = '❌`Role Disabling`', value = 'You can also ban certain roles from showing up in the game. Regardless of what happens, if you disable a role, it will not appear in the game.', inline=True)
        returnedEmbed.add_field(name = '🔄`Reset Role Selection`', value = 'This Button will simply clear the settings of that particular team and let you start your selection process over from scratch.', inline=True)
        return returnedEmbed


    async def howToPlayEmbed(currentTheme):
        returnedEmbed = discord.Embed(title = 'How to Play', description = f'The standard version of this game works like this: There are two teams in play. The {currentTheme.soldierPlural}, and the {currentTheme.warriorPlural}. When the game begins, all players will be assigned to certain roles, and be a part of one of these two teams. Members of BOTH teams want to portray themselves as and claim to be {currentTheme.soldierPlural}. This is a game of social deduction. Once the roles are decided, the rounds of the game will begin. Each round, players will take turns proposing a subset of players to be a part of the {currentTheme.expeditionTeam}, with the goal of the {currentTheme.soldierPlural} to include only {currentTheme.soldierPlural}, and for the {currentTheme.warriorPlural} to sneak in. Players will all vote on if they want the proposal to pass. If it passes, the players will go on the {currentTheme.expeditionName}. If everybody passes the {currentTheme.expeditionName}, it will count as a win for the {currentTheme.soldierPlural}! If somebody sabotages it, it will count as a round win for the {currentTheme.warriorPlural}. The game continues until either team has 3 round wins. If the {currentTheme.warriorPlural} get 3 round wins, the game is over and they won. If the {currentTheme.soldierPlural} get to 3 round wins first, the {currentTheme.warriorPlural} will have one last chance to win by identifying who they think the Coordinate is, hence why it is imperative that the {currentTheme.soldierPlural} hide the identity of the Coordinate. For more info and commands, select from the options below.', color = currentTheme.helpEmbedColor)
        returnedEmbed.add_field(name = f'💡`Game Info Commands`', value= 'Learn more about commands you can call at any point in the game for information about a particular ongoing game!', inline=True)
        returnedEmbed.add_field(name = f'📜`{currentTheme.expeditionName} Proposal`', value= 'Learn more about the commands you can use during the proposal phase of the game.', inline= True)
        returnedEmbed.add_field(name = f'☑️`{currentTheme.expeditionName} Voting`', value= 'Learn more about what happens during the voting phase of the game.', inline= True)
        returnedEmbed.add_field(name = f'🏇`{currentTheme.expeditionName} Actions`', value = f'Learn more about what happens when players are actually on {currentTheme.expeditionName}.', inline=True)
        returnedEmbed.add_field(name = f'🪄`Special Actions`', value= f'Learn more about some specific commands and actions only certain roles and teams can do in certain situtations during the game.', inline=True)
        return returnedEmbed
    
    async def gameInfoCommandsEmbed(currentTheme, prefix):
        returnedEmbed = discord.Embed(title = 'Mid-Game Commands', description = f'The following is a list of commands you can call at any point in the game', color=currentTheme.helpEmbedColor)
        returnedEmbed.add_field(name = f'`{prefix}status`', value= 'This command returns an embed containing the current game status and general information about the game.', inline=True)
        returnedEmbed.add_field(name = f'`{prefix}players`', value= f'This command returns a list of the living players in the game and the order for which they will take turns making {currentTheme.expeditionTeam} Proposals.', inline=True)
        returnedEmbed.add_field(name = f'`{prefix}roles`', value= 'This command returns a list of the roles currently active in the game. It also contains a list of killed players, if any exist.', inline=True)
        returnedEmbed.add_field(name = f'`{prefix}advantage`', value = 'This command will try to use the past success of the roles to predict who is more likely to win in a particular game.')
        return returnedEmbed
    
    async def helpEmbed(currentTheme, prefix):
        returnedEmbed = discord.Embed(title = 'Basic Help and Info Commands', description = 'The following is a list of commands that you can call for information regarding the game', color = currentTheme.helpEmbedColor)
        returnedEmbed.add_field(name = f'`{prefix}help`', value = f'You had to use this command to get where you are now! This command opens the help menu', inline=True)
        returnedEmbed.add_field(name = f'`{prefix}rolelist`', value = 'This command returns a list of all roles implemented into the game', inline= True)
        returnedEmbed.add_field(name= f'`{prefix}info`', value = f'This command skips straight to returning information about a particular role. Usage: `{prefix}info eren` will return help for Eren.', inline=True)
        return returnedEmbed
    
    async def expoProposalInfoEmbed(currentTheme, prefix):
        returnedEmbed = discord.Embed(title = f'{currentTheme.expeditionName} Proposal Information', description= f'This section is regarding the stage of the game where players take turns picking proposals for a {currentTheme.expeditionTeam}. An important note is that in this game, compared to previous games, there is no such thing as "2 to fail" rounds. In addition, in games of 7+ players, the size of the set of players you will choose is dynamic. Meaning, it will not be the same each game. How it works is that every time, round 1 has 2 players, round 2 will have 3 players. The following rounds will depend on the success of the previous rounds. If round 2 fails, then round 3 will have 3 players again. If round 2 instead succeeds, then round 3 will now have 4 players. This is another part of the strategy for choosing if you should pass rounds or not. This pattern continues, and a round can have up to 5 players required. If the number of players ever exceeds the number of {currentTheme.soldierPlural} that are alive, then the number of players required will become the number of living {currentTheme.soldierPlural}.', color=currentTheme.helpEmbedColor)
        returnedEmbed.add_field(name = f'`{prefix}pick`', value = f'This command is used by the {currentTheme.commanderName} in order to choose their {currentTheme.expeditionTeamMembers}. Usage: `{prefix}pick @player`', inline=True)
        returnedEmbed.add_field(name = f'`{prefix}pass`', value = f'This command is used by a {currentTheme.commanderName} who doesn\'t want to actually do their job. When this command is used, the responsibility is passed to the next guy and you don\'t have to pick players.', inline=True)
        returnedEmbed.add_field(name = f'`{prefix}clear`', value = f'This command is used by a {currentTheme.commanderName} who made a mistake and wants to re-do picking their {currentTheme.expeditionTeamMembers}. When this command is called, their {currentTheme.expeditionTeam} once again becomes empty and they can pick their team from scratch.', inline=True)
        return returnedEmbed
    
    async def expoVotingInfoEmbed(currentTheme, loadedRoles):
        returnedEmbed = discord.Embed(title = f'{currentTheme.expeditionName} Voting Information', description= f'The following contains possible vote choices and actions taken during this stage. It is important to note, that as a consequence of players being able to be killed in this game, it is possible for the number of living {currentTheme.soldierPlural} to be equal to {currentTheme.warriorPlural}. If this happens, you are warned that voting gridlock has occured, and any situation where the vote is tied will have a tiebreaker decided by the vote of the {currentTheme.commanderName} who proposed the {currentTheme.expeditionName}.', color = currentTheme.helpEmbedColor)
        
        returnedEmbed.add_field(name = f'{currentTheme.emojiAcceptExpedition}`Accept`', value= f'Choosing this option allows you to vote to approve the {currentTheme.expeditionName} Proposal. It will pass if the number of approvals is greater than the number of rejections.', inline=True)
        returnedEmbed.add_field(name = f'{currentTheme.emojiRejectExpedition}`Reject`', value = f'Choosing this option allows you to vote to reject the {currentTheme.expeditionName} Proposal.', inline= True)
        returnedEmbed.add_field(name = f'{currentTheme.emojiAbstainExpedition}`Abstain`', value = f'Choosing this option is the same as refraining from voting. The votes among the players that actually voted will be tallied, yours will not count as a rejection, it will be discarded entirely as if you weren\'t playing the game. This is the default choice made for players who do not vote in time.', inline=True)
        Jean = await searchFunctions.roleIDToRoleFromLoadedRoles(loadedRoles, 'Jean')
        returnedEmbed.add_field(name = f'{Jean.emoji}`Secure`', value = f'This option is exclusive to {Jean.emoji}{Jean.shortName}{Jean.emoji}. This is a special vote that can be used once per game, when used, the {currentTheme.expeditionName} is guaranteed to be approved, no matter what.', inline= True)
        Zachary = await searchFunctions.roleIDToRoleFromLoadedRoles(loadedRoles, 'Zachary')
        returnedEmbed.add_field(name = f'{Zachary.emoji}`Veto`', value = f'This option is exclusive to {Zachary.emoji}{Zachary.shortName}{Zachary.emoji}. This is a special vote that can be used once per game, when used, the {currentTheme.expeditionName} is guaranteed to be rejected regardless of other players votes. If the proposal secure happens the same turn as the veto, they both cancel and the votes are counted as usual.', inline=True)
        Samuel = await searchFunctions.roleIDToRoleFromLoadedRoles(loadedRoles, 'Samuel')
        returnedEmbed.add_field(name = f'{Samuel.emoji}`Clownery`', value = f'This is an option exclusive to {Samuel.emoji}{Samuel.shortName}{Samuel.emoji} that ALWAYS causes you to choose the wrong choice. It\'s a tactical decision, because if the proposals don\'t pass when you use this option, you can gain valuable info either way.', inline=True)
        Pieck = await searchFunctions.roleIDToRoleFromLoadedRoles(loadedRoles, 'Pieck')
        returnedEmbed.add_field(name = f'{Pieck.emoji}`Flip`', value = f'This is actually TWO separate options exclusive to {Pieck.emoji}{Pieck.shortName}{Pieck.emoji}. This is a special vote that can be used once per game, when used, every players votes will be FLIPPED! Players that rejected will be marked as accepting and vice versa. The player choosing this option may choose if they would like to accept or reject after the flip, hence making this option actually two choices. {Jean.shortName}\'s ability to Secure overrules this though, a Secure will result in a pass REGARDLESS of a flip.', inline= True)
        Falco = await searchFunctions.roleIDToRoleFromLoadedRoles(loadedRoles, 'Falco')
        returnedEmbed.add_field(name = f'{Falco.emoji}`Intercept`', value = f'This option is exclusive to {Falco.emoji}{Falco.shortName}{Falco.emoji}. This is another special vote that can be used once per game, how it works is this. When this option is chosen, it will result in an accept IF AND ONLY IF the proposal would pass if you accepted. Otherwise, it will make you reject. This is useful for when you would like to be aggressive and accept a proposal, but don\'t want to look suspicious if it wouldn\'t pass. It is important to note that this vote will take place BEFORE the interaction with {Pieck.shortName}\'s Flip option. Meaning the player choosing to Intercept will have their vote calculated and decided, and THEN the Flip happens. If it was the other way around, it would be way overpowered because an Intercept could guarantee a favorable Flip outcome, but that is NOT the case.', inline=True)
        Yelena = await searchFunctions.roleIDToRoleFromLoadedRoles(loadedRoles, 'Yelena')
        returnedEmbed.add_field(name = f'{Yelena.emoji}`Steal Vote`', value = f'This option is exclusive to {Yelena.emoji}{Yelena.shortName}{Yelena.emoji}. It allows you to take the person you choose\'s vote as your own, swapping theirs with the opposite of what they voted with.', inline=True)
        return returnedEmbed
    
    async def expoActionsInfoEmbed(currentTheme, loadedRoles):
        Reiner = await searchFunctions.roleIDToRoleFromLoadedRoles(loadedRoles, 'Reiner')
        Mikasa = await searchFunctions.roleIDToRoleFromLoadedRoles(loadedRoles, 'Mikasa')
        returnedEmbed = discord.Embed(title = f'{currentTheme.expeditionName} Action Information', description= f'A list of choices and commands regarding the action phase of the game. It is important to note that during this phase of the game after the results are viewed, players can ACTUALLY be killed. Whenever a reference is made to player kills, keep in mind that the interactions with {Mikasa.name} and {Reiner.name} may not result in the kill actually taking place due to those role\'s defensive abilities.', color = currentTheme.helpEmbedColor)
        returnedEmbed.add_field(name = f'{currentTheme.emojiPassExpedition}`Pass`', value = f'This option is available to everybody. It simply results in a pass and does not contribute to a round failure.', inline=True)
        returnedEmbed.add_field(name = f'{currentTheme.emojiSabotageExpedition}`Sabotage`', value = f'This option is available only to the {currentTheme.warriorPlural}. Choosing this option leads to you attempting to cause a round failure for the {currentTheme.soldierPlural}.', inline=True)
        Armin = await searchFunctions.roleIDToRoleFromLoadedRoles(loadedRoles, 'Armin')
        returnedEmbed.add_field(name = f'{Armin.emoji}`Nuke`', value = f'This choice is one of pure chaos. This is an option exclusive to {Armin.emoji}{Armin.shortName}{Armin.emoji} and despite this role being a part of the {currentTheme.soldierPlural}, selecting this option will still result in round failure. Therefore, this choice is prohibited if there are already 2 or more round failures, as that would be an insta loss. In addition to causing a round failure, this results in every single player on the {currentTheme.expeditionName} except for {Armin.shortName} dying. Use this option wisely and sparingly, this choice can win or lose you a game singlehandedly.', inline=True)
        Levi = await searchFunctions.roleIDToRoleFromLoadedRoles(loadedRoles, 'Levi')
        returnedEmbed.add_field(name = f'{Levi.emoji}`Attack or Defend`', value= f'Two options exclusive to {Levi.emoji}{Levi.shortName}{Levi.emoji}. The resident badass of the game, player has a choice of ONE of these options throughout the game. Attack will kill any player that chooses to sabotage that round, but will not protect the round from being sabotaged. Defend will not kill the players that choose to sabotage, but it will protect the round and ensure its success.', inline=True)
        Petra = await searchFunctions.roleIDToRoleFromLoadedRoles(loadedRoles, 'Petra')
        returnedEmbed.add_field(name = f'{Petra.emoji}`Watch`', value = f'This choice is excluse to {Petra.emoji}{Petra.shortName}{Petra.emoji}. Petra chooses one other player to keep an eye on. If they were caught trying to sabotage, they will be killed.', inline=True)
        Daz = await searchFunctions.roleIDToRoleFromLoadedRoles(loadedRoles, 'Daz')
        returnedEmbed.add_field(name = f'{Daz.emoji}`Chicken Out`', value = f'This is an option that is exclusive to {Daz.emoji}{Daz.shortName}{Daz.emoji}. This seems like a total meme choice, and to be honest, it kinda is, but it\'s also potentially insanely useful. How it works is that if you rejected the proposal for the {currentTheme.expeditionName} and are in it and forced to go on it anyway, you can choose this option and force it to be cancelled and make the next player start a proposal. Very importantly, and perhaps the best perk of the role, the Coward Out option appears IF AND ONLY IF you actually chose to reject. It DOES NOT CARE if the votes got flipped and forced you to accept, you will still retain the ability to cancel.', inline=True) 
        Hannes = await searchFunctions.roleIDToRoleFromLoadedRoles(loadedRoles, 'Hannes')
        returnedEmbed.add_field(name = f'{Hannes.emoji}`Escape`', value = f'This is an option exclusive to {Hannes.emoji}{Hannes.shortName}{Hannes.emoji}. This lets him escape from an ongoing {currentTheme.expeditionName}, while revealing his identity.')
        Hange = await searchFunctions.roleIDToRoleFromLoadedRoles(loadedRoles, 'Hange')
        returnedEmbed.add_field(name = f'{Hange.emoji}`Wiretap`', value = f'This is an option exclusive to {Hange.emoji}{Hange.shortName}{Hange.emoji} that can be used to plant a wiretap on another player. This wiretap will immediately alert you as to this player\'s votes and ability usages.', inline=True)
        Marco = await searchFunctions.roleIDToRoleFromLoadedRoles(loadedRoles, 'Marco')
        returnedEmbed.add_field(name = f'{Marco.emoji}`{currentTheme.suicideLabel}`', value = f'This is an option exclusive to {Marco.emoji}{Marco.shortName}{Marco.emoji} that allows you to ensure you die after the results of this round.')
        Bertholdt = await searchFunctions.roleIDToRoleFromLoadedRoles(loadedRoles, 'Bertholdt')
        returnedEmbed.add_field(name = f'{Bertholdt.emoji}`Cloak`', value = f'This is an option exclusive to {Bertholdt.emoji}{Bertholdt.shortName}{Bertholdt.emoji} that can be used multiple times per game. This option makes it so the results screen that shows how many players passed or sabotaged a round does not show up. This could be helpful to hide and better coordinate double sabotages, BUT can expose your role and who you are, because if the players see the cloak go off, it logically means {Bertholdt.shortName} logically must have been in that {currentTheme.expeditionName}.', inline=True)
        Willy = await searchFunctions.roleIDToRoleFromLoadedRoles(loadedRoles, 'Willy')
        returnedEmbed.add_field(name = f'{Willy.emoji}`Kamikaze`', value = f'This is a choice exclusive to {Willy.emoji}{Willy.shortName}{Willy.emoji}. It essentially results in him suicide bombing to kill another player of his choice.', inline=True)
        Lara = await searchFunctions.roleIDToRoleFromLoadedRoles(loadedRoles, 'Lara')
        returnedEmbed.add_field(name = f'{Lara.emoji}`Transform`', value = f'This is a choice exclusive to {Lara.emoji}{Lara.shortName}{Lara.emoji}. It causes a sabotage and allows you to transform into a scarier version of your role...')
        Kenny = await searchFunctions.roleIDToRoleFromLoadedRoles(loadedRoles, 'Kenny')
        returnedEmbed.add_field(name = f'{Kenny.emoji}`Kill`', value = f'This is a choice exclusive to {Kenny.emoji}{Kenny.shortName}{Kenny.emoji}. He can kill any player present on the {currentTheme.expeditionName}.', inline=True)
        return returnedEmbed
    
    async def specialActionsInfoEmbed(currentTheme, loadedRoles, prefix):
        returnedEmbed = discord.Embed(title = f'Special Actions Information', description= f'This is a list of commands and actions to be taken that are otherwise special from the typical flow of the game.', color = currentTheme.helpEmbedColor)

        
        returnedEmbed.add_field(name = f'{currentTheme.emojiWarrior}`{prefix}kidnap`', value=f'This is a command exclusive to {currentTheme.warriorPlural} during the kidnap phase. Usage: `{prefix}kidnap @player`', inline=True)
        Eren = await searchFunctions.roleIDToRoleFromLoadedRoles(loadedRoles, 'Eren')
        returnedEmbed.add_field(name = f'{Eren.emoji}`{prefix}attack`', value =f'This is a command exclusive to {currentTheme.yeageristPlural} when {currentTheme.rumblingName} is enabled and active, allowing them to choose who to attack. Usage: `{prefix}attack @player`', inline = True)
        Zeke = await searchFunctions.roleIDToRoleFromLoadedRoles(loadedRoles, 'Zeke')
        returnedEmbed.add_field(name = f'{Zeke.emoji}`{prefix}retreat`', value = f'This is a command exclusive to {Zeke.emoji}{Zeke.shortName}{Zeke.emoji}. When they send this command in their private DM, the game goes directly to the kidnap phase. Used in edge emergency situations when throwing in the towel is preferable to playing through the rounds of the game', inline=True)
        Sasha = await searchFunctions.roleIDToRoleFromLoadedRoles(loadedRoles, 'Sasha')
        returnedEmbed.add_field(name = f'{Sasha.emoji}`{prefix}target`', value = f'A command special to {Sasha.emoji}{Sasha.shortName}{Sasha.emoji}. Is used in their private channel to bring up the menu to choose what player to target. The next time that player goes on an {currentTheme.expeditionName} that {Sasha.shortName} is not on, they will fire off a long ranged attack that kills that player, but not until after the {currentTheme.expeditionName} is already finished. Can only be done once per game, but the target can be switched as many times as you want before the long ranged attack fires.', inline=True)
        Mikasa = await searchFunctions.roleIDToRoleFromLoadedRoles(loadedRoles, 'Mikasa')
        returnedEmbed.add_field(name = f'{Mikasa.emoji}`{prefix}guard`', value= f'This is a command excluse to {Mikasa.emoji}{Mikasa.shortName}{Mikasa.emoji}. This allows them to choose one person inside the {currentTheme.expeditionName} to make them immune from being killed, their choices includes but is not limited to themselves. They may choose to protect themselves OR somebody else. Or nobody.', inline=True)
        Pyxis = await searchFunctions.roleIDToRoleFromLoadedRoles(loadedRoles, 'Pyxis')
        returnedEmbed.add_field(name = f'{Pyxis.emoji}`{prefix}trial`', value = f'This is a one-time command special to {Pyxis.emoji}{Pyxis.shortName}{Pyxis.emoji}. This allows you to choose a player that has previously been on a {currentTheme.expeditionName} and have the players vote on if they should be executed or not. If the vote passes, the player is killed.', inline=True)
        Keith = await searchFunctions.roleIDToRoleFromLoadedRoles(loadedRoles, 'Keith')
        returnedEmbed.add_field(name = f'{Keith.emoji}`{prefix}summon`', value = f'A one-time special ability granted to {Keith.emoji}{Keith.shortName}{Keith.emoji}. This command designates a role you wish to change to. At the end of a passed round, you will change to that role.', inline=True)
        Erwin = await searchFunctions.roleIDToRoleFromLoadedRoles(loadedRoles, 'Erwin')
        Porco = await searchFunctions.roleIDToRoleFromLoadedRoles(loadedRoles, 'Porco')
        returnedEmbed.add_field(name = f'{Erwin.emoji}`{prefix}flare`', value =f'A one-time command special to {Erwin.emoji}{Erwin.shortName}{Erwin.emoji}. When used in their private channel during the proposal stage, it will reveal their identity as {Erwin.shortName}, give them the ability to be the {currentTheme.commanderName} instantly. If the player is currently gagged by {Porco.shortName}, it will instantly remove the gag.', inline=True)
        returnedEmbed.add_field(name = f'{Porco.emoji}`{prefix}gag`', value = f'A one-time special ability granted to {Porco.emoji}{Porco.shortName}{Porco.emoji}. When used in your private channel, it opens the menu for you to choose which player to gag. Which can be any player, including your teammates and yourself. When a player is gagged, for an entire round, they will be given a role called "GAGGED" that prohibits them from speaking in the channel. In addition, it will not allow them to be the {currentTheme.commanderName} and pick {currentTheme.expeditionTeamMembers}, it will skip over them. It also does not send an announcement when you do this, so it is possible that people will not notice what you did and you can get away with making an inconveniently loud player shut up for a round. However, {Erwin.shortName} is immune to this entirely once they fire a flare. Even if you had previously gagged them, they will break out upon the flare firing.', inline=True)
        Gabi = await searchFunctions.roleIDToRoleFromLoadedRoles(loadedRoles, 'Gabi')
        returnedEmbed.add_field(name = f'{Gabi.emoji}`{prefix}fire`', value = f'A one-time special ability granted to {Gabi.emoji}{Gabi.shortName}{Gabi.emoji}. This command designates a person to fire upon. Once the results are read, that player will be shot, and they will be wounded for a round. Wounded players cannot be on the {currentTheme.expeditionName}.', inline=True)
        Annie = await searchFunctions.roleIDToRoleFromLoadedRoles(loadedRoles, 'Annie')
        returnedEmbed.add_field(name = f'{Annie.emoji}`{prefix}scream`', value = f'This is a command able to be used by {Annie.emoji}{Annie.shortName}{Annie.emoji} once per game. It allows you to type a secret message that will be sent to all of the {currentTheme.warriorPlural} in their private channels the next time the results are read. The players in the main game will also see that you sent a scream message, but it will not tell them the content of the message, merely inform them that one was sent.', inline=True)
        Ymir = await searchFunctions.roleIDToRoleFromLoadedRoles(loadedRoles, 'Ymir')
        returnedEmbed.add_field(name = f'{Ymir.emoji}`{prefix}paths`', value = f'Opens up the menu for paths options. Unique to {Ymir.emoji}{Ymir.shortName}{Ymir.emoji}. This command is the center that lets you use the message send, blessing granting, or player revival.', inline=True)
        returnedEmbed.add_field(name = f'{currentTheme.emojiPaths}`{prefix}check @mention`', value = f'If the blessing was bestowed upon you, you can use this command to check to see what team any player is on.', inline=True)
        return returnedEmbed
    
    async def roleInfoHelpEmbed(currentTheme):
        returnedEmbed = discord.Embed(title = f'Role Information', description = f'This is the landing page for role information. To learn more about a role, choose a role from the selections below.', color=currentTheme.helpEmbedColor)
        return returnedEmbed
    
    async def specificRoleInfoEmbed(currentTheme, selectedRole):
        if selectedRole.team == 'Soldiers':
            embedColor = currentTheme.soldierColor
            roleTeam = currentTheme.soldierPlural
        elif selectedRole.team == 'Warriors':
            embedColor = currentTheme.warriorColor
            roleTeam = currentTheme.warriorPlural
        elif selectedRole.team == 'Wildcards':
            embedColor = currentTheme.wildcardColor
            roleTeam = currentTheme.wildcardPlural
        if selectedRole.rumblingTeam.startswith('yeagerist'):
            rumblingTeam = currentTheme.yeageristTeam
        elif selectedRole.rumblingTeam.startswith('alliance'):
            rumblingTeam = currentTheme.allianceTeam
        if selectedRole.rumblingTeam.endswith('Fighter'):
            rumblingFighter = True
        else:
            rumblingFighter = False
        returnedEmbed = discord.Embed(title = f'{selectedRole.name}', description = f'Role Information for {selectedRole.shortName}', color=embedColor)
        returnedEmbed.add_field(name = 'Team', value = f'`{roleTeam}`', inline=True)
        returnedEmbed.add_field(name = f'Is {currentTheme.titanSingle}?', value = f'`{selectedRole.isTitan}`', inline=True)
        returnedEmbed.add_field(name = f'Game Role', value = f'{selectedRole.gameRole}', inline=True)
        returnedEmbed.add_field(name = 'Role ID', value = f'`{selectedRole.id}`', inline= True)
        returnedEmbed.add_field(name = f'{currentTheme.rumblingName} Team', value=f'`{rumblingTeam}`', inline=True)
        returnedEmbed.add_field(name = f'Fights during {currentTheme.rumblingName}?', value = f'`{rumblingFighter}`', inline=True)
        returnedEmbed.add_field(name = f'Description', value = f'{selectedRole.helpInfo}', inline=False)
        if type(selectedRole.emoji) == str:
            thumbnailURL = selectedRole.imageURL
        else:
            thumbnailURL = selectedRole.emoji.url
        returnedEmbed.set_thumbnail(url = thumbnailURL)

        return returnedEmbed
    
    async def savedRulesetEmbed(currentTheme):
        returnedEmbed = discord.Embed(title = 'Saved Rulesets', description = 'Information on how to save your rulesets', color=currentTheme.helpEmbedColor)
        returnedEmbed.add_field(name = '🔃`Load Rulesets`', value= 'In order to load your rulesets, you simply must open the selection menu and click the named ruleset you wish to load. If you load an empty slot that you have not yet saved, nothing will change.', inline=True)
        returnedEmbed.add_field(name = '💾`Save Rulesets`', value = 'Saving your rulesets is also quite simple. First, ensure that the current lobby has the rules you actually intend on saving. Next, choose the slot from the save selection menu you would like to save your ruleset in. You may either choose to save it in an empty slot, or to overwrite and replace an old slot with a new ruleset. After you select a slot, a window will appear asking you to name the ruleset. Once you choose a name, that slot will be saved with the currently loaded rules in the lobby by the name you gave it.', inline=True)
        
        return returnedEmbed
    
    async def statsEmbed(currentTheme):
        returnedEmbed = discord.Embed(title = 'Stats and Award Help', description = 'A Landing page for information on Stats and Awards', color = currentTheme.helpEmbedColor)
        returnedEmbed.add_field(name = '📚`Stat and Award Information`', value='In order for information on what the stats and awards are and how they are derived from, choose this option', inline=True)
        returnedEmbed.add_field(name = '🧮`Stat and Award Commands`', value = 'In order to see what commands you can use associated with stats and awards, click this button', inline=True)
        return returnedEmbed
    
    async def statsInfoEmbed(currentTheme):
        returnedEmbed = discord.Embed(title = 'Stats and Awards Information', description = 'Information on various stats and awards throughout the game', color = currentTheme.helpEmbedColor)
        returnedEmbed.add_field(name = f'💎`Badges`', value= 'Badges are simply awards that you can earn as you progress through the game. At the end of a ranked game, if you earn a badge you will be notified and that badge will be added to your collection.', inline=True)
        returnedEmbed.add_field(name = f'🏅`Titles`', value = 'A title is something special. It means that you are the #1 player on a particular leaderboard that factors into the overall Legacy Points. Only 1 person can have each title!', inline=True)
        returnedEmbed.add_field(name = f'🏆`MVPS`', value = 'At the end of each ranked game, an MVP is selected from the winners. This is based on some tracked metrics to try to estimate player performance, only 1 MVP is chosen each game.', inline=True)
        returnedEmbed.add_field(name = f'🐐`Legacy Points`', value = 'Legacy Points are a metric that is used to track the leaderboard for who is the #1 player. They are calculated by a sum of up to 1000 points from 5 categories including WORP, Soldier WORP, Warrior WORP, MVP count, and Badge Points', inline=True)
        returnedEmbed.add_field(name = f'👑`WORP`', value = 'WORP is a special kind of stat. It means Wins Over Replacement Player, and in the end is not that complicated. It is calculated by performing a WORP calculation for each individual role and then summing the total. WORP is calculated using this simple manner. It takes your role win percentage minus the global role win percentage. This gets a metric of what % you win above average, and it can be positive and negative. It is then multiplied by your games played. That\'s it. As an example, if you played 10 games as Eren with an 80% winrate, and the global winrate is 50%, here is how we calculate that WORP. Your .8 winrate - .5 global winrate is equal to 0.3. Then, 0.3 * 10 = 3. Your WORP is 3. And this makes sense because if you won 50% you would have won 5 games, but thanks to your higher level you won 8, and 8 is 3 wins above 5. That\'s all it is.', inline=True)
        returnedEmbed.add_field(name = f'💠`True Winning %`', value = 'True Winning Percentage, or TW%, is another form of advanced stat. The main problem with win percentage is that the average win percentage is NOT always 50. And it does not take what roles you got into account, if you got harder roles, your win % may be lower! True Win Percentage normalizes all of this and ensures that 50% would mean a value of being perfectly average no matter what roles you got.', inline=True)
        returnedEmbed.add_field(name = '🎁`Assists`', value = 'In some of the stats you may see something called assists. This simply means that you were not on the round that passed/failed but you picked it, or accepted it. It can be thought of as helping your teammate achieve it. Commanding and Accepting is still just 1 assist. It doesn\'t matter how many ways you cover it.')
        returnedEmbed.add_field(name = '👷‍♂️`Responsible For`', value = 'This means a round you were either directly on or assisted on. It can be thought of as the amount of passed/failed rounds you contributed to.', inline=True)
        return returnedEmbed
    
    async def statsCommandsEmbed(currentTheme, prefix):
        returnedEmbed = discord.Embed(title = 'Stats and Awards Commands', description= 'Information on commands you can call related to Stats and Awards', color=currentTheme.helpEmbedColor)
        returnedEmbed.add_field(name = f'`{prefix}profile`', value = f'This command will give you your profile that displays your stats among some other things. This command has multiple usages, `{prefix}profile` by itself takes you directly to your profile. `{prefix}profile @mention` takes you to the profile of that person. `{prefix}profile text` would try to find a user by your text keyword. If it could find one, it returns their profile. Finally, `{prefix}profile global` returns global statistics. If a player can not be found by one of your searches, global will be defaulted to.', inline=True)
        returnedEmbed.add_field(name = f'`{prefix}stats`', value = f'This command is exactly the same as profile.', inline=True)
        returnedEmbed.add_field(name = f'`{prefix}badges`', value = f'This is a command that displays what badges you currently have. You can call it by itself, or with any of the arguments specified in profile except for global.', inline=True)
        returnedEmbed.add_field(name = f'`{prefix}leaderboard`', value = f'This command will display the leaderboard to you. You may add an additional database argument to it such as `{prefix}leaderboard kills` to get a special ranking by kills, as an example', inline=True)
        returnedEmbed.add_field(name = f'`{prefix}lb`', value = 'This command is exactly the same as leaderboard', inline=True)
        return returnedEmbed
    
    async def mainNavigatorView(navigatorContext, navigator, currentTheme, prefix, loadedRoles):
        returnedView = View()

        async def navigate(interaction, clickedButton, selectedRole = None):
            if navigator == interaction.user:
                if clickedButton == 'Go Back':
                    mainReturns = ['User Info', 'Starting a Game', 'Game Options and Rules', 'How to Play', 'Role Info', 'Help', 'Stats']
                    optionsAndRulesReturns = ['Game Themes', 'Kidnap Rules', 'Rumbling', 'Role Options', 'Saved Rulesets', 'Ranked', 'Wildcards', 'Team Captains']
                    howToPlayReturns = ['Game Info', 'Proposal Stage', 'Voting Stage', 'Action Stage', 'Special']
                    statsReturns = ['StatsInfo', 'StatsCommands']
                    if navigatorContext in mainReturns:
                        newNavigatorContext = 'Main'
                        refreshedEmbed = await helpBuilder.mainHelpEmbed(currentTheme)
                    
                    elif navigatorContext in optionsAndRulesReturns:
                        newNavigatorContext = 'Game Options and Rules'
                        refreshedEmbed = await helpBuilder.optionsAndRulesEmbed(currentTheme)

                    elif navigatorContext in howToPlayReturns:
                        newNavigatorContext = 'How to Play'
                        refreshedEmbed = await helpBuilder.howToPlayEmbed(currentTheme)

                    elif navigatorContext in statsReturns:
                        newNavigatorContext = 'Stats'
                        refreshedEmbed = await helpBuilder.statsEmbed(currentTheme)

                elif clickedButton == 'User Info':
                    newNavigatorContext = 'User Info'
                    refreshedEmbed = await helpBuilder.userInfoEmbed(currentTheme, prefix)

                elif clickedButton == 'Starting a Game':
                    newNavigatorContext = 'Starting a Game'
                    refreshedEmbed = await helpBuilder.lobbyInfoEmbed(currentTheme, prefix)

                elif clickedButton == 'Game Options and Rules':
                    newNavigatorContext = 'Game Options and Rules'
                    refreshedEmbed = await helpBuilder.optionsAndRulesEmbed(currentTheme)

                elif clickedButton == 'Role Info':
                    newNavigatorContext = 'Role Info'
                    refreshedEmbed = await helpBuilder.roleInfoHelpEmbed(currentTheme)

                elif clickedButton == 'Saved Rulesets':
                    newNavigatorContext = 'Saved Rulesets'
                    refreshedEmbed = await helpBuilder.savedRulesetEmbed(currentTheme)

                elif clickedButton == 'Selected Role Info':
                    newNavigatorContext = 'Role Info'
                    refreshedEmbed = await helpBuilder.specificRoleInfoEmbed(currentTheme, selectedRole)

                elif clickedButton == 'Game Themes':
                    newNavigatorContext = 'Game Themes'
                    refreshedEmbed = await helpBuilder.gameThemesEmbed(currentTheme)

                elif clickedButton == 'Team Captains':
                    newNavigatorContext = 'Team Captains'
                    refreshedEmbed = await helpBuilder.teamCaptainsEmbed(currentTheme, loadedRoles)

                elif clickedButton == 'Kidnap Rules':
                    newNavigatorContext = 'Kidnap Rules'
                    refreshedEmbed = await helpBuilder.kidnapRulesEmbed(currentTheme)

                elif clickedButton == 'Rumbling':
                    newNavigatorContext = 'Rumbling'
                    refreshedEmbed = await helpBuilder.rumblingInfoEmbed(currentTheme)

                elif clickedButton == 'Wildcards':
                    newNavigatorContext = 'Wildcards'
                    refreshedEmbed = await helpBuilder.wildcardEmbed(currentTheme, loadedRoles)

                elif clickedButton == 'Ranked':
                    newNavigatorContext = 'Ranked'
                    refreshedEmbed = await helpBuilder.rankedEmbed(currentTheme)

                elif clickedButton == 'Role Options':
                    newNavigatorContext = 'Role Options'
                    refreshedEmbed = await helpBuilder.roleOptionsInfoEmbed(currentTheme)

                elif clickedButton == 'Help':
                    newNavigatorContext = 'Help'
                    refreshedEmbed = await helpBuilder.helpEmbed(currentTheme, prefix)

                elif clickedButton == 'Stats':
                    newNavigatorContext = 'Stats'
                    refreshedEmbed = await helpBuilder.statsEmbed(currentTheme)

                elif clickedButton == 'StatsInfo':
                    newNavigatorContext = 'StatsInfo'
                    refreshedEmbed = await helpBuilder.statsInfoEmbed(currentTheme)
                
                elif clickedButton == 'StatsCommands':
                    newNavigatorContext = 'StatsCommands'
                    refreshedEmbed = await helpBuilder.statsCommandsEmbed(currentTheme, prefix)

                elif clickedButton == 'How to Play':
                    newNavigatorContext = 'How to Play'
                    refreshedEmbed = await helpBuilder.howToPlayEmbed(currentTheme)

                elif clickedButton == 'Game Info':
                    newNavigatorContext = 'Game Info'
                    refreshedEmbed = await helpBuilder.gameInfoCommandsEmbed(currentTheme, prefix)

                elif clickedButton == 'Proposal Stage':
                    newNavigatorContext = 'Proposal Stage'
                    refreshedEmbed = await helpBuilder.expoProposalInfoEmbed(currentTheme, prefix)

                elif clickedButton == 'Voting Stage':
                    newNavigatorContext = 'Voting Stage'
                    refreshedEmbed = await helpBuilder.expoVotingInfoEmbed(currentTheme, loadedRoles)

                elif clickedButton == 'Action Stage':
                    newNavigatorContext = 'Action Stage'
                    refreshedEmbed = await helpBuilder.expoActionsInfoEmbed(currentTheme, loadedRoles)

                elif clickedButton == 'Special':
                    newNavigatorContext = 'Special'
                    refreshedEmbed = await helpBuilder.specialActionsInfoEmbed(currentTheme, loadedRoles, prefix)

                refreshedView = await helpBuilder.mainNavigatorView(newNavigatorContext, navigator, currentTheme, prefix, loadedRoles)
                await interaction.message.edit(view=refreshedView, embed=refreshedEmbed)
                await interaction.response.defer()


        if navigatorContext != 'Main':
            backButton = Button(label = 'Go Back', style=discord.ButtonStyle.grey, emoji = str('◀️'))
            async def processBackButton(interaction):
                await navigate(interaction, 'Go Back')
            backButton.callback = processBackButton
            returnedView.add_item(backButton)

        if navigatorContext == 'Main':
            userInfoButton = Button(label = 'User Info', style=discord.ButtonStyle.grey, emoji = str('📝'))
            async def processUserInfoButton(interaction):
                await navigate(interaction, 'User Info')
            userInfoButton.callback = processUserInfoButton
            returnedView.add_item(userInfoButton)

            startingGameButton = Button(label = 'Starting a Game', style=discord.ButtonStyle.grey, emoji = str('🎮'))
            async def processStartingGameButton(interaction):
                await navigate(interaction, 'Starting a Game')
            startingGameButton.callback = processStartingGameButton
            returnedView.add_item(startingGameButton)

            optionsAndRulesButton = Button(label = 'Game Options and Rules', style= discord.ButtonStyle.grey, emoji = str('⚙️'))
            async def processOptionsAndRulesButton(interaction):
                await navigate(interaction, 'Game Options and Rules')
            optionsAndRulesButton.callback = processOptionsAndRulesButton
            returnedView.add_item(optionsAndRulesButton)

            howToPlayButton = Button(label = 'How to Play', style=discord.ButtonStyle.grey, emoji = str('🕹️'))
            async def processHowToPlayButton(interaction):
                await navigate(interaction, 'How to Play')
            howToPlayButton.callback = processHowToPlayButton
            returnedView.add_item(howToPlayButton)

            roleHelpButton = Button(label = 'Role Info', style = discord.ButtonStyle.grey, emoji=str('👥'))
            async def processRoleHelpButton(interaction):
                await navigate(interaction, 'Role Info')
            roleHelpButton.callback = processRoleHelpButton
            returnedView.add_item(roleHelpButton)

            helpButton = Button(label = 'Help and Info', style = discord.ButtonStyle.grey, emoji = str('❓'))
            async def processHelpButton(interaction):
                await navigate(interaction, 'Help')
            helpButton.callback = processHelpButton
            returnedView.add_item(helpButton)

            statButton = Button(label = 'Stats and Awards', style= discord.ButtonStyle.grey, emoji = str('📊'))
            async def processStatButton(interaction):
                await navigate(interaction, 'Stats')
            statButton.callback = processStatButton
            returnedView.add_item(statButton)

        elif navigatorContext == 'Game Options and Rules':
            themesButton = Button(label = 'Game Themes', style= discord.ButtonStyle.grey, emoji = str('🎭'))
            async def processThemesButton(interaction):
                await navigate(interaction, 'Game Themes')
            themesButton.callback = processThemesButton
            returnedView.add_item(themesButton)

            captainButton = Button(label = 'Team Captains', style=discord.ButtonStyle.grey, emoji = str('👨‍✈️'))
            async def processCaptainButton(interaction):
                await navigate(interaction, 'Team Captains')
            captainButton.callback = processCaptainButton
            returnedView.add_item(captainButton)

            kidnapRulesButton = Button(label = 'Kidnap Rules', style=discord.ButtonStyle.grey, emoji = str('🥷'))
            async def processKidnapRulesButton(interaction):
                await navigate(interaction, 'Kidnap Rules')
            kidnapRulesButton.callback = processKidnapRulesButton
            returnedView.add_item(kidnapRulesButton)

            rumblingButton = Button(label = f'{currentTheme.rumblingName}', style=discord.ButtonStyle.grey, emoji = currentTheme.emojiRumbling)
            async def processRumblingButton(interaction):
                await navigate(interaction, 'Rumbling')
            rumblingButton.callback = processRumblingButton
            returnedView.add_item(rumblingButton)

            wildcardButton = Button(label = f'{currentTheme.wildcardPlural}', style=discord.ButtonStyle.grey, emoji = currentTheme.emojiWildcard)
            async def processWildcardButton(interaction):
                await navigate(interaction, 'Wildcards')
            wildcardButton.callback = processWildcardButton
            returnedView.add_item(wildcardButton)

            rankedButton = Button(label = f'Ranked Status', style=discord.ButtonStyle.grey, emoji = currentTheme.emojiRanked)
            async def processRankedButton(interaction):
                await navigate(interaction, 'Ranked')
            rankedButton.callback = processRankedButton
            returnedView.add_item(rankedButton)

            roleOptionsButton = Button(label = 'Role Options', style= discord.ButtonStyle.grey, emoji = str('👥'))
            async def processRoleOptionsButton(interaction):
                await navigate(interaction, 'Role Options')
            roleOptionsButton.callback = processRoleOptionsButton
            returnedView.add_item(roleOptionsButton)

            savedRulesetsButton = Button(label = 'Saved Rulesets', style=discord.ButtonStyle.grey, emoji = str('💾'))
            async def processSavedRulesetsButton(interaction):
                await navigate(interaction, 'Saved Rulesets')
            savedRulesetsButton.callback = processSavedRulesetsButton
            returnedView.add_item(savedRulesetsButton)

        elif navigatorContext == 'How to Play':
            gameInfoButton = Button(label= 'Game Info', style= discord.ButtonStyle.grey, emoji = str('💡'))
            async def processGameInfoButton(interaction):
                await navigate(interaction, 'Game Info')
            gameInfoButton.callback = processGameInfoButton
            returnedView.add_item(gameInfoButton)

            expoProposalButton = Button(label = 'Proposal Stage', style= discord.ButtonStyle.grey, emoji = str('📜'))
            async def processExpoProposalButton(interaction):
                await navigate(interaction, 'Proposal Stage')
            expoProposalButton.callback = processExpoProposalButton
            returnedView.add_item(expoProposalButton)

            expoVotingButton = Button(label = 'Voting Stage', style=discord.ButtonStyle.grey, emoji = str('☑️'))
            async def processExpoVotingButton(interaction):
                await navigate(interaction, 'Voting Stage')
            expoVotingButton.callback = processExpoVotingButton
            returnedView.add_item(expoVotingButton)

            expoActionButton = Button(label = 'Action Stage', style=discord.ButtonStyle.grey, emoji = str('🏇'))
            async def processExpoActionButton(interaction):
                await navigate(interaction, 'Action Stage')
            expoActionButton.callback = processExpoActionButton
            returnedView.add_item(expoActionButton)

            specialButton = Button(label = 'Special', style=discord.ButtonStyle.grey, emoji = str('🪄'))
            async def processSpecialButton(interaction):
                await navigate(interaction, 'Special')
            specialButton.callback = processSpecialButton
            returnedView.add_item(specialButton)

        elif navigatorContext == 'Role Info':
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

            soldierSelection = Select(placeholder= f'Get Info about a {currentTheme.soldierSingle} Role', min_values=1, max_values=1)
            for role in soldierRoles:
                soldierSelection.add_option(label = role.shortName, emoji=role.emoji)
            warriorSelection = Select(placeholder= f'Get Info about a {currentTheme.warriorSingle} Role', min_values=1, max_values=1)
            for role in warriorRoles:
                warriorSelection.add_option(label = role.shortName, emoji = role.emoji)
            wildcardSelection = Select(placeholder= f'Get Info about a {currentTheme.wildcardSingle} Role', min_values=1, max_values=1)
            for role in wildcardRoles:
                wildcardSelection.add_option(label = role.shortName, emoji = role.emoji)
            async def processSoldierSelection(interaction):
                selectedRoleShortName = soldierSelection.values[0]
                for role in soldierRoles:
                    if role.shortName == selectedRoleShortName:
                        await navigate(interaction, 'Selected Role Info', role)
            async def processWarriorSelection(interaction):
                selectedRoleShortName = warriorSelection.values[0]
                for role in warriorRoles:
                    if role.shortName == selectedRoleShortName:
                        await navigate(interaction, 'Selected Role Info', role)
            async def processWildcardSelection(interaction):
                selectedRoleShortName = wildcardSelection.values[0]
                for role in wildcardRoles:
                    if role.shortName == selectedRoleShortName:
                        await navigate(interaction, 'Selected Role Info', role)
            soldierSelection.callback = processSoldierSelection
            warriorSelection.callback = processWarriorSelection
            wildcardSelection.callback = processWildcardSelection
            returnedView.add_item(soldierSelection)
            returnedView.add_item(warriorSelection)
            returnedView.add_item(wildcardSelection)

        elif navigatorContext == 'Stats':

            infoButton = Button(label='Information', style=discord.ButtonStyle.grey, emoji = str('📚'))
            async def processInfoButton(interaction):
                await navigate(interaction, 'StatsInfo')
            infoButton.callback = processInfoButton
            returnedView.add_item(infoButton)

            commandButton = Button(label = 'Commands', style=discord.ButtonStyle.grey, emoji= str('🧮'))
            async def processCommandButton(interaction):
                await navigate(interaction, 'StatsCommands')
            commandButton.callback = processCommandButton
            returnedView.add_item(commandButton)


        return returnedView

        


