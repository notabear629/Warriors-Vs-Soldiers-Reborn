#Please pay close attention to instructions when creating new theme classes.
#When creating new themes, you should only be trying to make COSMETIC changes. To truly add more roles or functionality to the game, you will need to do a lot more than change the theme.
#However, if you do create a new role, you will have to give them a theme in any themes you are using.
import os
from dotenv import load_dotenv
import discord
from discord.ext import commands
import random

#CHANGE THIS CLASS NAME. Your new file and your new class should NOT be named defaultGameTheme, each theme added should have different names.
class eggplant:
    global prefix

    prefix = os.getenv('BOT_PREFIX')


    #You have free reign to edit these as you please
    themeName = "Zeke's Nightmare"
    gameName = str('🍆')
    soldierSingle = str('🍆')
    soldierPlural = str('🍆')
    emojiSoldier = str('🍆')
    warriorSingle = str('🍆')
    warriorPlural = str('🍆')
    emojiWarrior = str('🍆')
    wildcardSingle = str('🍆')
    wildcardPlural = str('🍆')
    emojiWildcard = str('🍆')
    wallSingle = str('🍆')
    wallPlural = str('🍆')
    #By Default is the same as Eren Emoji
    emojiTheme = str('🍆')
    titanSingle = str('🍆')
    titanPlural = str('🍆')
    emojiDead = str('🍆')

    soldierThumbnail = 'https://upload.wikimedia.org/wikipedia/commons/thumb/f/f0/Twemoji_1f346.svg/1200px-Twemoji_1f346.svg.png'
    warriorThumbnail = 'https://upload.wikimedia.org/wikipedia/commons/thumb/f/f0/Twemoji_1f346.svg/1200px-Twemoji_1f346.svg.png'
    wildcardThumbnail = 'https://upload.wikimedia.org/wikipedia/commons/thumb/f/f0/Twemoji_1f346.svg/1200px-Twemoji_1f346.svg.png'
    globalThumbnail = 'https://upload.wikimedia.org/wikipedia/commons/thumb/f/f0/Twemoji_1f346.svg/1200px-Twemoji_1f346.svg.png'

    soldierColor = discord.Color.dark_purple()
    warriorColor = discord.Color.dark_purple()
    wildcardColor = discord.Color.dark_purple()

    soldierDefaultMessage = str('🍆')
    warriorDefaultMessage = str('🍆')
    wildcardDefaultMessage = str('🍆')

    #Lobby embed Aesthetics
    lobbyEmbedColor = discord.Color.dark_purple()
    
    #Help Aesthetics
    helpEmbedColor = discord.Color.dark_purple()

    #Rule Selection Aesthetics
    emojiBackButton = str('🍆')
    emojiRoleEnabled = str('🍆')
    emojiRoleDisabled = str('🍆')
    emojiRoleDefault = str('🍆')
    emojiCasual = str('🍆')
    emojiRanked = str('🍆')

    #Status Embed Aesthetics
    winningColor = discord.Color.dark_purple()
    neutralColor = discord.Color.dark_purple()
    losingColor = discord.Color.dark_purple()
    lostColor = discord.Color.dark_purple()

    statusProgress = 'Progress towards Basement'
    statusWalls = 'Status of the Walls'
    statusExpeditions = 'Expedition Info'

    expeditionName = 'Expedition'
    expoMembersName = 'members'

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
    emojiSecuredExpedition = str('🍆')

    #Pick expo member aesthetics
    pickColor = discord.Color.dark_purple()

    #Voting aesthetics
    emojiAcceptExpedition = str('🍆')
    emojiRejectExpedition = str('🍆')
    emojiAbstainExpedition = str('🍆')
    voteDMColor = discord.Color.dark_purple()
    acceptedExpeditionColor = discord.Color.dark_purple()
    rejectedExpeditionColor = discord.Color.dark_purple()
    jeanedExpeditionColor = discord.Color.dark_purple()
    mikeSmell = str('🍆')
    emojiNoEren = str('🍆')

    #Expedition DM aesthetics
    expeditionDMColor = discord.Color.dark_purple()

    #Temporary Message Aesthetics
    temporaryMessageColor = discord.Color.dark_purple()

    #Expedition results aesthetics
    expoPassedColor = discord.Color.dark_purple()
    expoSabotagedColor = discord.Color.dark_purple()
    expoSecuredColor = discord.Color.dark_purple()
    arminNukeColor = discord.Color.dark_purple()
    emojiNuke = str('🍆')
    wallMariaBreakMessage = str('🍆')
    wallRoseBreakMessage = str('🍆')
    wallSinaBreakMessage = str('🍆')

    #Game over Aesthetics
    wallBreakMessage = str('🍆')
    basementMessage = str('🍆')
    kidnapTimeoutMessage = str('🍆')
    multikidnapTimeoutMessage = str('🍆')
    multikidnapSuccessMessage = str('🍆')
    kidnapSuccessMessage = str('🍆')
    kidnapFailMessage = str('🍆')
    multikidnapFailMessage = str('🍆')
    endgameCardColor = discord.Color.dark_purple()
    emojiWinner = str('🍆')
    emojiLoser = str('🍆')
    emojiMVP = str('🍆')

    #Webhook Message Aesthetics
    jeanMessage = str('🍆')
    pieckMessageWithJean = str('🍆')
    pieckMessageWithoutJean = str('🍆')
    arminMessage = str('🍆')
    leviAttackMessage = str('🍆')
    leviDefendMessage = str('🍆')
    sashaMessage = str('🍆')
    dazMessage = str('🍆')
    dazMessageFollowUp = str('🍆')
    mikasaMessage = str('🍆')
    reinerMessage = str('🍆')
    bertholdtMessage = str('🍆')
    annieMessage = str('🍆')
    retreatMessage = str('🍆')

    #Other role messages
    flochMessageEren = str('🍆')
    flochMessageNoEren = str('🍆')

    #Timeout Messages
    timeoutCoreStart = str('🍆')
    timeoutCoreEnd = str('🍆')
    timeoutPick = str('🍆')
    timeoutVote = str('🍆')
    timeoutExpo = str('🍆')
    timeoutKidnap = str('🍆')
    timeoutRumblingFight = str('🍆')

    # Rumbling Aesthetics
    rumblingName = str('🍆')
    emojiRumbling = str('🍆')
    emojiRumblingWallExterior = str('🍆')
    emojiRumblingWallInterior = str('🍆')
    yeageristSingle = str('🍆')
    yeageristPlural = str('🍆')
    yeageristTeam = str('🍆')
    allianceSingle = str('🍆')
    alliancePlural = str('🍆')
    allianceTeam = str('🍆')
    rumblingStatusColor = discord.Color.dark_purple()
    rumblingAltStatusColor = discord.Color.dark_purple()
    rumblingStartAttachment = 'https://upload.wikimedia.org/wikipedia/commons/thumb/f/f0/Twemoji_1f346.svg/1200px-Twemoji_1f346.svg.png'
    rumblingFirstMessage = str('🍆')
    rumblingSecondMessage = str('🍆')
    rumblingThirdMessage = str('🍆')
    rumblingTimerOne = 2
    rumblingTimerTwo = 2
    rumblingTimerThree = 2
    rumblingIntroMessage = str('🍆')
    allianceFormMessage = str('🍆')
    yeageristInTheWay = str('🍆')
    allianceZekeClear = str('🍆')
    ZekeInTheWay = str('🍆')
    allianceZekeDefeated = str('🍆')
    ErenInTheWay = str('🍆')
    allianceMemberSlain = str('🍆')
    newFightPrompt = str('🍆')
    genericYeageristWin = str('🍆')
    genericAllianceWin = str('🍆')

    standardYeageristWin = str('🍆')
    flochDominationWin = str('🍆') 
    zekeDominationWin = str('🍆')
    erenDominationWin = str('🍆')

    standardAllianceWin = str('🍆')
    dominantAlliancewin = str('🍆')
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

        #The purpose of this variable is to determine if the player is on the side of the yeagerists on the rumbling, or the alliance.
        #There are 4 values this can/should be set to.
        #yeageristFighter means they will be on the rumbling team, and will actively fight. yeageristBench means they will win if the rumbling team wins, but they will not fight.
        #allianceFighter and allianceBench are the other possible values and well... You can probably figure the rest out.
        roleDict['rumblingTeam'] = 'yeageristFighter'

        #isTitan is used for stuff like the Pure Titan (may or may not be implemented yet) and Mike (may or may not be implemented yet). You may actually edit these to being True or False depending on the logic for the "Titan" you use in your theme.
        #For example, if you were making a Fate Stay/Night based theme, you may decide that the "titan" logic should instead work on the basis of "Servants".
        #Under this system, if the character is a servant, you would keep this as info['isTitan'] = True, and if they aren't, you would set this to info['isTitan'] = False.
        #Please keep in mind that removing isTitan from the coordinate equivalent will make very Mike overpowered in games with many Warriors as Titans.
        roleDict['isTitan'] = True

        #If you are using a custom emoji, just make this the integer emoji ID you wish to use. It is important your bot is in the server that the emoji is hosted in, or they will not be able to use the emoji and your game will break.
        #If you are using a default emoji, like the crown emoji, you can just put a String ':crown:' and it will work fine. The code will check if the type is an integer or String so dont worry about mixing types.
        roleDict['emoji'] = str('🍆')


        #Not all roles actually use secondary emojis. If this is None, it's fine. Should be an int or emoji string like any other emoji.
        roleDict['secondaryEmoji'] = str('🍆')

        #If you are using a custom emoji, then make sure this is set to None. Otherwise set this to a URL of the emoji you are using. Unfortunately, Webhook images and thumbnails can only be made with urls and default emojis dont have urls.
        #Thus, if you are using a built in emoji, you will need to define this dictionary key.
        roleDict['imageURL'] = 'https://upload.wikimedia.org/wikipedia/commons/thumb/f/f0/Twemoji_1f346.svg/1200px-Twemoji_1f346.svg.png'


        #Overwhelming majority have no purpose for secondaryImgeURL. Mainly here in case you want to display secondaryEmoji as a thumbnail.
        roleDict['secondaryImageURL'] = 'https://upload.wikimedia.org/wikipedia/commons/thumb/f/f0/Twemoji_1f346.svg/1200px-Twemoji_1f346.svg.png'

        #The roleMessage is the part of the message the bot sends that gives specific information regarding the role itself when you are assigned a role.
        #You may change any role message as you wish.
        roleDict['roleMessage'] = str('🍆')

        #The gameRole is basically a way to relate what the job of this role is without making use of any theme. Remember how Entropi's bot was theme-less, this would essentially be what this role might be called in Entropi's bot.
        #You *can* change these, but I would recommend not to.
        #I would also recommend keeping the format of :emoji:Name:emoji:
        roleDict['gameRole'] = ':map:Coordinate:map:'

        #helpInfo is the message that will be summoned when you do a ~help or ~info (may or may not be implemented yet) for a particular role
        #Highly recommend changing this entirely to match your role and your lore reasoning for why your themed character fits the role
        roleDict['helpInfo'] = str('🍆')

    #PLEASE PLEASE FOLLOW ALL INSTRUCTIONS PRESENT FOR THE EREN ROLE FOR THE FUTURE ROLES!

    class Historia:
        roleDict = {'roleID' : 'Historia'}

        roleDict['name'] = str('🍆🍆')

        roleDict['shortName'] = str('🍆🍆')

        roleDict['team'] = 'Soldiers'

        roleDict['rumblingTeam'] = 'yeageristBench'

        roleDict['isTitan'] = False

        roleDict['emoji'] = str('🍆')

        roleDict['secondaryEmoji'] = str('🍆')

        roleDict['imageURL'] = 'https://upload.wikimedia.org/wikipedia/commons/thumb/f/f0/Twemoji_1f346.svg/1200px-Twemoji_1f346.svg.png'

        roleDict['secondaryImageURL'] = 'https://upload.wikimedia.org/wikipedia/commons/thumb/f/f0/Twemoji_1f346.svg/1200px-Twemoji_1f346.svg.png'

        roleDict['roleMessage'] = str('🍆')

        roleDict['gameRole'] = ':angel:Queen:angel:'

        roleDict['helpInfo'] = str('🍆')

    class Hange:
        roleDict = {'roleID' : 'Hange'}

        roleDict['name'] = str('🍆🍆🍆')

        roleDict['shortName'] = str('🍆🍆🍆')

        roleDict['team'] = 'Soldiers'

        roleDict['rumblingTeam'] = 'allianceFighter'

        roleDict['isTitan'] = False

        roleDict['emoji'] = str('🍆')

        roleDict['secondaryEmoji'] = str('🍆')

        roleDict['imageURL'] = 'https://upload.wikimedia.org/wikipedia/commons/thumb/f/f0/Twemoji_1f346.svg/1200px-Twemoji_1f346.svg.png'

        roleDict['secondaryImageURL'] = 'https://upload.wikimedia.org/wikipedia/commons/thumb/f/f0/Twemoji_1f346.svg/1200px-Twemoji_1f346.svg.png'

        roleDict['roleMessage'] = str('🍆')

        roleDict['gameRole'] = ':bulb:Analyst:bulb:'

        roleDict['helpInfo'] = str('🍆')
    
    class Jean:
        roleDict = {'roleID' : 'Jean'}

        roleDict['name'] = str('🍆🍆🍆🍆')

        roleDict['shortName'] = str('🍆🍆🍆🍆')

        roleDict['team'] = 'Soldiers'

        roleDict['rumblingTeam'] = 'allianceFighter'

        roleDict['isTitan'] = False

        roleDict['emoji'] = str('🍆')

        roleDict['secondaryEmoji'] = str('🍆')

        roleDict['imageURL'] = 'https://upload.wikimedia.org/wikipedia/commons/thumb/f/f0/Twemoji_1f346.svg/1200px-Twemoji_1f346.svg.png'

        roleDict['secondaryImageURL'] = 'https://upload.wikimedia.org/wikipedia/commons/thumb/f/f0/Twemoji_1f346.svg/1200px-Twemoji_1f346.svg.png'

        roleDict['roleMessage'] = str('🍆')

        roleDict['gameRole'] = ':white_check_mark:Voting Ackermann:white_check_mark:'

        roleDict['helpInfo'] = str('🍆')

    class Mike:
        roleDict = {'roleID' : 'Mike'}

        roleDict['name'] = str('🍆🍆🍆🍆🍆')

        roleDict['shortName'] = str('🍆🍆🍆🍆🍆')

        roleDict['team'] = 'Soldiers'

        roleDict['rumblingTeam'] = 'allianceFighter'

        roleDict['isTitan'] = False

        roleDict['emoji'] = str('🍆')

        roleDict['secondaryEmoji'] = str('🍆')

        roleDict['imageURL'] = 'https://upload.wikimedia.org/wikipedia/commons/thumb/f/f0/Twemoji_1f346.svg/1200px-Twemoji_1f346.svg.png'

        roleDict['secondaryImageURL'] = 'https://upload.wikimedia.org/wikipedia/commons/thumb/f/f0/Twemoji_1f346.svg/1200px-Twemoji_1f346.svg.png'

        roleDict['roleMessage'] = str('🍆')

        roleDict['gameRole'] = ':nose:Mike:nose:'

        roleDict['helpInfo'] = str('🍆')

    class Hitch:
        roleDict = {'roleID' : 'Hitch'}

        roleDict['name'] = str('🍆🍆🍆🍆🍆🍆')

        roleDict['shortName'] = str('🍆🍆🍆🍆🍆🍆')

        roleDict['team'] = 'Soldiers'

        roleDict['rumblingTeam'] = 'yeageristBench'

        roleDict['isTitan'] = False

        roleDict['emoji'] = str('🍆')

        roleDict['secondaryEmoji'] = str('🍆') 

        roleDict['imageURL'] = 'https://upload.wikimedia.org/wikipedia/commons/thumb/f/f0/Twemoji_1f346.svg/1200px-Twemoji_1f346.svg.png'

        roleDict['secondaryImageURL'] = 'https://upload.wikimedia.org/wikipedia/commons/thumb/f/f0/Twemoji_1f346.svg/1200px-Twemoji_1f346.svg.png'

        roleDict['roleMessage'] = str('🍆')

        roleDict['gameRole'] = ':mag:Ability Investigator:mag:'

        roleDict['helpInfo'] = str('🍆')

    class Armin:
        roleDict = {'roleID' : 'Armin'}

        roleDict['name'] = str('🍆🍆🍆🍆🍆🍆🍆')

        roleDict['shortName'] = str('🍆🍆🍆🍆🍆🍆🍆')

        roleDict['team'] = 'Soldiers'

        roleDict['rumblingTeam'] = 'allianceFighter'

        roleDict['isTitan'] = True

        roleDict['emoji'] = str('🍆')

        roleDict['secondaryEmoji'] = str('🍆')

        roleDict['imageURL'] = 'https://upload.wikimedia.org/wikipedia/commons/thumb/f/f0/Twemoji_1f346.svg/1200px-Twemoji_1f346.svg.png'

        roleDict['secondaryImageURL'] = 'https://upload.wikimedia.org/wikipedia/commons/thumb/f/f0/Twemoji_1f346.svg/1200px-Twemoji_1f346.svg.png'

        roleDict['roleMessage'] = str('🍆')

        roleDict['gameRole'] = ':radioactive:Nuclear Bomb:radioactive:'

        roleDict['helpInfo'] = str('🍆')

    class Levi:
        roleDict = {'roleID' : 'Levi'}

        roleDict['name'] = str('🍆🍆🍆🍆🍆🍆🍆🍆')

        roleDict['shortName'] = str('🍆🍆🍆🍆🍆🍆🍆🍆')

        roleDict['team'] = 'Soldiers'

        roleDict['rumblingTeam'] = 'allianceFighter'

        roleDict['isTitan'] = False

        roleDict['emoji'] = str('🍆')

        roleDict['secondaryEmoji'] = str('🍆')

        roleDict['imageURL'] = 'https://upload.wikimedia.org/wikipedia/commons/thumb/f/f0/Twemoji_1f346.svg/1200px-Twemoji_1f346.svg.png'

        roleDict['secondaryImageURL'] = 'https://upload.wikimedia.org/wikipedia/commons/thumb/f/f0/Twemoji_1f346.svg/1200px-Twemoji_1f346.svg.png'

        roleDict['roleMessage'] = str('🍆')

        roleDict['gameRole'] = ':guard:Ackermann:guard:'

        roleDict['helpInfo'] = str('🍆')


    class Sasha:
        roleDict = {'roleID' : 'Sasha'}

        roleDict['name'] = str('🍆🍆🍆🍆🍆🍆🍆🍆🍆')

        roleDict['shortName'] = str('🍆🍆🍆🍆🍆🍆🍆🍆🍆')

        roleDict['team'] = 'Soldiers'

        roleDict['rumblingTeam'] = 'allianceFighter'

        roleDict['isTitan'] = False

        roleDict['emoji'] = str('🍆')

        roleDict['secondaryEmoji'] = str('🍆')

        roleDict['imageURL'] = 'https://upload.wikimedia.org/wikipedia/commons/thumb/f/f0/Twemoji_1f346.svg/1200px-Twemoji_1f346.svg.png'

        roleDict['secondaryImageURL'] = 'https://upload.wikimedia.org/wikipedia/commons/thumb/f/f0/Twemoji_1f346.svg/1200px-Twemoji_1f346.svg.png'

        roleDict['roleMessage'] = str('🍆')

        roleDict['gameRole'] = ':bow_and_arrow:Sniper:bow_and_arrow:'

        roleDict['helpInfo'] = str('🍆')

    class Erwin:
        roleDict = {'roleID' : 'Erwin'}

        roleDict['name'] = str('🍆🍆🍆🍆🍆🍆🍆🍆🍆🍆')

        roleDict['shortName'] = str('🍆🍆🍆🍆🍆🍆🍆🍆🍆🍆')

        roleDict['team'] = 'Soldiers'

        roleDict['rumblingTeam'] = 'allianceFighter'

        roleDict['isTitan'] = False

        roleDict['emoji'] = str('🍆')

        roleDict['secondaryEmoji'] = str('🍆')

        roleDict['imageURL'] = 'https://upload.wikimedia.org/wikipedia/commons/thumb/f/f0/Twemoji_1f346.svg/1200px-Twemoji_1f346.svg.png'

        roleDict['secondaryImageURL'] = 'https://upload.wikimedia.org/wikipedia/commons/thumb/f/f0/Twemoji_1f346.svg/1200px-Twemoji_1f346.svg.png'

        roleDict['roleMessage'] = str('🍆')

        roleDict['gameRole'] = ':dizzy:True Commander:dizzy:'

        roleDict['helpInfo'] = str('🍆')

    class Daz:
        roleDict = {'roleID' : 'Daz'}

        roleDict['name'] = str('🍆🍆🍆🍆🍆🍆🍆🍆🍆🍆🍆')

        roleDict['shortName'] = str('🍆🍆🍆🍆🍆🍆🍆🍆🍆🍆🍆')

        roleDict['team'] = 'Soldiers'

        roleDict['rumblingTeam'] = 'yeageristBench'

        roleDict['isTitan'] = False

        roleDict['emoji'] = str('🍆')

        roleDict['secondaryEmoji'] = str('🍆')

        roleDict['imageURL'] = 'https://upload.wikimedia.org/wikipedia/commons/thumb/f/f0/Twemoji_1f346.svg/1200px-Twemoji_1f346.svg.png'

        roleDict['secondaryImageURL'] = 'https://upload.wikimedia.org/wikipedia/commons/thumb/f/f0/Twemoji_1f346.svg/1200px-Twemoji_1f346.svg.png'

        roleDict['roleMessage'] = str('🍆')

        roleDict['gameRole'] = ':scream:Coward:scream:'

        roleDict['helpInfo'] = str('🍆')

    class Floch:
        roleDict = {'roleID' : 'Floch'}

        roleDict['name'] = str('🍆🍆🍆🍆🍆🍆🍆🍆🍆🍆🍆🍆')

        roleDict['shortName'] = str('🍆🍆🍆🍆🍆🍆🍆🍆🍆🍆🍆🍆')

        roleDict['team'] = 'Soldiers'

        roleDict['rumblingTeam'] = 'yeageristFighter'

        roleDict['isTitan'] = False

        roleDict['emoji'] = str('🍆')

        roleDict['secondaryEmoji'] = str('🍆')

        roleDict['imageURL'] = 'https://upload.wikimedia.org/wikipedia/commons/thumb/f/f0/Twemoji_1f346.svg/1200px-Twemoji_1f346.svg.png'

        roleDict['secondaryImageURL'] = 'https://upload.wikimedia.org/wikipedia/commons/thumb/f/f0/Twemoji_1f346.svg/1200px-Twemoji_1f346.svg.png'

        roleDict['roleMessage'] = str('🍆')

        roleDict['gameRole'] = ':punch:Coordinate\'s Fist:punch:'

        roleDict['helpInfo'] = str('🍆')

    class Mikasa:
        roleDict = {'roleID' : 'Mikasa'}

        roleDict['name'] = str('🍆🍆🍆🍆🍆🍆🍆🍆🍆🍆🍆🍆🍆')

        roleDict['shortName'] = str('🍆🍆🍆🍆🍆🍆🍆🍆🍆🍆🍆🍆🍆')

        roleDict['team'] = 'Soldiers'

        roleDict['rumblingTeam'] = 'allianceFighter'

        roleDict['isTitan'] = False

        roleDict['emoji'] = str('🍆')

        roleDict['secondaryEmoji'] = str('🍆')

        roleDict['imageURL'] = 'https://upload.wikimedia.org/wikipedia/commons/thumb/f/f0/Twemoji_1f346.svg/1200px-Twemoji_1f346.svg.png'

        roleDict['secondaryImageURL'] = 'https://upload.wikimedia.org/wikipedia/commons/thumb/f/f0/Twemoji_1f346.svg/1200px-Twemoji_1f346.svg.png'

        roleDict['roleMessage'] = str('🍆')

        roleDict['gameRole'] = ':fencer:Bodyguard:fencer:'

        roleDict['helpInfo'] = str('🍆')
    
    class Soldier:
        roleDict = {'roleID' : 'Soldier'}

        roleDict['name'] = str('🍆🍆🍆🍆🍆🍆🍆🍆🍆🍆🍆🍆🍆🍆')

        roleDict['shortName'] = str('🍆🍆🍆🍆🍆🍆🍆🍆🍆🍆🍆🍆🍆🍆')

        roleDict['team'] = 'Soldiers'

        roleDict['rumblingTeam'] = 'allianceBench'

        roleDict['isTitan'] = False

        roleDict['emoji'] = str('🍆')

        roleDict['secondaryEmoji'] = str('🍆')

        roleDict['imageURL'] = 'https://upload.wikimedia.org/wikipedia/commons/thumb/f/f0/Twemoji_1f346.svg/1200px-Twemoji_1f346.svg.png'

        roleDict['secondaryImageURL'] = 'https://upload.wikimedia.org/wikipedia/commons/thumb/f/f0/Twemoji_1f346.svg/1200px-Twemoji_1f346.svg.png'

        roleDict['roleMessage'] = str('🍆')

        roleDict['gameRole'] = ':shield:Default Soldier:shield:'

        roleDict['helpInfo'] = str('🍆')

    class Zeke:
        roleDict = {'roleID' : 'Zeke'}

        roleDict['name'] = str('🍆')

        roleDict['shortName'] = str('🍆')

        roleDict['team'] = 'Warriors'

        roleDict['rumblingTeam'] = 'yeageristFighter'

        roleDict['isTitan'] = True

        roleDict['emoji'] = str('🍆')

        roleDict['secondaryEmoji'] = str('🍆')

        roleDict['imageURL'] = 'https://upload.wikimedia.org/wikipedia/commons/thumb/f/f0/Twemoji_1f346.svg/1200px-Twemoji_1f346.svg.png'

        roleDict['secondaryImageURL'] = 'https://upload.wikimedia.org/wikipedia/commons/thumb/f/f0/Twemoji_1f346.svg/1200px-Twemoji_1f346.svg.png'

        roleDict['roleMessage'] = str('🍆')

        roleDict['gameRole'] = ':man_supervillain:Warchief:man_supervillain:'

        roleDict['helpInfo'] = str('🍆')
    

    class Pieck:
        roleDict = {'roleID' : 'Pieck'}

        roleDict['name'] = str('🍆🍆')

        roleDict['shortName'] = str('🍆🍆')

        roleDict['team'] = 'Warriors'

        roleDict['rumblingTeam'] = 'allianceFighter'

        roleDict['isTitan'] = True

        roleDict['emoji'] = str('🍆')

        roleDict['secondaryEmoji'] = str('🍆')

        roleDict['imageURL'] = 'https://upload.wikimedia.org/wikipedia/commons/thumb/f/f0/Twemoji_1f346.svg/1200px-Twemoji_1f346.svg.png'
        
        roleDict['secondaryImageURL'] = 'https://upload.wikimedia.org/wikipedia/commons/thumb/f/f0/Twemoji_1f346.svg/1200px-Twemoji_1f346.svg.png'

        roleDict['roleMessage'] = str('🍆')

        roleDict['gameRole'] = ':detective:Spy:detective:'

        roleDict['helpInfo'] = str('🍆')


    class Reiner:
        roleDict = {'roleID' : 'Reiner'}

        roleDict['name'] = str('🍆🍆🍆')

        roleDict['shortName'] = str('🍆🍆🍆')

        roleDict['team'] = 'Warriors'

        roleDict['rumblingTeam'] = 'allianceFighter'

        roleDict['isTitan'] = True

        roleDict['emoji'] = str('🍆')

        roleDict['secondaryEmoji'] = str('🍆')

        roleDict['imageURL'] = 'https://upload.wikimedia.org/wikipedia/commons/thumb/f/f0/Twemoji_1f346.svg/1200px-Twemoji_1f346.svg.png'
        
        roleDict['secondaryImageURL'] = 'https://upload.wikimedia.org/wikipedia/commons/thumb/f/f0/Twemoji_1f346.svg/1200px-Twemoji_1f346.svg.png'

        roleDict['roleMessage'] = str('🍆')

        roleDict['gameRole'] = ':rock:Invincible Shield:rock:'

        roleDict['helpInfo'] = str('🍆')

    class Bertholdt:
        roleDict = {'roleID' : 'Bertholdt'}

        roleDict['name'] = str('🍆🍆🍆🍆')

        roleDict['shortName'] = str('🍆🍆🍆🍆')

        roleDict['team'] = 'Warriors'

        roleDict['rumblingTeam'] = 'allianceFighter'

        roleDict['isTitan'] = True

        roleDict['emoji'] = str('🍆')

        roleDict['secondaryEmoji'] = str('🍆')

        roleDict['imageURL'] = 'https://upload.wikimedia.org/wikipedia/commons/thumb/f/f0/Twemoji_1f346.svg/1200px-Twemoji_1f346.svg.png'
        
        roleDict['secondaryImageURL'] = 'https://upload.wikimedia.org/wikipedia/commons/thumb/f/f0/Twemoji_1f346.svg/1200px-Twemoji_1f346.svg.png'

        roleDict['roleMessage'] = str('🍆')

        roleDict['gameRole'] = ':hotsprings:Sabotage Cloaker:hotsprings:'

        roleDict['helpInfo'] = str('🍆')

    class Annie:
        roleDict = {'roleID' : 'Annie'}

        roleDict['name'] = str('🍆🍆🍆🍆🍆')

        roleDict['shortName'] = str('🍆🍆🍆🍆🍆')

        roleDict['team'] = 'Warriors'

        roleDict['rumblingTeam'] = 'allianceFighter'

        roleDict['isTitan'] = True

        roleDict['emoji'] = str('🍆')

        roleDict['secondaryEmoji'] = str('🍆')

        roleDict['imageURL'] = 'https://upload.wikimedia.org/wikipedia/commons/thumb/f/f0/Twemoji_1f346.svg/1200px-Twemoji_1f346.svg.png'
        
        roleDict['secondaryImageURL'] = 'https://upload.wikimedia.org/wikipedia/commons/thumb/f/f0/Twemoji_1f346.svg/1200px-Twemoji_1f346.svg.png'

        roleDict['roleMessage'] = str('🍆')

        roleDict['gameRole'] = ':speaking_head:Screaming Titan:speaking_head:'

        roleDict['helpInfo'] = str('🍆')

    class Porco:
        roleDict = {'roleID' : 'Porco'}

        roleDict['name'] = str('🍆🍆🍆🍆🍆🍆')

        roleDict['shortName'] = str('🍆🍆🍆🍆🍆🍆')

        roleDict['team'] = 'Warriors'

        roleDict['rumblingTeam'] = 'allianceFighter'

        roleDict['isTitan'] = True

        roleDict['emoji'] = str('🍆')

        roleDict['secondaryEmoji'] = str('🍆')

        roleDict['imageURL'] = 'https://upload.wikimedia.org/wikipedia/commons/thumb/f/f0/Twemoji_1f346.svg/1200px-Twemoji_1f346.svg.png'
        
        roleDict['secondaryImageURL'] = 'https://upload.wikimedia.org/wikipedia/commons/thumb/f/f0/Twemoji_1f346.svg/1200px-Twemoji_1f346.svg.png'

        roleDict['roleMessage'] = str('🍆')

        roleDict['gameRole'] = ':shushing_face:Gag Orderer:shushing_face:'

        roleDict['helpInfo'] =  str('🍆')

    class Falco:
        roleDict = {'roleID' : 'Falco'}

        roleDict['name'] = str('🍆🍆🍆🍆🍆🍆🍆')

        roleDict['shortName'] = str('🍆🍆🍆🍆🍆🍆🍆')

        roleDict['team'] = 'Warriors'

        roleDict['rumblingTeam'] = 'allianceFighter'

        roleDict['isTitan'] = True

        roleDict['emoji'] = str('🍆')

        roleDict['secondaryEmoji'] = str('🍆')

        roleDict['imageURL'] = 'https://upload.wikimedia.org/wikipedia/commons/thumb/f/f0/Twemoji_1f346.svg/1200px-Twemoji_1f346.svg.png'
        
        roleDict['secondaryImageURL'] = 'https://upload.wikimedia.org/wikipedia/commons/thumb/f/f0/Twemoji_1f346.svg/1200px-Twemoji_1f346.svg.png'

        roleDict['roleMessage'] = str('🍆')

        roleDict['gameRole'] = ':mailbox:Mail Interceptor:mailbox:'

        roleDict['helpInfo'] =  str('🍆')

    class Warrior:
        roleDict = {'roleID' : 'Warrior'}

        roleDict['name'] = str('🍆🍆🍆🍆🍆🍆🍆🍆')

        roleDict['shortName'] = str('🍆🍆🍆🍆🍆🍆🍆🍆')

        roleDict['team'] = 'Warriors'

        roleDict['rumblingTeam'] = 'allianceBench'

        roleDict['isTitan'] = False

        roleDict['emoji'] = str('🍆')

        roleDict['secondaryEmoji'] = str('🍆')

        roleDict['imageURL'] = 'https://upload.wikimedia.org/wikipedia/commons/thumb/f/f0/Twemoji_1f346.svg/1200px-Twemoji_1f346.svg.png'

        roleDict['secondaryImageURL'] = 'https://upload.wikimedia.org/wikipedia/commons/thumb/f/f0/Twemoji_1f346.svg/1200px-Twemoji_1f346.svg.png'

        roleDict['roleMessage'] = str('🍆')

        roleDict['gameRole'] = ':crossed_swords:Default Warrior:crossed_swords:'

        roleDict['helpInfo'] = str('🍆')


    def getErenInfo(currentGame):
        return str('🍆')
    
    def getHistoriaInfo(currentGame):
        return str('🍆')
    
    def getHangeInfo(currentGame, Hange):
        return str('🍆')
    
    def getHitchInfo(currentGame, Hitch, hitchInfo):
        return str('🍆')

    
    def getWarriorInfo(currentGame, player):
        return str('🍆')
    
    def getLeviRevealMessage(Levi):
        return str('🍆')
    
    def getErwinMessage(Erwin):
        return str('🍆')
    
    def getArminDeathMessages(currentGame, currentTheme, Armin, Mikasa, Reiner):
        return str('🍆')
    
    def getLeviDeathMessages(currentGame, currentTheme, Levi, Mikasa, Reiner):
        return str('🍆')
    
    def getSashaDeathMessages(currentGame, currentTheme, Sasha, Mikasa, Reiner):
        return str('🍆')
    
    def getVictoriousWarriors(currentGame, currentTheme):
        return str('🍆')

            

