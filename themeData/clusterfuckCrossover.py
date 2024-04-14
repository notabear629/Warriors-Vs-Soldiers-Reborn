#Please pay close attention to instructions when creating new theme classes.
#When creating new themes, you should only be trying to make COSMETIC changes. To truly add more roles or functionality to the game, you will need to do a lot more than change the theme.
#However, if you do create a new role, you will have to give them a theme in any themes you are using.
import os
from dotenv import load_dotenv
import discord
from discord.ext import commands
import random

load_dotenv()
prefix = os.getenv('BOT_PREFIX')

#CHANGE THIS CLASS NAME. Your new file and your new class should NOT be named defaultGameTheme, each theme added should have different names.
class clusterfuckCrossover:
    global prefix

    #You have free reign to edit these as you please
    themeName = 'Clusterfuck Crossover Episode'
    gameName = 'Reds vs Blues'
    soldierSingle = 'Blue'
    soldierPlural = 'Blues'
    emojiSoldier = str('🟦')
    warriorSingle = 'Red'
    warriorPlural = 'Reds'
    emojiWarrior = str('🟥')
    wildcardSingle = 'Purple'
    wildcardPlural = 'Purples'
    emojiWildcard = str('🟪')
    wallSingle = 'Blue City'
    wallPlural = 'Blue Cities'
    #By Default is the same as Eren Emoji
    emojiTheme = str('❓')
    titanSingle = 'Woman'
    titanPlural = 'Women'
    emojiDead = '☠️'

    #MUST be integer emoji. No exceptions.
    emojiPaths = 1218660133945737287

    soldierThumbnail = 'https://em-content.zobj.net/source/twitter/185/large-blue-square_1f7e6.png'
    warriorThumbnail = 'https://em-content.zobj.net/source/twitter/376/large-red-square_1f7e5.png'
    wildcardThumbnail ='https://em-content.zobj.net/source/twitter/376/large-purple-square_1f7ea.png'
    deadThumbnail =  'https://em-content.zobj.net/source/twitter/53/skull-and-crossbones_2620.png'
    globalThumbnail = 'https://em-content.zobj.net/source/twitter/376/globe-showing-americas_1f30e.png'

    soldierColor = discord.Color.blue()
    warriorColor = discord.Color.red()
    wildcardColor = discord.Color.purple()
    deadColor = discord.Color.default()

    soldierDefaultMessage = 'Work with your fellow Blues to successfully complete 3 squads of defenders and protect the blue cities. Remember to conceal the true identity of L! Protecting the blue cities is not enough, after the main rounds of the game, the Reds will have one last shot of winning if they can successfully identity L!'
    warriorDefaultMessage = 'Work with your fellow Reds to destroy the Blue Cities before the Blues can build their defenses. Be mindful of how the Blues behave, even if you fail to destroy their cities, you will have one last chance of victory if you can successfully identify L!'
    wildcardDefaultMessage = 'Purples are neither Blues nor Reds, so the roles behave much differently. Shoot for your personal objective to the best of your abilities so that you may bask in the eternal glory of winning your own way!'

    #Lobby embed Aesthetics
    lobbyEmbedColor = discord.Color.blue()
    
    #Help Aesthetics
    helpEmbedColor = discord.Color.blue()

    #Rule Selection Aesthetics
    emojiBackButton = str('◀️')
    emojiRoleEnabled = str('✅')
    emojiRoleDisabled = str('❌')
    emojiRoleDefault = str('➖')
    emojiCasual = str('🤙')
    emojiRanked = str('🏅')

    #Status Embed Aesthetics
    winningColor = discord.Color.blue()
    neutralColor = discord.Color.purple()
    losingColor = discord.Color.red()
    lostColor = discord.Color.default()

    statusProgress = 'Blue Defensive Strength'
    statusWalls = 'Status of Blue Cities'
    statusExpeditions = 'Round Info'

    expeditionName = 'Defensive Mission'
    expoMembersName = 'members'

    executionName = 'Execution'

    #Note that for emojis, you may use a string of the unicode emoji for a default emoji, or an ID of a custom emoji.
    #Please be sure to put the emojis in the form of str('emoji') if you are using default unicode emojis.
    #The reason for typecasting a string as a string, is because the str() function is just an easy way to enable UTF-8 encoding to get the emoji to work.
    #We aren't really turning our input to a String, since the '' marks already make it a string, we're abusing the str() function for the encoding since it's a simple way to call it
    emojiWinMarkerOne = str('1️⃣')
    emojiWinMarkerTwo = str('2️⃣')
    emojiWinMarkerThree = str('3️⃣')
    emojiSpacer = 1205660142402535465
    emojiRoundVictoryMarker = str('✅')
    emojiVictoryMarker = str('🏁')
    emojiMariaExterior = str('🏠')
    emojiMariaInterior = str('🏠')
    emojiRoseExterior = str('🏦')
    emojiRoseInterior = str('🏦')
    emojiSinaExterior = str('🏰')
    emojiSinaInterior = str('🏰')
    emojiBrokenExterior = str('🏚️')
    emojiBrokenInterior = str('💥')
    emojiWinMarker = str('🟦')
    emojiFailMarker = str('🟥')
    emojiCurrentMarker = str('🛡️')

    #Roles embed aesthetics
    rolesEmbedColor = discord.Color.blue()

    #Players embed aesthetics
    playersEmbedColor = discord.Color.blue()
    commanderName = 'Commander'
    emojiCommanderMarker = str('👑')

    #Expedition aesthetics
    expeditionTeamMembers = 'Misson Team Members'
    expeditionTeam = 'Mission Team'
    emojiPassExpedition = str('✅')
    emojiSabotageExpedition = str('❌')
    emojiSecuredExpedition = str('🛡️')

    #Pick expo member aesthetics
    pickColor = discord.Color.blue()

    #Voting aesthetics
    emojiAcceptExpedition = str('✅')
    emojiRejectExpedition = str('❌')
    emojiAbstainExpedition = str('✖️')
    voteDMColor = discord.Color.blue()
    acceptedExpeditionColor = discord.Color.green()
    rejectedExpeditionColor = discord.Color.red()
    jeanedExpeditionColor = discord.Color.gold()
    zacharyExpeditionColor = discord.Color.red()
    mikeSmell = 'detect'
    emojiNoEren = str('✖️')

    #Expedition DM aesthetics
    expeditionDMColor = discord.Color.blue()

    #Temporary Message Aesthetics
    temporaryMessageColor = discord.Color.blue()

    #Expedition results aesthetics
    expoPassedColor = discord.Color.green()
    expoSabotagedColor = discord.Color.red()
    expoSecuredColor = discord.Color.blue()
    arminNukeColor = discord.Color.default()
    emojiNuke = 1205687713429327952
    suicideLabel = 'Become Porkchops'
    emojiSuicide = 1227894132605845515
    wallMariaBreakMessage = str('💥Blue Village has been destroyed!💥')
    wallRoseBreakMessage = str('💥Blue City has been destroyed!💥')
    wallSinaBreakMessage = str('💥Blue Metropolis has been destroyed!💥')

    #Game over Aesthetics
    wallBreakMessage = str('🟥All the Blue Cities have been destroyed!🟥\n\n🟥Reds Win!🟥')
    basementMessage = str(f'The Blues have successfully mounted a defense of their cities. The Reds still have one final chance to win! Use `{prefix}kidnap @mention` to kidnap who you think is the Coordinate for one final chance at victory!')
    kidnapTimeoutMessage = str(f'The Reds have failed to identify the Coordinate in time...\n\n🟦Blues Win!🟦')
    multikidnapTimeoutMessage = str(f'At least some of the Reds have failed to select their choice for the Coordinate in time...\n\nThey will be given a loss')
    multikidnapSuccessMessage = str('🟥The Reds have successfully chosen the Coordinate as their popular choice!🟥\n\n🟥Blues Lose!🟥')
    kidnapSuccessMessage = str('🟥The Reds have successfully identified the Coordinate!🟥\n\n🟥Reds Win!🟥')
    kidnapFailMessage = str('🟦The Reds did not manage to successfully identify the Coordinate and L\'s identity was kept secret.🟦\n\n🟦Blues Win!🟦')
    multikidnapFailMessage = str('🟦The Reds did not manage to successfully identify the Coordinate as the single most popular choice.🟦\n\n🟦Blues Win!🟦')
    noCordSuccessMessage = str('🟦The Soldiers have successfully mounted 3 defensive missions and protected their Cities.🟦\n\n🟦Soldiers Win!🟦')
    endgameCardColor = discord.Color.blue()
    emojiWinner ='🏅'
    emojiLoser = '☠️'
    emojiMVP = '🏆'

    #Webhook Message Aesthetics
    jeanMessage = f'Yes.'
    pieckMessageJean= f'I tried to flip the votes, but I am not sure if I was able to successfully do so because of that damn Yesman!'
    pieckMessageZachary= f'I tried to flip the votes, but I am not sure if I was able to successfully do so because of that damn slimeball lawyer!'
    pieckMessage = f'I flipped the votes!'
    arminMessage = f'HAHAHAHAHAHAHAHAAHAHAHAHAHA'
    leviAttackMessage = f'Now I will show you... A serious punch.'
    leviDefendMessage = f'Eh? Was there a Red? Couldn\'t tell'
    sashaMessage = f'Exactly as planned.'
    dazMessage = f'Waaaaaah! I\'m scared!'
    dazMessageFollowUp = 'The Mission has been cancelled!'
    mikasaMessage = 'That\'s not very da me da nice of you.'
    reinerMessage = 'Who wants a muffin?'
    bertholdtMessage = '*Ksch*'
    annieMessage = 'RESPECT MY AUTHORITAH, *BLAH BLAH BLAH BLAH BLAH*'
    retreatMessage = 'I\'m ordering a retreat! Pull back from the assault on the cities, and allow the Blues to assemble their defenses!'
    kennyMessage = 'Remember. No Russian.'
    kennySuicideMessage = 'Remember. I\'m Russian.'
    ymirMessage = 'The Old God smiles upon you...'
    ymirRevivalMessage = 'Death? In THIS Game? What happened to the Game of my time...'
    gabiMessage = 'HAVE A FREE .30-06 COURTESY OF TP ENTERPRISES!'
    keithMessage = '...'
    keithMessage2 = '?'
    zacharyMessage = 'Objection, your honor!'
    conflictJeanZacharyMessage = 'The fight between Chad and Saul Goodman has caused chaos! The mission will be voted on as usual.'
    petraMessage = 'Excalibur!'
    connieMessage = '⚠️Someone is lying! That mission was not safe!⚠️'
    hannesMessage = 'Pegasus. Let\'s go.'
    willyMessage = '***SSSSSS....***'
    pyxisMessage = 'Let us begin... A class trial!'
    marcoMessage = '...'
    laraMessage = '...'
    warhammerMessage = 'When I\'m done with you, you won\'t even be able to bark.'
    warhammerApologyMessage = 'Deal with it, vermin.'

    #Other role messages
    flochMessageEren = 'L is on the mission team!'
    flochMessageNoEren = 'L is not on the mission team!'

    #Timeout Messages
    timeoutCoreStart = 'You have '
    timeoutCoreEnd = ' left to'
    timeoutPick = ' pick your Defensive Mission Team!'
    timeoutVote = ' vote on the Defensive Mission Team!'
    timeoutExecution = ' vote on the Execution!'
    timeoutExpo = ' act on the Mission!'
    timeoutKidnap = ' kidnap the Coordinate!'
    timeoutRumblingFight = ' to choose who to attack!'

    # Rumbling Aesthetics
    rumblingName = 'L-Maggedon'
    emojiRumbling = str('🇱')
    emojiRumblingWallExterior = str('🇱')
    emojiRumblingWallInterior = str('💥')
    yeageristSingle = 'L-er'
    yeageristPlural = 'L-ers'
    yeageristTeam = 'L Namers'
    allianceSingle = 'Anti L Alliance Member'
    alliancePlural = 'Anti L Alliance Members'
    allianceTeam = 'Anti L Alliance'
    rumblingStatusColor = discord.Color.default()
    rumblingAltStatusColor = discord.Color.brand_red()
    rumblingStartAttachment = 'The Beginning of the End!'
    rumblingFirstMessage = 'L and Lelouch have made contact!'
    rumblingSecondMessage = 'They are charging their power!'
    rumblingThirdMessage = 'L and Lelouch have begun the L-maggedon! It can\'t be stopped anymore!'
    rumblingTimerOne = 5
    rumblingTimerTwo = 5
    rumblingTimerThree = 5
    rumblingIntroMessage = 'An entirely new game has begun! Past allegiances have broken down, and the distinction between Red and Blue is now meaningless! This battle is now fought between those who stand in favor of or oppose the L-mageddon'
    allianceFormMessage = 'The Alliance has been formed! They begin their fight to get to the L-eaders...'
    yeageristInTheWay = 'An L name Stands in the way to defend the path to the L-eaders!'
    allianceZekeClear = 'The Path to the L-eaders has been cleared! The Alliance advances towards them, in search of Lelouch...'
    ZekeInTheWay = 'The Alliance has reached Lelouch!'
    allianceZekeDefeated = 'Lelouch has been deafeated! The Alliance makes their way to L...'
    ErenInTheWay = 'The Final Battle has begun! The Alliance has reached L!'
    allianceMemberSlain = 'A member of the Alliance has been killed! The next steps up to take their place...'
    newFightPrompt = 'It is up to you to fight the Alliance!'
    genericYeageristWin = 'The L Namers have killed all of the Alliance fighters and reign victorious!'
    genericAllianceWin = 'The Alliance successfully stopped the L-Maggedon and have achieved victory!'

    standardYeageristWin = 'The L namers have successfully come together to eliminate everyone whos name doesn\'t start with an L!'
    flochDominationWin = 'The L namers have successfully come together to eliminate everyone whos name doesn\'t start with an L!'
    erenDominationWin = 'The L namers have successfully come together to eliminate everyone whos name doesn\'t start with an L!'

    standardAllianceWin = 'The Anti L-name Alliance successfully stopped the L-namers from achieving world domination! (Regular Alliance Win)'
    dominantAlliancewin = 'The Alliance completely devestated the L-Namers and dominated the battle from the start. The Alliance has decided that everyone with an L name should be immediately executed. (Dominant Alliance win)'
    #DO NOT CHANGE THIS CLASS NAME! Even if you rename the role, keep the function as Eren. Apply this advice to all roles.
    class Eren:
        #Do not change this roleID key. The code will look for "Eren" even if you re-skin it, it is important to keep all roleIDs the same.
        roleDict = {'roleID' : 'Eren'}

        #You may change 'Eren Yeager' to whatever you want his name to be.
        roleDict['name'] = 'L Lawliet'

        #You may change the shortname to whatever you want the name to be, this one is purely cosmetic.
        roleDict['shortName'] = 'L'

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
        roleDict['isTitan'] = False

        #If you are using a custom emoji, just make this the integer emoji ID you wish to use. It is important your bot is in the server that the emoji is hosted in, or they will not be able to use the emoji and your game will break.
        #If you are using a default emoji, like the crown emoji, you can just put a String ':crown:' and it will work fine. The code will check if the type is an integer or String so dont worry about mixing types.
        roleDict['emoji'] = 1227849148578136065


        #Not all roles actually use secondary emojis. If this is None, it's fine. Should be an int or emoji string like any other emoji.
        roleDict['secondaryEmoji'] = 1227849148578136065

        #If you are using a custom emoji, then make sure this is set to None. Otherwise set this to a URL of the emoji you are using. Unfortunately, Webhook images and thumbnails can only be made with urls and default emojis dont have urls.
        #Thus, if you are using a built in emoji, you will need to define this dictionary key.
        roleDict['imageURL'] = None


        #Overwhelming majority have no purpose for secondaryImgeURL. Mainly here in case you want to display secondaryEmoji as a thumbnail.
        roleDict['secondaryImageURL'] = None

        #The roleMessage is the part of the message the bot sends that gives specific information regarding the role itself when you are assigned a role.
        #You may change any role message as you wish.
        roleDict['roleMessage'] = f'You know the identity of all of the other Reds, except for Lelouch. Remember to not make the fact you know who the Reds are obvious, and do your best to protect your identity. If the Reds can successfully identify you, the Blues will lose!'

        #The gameRole is basically a way to relate what the job of this role is without making use of any theme. Remember how Entropi's bot was theme-less, this would essentially be what this role might be called in Entropi's bot.
        #You *can* change these, but I would recommend not to.
        #I would also recommend keeping the format of :emoji:Name:emoji:
        roleDict['gameRole'] = ':map:Coordinate:map:'

        #helpInfo is the message that will be summoned when you do a ~help or ~info (may or may not be implemented yet) for a particular role
        #Highly recommend changing this entirely to match your role and your lore reasoning for why your themed character fits the role
        roleDict['helpInfo'] = f'L is the Coordinate and the team captain of the Blues. This role is a mandatory role and appears in every game. L is an elite detective, and basically knows who\'s bad. He just has to prove it to the others definitively. L has the ability to see every Red in the game, with the exception of Lelouch the Warchief! However, he must do his best to not reveal himself to the other players, even if the Cities are defended, the Reds will have the opportunity to kidnap who they think the Coordinate is, and if they get it right the Blues will lose!'

    #PLEASE PLEASE FOLLOW ALL INSTRUCTIONS PRESENT FOR THE EREN ROLE FOR THE FUTURE ROLES!

    class Historia:
        roleDict = {'roleID' : 'Historia'}

        roleDict['name'] = 'Kaya'

        roleDict['shortName'] = 'Kaya'

        roleDict['team'] = 'Soldiers'

        roleDict['rumblingTeam'] = 'allianceFighter'

        roleDict['isTitan'] = True

        roleDict['emoji'] = 1228148030838931556

        roleDict['secondaryEmoji'] = None

        roleDict['imageURL'] = None

        roleDict['secondaryImageURL'] = None

        roleDict['roleMessage'] = f'You are given two names. One is L and one is Lelouch, but you don\'t know which is which! Use this information to help guide you to victory, but be careful! Don\'t expose the identity of L to the Reds!'

        roleDict['gameRole'] = ':angel:Queen:angel:'

        roleDict['helpInfo'] = 'OUR queen. Can see the names of both L and Lelouch but is unsure who is who.'

    class Hange:
        roleDict = {'roleID' : 'Hange'}

        roleDict['name'] = 'Loid Forger'

        roleDict['shortName'] = 'Loid'

        roleDict['team'] = 'Soldiers'

        roleDict['rumblingTeam'] = 'yeageristBench'

        roleDict['isTitan'] = False

        roleDict['emoji'] = 1228132346302173185

        roleDict['secondaryEmoji'] = str('📡')

        roleDict['imageURL'] = None

        roleDict['secondaryImageURL'] = None

        roleDict['roleMessage'] = f'You are a spy. As such, you have access to the latest technology in espionage. Once on an mission, you may choose someone to Wiretap. Then, throughout the rest of the game you will be alerted as to their votes and when they use a special ability! Be wary though and understand when the wiretap goes off. The wiretap goes off when commands are called, not when abilities are fired.'

        roleDict['gameRole'] = ':satellite:Wiretapper:satellite:'

        roleDict['helpInfo'] = 'Loid works as a spy. As such, he has excellent espionage equipment. Once per game, he can choose somebody in the same mission as him to wiretap. This will watch them the rest of the game, instantly pinging him when they vote or choose to use a special ability for the rest of the game. However, it is important to note WHEN the alert is made. He will NOT be alerted when an ability activates, but when a command is made to call it.'
    
    class Jean:
        roleDict = {'roleID' : 'Jean'}

        roleDict['name'] = 'Chad'

        roleDict['shortName'] = 'Chad'

        roleDict['team'] = 'Soldiers'

        roleDict['rumblingTeam'] = 'allianceFighter'

        roleDict['isTitan'] = False

        roleDict['emoji'] = 1228130461201727570

        roleDict['secondaryEmoji'] = None

        roleDict['imageURL'] = None

        roleDict['secondaryImageURL'] = None

        roleDict['roleMessage'] = 'You have the ability to force a mission proposal to pass once! But be careful! If you miscalculate, you could easily allow the Reds to get a wall!\n\n'

        roleDict['gameRole'] = ':white_check_mark:Voting Ackermann:white_check_mark:'

        roleDict['helpInfo'] = 'Chad says Yes and makes everyone else say yes. Chad has a one-time ability to guarantee that a mission proposal goes through'

    class Mike:
        roleDict = {'roleID' : 'Mike'}

        roleDict['name'] = 'James Morgan'

        roleDict['shortName'] = 'James'

        roleDict['team'] = 'Soldiers'

        roleDict['rumblingTeam'] = 'allianceFighter'

        roleDict['isTitan'] = False

        roleDict['emoji'] = 1227851055409139783

        roleDict['secondaryEmoji'] = 1227851054050443296

        roleDict['imageURL'] = None

        roleDict['secondaryImageURL'] = None

        roleDict['roleMessage'] = 'James has a desire to "blow those whining women back to the dark ages right where they belong", before voting even begins, you will know how many Women roles are on the expedition. But be very careful! Being too cavalier with the information you gain may lead the Reds to L! Be very careful with how you use the information you gain, it will not always be useful in determining who is Blue or Red.\n\n'

        roleDict['gameRole'] = ':nose:Mike:nose:'

        roleDict['helpInfo'] = 'James wants to, and I quote, "blow those whining women back to the dark ages right where they belong"! Whenever a mission team is proposed that he is on, he will be able to smell how many woman roles are on board! But be careful! You may accidentally tip off the identity of L to the Reds if you are careless and share this information!'

    class Hitch:
        roleDict = {'roleID' : 'Hitch'}

        roleDict['name'] = 'Satoru Gojo'

        roleDict['shortName'] = 'Gojo'

        roleDict['team'] = 'Soldiers'

        roleDict['rumblingTeam'] = 'allianceFighter'

        roleDict['isTitan'] = False

        roleDict['emoji'] = 1227880030139453520

        roleDict['secondaryEmoji'] = None

        roleDict['imageURL'] = None

        roleDict['secondaryImageURL'] = None

        roleDict['roleMessage'] = 'Satoru Gojo has curse energy-detecting eyes! As such, he sees everything on the battlefield. Whenever someone uses an ability, you will be alerted as to two names for who could be responsible in doing so.\n\n'

        roleDict['gameRole'] = ':mag:Ability Investigator:mag:'

        roleDict['helpInfo'] = 'Satoru Gojo has curse energy-detecting eyes! As such, he sees everything on the battlefield. Whenever someone uses an ability, he will be alerted as to two names for who could be responsible in doing so.'

    class Armin:
        roleDict = {'roleID' : 'Armin'}

        roleDict['name'] = 'Nagito Komaeda'

        roleDict['shortName'] = 'Nagito'

        roleDict['team'] = 'Soldiers'

        roleDict['rumblingTeam'] = 'allianceFighter'

        roleDict['isTitan'] = False

        roleDict['emoji'] = 1227852983799123978

        roleDict['secondaryEmoji'] = None

        roleDict['imageURL'] = None

        roleDict['secondaryImageURL'] = 'https://pbs.twimg.com/media/FDwmS5jX0AAN726.png'

        roleDict['roleMessage'] = 'You uh... Are perhaps a little too dedicated to the cause. While on an mission, as long as there\'s 2 or more cities left, you can decide to blow it all up and kill everybody else in the mission! This could be useful to get rid of Reds, but be EXTREMELY CAREFUL! An improperly played nuke can easily lose the game for the Blues.\n\n'

        roleDict['gameRole'] = ':radioactive:Nuclear Bomb:radioactive:'

        roleDict['helpInfo'] = 'Nagito is an incredibly unique Blue thanks to his uh... Alright he\'s just fucking weird. He can decide to nuke the missions! He is actually the only blue which is capable of sabotaging the mission when he decides to to blow it all up. If he does this, then every member of the mission team besides him will be killed! Therefore, use this ability VERY carefully! It is capable of eliminating Reds, but it\'s also capable of ending the game for the Blues!.'

    class Levi:
        roleDict = {'roleID' : 'Levi'}

        roleDict['name'] = 'One Punch Man'

        roleDict['shortName'] = 'Saitama'

        roleDict['team'] = 'Soldiers'

        roleDict['rumblingTeam'] = 'allianceFighter'

        roleDict['isTitan'] = False

        roleDict['emoji'] = 1227862918041964555

        roleDict['secondaryEmoji'] = 1227862805361987685

        roleDict['imageURL'] = None

        roleDict['secondaryImageURL'] = None

        roleDict['roleMessage'] = 'You are the strongest hero! While on a mission, you have two choices. `attack`, which will kill any Red that attempts to sabotage the mission. HOWEVER. Pressing this button will instantly alert the reds to your identity, regardless if you killed anybody or not. Secondly, you may press `defend`, which will prevent the mission from being sabotaged. The reds will be alerted to your identity if and only if they tried to sabotage the mission, and if they did indeed try, there will be an indicator in the game channel that says as such as well.\n\n'

        roleDict['gameRole'] = ':guard:Ackermann:guard:'

        roleDict['helpInfo'] = 'Saitama is the strongest Hero! He has an ability to secure a mission and ensure that it will pass, even if a red sabotages! Or, if defense isn\'t your style, he is also great at offense. He can also kill all Reds which attempt to sabotage an expo.'


    class Sasha:
        roleDict = {'roleID' : 'Sasha'}

        roleDict['name'] = 'Light Yagami'

        roleDict['shortName'] = 'Light'

        roleDict['team'] = 'Soldiers'

        roleDict['rumblingTeam'] = 'yeageristBench'

        roleDict['isTitan'] = False

        roleDict['emoji'] = '<:light:1227858280857206815>'

        roleDict['secondaryEmoji'] = 1227859630181584966

        roleDict['imageURL'] = 'https://i1.sndcdn.com/artworks-cqH4hiKoe6u0gLqj-MJ6mOw-t500x500.jpg'

        roleDict['secondaryImageURL'] = None

        roleDict['roleMessage'] = f'You have the ability to kill from long range with your death note! You can set a target to write in the death note `{prefix}target`, and the next time they are on a mission that you are not, you\'ll write your name in the death not and kill them! Be careful: This does NOT stop them from destroying cities, and if you Blue\'s name, they will still die!\n\n'

        roleDict['gameRole'] = ':bow_and_arrow:Sniper:bow_and_arrow:'

        roleDict['helpInfo'] = 'Light\'s death note can kill from range! He is able to choose a target, and the next time they are in a mission that goes through that he is NOT in, he will write their name in the death note, killing them! You can use this to eliminate someone you know is a Red, but be careful, this will NOT stop them from destroying a blue city!'

    class Erwin:
        roleDict = {'roleID' : 'Erwin'}

        roleDict['name'] = 'Uncle Iroh'

        roleDict['shortName'] = 'Iroh'

        roleDict['team'] = 'Soldiers'

        roleDict['rumblingTeam'] = 'allianceFighter'

        roleDict['isTitan'] = False

        roleDict['emoji'] = 1227897902265794610

        roleDict['secondaryEmoji'] = None

        roleDict['imageURL'] = None

        roleDict['secondaryImageURL'] = None

        roleDict['roleMessage'] = f'You have the ability to reveal your role once and instantly become the commander by using `{prefix}flare`! But be careful, while this will prove you are who you say you are, this will also make identifying L easier for the reds!\n\n'

        roleDict['gameRole'] = ':dizzy:True Commander:dizzy:'

        roleDict['helpInfo'] = 'Dude, everyone listens to Uncle Iroh! Thanks to this, for one time, he is able to prove his identity to everyone, and take control of being the mission commander. Use this wisely, however! Because your role being exposed makes getting to L easier!'

    class Daz:
        roleDict = {'roleID' : 'Daz'}

        roleDict['name'] = 'Luna'

        roleDict['shortName'] = 'Luna'

        roleDict['team'] = 'Soldiers'

        roleDict['rumblingTeam'] = 'yeageristBench'

        roleDict['isTitan'] = True

        roleDict['emoji'] = str('🌙')

        roleDict['secondaryEmoji'] = str('🐔')

        roleDict['imageURL'] = 'https://em-content.zobj.net/source/twitter/376/crescent-moon_1f319.png'

        roleDict['secondaryImageURL'] = None

        roleDict['roleMessage'] = f'You... Wuh... How the FUCK are you in here Luna?! Oh my god, did you SERIOUSLY manage to somehow break the laws of the universe and sneak in just because you heard Gojo would be here?... Dear lord... Because you don\'t belong here... You are absolutely shitting yourself. You have a one-time ability to cancel a mission that you rejected. To use this ability, simply select `Chicken Out` while on mission to abort and cancel the expedition!\n\n'

        roleDict['gameRole'] = ':scream:Coward:scream:'

        roleDict['helpInfo'] = f'You... Wuh... How the FUCK are you in here Luna?! Oh my god, did you SERIOUSLY manage to somehow break the laws of the universe and sneak in just because you heard Gojo would be here?... Dear lord... Because you don\'t belong here... You are absolutely shitting yourself. You have a one-time ability to cancel a mission that you rejected. To use this ability, simply select `Chicken Out` while on mission to abort and cancel the expedition!\n\n'

    class Floch:
        roleDict = {'roleID' : 'Floch'}

        roleDict['name'] = 'Blue M&M'

        roleDict['shortName'] = 'M&M'

        roleDict['team'] = 'Soldiers'

        roleDict['rumblingTeam'] = 'allianceFighter'

        roleDict['isTitan'] = False

        roleDict['emoji'] = 1228128700701216811

        roleDict['secondaryEmoji'] = None

        roleDict['imageURL'] = None

        roleDict['secondaryImageURL'] = None

        roleDict['roleMessage'] = f'When voting for an expedition, if you are inside the expedition, you will be told if L is in the expedition or not.\n\n'

        roleDict['gameRole'] = ':punch:Coordinate\'s Fist:punch:'

        roleDict['helpInfo'] = 'L constantly eats candy, and therefore the Blue M&M\'s kind. Thus, he is well acquainted with L. The Blue M&M will be alerted if L is inside an expedition with him.'

    class Mikasa:
        roleDict = {'roleID' : 'Mikasa'}

        roleDict['name'] = 'Kazuma Kiryu'

        roleDict['shortName'] = 'Kiryu'

        roleDict['team'] = 'Soldiers'

        roleDict['rumblingTeam'] = 'allianceFighter'

        roleDict['isTitan'] = False

        roleDict['emoji'] = 1227902275649802270

        roleDict['secondaryEmoji'] = str('🛡️')

        roleDict['imageURL'] = None

        roleDict['secondaryImageURL'] = None

        roleDict['roleMessage'] = f'You have the ability to act as a personal bodyguard to any **one** person on any mission (Inlcuding yourself if you choose yourself!) and prevent them from being killed. Use this ability wisely, only to protect yourself and Blues you really trust! After you successfully save someone, you will lose your ability for the rest of the game. Use `{prefix}guard` to set which player you want to guard.\n\n'

        roleDict['gameRole'] = ':fencer:Bodyguard:fencer:'

        roleDict['helpInfo'] = '**Credit to Messi (messsiii) for the idea of letting Mikasa guard on expos she\'s not on!**\nKiryu MAY be a Yakuza member, but really, he\'s not a bad guy! He has actually saved people on a few occasions. Because of this, plus his strength, he has the ability to guard players of his choice, preventing them from dying on missions.'

    class Keith:
        roleDict = {'roleID' : 'Keith'}

        roleDict['name'] = 'Ditto'

        roleDict['shortName'] = 'Ditto'

        roleDict['team'] = 'Soldiers'

        roleDict['rumblingTeam'] = 'allianceFighter'

        roleDict['isTitan'] = False

        roleDict['emoji'] = 1227855895761915914

        roleDict['secondaryEmoji'] = None

        roleDict['imageURL'] = None

        roleDict['secondaryImageURL'] = None

        roleDict['roleMessage'] = f'You are a Pokemon that can transform into anything! Use `{prefix}summon` to morph into another Blue. (This will make it so that you can choose any Blue role to morph into that isn\'t already present in the game. Your role will change upon a passed mission.)\n\n'

        roleDict['gameRole'] = ':man_teacher:Instructor:man_teacher:'

        roleDict['helpInfo'] = 'Ditto is a pokemon that can become anything! It has the ability to change its role, morphing into a different member of the Blue team. This effectively means, that the player with this role can change their role to any Blue role not already present in the game. Their role will not be changed until the next passed round\'s results are read, however.'

    class Zachary:
        roleDict = {'roleID' : 'Zachary'}

        roleDict['name'] = 'Saul Goodman'

        roleDict['shortName'] = 'Saul'

        roleDict['team'] = 'Soldiers'

        roleDict['rumblingTeam'] = 'allianceFighter'

        roleDict['isTitan'] = False

        roleDict['emoji'] = 1227891031614160936

        roleDict['secondaryEmoji'] = None

        roleDict['imageURL'] = None

        roleDict['secondaryImageURL'] = None

        roleDict['roleMessage'] = f'You are a slimy lawyer! As such you will have a one-time ability to call an objection and Veto a mission proposal, forcing it to cancel!\n\n'

        roleDict['gameRole'] = ':man_judge:Administrator:man_judge:'

        roleDict['helpInfo'] = 'Saul is a slimy lawyer! As such he will have a one-time ability to call an objection and Veto a mission proposal, forcing it to cancel!'
    
    class Petra:
        roleDict = {'roleID' : 'Petra'}

        roleDict['name'] = 'Artoria Pendragon'

        roleDict['shortName'] = 'Saber'

        roleDict['team'] = 'Soldiers'

        roleDict['rumblingTeam'] = 'allianceFighter'

        roleDict['isTitan'] = True

        roleDict['emoji'] = 1227885355731124264

        roleDict['secondaryEmoji'] = None

        roleDict['imageURL'] = None

        roleDict['secondaryImageURL'] = None

        roleDict['roleMessage'] = f'You are a powerful and righteous Servnant! As such, you have an outsized level of strength. Once per game, in an expo, you may choose one mission member to keep a watch on. If you see them attempt to destroy a City, you will be able to catch them and kill them. But unfortunately, not before they destroy the city.\n\n'

        roleDict['gameRole'] = ':axe:Executioner:axe:'

        roleDict['helpInfo'] = 'Saber is a strong blue, as expected of a member of a Servant. For those who remember the "Hunter" role from Entropi\'s game, this is that, but with death. Saber can once per game, pick a fellow mission member to watch. If that player is caught destroying the city, they will be killed. But not before they are able to destroy the city.'

    class Niccolo:
        roleDict = {'roleID' : 'Niccolo'}

        roleDict['name'] = 'Natural H. Gropius'

        roleDict['shortName'] = 'N'

        roleDict['team'] = 'Soldiers'

        roleDict['rumblingTeam'] = 'allianceFighter'

        roleDict['isTitan'] = False

        roleDict['emoji'] = 1228147047849394229

        roleDict['secondaryEmoji'] = None

        roleDict['imageURL'] = None

        roleDict['secondaryImageURL'] = None

        roleDict['roleMessage'] = f'You are DEFINITELY not a Zoroark who is DEFINITELY not creating an illusion for the Reds, making them see an additional decoy name in their teammate list...\n\n'

        roleDict['gameRole'] = ':ninja:Ex Warrior:ninja:'

        roleDict['helpInfo'] = 'N is definitely NOT a Zoroark. The reason why he creates an illusionary Red for the Reds to observe is because uh... Reasons. But he is DEFINITELY not a Zoroark (Guys i think hes a fucking zoroark). When N is in the game, the Reds get an additional Blue name in their list.'

    class Nile:
        roleDict = {'roleID' : 'Nile'}

        roleDict['name'] = 'Misa Amane'

        roleDict['shortName'] = 'Misa'

        roleDict['team'] = 'Soldiers'

        roleDict['rumblingTeam'] = 'allianceBench'

        roleDict['isTitan'] = True

        roleDict['emoji'] = 1228142679246901299

        roleDict['secondaryEmoji'] = None

        roleDict['imageURL'] = None

        roleDict['secondaryImageURL'] = None

        roleDict['roleMessage'] = f'You are fucking useless, but you have the shinigami eyes I guess... Whenever a city is broken, you will be informed of their true identities and which Red role was responsible.\n\n'

        roleDict['gameRole'] = ':man_police_officer:Police Chief:man_police_officer:'

        roleDict['helpInfo'] = f'Misa is fucking useless, but she at least has the shinigami eyes I guess... Whenever a city is broken, she will be informed of their true identities and which Red role was responsible.\n\n'

    class Connie:
        roleDict = {'roleID' : 'Connie'}

        roleDict['name'] = 'Toph Beifong'

        roleDict['shortName'] = 'Toph'

        roleDict['team'] = 'Soldiers'

        roleDict['rumblingTeam'] = 'allianceFighter'

        roleDict['isTitan'] = True

        roleDict['emoji'] = 1227887321836158996

        roleDict['secondaryEmoji'] = None

        roleDict['imageURL'] = None

        roleDict['secondaryImageURL'] = None

        roleDict['roleMessage'] = f'Toph has the incredible ability to tell if someone is lying just merely by detecting their heart rate through her feet! If you are in a mission that passes, you will be alerted that someone was lying if a Red was secretly in it.\n\n'

        roleDict['gameRole'] = ':fishing_pole_and_fish:Bait Spotter:fishing_pole_and_fish:'

        roleDict['helpInfo'] = f'Toph has the incredible ability to tell if someone is lying just merely by detecting their heart rate through her feet! If she is in a mission that passes, she will be alerted that someone was lying if a Red was secretly in it.\n\n'
    
    class Marco:
        roleDict = {'roleID' : 'Marco'}

        roleDict['name'] = 'The Pig Ymir Freed'

        roleDict['shortName'] = 'Pig Ymir Freed'

        roleDict['team'] = 'Soldiers'

        roleDict['rumblingTeam'] = 'allianceFighter'

        roleDict['isTitan'] = False

        roleDict['emoji'] = 1227893238195818586

        roleDict['secondaryEmoji'] = 1227894132605845515

        roleDict['imageURL'] = None

        roleDict['secondaryImageURL'] = None

        roleDict['roleMessage'] = f'You are... What the fuck. The Pig Ymir Freed??? Well... Okay then. Anyway. During a mission you will have a button labeled `Become Porkchops`. Click this to die. You will also have the ability to vote even after your death, clicking "abstain" will hide your vote and not blow your cover.\n\n'

        roleDict['gameRole'] = ':ghost:Phantom:ghost:'

        roleDict['helpInfo'] = '**Shoutout to Bob (bob\'s dad) and Luna (satorobin) for giving me the inspiration to add the Suicide Button!**\n...what the fuck? The Pig Ymir Freed??? Well... Okay then. Anyway. During a mission the pig will have a button labeled `Become Porkchops`. They can click this to die. They will also have the ability to vote even after their death, just like that DAMN pig was relevant for thousands of years after its death, clicking "abstain" will hide porkchop\'s vote and not blow their cover.'

    class Marlowe:
        roleDict = {'roleID' : 'Marlowe'}

        roleDict['name'] = 'Kyoko Kirigiri'

        roleDict['shortName'] = 'Kyoko'

        roleDict['team'] = 'Soldiers'

        roleDict['rumblingTeam'] = 'allianceFighter'

        roleDict['isTitan'] = True

        roleDict['emoji'] = 1227864127968641086

        roleDict['secondaryEmoji'] = None

        roleDict['imageURL'] = None

        roleDict['secondaryImageURL'] = None

        roleDict['roleMessage'] = f'You are the ultimate detective! As such, when players die, you will be able to perform basic searches of the corpses and identify their roles.\n\n'

        roleDict['gameRole'] = ':police_car:Detective:police_car:'

        roleDict['helpInfo'] = 'Kyoko is the ultimate detective. Thanks to this, she has crime scene investigatory skills. When players die, she will know their roles.'
    
    class Hannes:
        roleDict = {'roleID' : 'Hannes'}

        roleDict['name'] = 'Medusa'

        roleDict['shortName'] = 'Rider'

        roleDict['team'] = 'Soldiers'

        roleDict['rumblingTeam'] = 'allianceFighter'

        roleDict['isTitan'] = True

        roleDict['emoji'] = 1227889190276960286

        roleDict['secondaryEmoji'] = None

        roleDict['imageURL'] = None

        roleDict['secondaryImageURL'] = None

        roleDict['roleMessage'] = f'Medusa is a rider-class servant. Once on a mission, she can call Pegasus and instantly escape the mission, no longer being part of it.\n\n'

        roleDict['gameRole'] = ':rocket:Escape Pod:rocket:'

        roleDict['helpInfo'] = 'Medusa is a rider-class servant. Once on a mission, she can call Pegasus and instantly escape the mission, no longer being part of it.'
    
    class Pyxis:
        roleDict = {'roleID' : 'Pyxis'}

        roleDict['name'] = 'Monokuma'

        roleDict['shortName'] = 'Monokuma'

        roleDict['team'] = 'Soldiers'

        roleDict['rumblingTeam'] = 'allianceFighter'

        roleDict['isTitan'] = False

        roleDict['emoji'] = 1227865203404967996

        roleDict['secondaryEmoji'] = 1227865495890559028

        roleDict['imageURL'] = None

        roleDict['secondaryImageURL'] = None

        roleDict['roleMessage'] = f'You are the judge over the class trials! Use `{prefix}trial` to bring forth a list of the players that have been on a mission and start a trial against one of them during the command phase of the game. After you do this, a vote will be called on their execution.\n\n'

        roleDict['gameRole'] = ':knot:Hangman:knot:'

        roleDict['helpInfo'] = 'Monokuma is the judge over the class trials! He can put one player who has been on an expedition on trial for a possible execution, but he himself will not be the final judge. The players will serve as a jury and vote, if the vote passes, the player will be executed.'

    class Samuel:
        roleDict = {'roleID' : 'Samuel'}

        roleDict['name'] = 'Denji'

        roleDict['shortName'] = 'Denji'

        roleDict['team'] = 'Soldiers'

        roleDict['rumblingTeam'] = 'allianceFighter'

        roleDict['isTitan'] = False

        roleDict['emoji'] = 1227882827991875585

        roleDict['secondaryEmoji'] = str('🤡')

        roleDict['imageURL'] = None

        roleDict['secondaryImageURL'] = None

        roleDict['roleMessage'] = f'You are very strong!... But if someone asks you to use your brain... You MAY be cooked. Once after round 1, you can click the `Clownery` button to always make the wrong choice for the expo.\n\n'

        roleDict['gameRole'] = ':clown:Clown:clown:'

        roleDict['helpInfo'] = 'Denji is very strong!... But... If you ask him to use his brains and not his brawn... You MAY be cooked. After round 1, he has a one-time ability to choose a voting option that will accept if there is a Red inside the mission and reject otherwise.'
    
    
    class Soldier:
        roleDict = {'roleID' : 'Soldier'}

        roleDict['name'] = 'Crewmate'

        roleDict['shortName'] = 'Crewmate'

        roleDict['team'] = 'Soldiers'

        roleDict['rumblingTeam'] = 'allianceBench'

        roleDict['isTitan'] = False

        roleDict['emoji'] = 1228148917007286343

        roleDict['secondaryEmoji'] = None

        roleDict['imageURL'] = None

        roleDict['secondaryImageURL'] = None

        roleDict['roleMessage'] = f'You are an average Blue. You do not possess any special abilities or supplemental information.'

        roleDict['gameRole'] = ':shield:Default Soldier:shield:'

        roleDict['helpInfo'] = f'The Crewmate role is merely just a default Blue, they essentially have no role.'

    class Zeke:
        roleDict = {'roleID' : 'Zeke'}

        roleDict['name'] = 'Lelouch Lamperogue'

        roleDict['shortName'] = 'Lelouch'

        roleDict['team'] = 'Warriors'

        roleDict['rumblingTeam'] = 'yeageristFighter'

        roleDict['isTitan'] = False

        roleDict['emoji'] = 1228151630474510386

        roleDict['secondaryEmoji'] = 1228151630474510386

        roleDict['imageURL'] = None

        roleDict['secondaryImageURL'] = None

        roleDict['roleMessage'] = f'L does not see you as a Red, in fact, you are the only Red to be hidden in this matter. Be mindful of this when deciding if you want to be flagrant about your identity as a Red or not. You may also use `{prefix}retreat` to end the missions early and cut straight to the kidnap phase, for that niche situation where it makes more sense just to get to kidnapping.'

        roleDict['gameRole'] = ':man_supervillain:Warchief:man_supervillain:'

        roleDict['helpInfo'] = f'Lelouch is the warchief and team captain for the Reds! He will not be seen as a Red by L, and is a mandatory role that appears every game. He is more important than just being invisible to the Coordinate, however. He alone has the ability to end the mission rounds early and cut to the kidnapping early if the situation looks grim!'  
    

    class Pieck:
        roleDict = {'roleID' : 'Pieck'}

        roleDict['name'] = 'Yor Forger'

        roleDict['shortName'] = 'Yor'

        roleDict['team'] = 'Warriors'

        roleDict['rumblingTeam'] = 'allianceFighter'

        roleDict['isTitan'] = True

        roleDict['emoji'] = 1228153776414789643

        roleDict['secondaryEmoji'] = 1228153776414789643

        roleDict['imageURL'] = None
        
        roleDict['secondaryImageURL'] = None

        roleDict['roleMessage'] = f'Yor Forges the votes! Therefore, she has a one-time ability to choose to flip the results of the votes of the mission proposals!\n\n'

        roleDict['gameRole'] = ':detective:Spy:detective:'

        roleDict['helpInfo'] = 'Yor Forges the votes! Therefore, she has a one-time ability to choose to flip the results of the votes of the mission proposals!'


    class Reiner:
        roleDict = {'roleID' : 'Reiner'}

        roleDict['name'] = 'Suicidal Muffin'

        roleDict['shortName'] = 'Muffin'

        roleDict['team'] = 'Warriors'

        roleDict['rumblingTeam'] = 'allianceFighter'

        roleDict['isTitan'] = False

        roleDict['emoji'] = 1228820833468813313

        roleDict['secondaryEmoji'] = 1228820833468813313

        roleDict['imageURL'] = None
        
        roleDict['secondaryImageURL'] = None

        roleDict['roleMessage'] = 'You are a Suicidal Muffin. But no matter what you do, you can\'t seem to die! You cannot be killed.\n\n'

        roleDict['gameRole'] = ':rock:Invincible Shield:rock:'

        roleDict['helpInfo'] = 'The Suicidal Muffin wants to be eaten and be killed. However... They can never seem to manage to die. The Suicidal Muffin cannot be killed regardless of circumstance.'

    class Bertholdt:
        roleDict = {'roleID' : 'Bertholdt'}

        roleDict['name'] = 'Shiro'

        roleDict['shortName'] = 'Shiro'

        roleDict['team'] = 'Warriors'

        roleDict['rumblingTeam'] = 'allianceFighter'

        roleDict['isTitan'] = True

        roleDict['emoji'] = 1228830057783496755

        roleDict['secondaryEmoji'] = 1228831367714836480

        roleDict['imageURL'] = None
        
        roleDict['secondaryImageURL'] = None

        roleDict['roleMessage'] = 'You have the ability to go absolutely sicko Wretched Egg mode, leaving a rampage of a crime scene behind disastrous enough to make the Blues unable to tell how many Reds sabotaged their mission. Select `Cloak` on a mission to sabotage and choose this option!\n\n'

        roleDict['gameRole'] = ':hotsprings:Sabotage Cloaker:hotsprings:'

        roleDict['helpInfo'] = 'Shiro has the ability to choose to go full Wretched Egg and snap. Upon doing this, the havoc she creates makes it so it is too hard for the Blues to tell how many Reds sabotaged the mission! She can choose an option to cloak how many Reds sabotaged while on a mission.'

    class Annie:
        roleDict = {'roleID' : 'Annie'}

        roleDict['name'] = 'Eric Cartman'

        roleDict['shortName'] = 'Eric'

        roleDict['team'] = 'Warriors'

        roleDict['rumblingTeam'] = 'allianceFighter'

        roleDict['isTitan'] = False

        roleDict['emoji'] = 1228156275020271687

        roleDict['secondaryEmoji'] = 1228156275020271687

        roleDict['imageURL'] = None
        
        roleDict['secondaryImageURL'] = None

        roleDict['roleMessage'] = f'Your yapping gives you a unique screaming ability! In order to use it, use the `{prefix}scream` command to send a message to all of your Red comrades upon the next time results are read! When you use this ability, an alert will be shown in the home channel.\n\n'

        roleDict['gameRole'] = ':speaking_head:Screaming Titan:speaking_head:'

        roleDict['helpInfo'] = 'Eric Cartman is a YAPPER. He has the ability to use his yapping to send a secret message along to his fellow Reds'

    class Porco:
        roleDict = {'roleID' : 'Porco'}

        roleDict['name'] = 'The Joker'

        roleDict['shortName'] = 'Joker'

        roleDict['team'] = 'Warriors'

        roleDict['rumblingTeam'] = 'allianceFighter'

        roleDict['isTitan'] = False

        roleDict['emoji'] = 1228159685253795930

        roleDict['secondaryEmoji'] = None

        roleDict['imageURL'] = None
        
        roleDict['secondaryImageURL'] = None

        roleDict['roleMessage'] = f'Show the Blues how you got those scars! Use `{prefix}gag` to open the menu to choose to gag a player. When a player is gagged, they are not able to speak and their commander turn gets skipped! However, there is an important exception! A flared Iroh is ungaggable.\n\n'

        roleDict['gameRole'] = ':shushing_face:Gag Orderer:shushing_face:'

        roleDict['helpInfo'] =  'You wanna know how I got these scars? Well, I\'ll show you, by giving them to you! The Joker is able to gag somebody for a round, the pain of learning why he has the scars will prevent them from speaking for a round.'

    class Falco:
        roleDict = {'roleID' : 'Falco'}

        roleDict['name'] = 'Violet Evergarden'

        roleDict['shortName'] = 'Violet'

        roleDict['team'] = 'Warriors'

        roleDict['rumblingTeam'] = 'allianceFighter'

        roleDict['isTitan'] = True

        roleDict['emoji'] = 1228160871054835712

        roleDict['secondaryEmoji'] = None

        roleDict['imageURL'] = None
        
        roleDict['secondaryImageURL'] = None

        roleDict['roleMessage'] = 'You often find yourself around letters, so you will have the ability to do a special kind of a vote on the mission ONCE. This vote works such that, if the mission would pass if you accepted it, it will make you accept, otherwise, you will reject. This can be a game winning play if used tactically!\n\n'

        roleDict['gameRole'] = ':mailbox:Mail Interceptor:mailbox:'

        roleDict['helpInfo'] =  'Violet Evergarden spends a lot of time gathering mail and writing letters. Because of this, she has the ability to intercept the votes, reading if the mission proposal will pass or not, and making her decision based off that. She has a one-time ability vote that will make her accept if the mission would pass, and reject otherwise.'

    class Magath:
        roleDict = {'roleID' : 'Magath'}

        roleDict['name'] = 'Ryuk'

        roleDict['shortName'] = 'Ryuk'

        roleDict['team'] = 'Warriors'

        roleDict['rumblingTeam'] = 'allianceFighter'

        roleDict['isTitan'] = False

        roleDict['emoji'] = 1228832805040033803

        roleDict['secondaryEmoji'] = None

        roleDict['imageURL'] = None
        
        roleDict['secondaryImageURL'] = None

        roleDict['roleMessage'] = 'You are a Shinigami! As such, you have the Shinigami eyes, and therefore know your comrade\'s true identities. You will have knowledge over who has what Red roles. In addition to this, the other Reds will also know you are Ryuk. Use this advanced knowledge to expertly coordinate attacks against the Blues!\n\n'

        roleDict['gameRole'] = ':military_helmet:Commander:military_helmet:'

        roleDict['helpInfo'] =  'Ryuk is fairly non-interventionist, so does not particularly have a crazy special ability to turn the tide of battle for the Reds. However, Ryuk has the Shinigami eyes, so he knows all of the Roles of his Red comrades. In addition, they all know that he is Ryuk.'

    class Gabi:
        roleDict = {'roleID' : 'Gabi'}

        roleDict['name'] = 'Trevor Phillips'

        roleDict['shortName'] = 'Trevor'

        roleDict['team'] = 'Warriors'

        roleDict['rumblingTeam'] = 'allianceFighter'

        roleDict['isTitan'] = False

        roleDict['emoji'] = 1228162999064461362

        roleDict['secondaryEmoji'] = str('🎯')

        roleDict['imageURL'] = None
        
        roleDict['secondaryImageURL'] = None

        roleDict['roleMessage'] = f'You are a crazy SOB! Use `{prefix}fire` to open a menu to select a player to target. At the end of any mission, regardless if they are on the mission or not, you will fire a shot that wounds that player. A wounded player will not be able to be picked for the mission for a round.\n\n'

        roleDict['gameRole'] = ':gun:Marksman:gun:'

        roleDict['helpInfo'] =  f'Trevor Phillips is freaking crazy man. He can choose a player to shoot upon the reading of the results, prohibiting them from being picked for the mission for a round.'

    class Willy:
        roleDict = {'roleID' : 'Willy'}

        roleDict['name'] = 'Creeper'

        roleDict['shortName'] = 'Creeper'

        roleDict['team'] = 'Warriors'

        roleDict['rumblingTeam'] = 'allianceFighter'

        roleDict['isTitan'] = False

        roleDict['emoji'] = 1228834078711611493

        roleDict['secondaryEmoji'] = 1228834078711611493

        roleDict['imageURL'] = None
        
        roleDict['secondaryImageURL'] = None

        roleDict['roleMessage'] = f'You are a Creeper! Creepers have one job in life. To blow themselves up to cause hell for somebody else! While on a mission, you can choose to sacrifice yourself to kill another player on the mission.\n\n'

        roleDict['gameRole'] = ':bomb:Suicide Bomber:bomb:'

        roleDict['helpInfo'] =  f'The Creeper, as we all know, explodes itself to make your life hell. While on a mission, it has the option to explode itself to try to kill another player on mission.'
    
    class Yelena:
        roleDict = {'roleID' : 'Yelena'}

        roleDict['name'] = 'Azula'

        roleDict['shortName'] = 'Azula'

        roleDict['team'] = 'Warriors'

        roleDict['rumblingTeam'] = 'allianceFighter'

        roleDict['isTitan'] = True

        roleDict['emoji'] = 1228167720546078731

        roleDict['secondaryEmoji'] = None

        roleDict['imageURL'] = None
        
        roleDict['secondaryImageURL'] = None

        roleDict['roleMessage'] = f'Azula always lies! As such, you have tampered with the voting system ahead of time. Once per game, you will be able to choose to choose a player\'s vote to steal when voting on a mission. When you select this option, you will vote whatever they did, and they will vote the opposite. If you use this ability on someone who rejected, they will now accept, but you will reject in turn.\n\n'

        roleDict['gameRole'] = ':moneybag:Vote Thief:moneybag:'

        roleDict['helpInfo'] =  f'**Credit to Space (JustAboutEnoughSpace) for this role!**\n\nAzula always lies! Once per game, she can steal the vote of another player, switching that player\'s vote with the opposite of which they voted'

    class Lara:
        roleDict = {'roleID' : 'Lara'}

        roleDict['name'] = 'Makima'

        roleDict['shortName'] = 'Makima'

        roleDict['team'] = 'Warriors'

        roleDict['rumblingTeam'] = 'allianceFighter'

        roleDict['isTitan'] = True

        roleDict['emoji'] = 1228808367573831881

        roleDict['secondaryEmoji'] = None

        roleDict['imageURL'] = None
        
        roleDict['secondaryImageURL'] = None

        roleDict['roleMessage'] = f'You are the controller of the Control Devil! In order to activate it so you can use it, you need to get on a mission so that you can use the `Transform` button which will sabotage the mission and transform you into the Control Devil!'

        roleDict['gameRole'] = ':key:Armory Owner:key:'

        roleDict['helpInfo'] =  f'Makima is the controller of the Control Devil. Pretty much her only role is to get on a mission so that she can become the Control Devil'


    class Warhammer:
        roleDict = {'roleID' : 'Warhammer'}

        roleDict['name'] = 'The Control Devil'

        roleDict['shortName'] = 'Control Devil'

        roleDict['team'] = 'Warriors'

        roleDict['rumblingTeam'] = 'allianceFighter'

        roleDict['isTitan'] = True

        roleDict['emoji'] = 1228811083863687199

        roleDict['secondaryEmoji'] = 1228811083863687199

        roleDict['imageURL'] = None
        
        roleDict['secondaryImageURL'] = None

        roleDict['roleMessage'] = f'You are the Control Devil! Once, you have the ability to utilize a Blue\'s ability. Chad, Loid, Kiryu, and Ditto are forbidden, and all killer abilities can only kill your fellow Reds. In addition to the voting and mission abilities, you have access to\n`{prefix}target` to use Light\'s ability \n`{prefix}trial` to use Monokuma\'s ability\n`{prefix}flare` to use Iroh\'s ability\n\n'

        roleDict['gameRole'] = ':headstone:Weapons Expert:headstone:'

        roleDict['helpInfo'] =  f'The Control Devil has the ability to control other Devils. This player has the chance to use any single Blue\'s special ability, vote, or mission act once. There are exceptions of Chad, Loid, Kiryu, and Ditto. Any killing Blue abilities it uses can only kill Reds. Loid and Gojo will be alerted as to their true nature if their ability usage would notify them.'    
    
    class Warrior:
        roleDict = {'roleID' : 'Warrior'}

        roleDict['name'] = 'Imposter'

        roleDict['shortName'] = 'Imposter'

        roleDict['team'] = 'Warriors'

        roleDict['rumblingTeam'] = 'allianceBench'

        roleDict['isTitan'] = False

        roleDict['emoji'] = 1228836353941442620

        roleDict['secondaryEmoji'] = None

        roleDict['imageURL'] = None

        roleDict['secondaryImageURL'] = None

        roleDict['roleMessage'] = f'You are an average Red. You do not possess any special abilities to aid you in destroying Blue cities.'

        roleDict['gameRole'] = ':crossed_swords:Default Warrior:crossed_swords:'

        roleDict['helpInfo'] = f'The Imposter role is merely just a default Red, they essentially have no role.'

    class Kenny:
        roleDict = {'roleID' : 'Kenny'}

        roleDict['name'] = 'Vladimir Makarov'

        roleDict['shortName'] = 'Makarov'

        roleDict['team'] = 'Wildcards'

        roleDict['rumblingTeam'] = 'allianceFighter'

        roleDict['isTitan'] = False

        roleDict['emoji'] = 1228837478140608623

        roleDict['secondaryEmoji'] = 1228837478140608623

        roleDict['imageURL'] = None

        roleDict['secondaryImageURL'] = None

        roleDict['roleMessage'] = f'You are a mass murderer! You do not give a singular shit about the status of the blue cities. Your objective is simple. Get on missions. Murder at least 2 players. If you can achieve this, you win.\n\n'

        roleDict['gameRole'] = ':knife:Serial Killer:knife:'

        roleDict['helpInfo'] = f'Vladimir Makarov is a mass murdering terrorist. He does not care if the walls break or not, he wins through one glorious way. Murder. When he gets on a mission, he has the ability to kill another player on the mission. If he can kill at least 2 people in a match, he wins.'

    class Frecklemir:
        roleDict = {'roleID' : 'Frecklemir'}

        roleDict['name'] = 'Zuko'

        roleDict['shortName'] = 'Zuko'

        roleDict['team'] = 'Wildcards'

        roleDict['rumblingTeam'] = 'allianceFighter'

        roleDict['isTitan'] = False

        roleDict['emoji'] = 1228852324852699188

        roleDict['secondaryEmoji'] = None

        roleDict['imageURL'] = None

        roleDict['secondaryImageURL'] = None

        roleDict['roleMessage'] = f'You have not yet decided what team you want to be a part of! In order to pick a team, you need to get into a mission. If the mission you are on passes, you will join the Blues. If it breaks, you will join the Reds. You cannot win unless you are on a team, so do your best to pick a side!\n\n'

        roleDict['gameRole'] = ':snake:Disloyal Fighter:snake:'

        roleDict['helpInfo'] = f'Zuko starts conflicted, and does not know if he wants to join the Blues or Reds. As such, he begins on neither team. The first time he gets on a mission, he will join a team that depends on how the mission went. If the mission passes, then he joins the Blues. If it breaks, he joins the Reds.'

    class PureTitan:
        roleDict = {'roleID' : 'PureTitan'}

        roleDict['name'] = 'Sokka'

        roleDict['shortName'] = 'Sokka'

        roleDict['team'] = 'Wildcards'

        roleDict['rumblingTeam'] = 'allianceFighter'

        roleDict['isTitan'] = False

        roleDict['emoji'] = 1228853328046329876

        roleDict['secondaryEmoji'] = None

        roleDict['imageURL'] = None

        roleDict['secondaryImageURL'] = None

        roleDict['roleMessage'] = f'Sokka is pretending to be a woman for uh... Reasons. When you get in a mission with one, you will become them, and go in disguise as them, and they will become a Sokka! Whoever ends as Sokka, loses. IDK man, this is the best I can work with to make a pure titan role after decididing to make James a woman detector. Sue me.\n\n'

        roleDict['gameRole'] = ':potato:Hot Potato:potato:'

        roleDict['helpInfo'] = f'Sokka is pretending to be a woman for uh... Reasons. When you get in a mission with one, you will become them, and go in disguise as them, and they will become a Sokka! Whoever ends as Sokka, loses. IDK man, this is the best I can work with to make a pure titan role after decididing to make James a woman detector. Sue me.'

    class Ymir:
        roleDict = {'roleID' : 'Ymir'}

        roleDict['name'] = 'Game Master'

        roleDict['shortName'] = 'Game Master'

        roleDict['team'] = 'Wildcards'

        roleDict['rumblingTeam'] = 'allianceBench'

        roleDict['isTitan'] = False

        roleDict['emoji'] = 1228858987567644673

        roleDict['secondaryEmoji'] = None

        roleDict['imageURL'] = None

        roleDict['secondaryImageURL'] = None

        roleDict['roleMessage'] = f'The Old God...\n\nYou are the Game Master. You cannot directly participate in missions. There is someone out there you are assisting... But you aren\'t sure who. Or what decisions they will make. Use `{prefix}paths` to utilize PATHS to open the menu with your powers to assist the player you are guiding. If they win, you win. Your fates are tied. Guide them to victory.'

        roleDict['gameRole'] = ':milky_way:Pathfinder:milky_way:'

        roleDict['helpInfo'] = f'The Old God. We thought it was dead. We were wrong. Game Master is unable to participate in expeditions. A random person that it does not know the name of will be chosen, its objective is to guide that person to victory. It can use PATHS to communicate with them, revive a dead player, or grant somebody its blessing. It must guide it\'s chosen person to victory, at any cost.'

    def getErenInfo(currentGame):
        erenInfo = 'The Reds are:\n'
        warriorList = currentGame.warriors.copy()
        warriorList = random.sample(warriorList, len(warriorList))
        for warrior in warriorList:
            if warrior.role.id != 'Zeke':
                erenInfo += f'**{warrior.user.name}**'
                if warriorList.index(warrior) != len(warriorList) -1:
                    erenInfo += '\n'
        return erenInfo
    
    def getHistoriaInfo(currentGame):
        historiaInfo = 'L and Lelouch are:\n'
        yeagerBros = []
        for player in currentGame.players:
            if player.role.id == 'Zeke' or player.role.id == 'Eren':
                yeagerBros.append(player.user.name)
        yeagerBros = random.sample(yeagerBros, 2)
        historiaInfo += f'**{yeagerBros[0]}**\n**{yeagerBros[1]}**'
        return historiaInfo
    
    def getHitchInfo(currentGame, Hitch, hitchInfo):
        hitchMessage = ''
        for role, player in hitchInfo.items():
            Hitch.stats.hitchDiscover()
            altPlayers = currentGame.livingPlayers.copy()
            if Hitch in altPlayers:
                altPlayers.remove(Hitch)
            if player in altPlayers:
                altPlayers.remove(player)
            if len(altPlayers) <= 0:
                hitchMessage += f'I have discovered that the identity of **{player.role.name}** must be **{player.user.name}**!\n\n'
            else:
                altPlayer = random.choice(altPlayers)
                twoPossibilities = random.sample([player, altPlayer], 2)
                hitchMessage += f'I have discovered that the identity of **{player.role.name}** must either be **{twoPossibilities[0].user.name}**  or **{twoPossibilities[1].user.name}**!\n\n'
        return hitchMessage

    
    def getWarriorInfo(currentGame, player):
        warriorInfo = 'Your fellow Reds are:\n'
        warriorList = currentGame.warriors.copy()
        if currentGame.niccoloDecoy != None:
            warriorList.append(currentGame.niccoloDecoy)
        warriorList = random.sample(warriorList, len(warriorList))
        for warrior in warriorList:
            if player.user.name != warrior.user.name:
                if player.role.id != 'Magath':
                    if warrior.role.id != 'Magath':
                        warriorInfo += f'**{warrior.user.name}**'
                    else:
                        warriorInfo += f'**{warrior.role.emoji}{warrior.user.name}{warrior.role.emoji}**'
                else:
                    if warrior in currentGame.warriors:
                        warriorInfo += f'**{warrior.role.emoji}{warrior.user.name}{warrior.role.emoji}**'
                    else:
                        warriorInfo += f'**{warrior.user.name}**'
                if warriorList.index(warrior) != len(warriorList) - 1:
                    warriorInfo += '\n'
        if currentGame.niccoloDecoy != None:
            warriorInfo += '\n❗This list was tampered with❗'
        return warriorInfo
    
    def getLeviRevealMessage(Levi):
        return f'The identity of **One Punch Man (Saitama)** has been revealed to be **{Levi.user.name}**!'
    
    def getErwinMessage(Erwin):
        return f'My name is {Erwin.user.mention}. Why don\'t we all gather for a nice cup of tea?'
    
    def getArminDeathMessages(currentGame, currentTheme, Armin, Mikasa, Reiner):
        arminDeathMessages = ''
        for killedPlayer, causeOfDeath in Armin.killed.items():
            if causeOfDeath == 'Armin':
                arminDeathMessages += f'**{killedPlayer.user.name}** perished in the Blast!\n'
                if killedPlayer in currentGame.soldiers:
                    arminDeathMessages += f'They were a {currentTheme.emojiSoldier}**{currentTheme.soldierSingle}**{currentTheme.emojiSoldier}!\n\n'
                elif killedPlayer in currentGame.warriors:
                    arminDeathMessages += f'They were a {currentTheme.emojiWarrior}**{currentTheme.warriorSingle}**{currentTheme.emojiWarrior}!\n\n'
                elif killedPlayer in currentGame.wildcards:
                    arminDeathMessages += f'They were a {currentTheme.emojiWildcard}**{currentTheme.wildcardSingle}**{currentTheme.emojiWildcard}!\n\n'
        if type(currentGame.mikasaGuarded) == dict:
            for key, value in currentGame.mikasaGuarded.items():
                if value == 'Armin':
                    arminDeathMessages += f'{Mikasa.role.emoji} Kiryu saved **{key.user.name}** from the Blast!{Mikasa.role.emoji}\n\n'
        if type(currentGame.currentExpo.reinerBlocked) == dict:
            for key, value in currentGame.currentExpo.reinerBlocked.items():
                if value == 'Armin':
                    arminDeathMessages += f'{Reiner.role.secondaryEmoji}**{key.user.name}** Survived the Blast!{Reiner.role.secondaryEmoji}\n\n'
        return arminDeathMessages
    
    def getLeviDeathMessages(currentGame, currentTheme, Levi, Mikasa, Reiner):
        leviDeathMessages = ''
        for killedPlayer, causeOfDeath in Levi.killed.items():
            if causeOfDeath == 'Levi':
                leviDeathMessages += f'**{killedPlayer.user.name}** was serious punched by Saitama!\n'
                if killedPlayer in currentGame.soldiers:
                    leviDeathMessages += f'They were a {currentTheme.emojiSoldier}**{currentTheme.soldierSingle}**{currentTheme.emojiSoldier}!\n\n'
                elif killedPlayer in currentGame.warriors:
                    leviDeathMessages += f'They were a {currentTheme.emojiWarrior}**{currentTheme.warriorSingle}**{currentTheme.emojiWarrior}!\n\n'
                elif killedPlayer in currentGame.wildcards:
                    leviDeathMessages += f'They were a {currentTheme.emojiWildcard}**{currentTheme.wildcardSingle}**{currentTheme.emojiWildcard}!\n\n'
        if type(currentGame.mikasaGuarded) == dict:
            for key, value in currentGame.mikasaGuarded.items():
                if value == 'Levi':
                    leviDeathMessages += f'**{key.user.name}** Was a target of a serious punch!\n{Mikasa.role.emoji}But was Kiryu got them out of the way first!{Mikasa.role.emoji}\n\n'
        if type(currentGame.currentExpo.reinerBlocked) == dict:
            for key, value in currentGame.currentExpo.reinerBlocked.items():
                if value == 'Levi':
                    leviDeathMessages += f'{Reiner.role.secondaryEmoji}**{key.user.name}**\'s Muffiny Goodness made Saitama not punch them!{Reiner.role.secondaryEmoji}\n\n'
        return leviDeathMessages
    
    def getPetraDeathMessages(currentGame, currentTheme, Petra, Mikasa, Reiner):
        petraDeathMessages = ''
        for killedPlayer, causeOfDeath in Petra.killed.items():
            if causeOfDeath == 'Petra':
                petraDeathMessages += f'**{killedPlayer.user.name}** was slain by Saber!\n'
                if killedPlayer in currentGame.soldiers:
                    petraDeathMessages += f'They were a {currentTheme.emojiSoldier}**{currentTheme.soldierSingle}**{currentTheme.emojiSoldier}!\n\n'
                elif killedPlayer in currentGame.warriors:
                    petraDeathMessages += f'They were a {currentTheme.emojiWarrior}**{currentTheme.warriorSingle}**{currentTheme.emojiWarrior}!\n\n'
                elif killedPlayer in currentGame.wildcards:
                    petraDeathMessages += f'They were a {currentTheme.emojiWildcard}**{currentTheme.wildcardSingle}**{currentTheme.emojiWildcard}!\n\n'
        if type(currentGame.mikasaGuarded) == dict:
            for key, value in currentGame.mikasaGuarded.items():
                if value == 'Petra':
                    petraDeathMessages += f'**{key.user.name}** was attacked by Saber!\n{Mikasa.role.emoji}But was protected by Kiryu!{Mikasa.role.emoji}\n\n'
        if type(currentGame.currentExpo.reinerBlocked) == dict:
            for key, value in currentGame.currentExpo.reinerBlocked.items():
                if value == 'Petra':
                    petraDeathMessages += f'{Reiner.role.secondaryEmoji}**{key.user.name}** distracted Saber with the smell of Muffiny deliciousness, causing her to miss!{Reiner.role.secondaryEmoji}\n\n'
        return petraDeathMessages
    
    def getSashaDeathMessages(currentGame, currentTheme, Sasha, Mikasa, Reiner, realSasha=None):
        if realSasha == None:
            secEmo = Sasha.role.secondaryEmoji
        else:
            secEmo = realSasha.role.secondaryEmoji
        sashaDeathMessages = ''
        for killedPlayer, causeOfDeath in Sasha.killed.items():
            if causeOfDeath == 'Sasha':
                sashaDeathMessages += f'{secEmo}**{killedPlayer.user.name}** has died of a Heart Attack!{secEmo}\n'
                if killedPlayer in currentGame.soldiers:
                    sashaDeathMessages += f'They were a {currentTheme.emojiSoldier}**{currentTheme.soldierSingle}**{currentTheme.emojiSoldier}!\n\n'
                elif killedPlayer in currentGame.warriors:
                    sashaDeathMessages += f'They were a {currentTheme.emojiWarrior}**{currentTheme.warriorSingle}**{currentTheme.emojiWarrior}!\n\n'
                elif killedPlayer in currentGame.wildcards:
                    sashaDeathMessages += f'They were a {currentTheme.emojiWildcard}**{currentTheme.wildcardSingle}**{currentTheme.emojiWildcard}!\n\n'
        if type(currentGame.mikasaGuarded) == dict:
            for key, value in currentGame.mikasaGuarded.items():
                if value == 'Sasha':
                    sashaDeathMessages += f'{Mikasa.role.emoji}Kiryu calmly explained to Light why writing **{key.user.name}**\'s name in the notebook is wrong!{Mikasa.role.emoji}\n\n'
        if type(currentGame.currentExpo.reinerBlocked) == dict:
            for key, value in currentGame.currentExpo.reinerBlocked.items():
                if value == 'Sasha':
                    sashaDeathMessages += f'{Reiner.role.secondaryEmoji}Light accidentally thought of the wrong muffin flavor when writing **{key.user.name}**\'s name, and killed some other Muffin!{Reiner.role.secondaryEmoji}\n\n'
        return sashaDeathMessages
    
    def getMarcoDeathMessages(currentGame, currentTheme, Marco):
        marcoDeathMessages = ''
        for killedPlayer, causeOfDeath in Marco.killed.items():
            if causeOfDeath == 'Marco':
                marcoDeathMessages += f'{Marco.role.secondaryEmoji}**{killedPlayer.user.name}** Turned themselves into a Porkchop!{Marco.role.secondaryEmoji}\n'
                if killedPlayer in currentGame.soldiers:
                    marcoDeathMessages += f'They were a {currentTheme.emojiSoldier}**{currentTheme.soldierSingle}**{currentTheme.emojiSoldier}!\n\n'
                elif killedPlayer in currentGame.warriors:
                    marcoDeathMessages += f'They were a {currentTheme.emojiWarrior}**{currentTheme.warriorSingle}**{currentTheme.emojiWarrior}!\n\n'
                elif killedPlayer in currentGame.wildcards:
                    marcoDeathMessages += f'They were a {currentTheme.emojiWildcard}**{currentTheme.wildcardSingle}**{currentTheme.emojiWildcard}!\n\n'
        return marcoDeathMessages
    
    def getPyxisDeathMessages(currentGame, currentTheme, Pyxis, Mikasa, Reiner, realPyxis=None):
        if realPyxis == None:
            secEmo = Pyxis.role.secondaryEmoji
        else:
            secEmo = realPyxis.role.secondaryEmoji
        pyxisDeathMessages = ''
        for killedPlayer, causeOfDeath in Pyxis.killed.items():
            if causeOfDeath == 'Pyxis':
                pyxisDeathMessages += f'{secEmo}**{killedPlayer.user.name}** has been found guilty! They will now be punished by **Monokuma**.{secEmo}\n'
                if killedPlayer in currentGame.soldiers:
                    pyxisDeathMessages += f'They were a {currentTheme.emojiSoldier}**{currentTheme.soldierSingle}**{currentTheme.emojiSoldier}!\n\n'
                elif killedPlayer in currentGame.warriors:
                    pyxisDeathMessages += f'They were a {currentTheme.emojiWarrior}**{currentTheme.warriorSingle}**{currentTheme.emojiWarrior}!\n\n'
                elif killedPlayer in currentGame.wildcards:
                    pyxisDeathMessages += f'They were a {currentTheme.emojiWildcard}**{currentTheme.wildcardSingle}**{currentTheme.emojiWildcard}!\n\n'
        if type(currentGame.mikasaGuarded) == dict:
            for key, value in currentGame.mikasaGuarded.items():
                if value == 'Pyxis':
                    pyxisDeathMessages += f'{Mikasa.role.emoji}Kiryu has saved **{key.user.name}** from being punished!{Mikasa.role.emoji}\n\n'
        if type(currentGame.currentExpo.reinerBlocked) == dict:
            for key, value in currentGame.currentExpo.reinerBlocked.items():
                if value == 'Pyxis':
                    pyxisDeathMessages += f'{Reiner.role.secondaryEmoji}**{key.user.name}** survived the punishment attempt, because Monokuma didn\'t realize that baked goods can survive ovens!{Reiner.role.secondaryEmoji}\n\n'
        return pyxisDeathMessages
    
    def getKennyDeathMessages(currentGame, currentTheme, Kenny, Mikasa, Reiner):
        kennyDeathMessages = ''
        for killedPlayer, causeOfDeath in Kenny.killed.items():
            if killedPlayer not in currentGame.kennyDisplayedKills:
                if causeOfDeath == 'Kenny':
                    if killedPlayer == Kenny:
                        kennyDeathMessages += f'{Kenny.role.secondaryEmoji}**{killedPlayer.user.name}** has decided his terrorist ways were wrong and exited this world.{Kenny.role.secondaryEmoji}\n'
                    else:
                        kennyDeathMessages += f'{Kenny.role.secondaryEmoji}**{killedPlayer.user.name}** was murdered by Makarov!{Kenny.role.secondaryEmoji}\n'
                    if killedPlayer in currentGame.soldiers:
                        kennyDeathMessages += f'They were a {currentTheme.emojiSoldier}**{currentTheme.soldierSingle}**{currentTheme.emojiSoldier}!\n\n'
                    elif killedPlayer in currentGame.warriors:
                        kennyDeathMessages += f'They were a {currentTheme.emojiWarrior}**{currentTheme.warriorSingle}**{currentTheme.emojiWarrior}!\n\n'
                    elif killedPlayer in currentGame.wildcards:
                        kennyDeathMessages += f'They were a {currentTheme.emojiWildcard}**{currentTheme.wildcardSingle}**{currentTheme.emojiWildcard}!\n\n'
                    currentGame.displayKennyKill(killedPlayer)
        if type(currentGame.mikasaGuarded) == dict:
            for key, value in currentGame.mikasaGuarded.items():
                if value == 'Kenny':
                    kennyDeathMessages += f'{Mikasa.role.emoji}Kiryu has protected **{key.user.name}** from being murdered by Makarov!{Mikasa.role.emoji}\n\n'
        if type(currentGame.currentExpo.reinerBlocked) == dict:
            for key, value in currentGame.currentExpo.reinerBlocked.items():
                if value == 'Kenny':
                    kennyDeathMessages += f'{Reiner.role.secondaryEmoji} **{key.user.name}**\'s Muffin body was too small of a target for Makarov, and they survived!{Reiner.role.secondaryEmoji}\n\n'
        return kennyDeathMessages
    
    def getWillyDeathMessages(currentGame, currentTheme, Willy, Mikasa, Reiner):
        willyDeathMessages = ''
        for killedPlayer, causeOfDeath in Willy.killed.items():
            if causeOfDeath == 'Willy':
                if killedPlayer.role.id == 'Willy':
                    willyDeathMessages += f'{Willy.role.secondaryEmoji}**{killedPlayer.user.name}** has exploded!{Willy.role.secondaryEmoji}\n'
                else:
                    willyDeathMessages += f'{Willy.role.secondaryEmoji}**{killedPlayer.user.name}** has been killed by a Creeper!{Willy.role.secondaryEmoji}\n'
                if killedPlayer in currentGame.soldiers:
                    willyDeathMessages += f'They were a {currentTheme.emojiSoldier}**{currentTheme.soldierSingle}**{currentTheme.emojiSoldier}!\n\n'
                elif killedPlayer in currentGame.warriors:
                    willyDeathMessages += f'They were a {currentTheme.emojiWarrior}**{currentTheme.warriorSingle}**{currentTheme.emojiWarrior}!\n\n'
                elif killedPlayer in currentGame.wildcards:
                    willyDeathMessages += f'They were a {currentTheme.emojiWildcard}**{currentTheme.wildcardSingle}**{currentTheme.emojiWildcard}!\n\n'
        if type(currentGame.mikasaGuarded) == dict:
            for key, value in currentGame.mikasaGuarded.items():
                if value == 'Willy':
                    willyDeathMessages += f'{Mikasa.role.emoji}Kiryu has saved **{key.user.name}** from the Creeper\'s explosion!{Mikasa.role.emoji}\n\n'
        if type(currentGame.currentExpo.reinerBlocked) == dict:
            for key, value in currentGame.currentExpo.reinerBlocked.items():
                if value == 'Willy':
                    willyDeathMessages += f'{Reiner.role.secondaryEmoji}The Creeper\'s traitorous attack was no match for **{key.user.name}**\'s Muffiny Plot Armor!{Reiner.role.secondaryEmoji}\n\n'
        return willyDeathMessages
    
    def getGabiWoundMessage(currentGame, currentTheme, Gabi):
        gabiWoundMessage = f'{Gabi.role.secondaryEmoji}Trevor has shot **{currentGame.woundedPlayer.user.name}**! They have been evacuated to the Field Hospital and will not be able to attend the next mission!{Gabi.role.secondaryEmoji}\n\n'
        return gabiWoundMessage
    
    def getHealMessage(player):
        healMessage = f'{player.user.mention} has healed and returned to the fight!'
        return healMessage
    
    def getYmirRevivalMessage(currentGame, currentTheme, Ymir):
        ymirMessage = ''
        for player, clause in currentGame.ymirRevival.items():
            if clause:
                ymirMessage += f'{Ymir.role.emoji}The Game Master has used their godly powers to revive **{player.user.name}** back from the dead!{Ymir.role.emoji}'
        return ymirMessage
    
    def getVictoriousWarriors(currentGame, currentTheme):
        victoriousWarriors = []
        for winner in currentGame.winners:
            if winner in currentGame.warriors:
                victoriousWarriors.append(winner)
        if len(victoriousWarriors) == 0:
            return None
        else:
            returnMessage = f'The Following {currentTheme.warriorPlural} have reigned victorious:\n'
            for warrior in victoriousWarriors:
                returnMessage += f'**{currentTheme.emojiWarrior}{warrior.user.name}{currentTheme.emojiWarrior}**\n'
            return returnMessage

            

