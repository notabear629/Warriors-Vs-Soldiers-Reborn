
#an immature way of testing themes

import os
from dotenv import load_dotenv
import discord
from discord.ext import commands
import random

#CHANGE THIS CLASS NAME. Your new file and your new class should NOT be named defaultGameTheme, each theme added should have different names.
class eggplant:
    #You have free reign to edit these as you please
    themeName = str('🍆')
    gameName = str('🍆')
    soldierSingle = str('🍆')
    soldierPlural = str('🍆')
    emojiSoldier = str('🍆')
    warriorSingle = str('🍆')
    warriorPlural = str('🍆')
    emojiWarrior = str('🍆')
    wallSingle = str('🍆')
    wallPlural = str('🍆')

    soldierThumbnail = 'https://upload.wikimedia.org/wikipedia/commons/thumb/f/f0/Twemoji_1f346.svg/1200px-Twemoji_1f346.svg.png'
    warriorThumbnail = 'https://upload.wikimedia.org/wikipedia/commons/thumb/f/f0/Twemoji_1f346.svg/1200px-Twemoji_1f346.svg.png'
    wildcardThumbnail ='https://upload.wikimedia.org/wikipedia/commons/thumb/f/f0/Twemoji_1f346.svg/1200px-Twemoji_1f346.svg.png'

    soldierColor = discord.Color.dark_purple()
    warriorColor = discord.Color.dark_purple()
    wildcardColor = discord.Color.dark_purple()

    soldierDefaultMessage = 'Work with your fellow Soldiers to successfully complete 3 expeditions and reach the basement. Remember to conceal the true identity of Eren! Securing the walls is not enough, after the rounds of expeditions, the Warriors will have one last shot of winning if they can successfully identity Eren!'
    warriorDefaultMessage = 'Work with your fellow Warriors to try to knock down the walls before the Soldiers can reach the basement. Be mindful of how the Soldiers behave, even if you fail to destroy the walls, you will have one last chance of victory if you can successfully identify Eren!'
    wildcardDefaultMessage = 'Wildcards are neither Soldiers nor Warriors, so the roles behave much differently. Shoot for your personal objective to the best of your abilities so that you may bask in the eternal glory of winning your own way!'

    #Status Embed Aesthetics
    winningColor = discord.Color.dark_purple()
    neutralColor = discord.Color.dark_purple()
    losingColor = discord.Color.dark_purple()
    lostColor = discord.Color.dark_purple()

    statusProgress = str('🍆')
    statusWalls = str('🍆')
    statusExpeditions = str('🍆')

    expeditionName = str('🍆')
    expoMembersName = str('🍆')

    #Note that for emojis, you may use a string of the unicode emoji for a default emoji, or an ID of a custom emoji.
    #Please be sure to put the emojis in the form of str('emoji') if you are using default unicode emojis.
    #The reason for typecasting a string as a string, is because the str() function is just an easy way to enable UTF-8 encoding to get the emoji to work.
    #We aren't really turning our input to a String, since the '' marks already make it a string, we're abusing the str() function for the encoding since it's a simple way to call it
    emojiWinMarkerOne = str('🍆')
    emojiWinMarkerTwo = str('🍆')
    emojiWinMarkerThree = str('🍆')
    emojiSpacer = str('🍆')
    emojiRoundVictoryMarker = str('🍆')
    emojiVictoryMarker = str('🍆')
    emojiMariaExterior = str('🍆')
    emojiMariaInterior = str('🍆')
    emojiRoseExterior = str('🍆')
    emojiRoseInterior = str('🍆')
    emojiSinaExterior = str('🍆')
    emojiSinaInterior = str('🍆')
    emojiBrokenExterior = str('🍆')
    emojiBrokenInterior = str('🍆')
    emojiWinMarker = str('🍆')
    emojiFailMarker = str('🍆')
    emojiCurrentMarker = str('🍆')

    #Roles embed aesthetics
    rolesEmbedColor = discord.Color.dark_purple()

    #Players embed aesthetics
    playersEmbedColor = discord.Color.dark_purple()
    commanderName = str('🍆')
    emojiCommanderMarker = str('🍆')

    #Expedition aesthetics
    expeditionTeamMembers = str('🍆')
    expeditionTeam = str('🍆')
    emojiPassExpedition = str('🍆')
    emojiSabotageExpedition = str('🍆')

    #Pick expo member aesthetics
    pickColor = discord.Color.dark_purple()

    #Voting aesthetics
    emojiAcceptExpedition = str('🍆')
    emojiRejectExpedition = str('🍆')
    emojiAbstainExpedition = str('🍆')
    voteDMColor = discord.Color.dark_purple()
    acceptedExpeditionColor = discord.Color.dark_purple()
    rejectedExpeditionColor = discord.Color.dark_purple()

    #Expedition DM aesthetics
    expeditionDMColor = discord.Color.dark_purple()

    #Temporary Message Aesthetics
    temporaryMessageColor = discord.Color.dark_purple()

    #Expedition results aesthetics
    expoPassedColor = discord.Color.dark_purple()
    expoSabotagedColor = discord.Color.dark_purple()
    wallMariaBreakMessage = str('🍆')
    wallRoseBreakMessage = str('🍆')
    wallSinaBreakMessage = str('🍆')

    #Game over Aesthetics
    wallBreakMessage = str('🍆')
    basementMessage = str('🍆')


    global prefix

    prefix = os.getenv('BOT_PREFIX')


    #DO NOT CHANGE THIS CLASS NAME! Even if you rename the role, keep the function as Eren. Apply this advice to all roles.
    class Eren:
        #Do not change this roleID key. The code will look for "Eren" even if you re-skin it, it is important to keep all roleIDs the same.
        roleDict = {'roleID' : 'Eren'}

        #You may change 'Eren Yeager' to whatever you want his name to be.
        roleDict['name'] = str('🍆')

        #You may change the shortname to whatever you want the name to be, this one is purely cosmetic.
        roleDict['shortName'] = str('🍆')

        #Do not edit the team at all. Even if you rename the "Soldiers" team, the code will look for "Soldiers" and re-naming the team will break the code.
        roleDict['team'] = 'Soldiers'

        #isTitan is used for stuff like the Pure Titan (may or may not be implemented yet) and Mike (may or may not be implemented yet). You may actually edit these to being True or False depending on the logic for the "Titan" you use in your theme.
        #For example, if you were making a Fate Stay/Night based theme, you may decide that the "titan" logic should instead work on the basis of "Servants".
        #Under this system, if the character is a servant, you would keep this as info['isTitan'] = True, and if they aren't, you would set this to info['isTitan'] = False.
        #Please keep in mind that removing isTitan from the coordinate equivalent will make very Mike overpowered in games with many Warriors as Titans.
        roleDict['isTitan'] = True

        #If you are using a custom emoji, just make this the integer emoji ID you wish to use. It is important your bot is in the server that the emoji is hosted in, or they will not be able to use the emoji and your game will break.
        #If you are using a default emoji, like the crown emoji, you can just put a String ':crown:' and it will work fine. The code will check if the type is an integer or String so dont worry about mixing types.
        roleDict['emoji'] = str('🍆')

        #The roleMessage is the part of the message the bot sends that gives specific information regarding the role itself when you are assigned a role.
        #You may change any role message as you wish.
        roleDict['roleMessage'] = str('🍆')

        #The gameRole is basically a way to relate what the job of this role is without making use of any theme. Remember how Entropi's bot was theme-less, this would essentially be what this role might be called in Entropi's bot.
        #You *can* change these, but I would recommend not to.
        #I would also recommend keeping the format of :emoji:Name:emoji:
        roleDict['gameRole'] = str('🍆')

        #helpInfo is the message that will be summoned when you do a ~help or ~info (may or may not be implemented yet) for a particular role
        #Highly recommend changing this entirely to match your role and your lore reasoning for why your themed character fits the role
        roleDict['helpInfo'] = str('🍆')

    #PLEASE PLEASE FOLLOW ALL INSTRUCTIONS PRESENT FOR THE EREN ROLE FOR THE FUTURE ROLES!

    class Soldier:
        roleDict = {'roleID' : 'Soldier'}

        roleDict['name'] = str('🍆')

        roleDict['shortName'] = str('🍆')

        roleDict['team'] = 'Soldiers'

        roleDict['isTitan'] = False

        roleDict['emoji'] = str('🍆')

        roleDict['roleMessage'] = str('🍆')

        roleDict['gameRole'] = str('🍆')

        roleDict['helpInfo'] = str('🍆')

    class Zeke:
        roleDict = {'roleID' : 'Zeke'}

        roleDict['name'] = str('🍆')

        roleDict['shortName'] = str('🍆')

        roleDict['team'] = 'Warriors'

        roleDict['isTitan'] = True

        roleDict['emoji'] = str('🍆')

        roleDict['roleMessage'] = str('🍆')

        roleDict['gameRole'] = str('🍆')

        roleDict['helpInfo'] = str('🍆')
    

    class Warrior:
        roleDict = {'roleID' : 'Warrior'}

        roleDict['name'] = str('🍆')

        roleDict['shortName'] = str('🍆')

        roleDict['team'] = 'Warriors'

        roleDict['isTitan'] = False

        roleDict['emoji'] = str('🍆')

        roleDict['roleMessage'] = str('🍆')

        roleDict['gameRole'] = str('🍆')

        roleDict['helpInfo'] = str('🍆')


    def getErenInfo(CurrentGame):
        erenInfo = str('🍆')
        return erenInfo
    
    def getWarriorInfo(CurrentGame, player):
        warriorInfo = str('🍆')
        return warriorInfo