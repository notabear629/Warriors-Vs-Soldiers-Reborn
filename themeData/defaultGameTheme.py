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
class defaultGameTheme:
    global prefix

    #You have free reign to edit these as you please
    themeName = 'Default Warriors vs Soldiers'
    gameName = 'Warriors vs Soldiers'
    soldierSingle = 'Soldier'
    soldierPlural = 'Soldiers'
    emojiSoldier = str('🛡️')
    warriorSingle = 'Warrior'
    warriorPlural = 'Warriors'
    emojiWarrior = str('⚔️')
    wildcardSingle = 'Wildcard'
    wildcardPlural = 'Wildcards'
    emojiWildcard = str('🃏')
    wallSingle = 'Wall'
    wallPlural = 'Walls'
    #By Default is the same as Eren Emoji
    emojiTheme = 1205662731659780106
    titanSingle = 'Titan'
    titanPlural = 'Titans'
    emojiDead = '☠️'

    #MUST be integer emoji. No exceptions.
    emojiPaths = 1218660133945737287

    soldierThumbnail = 'https://cdn.discordapp.com/emojis/934488343343927367.webp?size=128&quality=lossless'
    warriorThumbnail = 'https://cdn.discordapp.com/emojis/934488802213384292.webp?size=128&quality=lossless'
    wildcardThumbnail ='https://cdn.discordapp.com/emojis/934489212277882932.webp?size=128&quality=lossless'
    deadThumbnail =  'https://em-content.zobj.net/source/twitter/53/skull-and-crossbones_2620.png'
    globalThumbnail = 'https://em-content.zobj.net/source/twitter/376/globe-showing-americas_1f30e.png'

    soldierColor = discord.Color.blue()
    warriorColor = discord.Color.red()
    wildcardColor = discord.Color.gold()
    deadColor = discord.Color.default()

    soldierDefaultMessage = 'Work with your fellow Soldiers to successfully complete 3 expeditions and reach the basement. Remember to conceal the true identity of Eren! Securing the walls is not enough, after the rounds of expeditions, the Warriors will have one last shot of winning if they can successfully identity Eren!'
    warriorDefaultMessage = 'Work with your fellow Warriors to try to knock down the walls before the Soldiers can reach the basement. Be mindful of how the Soldiers behave, even if you fail to destroy the walls, you will have one last chance of victory if you can successfully identify Eren!'
    wildcardDefaultMessage = 'Wildcards are neither Soldiers nor Warriors, so the roles behave much differently. Shoot for your personal objective to the best of your abilities so that you may bask in the eternal glory of winning your own way!'

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
    winningColor = discord.Color.green()
    neutralColor = discord.Color.gold()
    losingColor = discord.Color.red()
    lostColor = discord.Color.default()

    statusProgress = 'Progress towards Basement'
    statusWalls = 'Status of the Walls'
    statusExpeditions = 'Expedition Info'

    expeditionName = 'Expedition'
    expeditionPlural = 'Expeditions'
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
    emojiMariaInterior = 1205660141156835328
    emojiRoseExterior = str('🏦')
    emojiRoseInterior = 1205660139927896084
    emojiSinaExterior = str('🏰')
    emojiSinaInterior = 1205660138627928185
    emojiBrokenExterior = str('🏚️')
    emojiBrokenInterior = str('💥')
    emojiWinMarker = str('🛡️')
    emojiFailMarker = str('⚔️')
    emojiCurrentMarker = str('🏇')

    #Roles embed aesthetics
    rolesEmbedColor = discord.Color.blue()

    #Players embed aesthetics
    playersEmbedColor = discord.Color.blue()
    commanderName = 'Commander'
    emojiCommanderMarker = str('👑')

    #Expedition aesthetics
    expeditionTeamMembers = 'Expedition Team Members'
    expeditionTeam = 'Expedition Team'
    emojiPassExpedition = str('✅')
    emojiSabotageExpedition = str('❌')
    emojiSecuredExpedition = str('🛡️')

    #Pick expo member aesthetics
    pickColor = discord.Color.blue()

    #Voting aesthetics
    emojiAcceptExpedition = str('✅')
    emojiRejectExpedition = str('❌')
    emojiAbstainExpedition = str('✖️')
    emojiBlackoutExpedition = str('✴️')
    voteDMColor = discord.Color.blue()
    acceptedExpeditionColor = discord.Color.green()
    rejectedExpeditionColor = discord.Color.red()
    jeanedExpeditionColor = discord.Color.gold()
    zacharyExpeditionColor = discord.Color.red()
    mikeSmell = 'smell'
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
    suicideLabel = 'Feed The Titans'
    emojiSuicide = 1205684706431991818
    wallMariaBreakMessage = str('💥Wall Maria has Fallen!💥')
    wallRoseBreakMessage = str('💥Wall Rose has Fallen!💥')
    wallSinaBreakMessage = str('💥Wall Sina has Fallen!💥')

    #Game over Aesthetics
    wallBreakMessage = str('⚔️All the Walls have Fallen and Paradis has been destroyed!⚔️\n\n⚔️Warriors Win!⚔️')
    basementMessage = str(f'The Soldiers have reached the Basement. The Warriors still have one final chance to win! Use `{prefix}kidnap @mention` to kidnap who you think is the Coordinate for one final chance at victory!')
    kidnapTimeoutMessage = str(f'The Warriors have failed to identify the Coordinate in time...\n\n🛡️Soldiers Win!🛡️')
    multikidnapTimeoutMessage = str(f'At least some of the Warriors have failed to select their choice for the Coordinate in time...\n\nThey will be given a loss')
    multikidnapSuccessMessage = str('⚔️The Warriors have successfully chosen the Coordinate as their popular choice!⚔️\n\n⚔️Soldiers Lose!⚔️')
    kidnapSuccessMessage = str('⚔️The Warriors have successfully identified the Coordinate!⚔️\n\n⚔️Warriors Win!⚔️')
    kidnapFailMessage = str('🛡️The Warriors did not manage to successfully identify the Coordinate and Eren\'s identity was kept secret.🛡️\n\n🛡️Soldiers Win!🛡️')
    multikidnapFailMessage = str('🛡️The Warriors did not manage to successfully identify the Coordinate as the single most popular choice.🛡️\n\n🛡️Soldiers Win!🛡️')
    noCordSuccessMessage = str('🛡️The Soldiers have successfully completed 3 expeditions and protected the Walls.🛡️\n\n🛡️Soldiers Win!🛡️')
    endgameCardColor = discord.Color.blue()
    emojiWinner ='🏅'
    emojiLoser = '☠️'
    emojiMVP = '🏆'

    #Webhook Message Aesthetics
    jeanMessage = f'I\'m securing this Expedition!'
    pieckMessageJean= f'I tried to flip the votes, but I am not sure if I was able to successfully do so because of **Jean**!'
    pieckMessageZachary= f'I tried to flip the votes, but I am not sure if I was able to successfully do so because of **Zachary**!'
    pieckMessage = f'I flipped the votes!'
    arminMessage = f'I blew up the Expedition!'
    leviAttackMessage = f'I... Won\'t let a single one of you get away!'
    leviDefendMessage = f'I will defend this expedition at all costs!'
    sashaMessage = f'I have fired an arrow!'
    dazMessage = f'Waaaaaah! I\'m scared!'
    dazMessageFollowUp = 'The Expedition has been cancelled!'
    mikasaMessage = 'My guard is unbreakable...'
    reinerMessage = 'Marley\'s Shield is not broken so easily...'
    bertholdtMessage = 'I\'ll deploy a cloak of steam!'
    ksaverMessage = 'I\'ll trigger a blackout!'
    annieMessage = '***RAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA***'
    retreatMessage = 'I\'m ordering a retreat! Pull back from the assault on the walls, and allow the Soldiers to advance to the basement!'
    kennyMessage = 'I hope you don\'t mind being without your throat!'
    kennySuicideMessage = 'That\'s it! I hate every last one of you! I\'m getting the HELL off this damned island the only way I know how!'
    ymirMessage = 'To you, 2000 years from now...'
    ymirRevivalMessage = 'I will re-make you with these sands...'
    gabiMessage = 'I\'m firing my rifle!'
    keithMessage = 'I am but a bystander... I leave this to my students.'
    keithMessage2 = 'Reporting for duty.'
    zacharyMessage = 'I am vetoing this Expedition Team Proposal!'
    conflictJeanZacharyMessage = 'The confusing orders have lead to chaos! The expedition will be voted on as usual.'
    petraMessage = 'I saw someone try to break the wall! I won\'t let them get away!'
    connieMessage = '⚠️We have been betrayed! That Expedition was not safe!⚠️'
    hannesMessage = 'I\'m getting out of here!'
    willyMessage = 'To the enemy forces of Paradis, a declaration of war!'
    pyxisMessage = 'You will stand trial for your crimes.'
    marcoMessage = '...'
    warhammerApologyMessage = 'Comrades... I am sorry.'
    ricoMessage = 'You\'ve stepped into my trap!'
    magathMessage = 'This will be my final order...'
    onyankoponMessage = 'Hold on, I\'m flying you in!'
    frecklemirMessage = '***RAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA***'
    greenFiredMessage = 'https://i.imgur.com/QsobXCg.gif'
    redFiredMessage = 'https://i.imgur.com/dU8Qxne.gif'
    blackFiredMessage = 'https://i.imgur.com/D6aqnNM.gif'
    kitzCancelMessage = 'Ugh, fine! You can stand down!'

    #Other role messages
    flochMessageEren = 'Eren Yeager is on the expedition team!'
    flochMessageNoEren = 'Eren Yeager is not on the expedition team.'

    #Timeout Messages
    timeoutCoreStart = 'You have '
    timeoutCoreEnd = ' left to'
    timeoutPick = ' pick your Expedition Team!'
    timeoutVote = ' vote on the Expedition Team!'
    timeoutExecution = ' vote on the Execution!'
    timeoutExpo = ' act on the Expedition!'
    timeoutKidnap = ' kidnap the Coordinate!'
    timeoutRumblingFight = ' to choose who to attack!'

    # Rumbling Aesthetics
    rumblingName = 'Rumbling'
    emojiRumbling = 1205660709162319922
    emojiRumblingWallExterior = 1205660709162319922
    emojiRumblingWallInterior = str('💥')
    yeageristSingle = 'Yeagerist'
    yeageristPlural = 'Yeagerists'
    yeageristTeam = 'Yeagerists'
    allianceSingle = 'Alliance Member'
    alliancePlural = 'Alliance Members'
    allianceTeam = 'Alliance'
    rumblingStatusColor = discord.Color.default()
    rumblingAltStatusColor = discord.Color.brand_red()
    rumblingStartAttachment = 'https://cdn.discordapp.com/attachments/751512233011445770/1202770592835567696/Untitled.gif?ex=65ceaa67&is=65bc3567&hm=72e1302afefb9b5ac7d926bca42bf84190a85499ef504baafb206479d0204a6a&'
    rumblingFirstMessage = 'Eren and Zeke Yeager have made contact!'
    rumblingSecondMessage = 'The Walls are coming down!'
    rumblingThirdMessage = 'Eren and the Colossal Titans are on the move! It can\'t be stopped anymore!'
    rumblingTimerOne = 12
    rumblingTimerTwo = 13
    rumblingTimerThree = 10
    rumblingIntroMessage = 'An entirely new game has begun! Past allegiances have broken down, and the distinction between Warrior and Soldier is now meaningless! This battle is now fought between those who stand in favor of or oppose the Rumbling...'
    allianceFormMessage = 'The Alliance has been formed! They begin their fight to get to the brothers...'
    yeageristInTheWay = 'A Yeagerist Stands in the way to defend the path to the Yeager Brothers!'
    allianceZekeClear = 'The Path to the Yeager Brothers has been cleared! The Alliance advances towards them, in search of Zeke...'
    ZekeInTheWay = 'The Alliance has reached Zeke!'
    allianceZekeDefeated = 'Zeke has been deafeated! The Alliance makes their way to Eren...'
    ErenInTheWay = 'The Final Battle has begun! The Alliance has reached Eren!'
    allianceMemberSlain = 'A member of the Alliance has been killed! The next steps up to take their place...'
    newFightPrompt = 'It is up to you to fight the Alliance!'
    genericYeageristWin = 'The Yeagerists have killed all of the Alliance fighters and reign victorious!'
    genericAllianceWin = 'The Alliance successfully stopped the Rumbling and have achieved victory!'

    standardYeageristWin = 'The Yeagerists have eliminated 95% of all life on Earth, sparing only a few pockets of civilization. The Titan Powers have been removed from Eldians, but the world has been so thoroughly smashed that Paradis can safely dominate what is left even without them. \n\nEnding Achieved: "The Grand Yeagerist Compromise" (Standard Yeagerist Win)'
    flochDominationWin = 'The Yeagerists have completely wiped out every last human on Earth outside of Paradis, sparing absolutely no one. The Titan Powers continue to thrive, as an integral part of a new global-spanning Eldian Empire, which will claim the destroyed land for itself.\n\nEnding Achieved: "Empire of Ashes" (Floch Domination Win)'
    zekeDominationWin = 'Approximately 20% of life on Earth, and the majority of it\'s military capacity was destroyed before Zeke took over the Rumbling, stopping it, and then enacting his Euthanasia plan. Successfully revoking the Eldian\'s right to reproduce, easily overcoming Eren\'s betrayal to do so. Zeke has achieved his dream. \n\nEnding Achieved: "A Longtime Dream, a Longtime Sleep" (Zeke Domination Win)'
    erenDominationWin = 'The Yeagerists have completely wiped out every last human on Earth outside of Paradis, sparing absolutely no one. The Titan Powers have ended, and Ymir has been freed... But at a great cost. Eren now must return home with the weight of his actions on his shoulders for the remainder of his life.\n\nEnding Achieved: "Akatsuki No Requiem" (Eren Domination Win)'

    standardAllianceWin = 'The Alliance ultimately achieved their goals, but at great cost. Approximately 80% of Humanity was destroyed in the Rumbling. The survivng Alliance members will do their best to try to negotiate peace, and while they are optimistic, it remains to be seen if they will be successful.\n\nEnding Achieved: "Wait, isn\'t this just 139 with some cringe removed?" (Standard Alliance Win)'
    dominantAlliancewin = 'The Alliance completely devestated the Yeagerists and dominated the battle from the start. Thanks to their efforts, only 15% of humanity perished in the Rumbling. The Talk No Jitsuus worked, and everybody made peace and wars were ended, and everybody shat rainbows. Oh God, we somehow managed to get worse than 139.\n\nEnding Achieved: "Cringevengers, Assemble!" (Dominant Alliance win)'
    #DO NOT CHANGE THIS CLASS NAME! Even if you rename the role, keep the function as Eren. Apply this advice to all roles.
    class Eren:
        #Do not change this roleID key. The code will look for "Eren" even if you re-skin it, it is important to keep all roleIDs the same.
        roleDict = {'roleID' : 'Eren'}

        #You may change 'Eren Yeager' to whatever you want his name to be.
        roleDict['name'] = 'Eren Yeager'

        #You may change the shortname to whatever you want the name to be, this one is purely cosmetic.
        roleDict['shortName'] = 'Eren'

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
        roleDict['emoji'] = 1205662731659780106


        #Not all roles actually use secondary emojis. If this is None, it's fine. Should be an int or emoji string like any other emoji.
        roleDict['secondaryEmoji'] = 1205669634809012274

        #If you are using a custom emoji, then make sure this is set to None. Otherwise set this to a URL of the emoji you are using. Unfortunately, Webhook images and thumbnails can only be made with urls and default emojis dont have urls.
        #Thus, if you are using a built in emoji, you will need to define this dictionary key.
        roleDict['imageURL'] = None


        #Overwhelming majority have no purpose for secondaryImgeURL. Mainly here in case you want to display secondaryEmoji as a thumbnail.
        roleDict['secondaryImageURL'] = None

        #The roleMessage is the part of the message the bot sends that gives specific information regarding the role itself when you are assigned a role.
        #You may change any role message as you wish.
        roleDict['roleMessage'] = f'You know the identity of all of the other Warriors, except for Zeke. Remember to not make the fact you know who the Warriors are obvious, and do your best to protect your identity. If the Warriors can successfully identify you, the Soldiers will lose!'

        #The gameRole is basically a way to relate what the job of this role is without making use of any theme. Remember how Entropi's bot was theme-less, this would essentially be what this role might be called in Entropi's bot.
        #You *can* change these, but I would recommend not to.
        #I would also recommend keeping the format of :emoji:Name:emoji:
        roleDict['gameRole'] = ':map:Coordinate:map:'

        #helpInfo is the message that will be summoned when you do a ~help or ~info (may or may not be implemented yet) for a particular role
        #Highly recommend changing this entirely to match your role and your lore reasoning for why your themed character fits the role
        roleDict['helpInfo'] = f'Eren is the Coordinate and the team captain of the Soldiers. This role is a mandatory role and appears in every game. Eren has the ability to see every Warrior in the game, with the exception of Zeke the Warchief! However, he must do his best to not reveal himself to the other players, even if the Walls are secured, the Warriors will have the opportunity to kidnap who they think the Coordinate is, and if they get it right the Soldiers will lose!'


    #PLEASE PLEASE FOLLOW ALL INSTRUCTIONS PRESENT FOR THE EREN ROLE FOR THE FUTURE ROLES!

    class Historia:
        roleDict = {'roleID' : 'Historia'}

        roleDict['name'] = 'Historia Reiss'

        roleDict['shortName'] = 'Historia'

        roleDict['team'] = 'Soldiers'

        roleDict['rumblingTeam'] = 'yeageristBench'

        roleDict['isTitan'] = False

        roleDict['emoji'] = 1205677062040326164

        roleDict['secondaryEmoji'] = None

        roleDict['imageURL'] = None

        roleDict['secondaryImageURL'] = None

        roleDict['roleMessage'] = f'You are given two names. One is Eren and one is Zeke, but you don\'t know which is which! Use this information to help guide you to victory, but be careful! Don\'t expose the identity of Eren to the Warriors!'

        roleDict['gameRole'] = ':angel:Queen:angel:'

        roleDict['helpInfo'] = 'Historia is the queen of Paradis and has closer knowledge of the situation than most Soldiers due to being in communications with the Yeager brothers, but there was a mistake in the line of communications! Now, she knows which 2 players are Eren and Zeke, but not which is which!'

    class Hange:
        roleDict = {'roleID' : 'Hange'}

        roleDict['name'] = 'Hange Zoë'

        roleDict['shortName'] = 'Hange'

        roleDict['team'] = 'Soldiers'

        roleDict['rumblingTeam'] = 'allianceFighter'

        roleDict['isTitan'] = False

        roleDict['emoji'] = 1205677240982183967

        roleDict['secondaryEmoji'] = str('📡')

        roleDict['imageURL'] = None

        roleDict['secondaryImageURL'] = None

        roleDict['roleMessage'] = f'You are the leader of the Engineering corps of Paradis. As such, you have access to the latest technology in espionage. Once on an expo, you may choose someone to Wiretap. Then, throughout the rest of the game you will be alerted as to their votes and when they use a special ability! Be wary though and understand when the wiretap goes off. The wiretap will NOT go off when Sasha or Gabi fire their shots for instance, but will go off when a player uses ~target or ~fire. The actual player selection is what you track, because you are tracking their choices.'

        roleDict['gameRole'] = ':satellite:Wiretapper:satellite:'

        roleDict['helpInfo'] = 'Hange is the leader of the Engineering corps and a spearhead of many innovations in anti-warrior technologies. As such, she has excellent espionage equipment. Once per game, she can choose somebody in the same expedition as her to wiretap. This will watch them the rest of the game, instantly pinging her when they vote or choose to use a special ability for the rest of the game. However, it is important to note WHEN the alert is made. She will NOT be alerted when Keith transforms, but she WILL be alerted when Keith uses ~summon. She tracks the decision making.'
    
    class Jean:
        roleDict = {'roleID' : 'Jean'}

        roleDict['name'] = 'Jean Kirschstein'

        roleDict['shortName'] = 'Jean'

        roleDict['team'] = 'Soldiers'

        roleDict['rumblingTeam'] = 'allianceFighter'

        roleDict['isTitan'] = False

        roleDict['emoji'] = 1205684278596477000

        roleDict['secondaryEmoji'] = None

        roleDict['imageURL'] = None

        roleDict['secondaryImageURL'] = None

        roleDict['roleMessage'] = 'You have the ability to force an expedition proposal to pass once! But be careful! If you miscalculate, you could easily allow the Warriors to get a wall!\n\n'

        roleDict['gameRole'] = ':white_check_mark:Voting Ackermann:white_check_mark:'

        roleDict['helpInfo'] = 'Jean has an excellent ability to rally his comrades! Thanks to this, he has the ability to force an expedition proposal to be passed one time.'

    class Mike:
        roleDict = {'roleID' : 'Mike'}

        roleDict['name'] = 'Mike Zacharius'

        roleDict['shortName'] = 'Mike'

        roleDict['team'] = 'Soldiers'

        roleDict['rumblingTeam'] = 'allianceFighter'

        roleDict['isTitan'] = False

        roleDict['emoji'] = 1205685715623485460

        roleDict['secondaryEmoji'] = 1205684706431991818

        roleDict['imageURL'] = None

        roleDict['secondaryImageURL'] = None

        roleDict['roleMessage'] = 'You have the uncanny ability to smell Titans! When you are put on an expo, before voting even begins, you will know how many Titans are on the expedition. But be very careful! Not every Titan is a Warrior, in fact, the Coordinate is a Titan! In addition, not every Warrior is a Titan. Be very careful with how you use the information you gain, it will not always be useful.\n\n'

        roleDict['gameRole'] = ':nose:Mike:nose:'

        roleDict['helpInfo'] = 'Mike was born with the bizarre gift of being able to smell titans! Whenever an expedition is proposed that he is on, he will be able to smell how many titans are on board! But be careful, not EVERY warrior is a titan, and not EVERY titan is a warrior! In fact, Eren himself is a titan! Mike will be alerted as to which of the roles are considered titans, and must carefully deduce who to trust from that information, but be careful! You may accidentally tip off the identity of Eren to the Warriors if you are careless and share this information!'

    class Hitch:
        roleDict = {'roleID' : 'Hitch'}

        roleDict['name'] = 'Hitch Dreyse'

        roleDict['shortName'] = 'Hitch'

        roleDict['team'] = 'Soldiers'

        roleDict['rumblingTeam'] = 'yeageristBench'

        roleDict['isTitan'] = False

        roleDict['emoji'] = 1205687306124791909

        roleDict['secondaryEmoji'] = None

        roleDict['imageURL'] = None

        roleDict['secondaryImageURL'] = None

        roleDict['roleMessage'] = 'You have the ability to investigate who used special abilities! As such, at the end of a round, for every one-time-use special ability used in that round, you will be given two names, of which, one of those players was responsible for that ability being used.\n\n'

        roleDict['gameRole'] = ':mag:Ability Investigator:mag:'

        roleDict['helpInfo'] = 'Hitch is a part of the Military Police! Thanks to her enhanced access to investigative scenes and crime scene training, she is able to extract information based on who used a special ability. When a one-time special ability is used, Soldier or Warrior, She will be able to determine 2 players, of which one of them used the ability.'

    class Armin:
        roleDict = {'roleID' : 'Armin'}

        roleDict['name'] = 'Armin Arlert'

        roleDict['shortName'] = 'Armin'

        roleDict['team'] = 'Soldiers'

        roleDict['rumblingTeam'] = 'allianceFighter'

        roleDict['isTitan'] = True

        roleDict['emoji'] = 1205689207696265216

        roleDict['secondaryEmoji'] = 1205690550246965300

        roleDict['imageURL'] = None

        roleDict['secondaryImageURL'] = None

        roleDict['roleMessage'] = 'Your Colossal Titan has a terrible ability! While on an expedition, as long as there\'s 2 or more walls left, you can use your titan to explode and kill everybody else in the expedition! This could be useful to get rid of Warriors, but be EXTREMELY CAREFUL! An improperly played Colossal Titan can easily lose the game for the Soldiers.\n\n'

        roleDict['gameRole'] = ':radioactive:Nuclear Bomb:radioactive:'

        roleDict['helpInfo'] = 'Armin is an incredibly unique Soldier thanks to the destructive ability of his colossal titan! He is actually the only soldier which is capable of sabotaging the expedition by using his titan to blow it all up. If he does this, then every member of the expedition besides him will be killed! Therefore, use this ability VERY carefully! It is capable of eliminating warriors, but it\'s also capable of ending the game for the Soldiers!.'

    class Levi:
        roleDict = {'roleID' : 'Levi'}

        roleDict['name'] = 'Levi Ackermann'

        roleDict['shortName'] = 'Levi'

        roleDict['team'] = 'Soldiers'

        roleDict['rumblingTeam'] = 'allianceFighter'

        roleDict['isTitan'] = False

        roleDict['emoji'] = 1211171011941236786

        roleDict['secondaryEmoji'] = 1211171033634181160

        roleDict['imageURL'] = None

        roleDict['secondaryImageURL'] = None

        roleDict['roleMessage'] = 'You are Humanity\'s strongest soldier! While on expedition, you have two choices. `attack`, which will kill any Warrior that attempts to sabotage the expedition. HOWEVER. Pressing this button will instantly alert the warriors to your identity, regardless if you killed anybody or not. Secondly, you may press `defend`, which will prevent the expedition from being sabotaged. The warriors will be alerted to your identity if and only if they tried to sabotage the expedition, and if they did indeed try, there will be an indicator in the game channel that says as such as well.\n\n'

        roleDict['gameRole'] = ':guard:Ackermann:guard:'

        roleDict['helpInfo'] = 'Levi is the strongest Soldier of all time! He has an ability to secure an expedition and ensure that it will pass, even if a warrior sabotages! Or, if defense isn\'t your style, he is also great at offense. He can also kill all Warriors which attempt to sabotage an expo.'


    class Sasha:
        roleDict = {'roleID' : 'Sasha'}

        roleDict['name'] = 'Sasha Braus'

        roleDict['shortName'] = 'Sasha'

        roleDict['team'] = 'Soldiers'

        roleDict['rumblingTeam'] = 'allianceFighter'

        roleDict['isTitan'] = False

        roleDict['emoji'] = 1205694976520884284

        roleDict['secondaryEmoji'] = str('🏹')

        roleDict['imageURL'] = None

        roleDict['secondaryImageURL'] = None

        roleDict['roleMessage'] = f'You have the ability to attack from long range! You can set a target to fire at using `{prefix}target`, and the next time they are on an expedition that you are not, you\'ll fire an arrow at them and kill them! Be careful: This does NOT stop them from breaking the walls, and if you attack a soldier, they will still die!\n\n'

        roleDict['gameRole'] = ':bow_and_arrow:Sniper:bow_and_arrow:'

        roleDict['helpInfo'] = 'Sasha is a master at long range weapons! She is able to choose a target, and the next time they are in an expedition that goes through that she is NOT in, she will send an arrow to them, killing them! You can use this to eliminate someone you know is a warrior, but be careful, this will NOT stop them from sabotaging the walls!'

    class Erwin:
        roleDict = {'roleID' : 'Erwin'}

        roleDict['name'] = 'Erwin Smith'

        roleDict['shortName'] = 'Erwin'

        roleDict['team'] = 'Soldiers'

        roleDict['rumblingTeam'] = 'allianceFighter'

        roleDict['isTitan'] = False

        roleDict['emoji'] = 1205696451301089341

        roleDict['secondaryEmoji'] = None

        roleDict['imageURL'] = None

        roleDict['secondaryImageURL'] = None

        roleDict['roleMessage'] = f'You have the ability to reveal your role once and instantly become the commander by using `{prefix}flare`! But be careful, while this will prove you are who you say you are, this will also make identifying Eren easier for the warriors!\n\n'

        roleDict['gameRole'] = ':dizzy:True Commander:dizzy:'

        roleDict['helpInfo'] = 'Erwin is one of the greatest leaders of all time and the true commander for the Soldiers! Thanks to this, for one time, he is able to prove his identity to everyone, and take control of being the expedition commander. Use this wisely, however! Because your role being exposed makes getting to Eren easier!'

    class Daz:
        roleDict = {'roleID' : 'Daz'}

        roleDict['name'] = 'Daz'

        roleDict['shortName'] = 'Daz'

        roleDict['team'] = 'Soldiers'

        roleDict['rumblingTeam'] = 'yeageristBench'

        roleDict['isTitan'] = False

        roleDict['emoji'] = 1205696737210146847

        roleDict['secondaryEmoji'] = str('🐔')

        roleDict['imageURL'] = None

        roleDict['secondaryImageURL'] = None

        roleDict['roleMessage'] = f'You have the one time ability to abort any expedition you are on in which you rejected! To use this ability, simply select `Chicken Out` while on an expedition you rejected to abort and cancel the expedition!\n\n'

        roleDict['gameRole'] = ':scream:Coward:scream:'

        roleDict['helpInfo'] = 'Daz is a known coward... When rations are low, there\'s rumors in the barracks that he\'s such a chicken that he tastes exactly like KFC when deepfried. ~~He has already had to be saved from Sasha on 4 separate occassions~~ But this cowardice has a plus. When on any expedition he rejects, he has a one time ability to abort the expedition and cancel the whole thing altogether. Note, this applies REGARDLESS of if a spy flips the vote. If you rejected but got flipped, you are allowed to abort the mission. If you accepted but flipped to a reject, you are not.'

    class Floch:
        roleDict = {'roleID' : 'Floch'}

        roleDict['name'] = 'Floch Forster'

        roleDict['shortName'] = 'Floch'

        roleDict['team'] = 'Soldiers'

        roleDict['rumblingTeam'] = 'yeageristFighter'

        roleDict['isTitan'] = False

        roleDict['emoji'] = 1205696923076534272

        roleDict['secondaryEmoji'] = None

        roleDict['imageURL'] = None

        roleDict['secondaryImageURL'] = None

        roleDict['roleMessage'] = f'When voting for an expedition, if you are inside the expedition, you will be told if Eren is in the expedition or not.\n\n'

        roleDict['gameRole'] = ':punch:Coordinate\'s Fist:punch:'

        roleDict['helpInfo'] = 'Floch is the quintessential Yeagerist. He will follow a complete rumbling to the bitter end, and will help it come to fruition. In addition, he has the ability to gain intel from Eren. After every Expedition proposed, if he is in the expedition, he will be informed by Eren if he is in the expo or not.'

    class Mikasa:
        roleDict = {'roleID' : 'Mikasa'}

        roleDict['name'] = 'Mikasa Ackermann'

        roleDict['shortName'] = 'Mikasa'

        roleDict['team'] = 'Soldiers'

        roleDict['rumblingTeam'] = 'allianceFighter'

        roleDict['isTitan'] = False

        roleDict['emoji'] = 1205698006704197732

        roleDict['secondaryEmoji'] = str('🛡️')

        roleDict['imageURL'] = None

        roleDict['secondaryImageURL'] = None

        roleDict['roleMessage'] = f'You have the ability to act as a personal bodyguard to any **one** person on any expedition (Inlcuding yourself if you choose yourself!) and prevent them from being killed. Use this ability wisely, only to protect yourself and Soldiers you really trust! After you successfully save someone, you will lose your ability for the rest of the game. Use `{prefix}guard` to set which player you want to guard.\n\n'

        roleDict['gameRole'] = ':fencer:Bodyguard:fencer:'

        roleDict['helpInfo'] = '**Credit to Messi (messsiii) for the idea of letting Mikasa guard on expos she\'s not on!**\nMikasa is an extremely strong Soldier! Thanks to this and an unwavering ~~desire to be a pathetic fucking simp~~ loyal streak, she has the ability to protect 1 person on any expo INCLUDING herself to prevent them from being killed! Once she successfully saves somebody, her ability is lost the rest of the game.'

    class Keith:
        roleDict = {'roleID' : 'Keith'}

        roleDict['name'] = 'Keith Shadis'

        roleDict['shortName'] = 'Keith'

        roleDict['team'] = 'Soldiers'

        roleDict['rumblingTeam'] = 'allianceFighter'

        roleDict['isTitan'] = False

        roleDict['emoji'] = 1218766701605425192

        roleDict['secondaryEmoji'] = None

        roleDict['imageURL'] = None

        roleDict['secondaryImageURL'] = None

        roleDict['roleMessage'] = f'You are responsible for training the Soldiers of Paradis! As such, you have many students that trained under you to call upon. Use `{prefix}summon` to step aside, and allow them to take your place. (This will make it so that you can choose any Soldier role to morph into that isn\'t already present in the game. Your role will change upon a passed expedition, or upon the circumstance the Soldiers go down 0-2)\n\n'

        roleDict['gameRole'] = ':man_teacher:Instructor:man_teacher:'

        roleDict['helpInfo'] = 'Keith is the instructor for the cadet corps! As such, he has made many connections with his students. As he himself, is a mere bystander, he has the ability to leave the battlefield, calling one of his students to take his place. This effectively means, that the player with this role can change their role to any Soldier role not already present in the game. Their role will not be changed until the next passed round\'s results are read, however. (Or until the Soldiers go down 0-2)'

    class Zachary:
        roleDict = {'roleID' : 'Zachary'}

        roleDict['name'] = 'Darius Zachary'

        roleDict['shortName'] = 'Zachary'

        roleDict['team'] = 'Soldiers'

        roleDict['rumblingTeam'] = 'allianceFighter'

        roleDict['isTitan'] = False

        roleDict['emoji'] = 1220678440030699530

        roleDict['secondaryEmoji'] = None

        roleDict['imageURL'] = None

        roleDict['secondaryImageURL'] = None

        roleDict['roleMessage'] = f'You are in charge of administration of Paradis island! As such, you oversee the expedition operations, and will have a one-time ability to Veto and expedition proposal, forcing it to cancel!\n\n'

        roleDict['gameRole'] = ':man_judge:Administrator:man_judge:'

        roleDict['helpInfo'] = 'Zachary is the administrator of Paradis Island and its defense forces! Thanks to this, he has the ability to veto an expedition one time to ensure that it does not pass. This role is a reverse Jean. However, if both Jean and Zackary use their abilities on the same turn, neither will work and they will both cancel.'
    
    class Petra:
        roleDict = {'roleID' : 'Petra'}

        roleDict['name'] = 'Petra Ral'

        roleDict['shortName'] = 'Petra'

        roleDict['team'] = 'Soldiers'

        roleDict['rumblingTeam'] = 'allianceFighter'

        roleDict['isTitan'] = False

        roleDict['emoji'] = 1220701264967635057

        roleDict['secondaryEmoji'] = None

        roleDict['imageURL'] = None

        roleDict['secondaryImageURL'] = None

        roleDict['roleMessage'] = f'You are one of Paradis\' finest Soldiers and are in Levi Squad! As such, you have an outsized level of strength. Once per game, in an expo, you may choose one expedition member to keep a watch on. If you see them attempt to break the Walls, you will be able to catch them and kill them. But unfortunately, not before they break the walls.\n\n'

        roleDict['gameRole'] = ':axe:Executioner:axe:'

        roleDict['helpInfo'] = 'Petra Ral is a top Soldier, as expected of a member of Levi Squad. For those who remember the "Hunter" role from Entropi\'s game, this is that, but with death. Petra can once per game, pick a fellow expeditioner member to watch. If that player is caught breaking the walls, they will be killed. But not before they are able to break the wall.'

    class Niccolo:
        roleDict = {'roleID' : 'Niccolo'}

        roleDict['name'] = 'Niccolo'

        roleDict['shortName'] = 'Niccolo'

        roleDict['team'] = 'Soldiers'

        roleDict['rumblingTeam'] = 'allianceBench'

        roleDict['isTitan'] = False

        roleDict['emoji'] = 1220729879926931516

        roleDict['secondaryEmoji'] = None

        roleDict['imageURL'] = None

        roleDict['secondaryImageURL'] = None

        roleDict['roleMessage'] = f'You are originally from the homeland of the Warriors. But, as you came to Paradis island you realized that you didn\'t actually want to attack the Soldiers. As such, you have joined the side of the Soldiers. While having access to the Warriors documents, you tampered with them, and now a random Soldier\'s name appears among the list.\n\n'

        roleDict['gameRole'] = ':ninja:Ex Warrior:ninja:'

        roleDict['helpInfo'] = 'Niccolo grew up in the homeland of the Warriors. But, as he came to Paradis island, he switched allegiances and realized he did not want to attack the Soldiers. He has, in fact, joined the Soldiers. While he had access to the Warriors important documentation, he tampered with them. As such, one of the Warriors in the list of names they receives is actually a random soldier.'

    class Nile:
        roleDict = {'roleID' : 'Nile'}

        roleDict['name'] = 'Nile Dok'

        roleDict['shortName'] = 'Nile'

        roleDict['team'] = 'Soldiers'

        roleDict['rumblingTeam'] = 'allianceFighter'

        roleDict['isTitan'] = False

        roleDict['emoji'] = 1220742818042085416

        roleDict['secondaryEmoji'] = None

        roleDict['imageURL'] = None

        roleDict['secondaryImageURL'] = None

        roleDict['roleMessage'] = f'You are the Commander of the Military Police. You have direct access to police reports submitted by the citizens of Paradis, whenever a wall is broken, you will be informed of which Warrior role was responsible.\n\n'

        roleDict['gameRole'] = ':man_police_officer:Police Chief:man_police_officer:'

        roleDict['helpInfo'] = 'Nile Dok is the Commander of the Military Police. As such, he has direct access to all of the police reports filed by the citizenry of Paradis. Whenever a wall is sabotaged, he wil learn about the reports of Warrior sightings filed. As such, he will be informed of which Roles were responsible for breaking the Wall.'

    class Connie:
        roleDict = {'roleID' : 'Connie'}

        roleDict['name'] = 'Connie Springer'

        roleDict['shortName'] = 'Connie'

        roleDict['team'] = 'Soldiers'

        roleDict['rumblingTeam'] = 'allianceFighter'

        roleDict['isTitan'] = False

        roleDict['emoji'] = 1220773736257552486

        roleDict['secondaryEmoji'] = None

        roleDict['imageURL'] = None

        roleDict['secondaryImageURL'] = None

        roleDict['roleMessage'] = f'You are someone who is eternally betrayed! As such, you recognize betrayal when you see it. When you are on an expedition that successfully passes, you will be alerted if there was actually a Warrior within it.\n\n'

        roleDict['gameRole'] = ':fishing_pole_and_fish:Bait Spotter:fishing_pole_and_fish:'

        roleDict['helpInfo'] = 'Connie Springer is perpetually betrayed! As such, he has gotten very good at spotting betrayal when he sees it. If he is on an expedition that successfully passes, he will be alerted if it actually secretly contained a Warrior within it.'
    
    class Marco:
        roleDict = {'roleID' : 'Marco'}

        roleDict['name'] = 'Marco Bodt'

        roleDict['shortName'] = 'Marco'

        roleDict['team'] = 'Soldiers'

        roleDict['rumblingTeam'] = 'allianceFighter'

        roleDict['isTitan'] = False

        roleDict['emoji'] = 1225241493443444736

        roleDict['secondaryEmoji'] = 1225241959111856148

        roleDict['imageURL'] = None

        roleDict['secondaryImageURL'] = None

        roleDict['roleMessage'] = f'You... May be destined for death. But that\'s okay! Your comrades will remember you and your memory will last with them forever. Because of this, when you die, you will still be able to vote. BUT LISTEN CAREFULLY. If you "Abstain", it will NOT show your name, so will therefore not reveal your role. If you "Accept" or "Reject", it WILL. So use this when there is a gridlocked emergency only! In addition, when on expo, you will have an option to Feed The Titans and ensure your death!\n\n'

        roleDict['gameRole'] = ':ghost:Phantom:ghost:'

        roleDict['helpInfo'] = '**Shoutout to Bob (bob\'s dad) and Luna (satorobin) for giving me the inspiration to add the Suicide Button!**\nMarco had a rather quick and undignified death. Despite this, his death stuck with his comrades and his memory and wishes lived on, especially through Jean. Because of this, he can still vote on expeditions after he dies. HOWEVER. If he "Abstains" his name will not appear in the vote results, therefore not blowing his cover. If he uses "Accept" or "Reject", his name will appear, and therefore he will be exposed. Marco also has a button to kill himself on an expo to ensure his death! When this button is selected, any mikasa guards on him will NOT work, and anybody else trying to kill him will be allowed to kill him, therefore not exposing him as Marco if somebody else tried to kill him first.'

    class Marlowe:
        roleDict = {'roleID' : 'Marlowe'}

        roleDict['name'] = 'Marlowe Freudenberg'

        roleDict['shortName'] = 'Marlowe'

        roleDict['team'] = 'Soldiers'

        roleDict['rumblingTeam'] = 'yeageristBench'

        roleDict['isTitan'] = False

        roleDict['emoji'] = 1225263662734770307

        roleDict['secondaryEmoji'] = None

        roleDict['imageURL'] = None

        roleDict['secondaryImageURL'] = None

        roleDict['roleMessage'] = f'You have special training from the Military Police! As such, when players die, you will be able to perform basic searches of the corpses and identify their roles in addition to who killed them.\n\n'

        roleDict['gameRole'] = ':police_car:Detective:police_car:'

        roleDict['helpInfo'] = 'Marlowe was a member of the Military Police before coming over to the Scouts. Thanks to this, he has some basic crime scene investigatory skills. When players die, he will know their roles and who killed them.'
    
    class Hannes:
        roleDict = {'roleID' : 'Hannes'}

        roleDict['name'] = 'Hannes'

        roleDict['shortName'] = 'Hannes'

        roleDict['team'] = 'Soldiers'

        roleDict['rumblingTeam'] = 'yeageristBench'

        roleDict['isTitan'] = False

        roleDict['emoji'] = 1225274587663831040

        roleDict['secondaryEmoji'] = None

        roleDict['imageURL'] = None

        roleDict['secondaryImageURL'] = None

        roleDict['roleMessage'] = f'Unfortunately... You are mostly known for running away. But fortunately, running away is a skill. Once per game, on an expedition, you will have the ability to choose to `Escape`, which will keep the expedition going, but you will leave and escape it before it can continue. But be careful! Choosing this option WILL expose your role identity.\n\n'

        roleDict['gameRole'] = ':rocket:Escape Pod:rocket:'

        roleDict['helpInfo'] = 'Hannes is... Mostly known for running away from the smiling titan in season 1. But hey, running away is a skill! Once per game, while on an expo, Hannes can choose to `Escape`, which will allow him to leave the expedition. The expedition will still go on as usual, but he will not be in it. The advantage to this is that you can clear yourself of suspicion by showing what role you are, you lower the suspect list for any possible sabotagers, and you can avoid an untimely death!'
    
    class Pyxis:
        roleDict = {'roleID' : 'Pyxis'}

        roleDict['name'] = 'Dot Pyxis'

        roleDict['shortName'] = 'Pyxis'

        roleDict['team'] = 'Soldiers'

        roleDict['rumblingTeam'] = 'allianceFighter'

        roleDict['isTitan'] = False

        roleDict['emoji'] = 1225544954755940465

        roleDict['secondaryEmoji'] = str('🪢')

        roleDict['imageURL'] = None

        roleDict['secondaryImageURL'] = None

        roleDict['roleMessage'] = f'You are a commander of the Garrison Corps! Thanks to this, you have a lot of influence, and you have the authority to turn in other players for possible crimes. Use `{prefix}trial` to bring forth a list of the players that have been on an expedition and start a trial against one of them during the command phase of the game. After you do this, a vote will be called on their execution.\n\n'

        roleDict['gameRole'] = ':knot:Hangman:knot:'

        roleDict['helpInfo'] = 'Dot Pyxis is the commander of the Garrison corps! As a result, he has a lot of influence in the military\'s disciplinary structure. However, he is not in charge of their judicial system himself. Thanks to his influence, he can put one player who has been on an expedition on trial for a possible execution, but he himself cannot be the final judge. The players will serve as a jury and vote, if the vote passes, the player will be executed.'

    class Samuel:
        roleDict = {'roleID' : 'Samuel'}

        roleDict['name'] = 'Samuel L. Jackson'

        roleDict['shortName'] = 'Samuel'

        roleDict['team'] = 'Soldiers'

        roleDict['rumblingTeam'] = 'yeageristBench'

        roleDict['isTitan'] = False

        roleDict['emoji'] = 1226353088214859788

        roleDict['secondaryEmoji'] = str('🤡')

        roleDict['imageURL'] = None

        roleDict['secondaryImageURL'] = None

        roleDict['roleMessage'] = f'You are... I\'m just gonna be honest, you\'re incompetent. After round 1, you have a one-time special voting ability. If you click this ability, you will accept the expedition if it has a Warrior in it, and reject otherwise. Therefore, you will always make the wrong choice. This also extends to execution votes, where if the player is a warrior you would then actually reject the execution and accept if the player is not a warrior. You make the wrong decision regardless of the context. This can provide you with valuable info! Will you choose to take the gamble?\n\n'

        roleDict['gameRole'] = ':clown:Clown:clown:'

        roleDict['helpInfo'] = 'I\'M TIRED OF THESE MOTHERFUCKING WARRIORS ON THIS MOTHERFUCKING EXP- *ahem*. I apologize for that, that was some weird thing. Anyway. Samuel is... Not necessarily known for his competence. He is most known for dangling off the wall on Sasha\'s hook and immediately dying at the port battle. He has a special ability, after round 1, he can use a special kind of vote where he gets the wrong answer every time. If the expo has a warrior, he accepts, if it\'s completely safe, he rejects. HOWEVER. If he is voting on an execution, the rule is reversed. He only accepts if the person on trial is not a Warrior. The general rule is, this guy ALWAYS makes the wrong decision.'
    
    
    class Moblit:
        roleDict = {'roleID' : 'Moblit'}

        roleDict['name'] = 'Moblit Berner'

        roleDict['shortName'] = 'Moblit'

        roleDict['team'] = 'Soldiers'

        roleDict['rumblingTeam'] = 'allianceBench'

        roleDict['isTitan'] = False

        roleDict['emoji'] = 1376442089184821248

        roleDict['secondaryEmoji'] = str('🔍')

        roleDict['imageURL'] = None

        roleDict['secondaryImageURL'] = None

        roleDict['roleMessage'] = f'You are Hange\'s personal assistant and messenger, alongside being a member of the Engineering corps! As such, you have extensive records and documentations regarding essentially everything, in fact, you have so much of it that you can really only use your time to investigate one thing through the course of the game. Use `{prefix}analyze` to open up a menu, and you can analyze all your records to check to see if a player is a particular role or not!\n\n'

        roleDict['gameRole'] = ':dividers:Bureaucrat:dividers:'

        roleDict['helpInfo'] = 'Moblit is Hange\'s personal assistant, personal messenger, and a valuable member of the Engineering corps. As such, he has access to... Way too much freaking documentation, man. Bureaucracy is ~~the absolute fucking bane of my existence, the fuck is a jira~~ useful for creating a paper trail of just about everything. As such, once per game, he will be able to check to see if 1 player\'s role, is any particular role he chooses, with the exception that he CANNOT check to see if their identity is Eren.'

    class Frieda:
        roleDict = {'roleID' : 'Frieda'}

        roleDict['name'] = 'Frieda Reiss'

        roleDict['shortName'] = 'Frieda'

        roleDict['team'] = 'Soldiers'

        roleDict['rumblingTeam'] = 'allianceBench'

        roleDict['isTitan'] = True

        roleDict['emoji'] = 1376750362375229631

        roleDict['secondaryEmoji'] = str('✋')

        roleDict['imageURL'] = None

        roleDict['secondaryImageURL'] = None

        roleDict['roleMessage'] = f'You also are a Founding Titan!... But for some reason, aren\'t out to get kidnapped. Whatever, point being, once per game, you can use `{prefix}vow` BEFORE an expedition has been picked to select a player to vow, it will announce to the lobby that the player is vowed for that round, and they will not be able to pass the expedition if they are a Warrior, ensuring their honesty!\n\n'

        roleDict['gameRole'] = ':raised_hand:Vow Maker:raised_hand:'

        roleDict['helpInfo'] = 'Frieda is a founding Titan!... And... Well, her being kidnapped doesn\'t matter because... It just doesn\'t okay?! Thanks to her powers, however, she has the ability once per game to use the power of the founder to force a player to take a vow, this vow will be announced to the lobby and for the duration of that round, they will be UNABLE to pass an expedition as a Warrior, being forced into using sabotage or a special ability only, ensuring they are being outright and forthcoming with their honesty!' 
    
    class Rico:
        roleDict = {'roleID' : 'Rico'}

        roleDict['name'] = 'Rico Brzenska'

        roleDict['shortName'] = 'Rico'

        roleDict['team'] = 'Soldiers'

        roleDict['rumblingTeam'] = 'yeageristBench'

        roleDict['isTitan'] = False

        roleDict['emoji'] = 1376759011025752174

        roleDict['secondaryEmoji'] = str('🪤')

        roleDict['imageURL'] = None

        roleDict['secondaryImageURL'] = None

        roleDict['roleMessage'] = f'You are a member of the defensive Garrison corps! As such, you have expertise in building defenses. While on an expedition, you can use your expertise in building defenses to sneakily set a trap. From there, once you have set a trap, you can use `{prefix}trap` to target someone, such that your trap will spring on them, killing them if they try to break the wall! A bit like a mixture between Sasha and Petra. Your trap WILL be used regardless of if they were killed or not, so be sure to only have an active trap target when you want it to be used!\n\n'

        roleDict['gameRole'] = ':mouse_trap:Trapper:mouse_trap:'

        roleDict['helpInfo'] = f'Rico is a member of the Garrison Corps! As such, she has learned how to build defenses. When she is on an expedition, she can choose to use her expertise in constructing defenses to set a trap. Once this trap has been engaged, she can use `{prefix}trap` akin to Sasha\'s target mechanism to choose who to spring the trap on the next time they participate in an expedition! This trap will spring regardless, but it will only kill the target if they try to break the wall, like with Petra\'s ability.' 
    
    class Onyankopon:
        roleDict = {'roleID' : 'Onyankopon'}

        roleDict['name'] = 'Onyankopon'

        roleDict['shortName'] = 'Onyankopon'

        roleDict['team'] = 'Soldiers'

        roleDict['rumblingTeam'] = 'allianceFighter'

        roleDict['isTitan'] = False

        roleDict['emoji'] = 1377337095319977994

        roleDict['secondaryEmoji'] = str('🛩️')

        roleDict['imageURL'] = None

        roleDict['secondaryImageURL'] = None

        roleDict['roleMessage'] = f'You are a talented pilot! As such, when an expedition is ongoing, regardless if you are in it or not, you will have the choice to airdrop another player into the expedition! Use this to your tactical advantage by shipping in a strong defender (or a tactical nuke) when the situation seems dire! **IF YOU WANT TO FLY SOMEBODY INTO AN EXPO THAT YOU ARE ALREADY IN, MAKE SURE THAT YOU CHOOSE TO FLY BEFORE YOU CHOOSE WHAT TO DO ON THE EXPEDITION!**\n\n'

        roleDict['gameRole'] = ':airplane_small:Pilot:airplane_small:'

        roleDict['helpInfo'] = f'Onyankopon is a talented pilot. As such, when an expedition is ongoing, regardless if he is present or not, once per game, he will be able to elect to fly-in another player inside of the expedition, forcing them on! If he is smart, he could possibly save a wall by airdropping Levi, send in a nuke with Armin, or even drop in a Warrior to an already existing nuke!' 

    class Frecklemir:
        roleDict = {'roleID' : 'Frecklemir'}

        roleDict['name'] = 'Ymir Freckles'

        roleDict['shortName'] = 'Frecklemir'

        roleDict['team'] = 'Soldiers'

        roleDict['rumblingTeam'] = 'yeageristBench'

        roleDict['isTitan'] = True

        roleDict['emoji'] = 1218288982572400700

        roleDict['secondaryEmoji'] = 1377427508496044072

        roleDict['imageURL'] = None

        roleDict['secondaryImageURL'] = None

        roleDict['roleMessage'] = f'You are a holder of the Jaw Titan! As such, you can be viscious and brutal. An unlimited number of times per game, on the expedition, you will have the ability to maul and kill one of the other expedition members.\n\n'

        roleDict['gameRole'] = ':drop_of_blood:Mauler:drop_of_blood:'

        roleDict['helpInfo'] = f'Ymir is the holder of the Jaw Titan! As such, an unlimited number of times per games, while on the expedition, she will have the ability to maul and kill one of the expedition members with the power of her titan.' 

    class Anka:
        roleDict = {'roleID' : 'Anka'}

        roleDict['name'] = 'Anka Rheinberger'

        roleDict['shortName'] = 'Anka'

        roleDict['team'] = 'Soldiers'

        roleDict['rumblingTeam'] = 'yeageristBench'

        roleDict['isTitan'] = False

        roleDict['emoji'] = 1377618964833763494

        roleDict['secondaryEmoji'] = str('⚖️')

        roleDict['imageURL'] = None

        roleDict['secondaryImageURL'] = None

        roleDict['roleMessage'] = f'You are the assistant to Dot Pyxis, one of the highest authorities in Paradis! As such, you have the authority to hand out orders for demotion. Once per game, you can IRREVERSIBLY remove a player from the commander order permanently by utilizing `{prefix}demote` and choosing who to demote, during the Expedition picking phase of the game.\n\n'

        roleDict['gameRole'] = ':scales:Court Martialer:scales:'

        roleDict['helpInfo'] = f'Anka is the personal assistant of Dot Pyxis. As such, she has the authority to carry out and deliver orders in his stead. Once per game, she can use `{prefix}demote` during the Expedition picking phase of the game to permanently and irreversibly remove a player from the commander order.'

    class Mina:
        roleDict = {'roleID' : 'Mina'}

        roleDict['name'] = 'Mina Carolina'

        roleDict['shortName'] = 'Mina'

        roleDict['team'] = 'Soldiers'

        roleDict['rumblingTeam'] = 'yeageristBench'

        roleDict['isTitan'] = False

        roleDict['emoji'] = 1377640328521187408

        roleDict['secondaryEmoji'] = 1377640840549241002

        roleDict['imageURL'] = None

        roleDict['secondaryImageURL'] = None

        roleDict['roleMessage'] = f'You are a new cadet to the Paradisian Military! As such, you have little to offer in regards to actual tactical skill. The best you can offer, is using `{prefix}smoke` to fire Signal Flares of various smoke colors to try to signal to your team certain ideas based on the color! You get 1 cannister of each color of smoke: Green, Red, and Black.\n\n'

        roleDict['gameRole'] = ':fireworks:Smoke Signaler:fireworks:'

        roleDict['helpInfo'] = f'Mina is a new cadet to the Paradisian Military! As such... She can\'t really do anything besides fire her signal flare gun. But she CAN do that! She has three colors of smoke cannisters, Green, Red, and Black, with one cannister of each variant. She can use `{prefix}smoke` to fire the various signals to make signals for her team!'


    class Kitz:
        roleDict = {'roleID' : 'Kitz'}

        roleDict['name'] = 'Kitz Woermann'

        roleDict['shortName'] = 'Kitz'

        roleDict['team'] = 'Soldiers'

        roleDict['rumblingTeam'] = 'yeageristBench'

        roleDict['isTitan'] = True

        roleDict['emoji'] = 1384672380978204732

        roleDict['secondaryEmoji'] = None

        roleDict['imageURL'] = None

        roleDict['secondaryImageURL'] = None

        roleDict['roleMessage'] = f'You have some authority, but are an absolute freakin\' coward! Once per game, while Expeditions are being picked, you can use the `{prefix}order` command to order someone onto the expedition, forcing them onto the expedition! If you regret your choice, you may use the same command to cancel your order.\n\n'

        roleDict['gameRole'] = ':chicken:Cowardly Commander:chicken:'

        roleDict['helpInfo'] = f'Kitz is an absolute freaking chicken! However, thankfully for him, he does have a position of power. As such, once per game, he can use the `{prefix}order` command to choose one individual (including himself) to be forced into being picked for the Expedition, with all expo choices automatically starting with that player until the round is over.'

    
    class Soldier:
        roleDict = {'roleID' : 'Soldier'}

        roleDict['name'] = 'Soldier'

        roleDict['shortName'] = 'Soldier'

        roleDict['team'] = 'Soldiers'

        roleDict['rumblingTeam'] = 'allianceBench'

        roleDict['isTitan'] = False

        roleDict['emoji'] = str('🛡️')

        roleDict['secondaryEmoji'] = None

        roleDict['imageURL'] = 'https://cdn.discordapp.com/emojis/934488343343927367.webp?size=128&quality=lossless'

        roleDict['secondaryImageURL'] = None

        roleDict['roleMessage'] = f'You are an average Soldier. You do not possess any special abilities or supplemental information.'

        roleDict['gameRole'] = ':shield:Default Soldier:shield:'

        roleDict['helpInfo'] = f'The Soldier role is merely just a default Soldier, they essentially have no role.'

    class Zeke:
        roleDict = {'roleID' : 'Zeke'}

        roleDict['name'] = 'Zeke Yeager'

        roleDict['shortName'] = 'Zeke'

        roleDict['team'] = 'Warriors'

        roleDict['rumblingTeam'] = 'yeageristFighter'

        roleDict['isTitan'] = True

        roleDict['emoji'] = 1205673427311009863

        roleDict['secondaryEmoji'] = 1205674306177077328

        roleDict['imageURL'] = None

        roleDict['secondaryImageURL'] = None

        roleDict['roleMessage'] = f'Eren does not see you as a Warrior, in fact, you are the only Warrior to be hidden in this matter. Be mindful of this when deciding if you want to be flagrant about your identity as a Warrior or not. You may also use `{prefix}retreat` to end the expeditions early and cut straight to the kidnap phase, for that niche situation where it makes more sense just to get to kidnapping.'

        roleDict['gameRole'] = ':man_supervillain:Warchief:man_supervillain:'

        roleDict['helpInfo'] = f'Zeke is the warchief and team captain for the Warriors! He will not be seen as a Warrior by Eren, and is a mandatory role that appears every game. He is more important than just being invisible to the Coordinate, however. He alone has the ability to end the expedition rounds early and cut to the basement early if the situation looks grim!'  
    

    class Pieck:
        roleDict = {'roleID' : 'Pieck'}

        roleDict['name'] = 'Pieck Finger'

        roleDict['shortName'] = 'Pieck'

        roleDict['team'] = 'Warriors'

        roleDict['rumblingTeam'] = 'allianceFighter'

        roleDict['isTitan'] = True

        roleDict['emoji'] = 1205700461160701972

        roleDict['secondaryEmoji'] = 1205699056471375923

        roleDict['imageURL'] = None
        
        roleDict['secondaryImageURL'] = None

        roleDict['roleMessage'] = f'You are an expert inflitrator! As such, you have the ability to drop into the expedition voting and flip the results once. When properly used, this ability is incredibly powerful, so be wise in your use of it!\n\n'

        roleDict['gameRole'] = ':detective:Spy:detective:'

        roleDict['helpInfo'] = 'Pieck is great at inflitrating enemy lines undetected. Thanks to this spying ability, she has the ability to mess with the votes for an expedition once and flip them all! This is an incredibly powerful ability when used properly, as it can turn a rejected expo into a free wall for the Warriors!'


    class Reiner:
        roleDict = {'roleID' : 'Reiner'}

        roleDict['name'] = 'Reiner Braun'

        roleDict['shortName'] = 'Reiner'

        roleDict['team'] = 'Warriors'

        roleDict['rumblingTeam'] = 'allianceFighter'

        roleDict['isTitan'] = True

        roleDict['emoji'] = 1205702950593499198

        roleDict['secondaryEmoji'] = 1205702948533964870

        roleDict['imageURL'] = None
        
        roleDict['secondaryImageURL'] = None

        roleDict['roleMessage'] = 'You have extremely durable levels of armor. As such, You are unkillable! If a soldier tries to kill you, you will still be exposed, but you will be allowed to keep playing.\n\n'

        roleDict['gameRole'] = ':rock:Invincible Shield:rock:'

        roleDict['helpInfo'] = 'Reiner is the owner of the Armored Titan! Thanks to his impressive armor, he will not be able to be killed by killer Soldiers, however, he will still be exposed! The ability to stay in the game and keep your ability to vote and be a commander is important though, so make sure to support your comrades even if you are exposed!'

    class Bertholdt:
        roleDict = {'roleID' : 'Bertholdt'}

        roleDict['name'] = 'Bertholdt Hoover'

        roleDict['shortName'] = 'Bertholdt'

        roleDict['team'] = 'Warriors'

        roleDict['rumblingTeam'] = 'allianceFighter'

        roleDict['isTitan'] = True

        roleDict['emoji'] = 1205707375512920074

        roleDict['secondaryEmoji'] = 1205707556299874354

        roleDict['imageURL'] = None
        
        roleDict['secondaryImageURL'] = None

        roleDict['roleMessage'] = 'Your Titan can produce an immense amount of steam, as such, you have the ability to cloak how many x\'s there were in an expo if you so choose! This ability would gracefully allow for doubling, but be careful with how you use it. If it is used, the Soldiers would see it and will know Bert is in the expo! Making you look incredibly suspicious if you were on 2 blocked expos. In addition, a successful double without using this ability makes a double seem more implausible. Keep all of this in mind when you choose how to break the walls!\n\n'

        roleDict['gameRole'] = ':hotsprings:Sabotage Cloaker:hotsprings:'

        roleDict['helpInfo'] = 'Bertholdt is an owner of the Colossal Titan! Thanks to this, he is able to completely cloak the evidence of what transpired on an expedition thanks to an immense cloud of steam blocking the view and immense heat burning away key evidence. Because of this, when he chooses to hide evidence, the Soldiers won\'t know how many Warriors sabotaged the expedition! Just that it got broken.'

    class Annie:
        roleDict = {'roleID' : 'Annie'}

        roleDict['name'] = 'Annie Leonhart'

        roleDict['shortName'] = 'Annie'

        roleDict['team'] = 'Warriors'

        roleDict['rumblingTeam'] = 'allianceFighter'

        roleDict['isTitan'] = True

        roleDict['emoji'] = 1205712075587063878

        roleDict['secondaryEmoji'] = 1205713542720782337

        roleDict['imageURL'] = None
        
        roleDict['secondaryImageURL'] = None

        roleDict['roleMessage'] = f'Your titan has a unique screaming ability! In order to use it, use the `{prefix}scream` command to send a message to all of your Warrior comrades up to once per round! When you use this ability, an alert will be shown in the home channel.\n\n'

        roleDict['gameRole'] = ':speaking_head:Screaming Titan:speaking_head:'

        roleDict['helpInfo'] = 'Annie is the owner of the Female Titan! One of this titan\'s abilities is its scream can be used to attract titans. However, it can also be used to convey hidden messages! Once per round, Annie can send a message to all of the Warriors, and the Soldiers will only know that a message was sent, but not what it was!'

    class Porco:
        roleDict = {'roleID' : 'Porco'}

        roleDict['name'] = 'Porco Galliard'

        roleDict['shortName'] = 'Porco'

        roleDict['team'] = 'Warriors'

        roleDict['rumblingTeam'] = 'allianceFighter'

        roleDict['isTitan'] = True

        roleDict['emoji'] = 1205716688268435506

        roleDict['secondaryEmoji'] = None

        roleDict['imageURL'] = None
        
        roleDict['secondaryImageURL'] = None

        roleDict['roleMessage'] = f'You are the "Shut-Your-Jaw" Titan! Use `{prefix}gag` to open the menu to choose to gag a player. When a player is gagged, they are not able to speak and their commander turn gets skipped! However, there is an important exception! A flared Erwin is ungaggable. In addition, you can use `{prefix}ungag` to remove the gag. This will NOT allow you to gag somebody else or refund your ability in any way.\n\n'

        roleDict['gameRole'] = ':shushing_face:Gag Orderer:shushing_face:'

        roleDict['helpInfo'] =  'Porco, the owner of the "Shut-Your-Jaw" Titan ~~dear god I have fucking lost it please just end my misery~~ can gag a player so they are not able to speak for an entire round. Their turn in the commander order also gets skipped, so this ability can be quite powerful. However, there are important exceptions and wrinkles to understand. First, a flared Erwin is ungaggable, there is nothing you can do to contain him. Next, a gagged player is NOT confirmed good, Porco has the ability to gag a Warrior or even himself to do a little trolling and trick the Soldiers. Hitch is not notified about this ability!'

    class Falco:
        roleDict = {'roleID' : 'Falco'}

        roleDict['name'] = 'Falco Grice'

        roleDict['shortName'] = 'Falco'

        roleDict['team'] = 'Warriors'

        roleDict['rumblingTeam'] = 'allianceFighter'

        roleDict['isTitan'] = True

        roleDict['emoji'] = 1205718045037961336

        roleDict['secondaryEmoji'] = None

        roleDict['imageURL'] = None
        
        roleDict['secondaryImageURL'] = None

        roleDict['roleMessage'] = 'You often find yourself around letters, so you will have the ability to do a special kind of a vote on the expedition ONCE. This vote works such that, if the expedition would pass if you accepted it, it will make you accept, otherwise, you will reject. This can be a game winning play if used tactically!\n\n'

        roleDict['gameRole'] = ':mailbox:Mail Interceptor:mailbox:'

        roleDict['helpInfo'] =  'Falco spends a lot of time with mail and the letters thanks to Eren\'s shenanigans. As such, he has learned how to intercept letters and receive notice as what is to come. Thanks to this, he has the 1 time ability to use a special vote when voting for an expedition proposal. What this vote will do, is that it will reject the expedition UNLESS it would pass with your vote! This ability is powerful when used properly, as it allows you the chance to accept one of your teammates, while not blowing your cover if it fails!'

    class Colt:
        roleDict = {'roleID' : 'Colt'}

        roleDict['name'] = 'Colt Grice'

        roleDict['shortName'] = 'Colt'

        roleDict['team'] = 'Warriors'

        roleDict['rumblingTeam'] = 'allianceBench'

        roleDict['isTitan'] = False

        roleDict['emoji'] = 1376887889253629962

        roleDict['secondaryEmoji'] = None

        roleDict['imageURL'] = None
        
        roleDict['secondaryImageURL'] = None

        roleDict['roleMessage'] = 'You are being trained as the new Warchief in the Warriors corps! As part of your training, you have been extensively given communications links to rapidly communicate with your teammates. Because of this, you will know all of their roles, they will know you, and you will receive frequent updates on their actions, being alerted to all their votes and ability usages!'

        roleDict['gameRole'] = ':military_helmet:Captain:military_helmet:'

        roleDict['helpInfo'] =  'Colt Grice is being trained as a new leader in the Warriors corps! Thanks to being prepared for leadership, he has comm-links and the ability to rapidly communicate with all his teammates, thanks to this ability, he will know all of his teammates roles, his teammates will know he is Colt, and he will receive updates on the actions of his Warrior comrades, getting alerts on their votes and ability usages!'

    class Magath:
        roleDict = {'roleID' : 'Magath'}

        roleDict['name'] = 'Theo Magath'

        roleDict['shortName'] = 'Magath'

        roleDict['team'] = 'Warriors'

        roleDict['rumblingTeam'] = 'allianceFighter'

        roleDict['isTitan'] = False

        roleDict['emoji'] = 1206505938606100521

        roleDict['secondaryEmoji'] = str('⚔️')

        roleDict['imageURL'] = None
        
        roleDict['secondaryImageURL'] = None

        roleDict['roleMessage'] = 'You are the Commander of the Marleyian military! Up your sleeve, you have a terrible card... Your final order. When an expedition you are not in is being proposed, you can sacrifice yourself, dying on the spot, to ensure that every Warrior accepts the expedition.'

        roleDict['gameRole'] = ':military_medal:Commander:military_medal:'

        roleDict['helpInfo'] =  'Theo Magath is the Commander of the Marleyian military, and he has a disgusting card up his sleeve... His final order. When there is an expedition being proposed he is not present in, he can choose to sacrifice himself, dying instantly on the spot, but ensuring that all the Warriors accept the proposal.'


    class Gabi:
        roleDict = {'roleID' : 'Gabi'}

        roleDict['name'] = 'Gabi Braun'

        roleDict['shortName'] = 'Gabi'

        roleDict['team'] = 'Warriors'

        roleDict['rumblingTeam'] = 'allianceFighter'

        roleDict['isTitan'] = False

        roleDict['emoji'] = 1218690811630456922

        roleDict['secondaryEmoji'] = str('🎯')

        roleDict['imageURL'] = None
        
        roleDict['secondaryImageURL'] = None

        roleDict['roleMessage'] = f'You are a ranged weapons specialist! At any time, you can use `{prefix}fire` to open a menu to select a player to target. At the end of any expo, regardless if they are on the expo or not, you will fire a shot that wounds that player. A wounded player will not be able to be picked for the expedition for a round.\n\n'

        roleDict['gameRole'] = ':gun:Marksman:gun:'

        roleDict['helpInfo'] =  f'The worst character on the face of the planet, if I had my way they would instantly lose as soon as they start the game. Unfortunately... That wouldn\'t make for a very good role. Gabi is a ranged weapons "expert" and can somehow wield weapons that outweigh her by 5x expertly. Gabi can use `{prefix}fire` to open a menu to choose a player to fire upon. Then, when the next results are read, she will fire a shot that wounds the player. A wounded player cannot be chosen for an expedition for a round.'

    class Willy:
        roleDict = {'roleID' : 'Willy'}

        roleDict['name'] = 'Willy Tybur'

        roleDict['shortName'] = 'Willy'

        roleDict['team'] = 'Warriors'

        roleDict['rumblingTeam'] = 'allianceFighter'

        roleDict['isTitan'] = False

        roleDict['emoji'] = 1225288761810747423

        roleDict['secondaryEmoji'] = 1225289648268509327

        roleDict['imageURL'] = None
        
        roleDict['secondaryImageURL'] = None

        roleDict['roleMessage'] = f'You are the shadowy figure behind the Marleyian Government! You are devoted to seeing this out through the end. As such, once in an expo (and for the rest of your life), you will have the option to sacrifice your life to kill somebody else!\n\n'

        roleDict['gameRole'] = ':bomb:Suicide Bomber:bomb:'

        roleDict['helpInfo'] =  f'Willy is the shadowy figure behind the Marleyian Government! He also has great devotion to seeing this operation out through the end. Thanks to this, once a game, and for the rest of his life for that matter, inside the expo he will have the option to sacrifice himself in order to kill somebody else.'
    
    class Yelena:
        roleDict = {'roleID' : 'Yelena'}

        roleDict['name'] = 'Yelena'

        roleDict['shortName'] = 'Yelena'

        roleDict['team'] = 'Warriors'

        roleDict['rumblingTeam'] = 'yeageristBench'

        roleDict['isTitan'] = False

        roleDict['emoji'] = 1225304583882932234

        roleDict['secondaryEmoji'] = None

        roleDict['imageURL'] = None
        
        roleDict['secondaryImageURL'] = None

        roleDict['roleMessage'] = f'You have inflitrated Paradis for Zeke! As such, you have tampered with their voting system ahead of time. Once per game, you will be able to choose to choose a player\'s vote to steal when voting on an expo. When you select this option, you will vote whatever they did, and they will vote the opposite. If you use this ability on someone who rejected, they will now accept, but you will reject in turn.\n\n'

        roleDict['gameRole'] = ':moneybag:Vote Thief:moneybag:'

        roleDict['helpInfo'] =  f'**Credit to Space (JustAboutEnoughSpace) for this role!**\n\nThe Soldiers gave Yelena the ability to run around Paradis. Big Mistake. As it turns out, she is uniquely personally loyal to Zeke. Therefore, has had plenty of time to tamper with the Soldiers\' voting systems. Once per game, she can steal the vote of another player, switching that player\'s vote with the opposite of which they voted'


    class Warhammer:
        roleDict = {'roleID' : 'Warhammer'}

        roleDict['name'] = 'The Warhammer Titan'

        roleDict['shortName'] = 'Warhammer'

        roleDict['team'] = 'Warriors'

        roleDict['rumblingTeam'] = 'allianceFighter'

        roleDict['isTitan'] = True

        roleDict['emoji'] = 1226421467261177947

        roleDict['secondaryEmoji'] = 1226421467261177947

        roleDict['imageURL'] = None
        
        roleDict['secondaryImageURL'] = None

        roleDict['roleMessage'] = f'You are an absolute War Machine! Once, you have the ability to utilize a soldier\'s ability. Jean, Hange, Mikasa, Frieda and Keith are forbidden, and all killer abilities can only kill your fellow Warriors. In addition to the voting and expo abilities, you have access to\n`{prefix}target` to use Sasha\'s ability\n`{prefix}trial` to use Pyxis\' ability\n`{prefix}flare` to use Erwin\'s ability\n`{prefix}trap` to use Rico\'s ability (No Trap-setting necessary!)\n`{prefix}demote` to use Anka\'s ability\n`{prefix}smoke` to use Mina\'s ability\n\n'

        roleDict['gameRole'] = ':headstone:Weapons Expert:headstone:'

        roleDict['helpInfo'] =  f'A War Machine, a Monster, the God of War itself. The Warhammmer has the ability to use it\'s hardening to conjure up whatever weapons it wants. This player has the chance to use any single soldier\'s special ability, vote, or expo act once. There are exceptions of Jean, Hange, Mikasa, Freida, Onyankopon, Moblit, and Keith. Any killing soldier abilities it uses can only kill Warriors. Hange and Hitch will be alerted as to their true nature if their ability usage would notify them.'    

    class Marcel:
        roleDict = {'roleID' : 'Marcel'}

        roleDict['name'] = 'Marcel Galliard'

        roleDict['shortName'] = 'Marcel'

        roleDict['team'] = 'Warriors'

        roleDict['rumblingTeam'] = 'allianceFighter'

        roleDict['isTitan'] = True

        roleDict['emoji'] = 1376912725988605952

        roleDict['secondaryEmoji'] = None

        roleDict['imageURL'] = None
        
        roleDict['secondaryImageURL'] = None

        roleDict['roleMessage'] = f'You are the famously long dead baby version of the Shut-Your-Jaw Titan! As such, when a soldier dies, they will be unable to speak, you make the DEAD shut their jaw. You don\'t have to do anything to activate this ability, it is a passively active abiltiy that is always on.\n\n'

        roleDict['gameRole'] = ':zipper_mouth:Ghostbuster:zipper_mouth:'

        roleDict['helpInfo'] =  f'Marcel is a famously long dead baby version of the Shut-Your-Jaw Titan! Fittingly, when a soldier dies with this Warrior in the field, they will be unable to speak, Marcel makes the DEAD shut their jaw.'    


    class Ksaver:
        roleDict = {'roleID' : 'Ksaver'}

        roleDict['name'] = 'Tom Ksaver'

        roleDict['shortName'] = 'Ksaver'

        roleDict['team'] = 'Warriors'

        roleDict['rumblingTeam'] = 'allianceBench'

        roleDict['isTitan'] = True

        roleDict['emoji'] = 1381784284066611252

        roleDict['secondaryEmoji'] = str('✴️')

        roleDict['imageURL'] = None
        
        roleDict['secondaryImageURL'] = None

        roleDict['roleMessage'] = f'You are a top scientist of Marley! As such, you have developed tools for jamming communications technology! Once per game, in an expo, you can choose the "Blackout" option, which will sabotage the wall AND hide the voting results of the immediate next rounds.\n\n'

        roleDict['gameRole'] = ':eight_pointed_black_star:Blackout:eight_pointed_black_star:'

        roleDict['helpInfo'] =  f'Tom Ksaver is one of the top scientists of Marley! As such, he has developed anti-communications technology. Once per game, during the expo he can choose the "Blackout" option, which will break the wall and make it so voting results the immediate following round will not be visible!'

    class Warrior:
        roleDict = {'roleID' : 'Warrior'}

        roleDict['name'] = 'Warrior'

        roleDict['shortName'] = 'Warrior'

        roleDict['team'] = 'Warriors'

        roleDict['rumblingTeam'] = 'allianceBench'

        roleDict['isTitan'] = False

        roleDict['emoji'] = str('⚔️')

        roleDict['secondaryEmoji'] = None

        roleDict['imageURL'] = 'https://cdn.discordapp.com/emojis/934488802213384292.webp?size=128&quality=lossless'

        roleDict['secondaryImageURL'] = None

        roleDict['roleMessage'] = f'You are an average Warrior. You do not possess any special abilities to aid you in breaking the walls.'

        roleDict['gameRole'] = ':crossed_swords:Default Warrior:crossed_swords:'

        roleDict['helpInfo'] = f'The Warrior role is merely just a default Warrior, they essentially have no role.'

    class Kenny:
        roleDict = {'roleID' : 'Kenny'}

        roleDict['name'] = 'Kenny Ackermann'

        roleDict['shortName'] = 'Kenny'

        roleDict['team'] = 'Wildcards'

        roleDict['rumblingTeam'] = 'yeageristBench'

        roleDict['isTitan'] = False

        roleDict['emoji'] = 1218103275782410360

        roleDict['secondaryEmoji'] = '🔪'

        roleDict['imageURL'] = None

        roleDict['secondaryImageURL'] = None

        roleDict['roleMessage'] = f'You are a serial killer! You do not give a singular shit about the status of the walls. Your objective is simple. Get on expos. Murder at least 2 players. If you can achieve this, you win.\n\n'

        roleDict['gameRole'] = ':knife:Serial Killer:knife:'

        roleDict['helpInfo'] = f'Kenny Ackermann is a serial killer. He does not care if the walls break or not, he wins through one glorious way. Murder. When he gets on an expo, he has the ability to kill another player on the expo. If he can kill at least 2 people in a match, he wins.'


    class PureTitan:
        roleDict = {'roleID' : 'PureTitan'}

        roleDict['name'] = 'Pure Titan'

        roleDict['shortName'] = 'Pure Titan'

        roleDict['team'] = 'Wildcards'

        roleDict['rumblingTeam'] = 'yeageristBench'

        roleDict['isTitan'] = True

        roleDict['emoji'] = 1205684706431991818

        roleDict['secondaryEmoji'] = None

        roleDict['imageURL'] = None

        roleDict['secondaryImageURL'] = None

        roleDict['roleMessage'] = f'Whoever ends the game with this role will lose! But fret not, you can shed yourself of this role! When on an expedition with another titan, it is possible for you to eat them, and then steal their role, giving the person you ate the Pure Titan role! Find a new role and claim victory before it\'s too late!\n\n'

        roleDict['gameRole'] = ':potato:Hot Potato:potato:'

        roleDict['helpInfo'] = f'Whoever is the Pure Titan at the end of the game, will instantly lose. However, they have an opportunity to lose this role. When on an expo with another titan, they can eat that player and change roles with them. Inheriting a new role, and giving the eaten player this role.'

    class Ymir:
        roleDict = {'roleID' : 'Ymir'}

        roleDict['name'] = 'Founder Ymir'

        roleDict['shortName'] = 'Ymir'

        roleDict['team'] = 'Wildcards'

        roleDict['rumblingTeam'] = 'yeageristBench'

        roleDict['isTitan'] = True

        roleDict['emoji'] = 1218401634556710972

        roleDict['secondaryEmoji'] = None

        roleDict['imageURL'] = None

        roleDict['secondaryImageURL'] = None

        roleDict['roleMessage'] = f'To you, 2000 years from now...\n\nYou are the Founder Ymir. You cannot directly participate in expeditions. There is someone out there you are waiting for... But you aren\'t sure who. Or what decisions they will make. Use `{prefix}paths` to utilize PATHS to open the menu with your powers to assist the player you are guiding. If they win, you win. Your fates are tied. Guide them to victory.'

        roleDict['gameRole'] = ':milky_way:Pathfinder:milky_way:'

        roleDict['helpInfo'] = f'Founder Ymir is unable to participate in expeditions. A random person that she does not know the name of will be chosen, her objective is to guide that person to victory. She can use PATHS to communicate with them, revive a dead player, or grant somebody her blessing. She must work her way to that person she has been waiting for... All this time.'

    def getErenInfo(currentGame):
        erenInfo = 'The Warriors are:\n'
        warriorList = currentGame.warriors.copy()
        warriorList = random.sample(warriorList, len(warriorList))
        for warrior in warriorList:
            if warrior.role.id != 'Zeke':
                erenInfo += f'**{warrior.user.name}**'
                if warriorList.index(warrior) != len(warriorList) -1:
                    erenInfo += '\n'
        return erenInfo
    
    def getHistoriaInfo(currentGame):
        historiaInfo = 'The Yeager Brothers are:\n'
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
        warriorInfo = 'Your fellow Warriors are:\n'
        warriorList = currentGame.warriors.copy()
        if currentGame.niccoloDecoy != None:
            warriorList.append(currentGame.niccoloDecoy)
        warriorList = random.sample(warriorList, len(warriorList))
        for warrior in warriorList:
            if player.user.name != warrior.user.name:
                if player.role.id != 'Colt':
                    if warrior.role.id != 'Colt':
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
        return f'The identity of **Levi Ackermann** has been revealed to be **{Levi.user.name}**!'
    
    def getErwinMessage(Erwin):
        return f'I, {Erwin.user.mention}, am activating a signal flare!'
    
    def getFriedaMessage(currentGame):
        return f'{currentGame.friedaVowedPlayer.user.mention}, your true colors will be revealed.'
    
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
                    arminDeathMessages += f'{Mikasa.role.emoji} Mikasa saved **{key.user.name}** from the Blast!{Mikasa.role.emoji}\n\n'
        if type(currentGame.currentExpo.reinerBlocked) == dict:
            for key, value in currentGame.currentExpo.reinerBlocked.items():
                if value == 'Armin':
                    arminDeathMessages += f'{Reiner.role.secondaryEmoji}**{key.user.name}** Survived the Blast!{Reiner.role.secondaryEmoji}\n\n'
        return arminDeathMessages
    
    def getLeviDeathMessages(currentGame, currentTheme, Levi, Mikasa, Reiner):
        leviDeathMessages = ''
        for killedPlayer, causeOfDeath in Levi.killed.items():
            if causeOfDeath == 'Levi':
                leviDeathMessages += f'**{killedPlayer.user.name}** was slain by Levi!\n'
                if killedPlayer in currentGame.soldiers:
                    leviDeathMessages += f'They were a {currentTheme.emojiSoldier}**{currentTheme.soldierSingle}**{currentTheme.emojiSoldier}!\n\n'
                elif killedPlayer in currentGame.warriors:
                    leviDeathMessages += f'They were a {currentTheme.emojiWarrior}**{currentTheme.warriorSingle}**{currentTheme.emojiWarrior}!\n\n'
                elif killedPlayer in currentGame.wildcards:
                    leviDeathMessages += f'They were a {currentTheme.emojiWildcard}**{currentTheme.wildcardSingle}**{currentTheme.emojiWildcard}!\n\n'
        if type(currentGame.mikasaGuarded) == dict:
            for key, value in currentGame.mikasaGuarded.items():
                if value == 'Levi':
                    leviDeathMessages += f'**{key.user.name}** was attacked by Levi!\n{Mikasa.role.emoji}But was protected by Mikasa!{Mikasa.role.emoji}\n\n'
        if type(currentGame.currentExpo.reinerBlocked) == dict:
            for key, value in currentGame.currentExpo.reinerBlocked.items():
                if value == 'Levi':
                    leviDeathMessages += f'{Reiner.role.secondaryEmoji}**{key.user.name}**\'s Armor protected them from Levi\'s onslaught!{Reiner.role.secondaryEmoji}\n\n'
        return leviDeathMessages
    
    def getPetraDeathMessages(currentGame, currentTheme, Petra, Mikasa, Reiner):
        petraDeathMessages = ''
        for killedPlayer, causeOfDeath in Petra.killed.items():
            if causeOfDeath == 'Petra':
                petraDeathMessages += f'**{killedPlayer.user.name}** was slain by Petra!\n'
                if killedPlayer in currentGame.soldiers:
                    petraDeathMessages += f'They were a {currentTheme.emojiSoldier}**{currentTheme.soldierSingle}**{currentTheme.emojiSoldier}!\n\n'
                elif killedPlayer in currentGame.warriors:
                    petraDeathMessages += f'They were a {currentTheme.emojiWarrior}**{currentTheme.warriorSingle}**{currentTheme.emojiWarrior}!\n\n'
                elif killedPlayer in currentGame.wildcards:
                    petraDeathMessages += f'They were a {currentTheme.emojiWildcard}**{currentTheme.wildcardSingle}**{currentTheme.emojiWildcard}!\n\n'
        if type(currentGame.mikasaGuarded) == dict:
            for key, value in currentGame.mikasaGuarded.items():
                if value == 'Petra':
                    petraDeathMessages += f'**{key.user.name}** was attacked by Petra!\n{Mikasa.role.emoji}But was protected by Mikasa!{Mikasa.role.emoji}\n\n'
        if type(currentGame.currentExpo.reinerBlocked) == dict:
            for key, value in currentGame.currentExpo.reinerBlocked.items():
                if value == 'Petra':
                    petraDeathMessages += f'{Reiner.role.secondaryEmoji}**{key.user.name}**\'s Armor protected them from Petra\'s attack!{Reiner.role.secondaryEmoji}\n\n'
        return petraDeathMessages
    
    def getFrecklemirDeathMessages(currentGame, currentTheme, Frecklemir, Mikasa, Reiner):
        frecklemirDeathMessages = ''
        for killedPlayer, causeOfDeath in Frecklemir.killed.items():
            frecklemirDeathMessages = ''
            if causeOfDeath == 'Frecklemir':
                frecklemirDeathMessages += f'**{killedPlayer.user.name}** was mauled by Ymir!\n'
                if killedPlayer in currentGame.soldiers:
                    frecklemirDeathMessages += f'They were a {currentTheme.emojiSoldier}**{currentTheme.soldierSingle}**{currentTheme.emojiSoldier}!\n\n'
                elif killedPlayer in currentGame.warriors:
                    frecklemirDeathMessages += f'They were a {currentTheme.emojiWarrior}**{currentTheme.warriorSingle}**{currentTheme.emojiWarrior}!\n\n'
                elif killedPlayer in currentGame.wildcards:
                    frecklemirDeathMessages += f'They were a {currentTheme.emojiWildcard}**{currentTheme.wildcardSingle}**{currentTheme.emojiWildcard}!\n\n'
        if type(currentGame.mikasaGuarded) == dict:
            for key, value in currentGame.mikasaGuarded.items():
                if value == 'Frecklemir':
                    frecklemirDeathMessages += f'**{key.user.name}** was the target of a mauling by Ymir!\n{Mikasa.role.emoji}But was protected by Mikasa!{Mikasa.role.emoji}\n\n'
        if type(currentGame.currentExpo.reinerBlocked) == dict:
            for key, value in currentGame.currentExpo.reinerBlocked.items():
                if value == 'Frecklemir':
                    frecklemirDeathMessages += f'{Reiner.role.secondaryEmoji}**{key.user.name}**\'s Armor protected them from Ymir\'s mauling!{Reiner.role.secondaryEmoji}\n\n'
        return frecklemirDeathMessages
    
    def getRicoDeathMessages(currentGame, currentTheme, Rico, Mikasa, Reiner):
        ricoDeathMessages = ''
        for killedPlayer, causeOfDeath in Rico.killed.items():
            if causeOfDeath == 'Rico':
                ricoDeathMessages += f'**{killedPlayer.user.name}** was caught by Rico\'s trap!\n'
                if killedPlayer in currentGame.soldiers:
                    ricoDeathMessages += f'They were a {currentTheme.emojiSoldier}**{currentTheme.soldierSingle}**{currentTheme.emojiSoldier}!\n\n'
                elif killedPlayer in currentGame.warriors:
                    ricoDeathMessages += f'They were a {currentTheme.emojiWarrior}**{currentTheme.warriorSingle}**{currentTheme.emojiWarrior}!\n\n'
                elif killedPlayer in currentGame.wildcards:
                    ricoDeathMessages += f'They were a {currentTheme.emojiWildcard}**{currentTheme.wildcardSingle}**{currentTheme.emojiWildcard}!\n\n'
        if type(currentGame.mikasaGuarded) == dict:
            for key, value in currentGame.mikasaGuarded.items():
                if value == 'Rico':
                    ricoDeathMessages += f'**{key.user.name}** was caught in Rico\'s trap!\n{Mikasa.role.emoji}But was protected by Mikasa!{Mikasa.role.emoji}\n\n'
        if type(currentGame.currentExpo.reinerBlocked) == dict:
            for key, value in currentGame.currentExpo.reinerBlocked.items():
                if value == 'Rico':
                    ricoDeathMessages += f'{Reiner.role.secondaryEmoji}**{key.user.name}**\'s Armor protected them from Rico\'s trap!{Reiner.role.secondaryEmoji}\n\n'
        return ricoDeathMessages
    
    def getSashaDeathMessages(currentGame, currentTheme, Sasha, Mikasa, Reiner, realSasha=None):
        if realSasha == None:
            secEmo = Sasha.role.secondaryEmoji
        else:
            secEmo = realSasha.secondaryEmoji
        sashaDeathMessages = ''
        for killedPlayer, causeOfDeath in Sasha.killed.items():
            if causeOfDeath == 'Sasha':
                sashaDeathMessages += f'{secEmo}**{killedPlayer.user.name}** was struck by Sasha\'s Arrow!{secEmo}\n'
                if killedPlayer in currentGame.soldiers:
                    sashaDeathMessages += f'They were a {currentTheme.emojiSoldier}**{currentTheme.soldierSingle}**{currentTheme.emojiSoldier}!\n\n'
                elif killedPlayer in currentGame.warriors:
                    sashaDeathMessages += f'They were a {currentTheme.emojiWarrior}**{currentTheme.warriorSingle}**{currentTheme.emojiWarrior}!\n\n'
                elif killedPlayer in currentGame.wildcards:
                    sashaDeathMessages += f'They were a {currentTheme.emojiWildcard}**{currentTheme.wildcardSingle}**{currentTheme.emojiWildcard}!\n\n'
        if type(currentGame.mikasaGuarded) == dict:
            for key, value in currentGame.mikasaGuarded.items():
                if value == 'Sasha':
                    sashaDeathMessages += f'{Mikasa.role.emoji}Mikasa deflected Sasha\'s Arrow away from **{key.user.name}**!{Mikasa.role.emoji}\n\n'
        if type(currentGame.currentExpo.reinerBlocked) == dict:
            for key, value in currentGame.currentExpo.reinerBlocked.items():
                if value == 'Sasha':
                    sashaDeathMessages += f'{Reiner.role.secondaryEmoji}The Arrow merely bounced off **{key.user.name}**\'s Armor!{Reiner.role.secondaryEmoji}\n\n'
        return sashaDeathMessages
    
    def getMarcoDeathMessages(currentGame, currentTheme, Marco):
        marcoDeathMessages = ''
        for killedPlayer, causeOfDeath in Marco.killed.items():
            if causeOfDeath == 'Marco':
                marcoDeathMessages += f'{Marco.role.secondaryEmoji}**{killedPlayer.user.name}** was was eaten by the Titans!{Marco.role.secondaryEmoji}\n'
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
            secEmo = realPyxis.secondaryEmoji
        pyxisDeathMessages = ''
        for killedPlayer, causeOfDeath in Pyxis.killed.items():
            if causeOfDeath == 'Pyxis':
                pyxisDeathMessages += f'{secEmo}**{killedPlayer.user.name}** has been condemned by the jury to hang!{secEmo}\n'
                if killedPlayer in currentGame.soldiers:
                    pyxisDeathMessages += f'They were a {currentTheme.emojiSoldier}**{currentTheme.soldierSingle}**{currentTheme.emojiSoldier}!\n\n'
                elif killedPlayer in currentGame.warriors:
                    pyxisDeathMessages += f'They were a {currentTheme.emojiWarrior}**{currentTheme.warriorSingle}**{currentTheme.emojiWarrior}!\n\n'
                elif killedPlayer in currentGame.wildcards:
                    pyxisDeathMessages += f'They were a {currentTheme.emojiWildcard}**{currentTheme.wildcardSingle}**{currentTheme.emojiWildcard}!\n\n'
        if type(currentGame.mikasaGuarded) == dict:
            for key, value in currentGame.mikasaGuarded.items():
                if value == 'Pyxis':
                    pyxisDeathMessages += f'{Mikasa.role.emoji}Mikasa has intervened to stop **{key.user.name}** from being hanged!{Mikasa.role.emoji}\n\n'
        if type(currentGame.currentExpo.reinerBlocked) == dict:
            for key, value in currentGame.currentExpo.reinerBlocked.items():
                if value == 'Pyxis':
                    pyxisDeathMessages += f'{Reiner.role.secondaryEmoji}**{key.user.name}** titanized and escaped hanging, their armor allowing them to survive the soldier\'s attacks!{Reiner.role.secondaryEmoji}\n\n'
        return pyxisDeathMessages
    
    def getKennyDeathMessages(currentGame, currentTheme, Kenny, Mikasa, Reiner):
        kennyDeathMessages = ''
        for killedPlayer, causeOfDeath in Kenny.killed.items():
            if killedPlayer not in currentGame.kennyDisplayedKills:
                if causeOfDeath == 'Kenny':
                    if killedPlayer == Kenny:
                        kennyDeathMessages += f'{Kenny.role.secondaryEmoji}**{killedPlayer.user.name}** has decided that they would rather kill themselves than deal with another second of your babbling.{Kenny.role.secondaryEmoji}\n'
                    else:
                        kennyDeathMessages += f'{Kenny.role.secondaryEmoji}**{killedPlayer.user.name}** was murdered by Kenny!{Kenny.role.secondaryEmoji}\n'
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
                    kennyDeathMessages += f'{Mikasa.role.emoji}Mikasa has protected **{key.user.name}** from being murdered by Kenny!{Mikasa.role.emoji}\n\n'
        if type(currentGame.currentExpo.reinerBlocked) == dict:
            for key, value in currentGame.currentExpo.reinerBlocked.items():
                if value == 'Kenny':
                    kennyDeathMessages += f'{Reiner.role.secondaryEmoji}Kenny\'s pitiful murder attempt was no match for **{key.user.name}**\'s Armor!{Reiner.role.secondaryEmoji}\n\n'
        return kennyDeathMessages
    
    def getWillyDeathMessages(currentGame, currentTheme, Willy, Mikasa, Reiner):
        willyDeathMessages = ''
        for killedPlayer, causeOfDeath in Willy.killed.items():
            if causeOfDeath == 'Willy':
                if killedPlayer.role.id == 'Willy':
                    willyDeathMessages += f'{Willy.role.secondaryEmoji}**{killedPlayer.user.name}** has sacrificed themselves!{Willy.role.secondaryEmoji}\n'
                else:
                    willyDeathMessages += f'{Willy.role.secondaryEmoji}**{killedPlayer.user.name}** has been killed by Willy!{Willy.role.secondaryEmoji}\n'
                if killedPlayer in currentGame.soldiers:
                    willyDeathMessages += f'They were a {currentTheme.emojiSoldier}**{currentTheme.soldierSingle}**{currentTheme.emojiSoldier}!\n\n'
                elif killedPlayer in currentGame.warriors:
                    willyDeathMessages += f'They were a {currentTheme.emojiWarrior}**{currentTheme.warriorSingle}**{currentTheme.emojiWarrior}!\n\n'
                elif killedPlayer in currentGame.wildcards:
                    willyDeathMessages += f'They were a {currentTheme.emojiWildcard}**{currentTheme.wildcardSingle}**{currentTheme.emojiWildcard}!\n\n'
        if type(currentGame.mikasaGuarded) == dict:
            for key, value in currentGame.mikasaGuarded.items():
                if value == 'Willy':
                    willyDeathMessages += f'{Mikasa.role.emoji}Mikasa has saved **{key.user.name}** from Willy\'s attack!{Mikasa.role.emoji}\n\n'
        if type(currentGame.currentExpo.reinerBlocked) == dict:
            for key, value in currentGame.currentExpo.reinerBlocked.items():
                if value == 'Willy':
                    willyDeathMessages += f'{Reiner.role.secondaryEmoji}Willy\'s traitorous attack was no match for **{key.user.name}**\'s Armor!{Reiner.role.secondaryEmoji}\n\n'
        return willyDeathMessages
    
    def getMagathDeathMessage(currentGame, currentTheme, Magath):
        return f'{Magath.role.emoji}**{Magath.user.name}** has sacrificed themselves to give their Final Order!{Magath.role.emoji}\nThey were a {currentTheme.emojiWarrior}**{currentTheme.warriorSingle}**{currentTheme.emojiWarrior}!\n\n'
    
    def getGabiWoundMessage(currentGame, currentTheme, Gabi):
        gabiWoundMessage = f'{Gabi.role.secondaryEmoji}Gabi has shot **{currentGame.woundedPlayer.user.name}**! They have been evacuated to the Field Hospital and will not be able to attend the next expedition!{Gabi.role.secondaryEmoji}\n\n'
        return gabiWoundMessage
    
    def getPlaneMessage(currentGame, Onyankopon, player):
        return f'{Onyankopon.role.secondaryEmoji}**{player.user.name}** has been flown into the Expedition!{Onyankopon.role.secondaryEmoji}\n\n'
    
    def getHealMessage(player):
        healMessage = f'{player.user.mention} has healed and returned to the fight!'
        return healMessage
    
    def getYmirRevivalMessage(currentGame, currentTheme, Ymir):
        ymirMessage = ''
        for player, clause in currentGame.ymirRevival.items():
            if clause:
                ymirMessage += f'{Ymir.role.emoji}The Founder Ymir has used the power of the Titans to revive **{player.user.name}** back from the dead!{Ymir.role.emoji}'
        return ymirMessage
    
    def getAnkaMessage(currentGame, Anka):
        if Anka.role.id == 'Anka':
            return f'**{currentGame.demotedPlayer.user.mention}**, you have been demoted!'
        else:
            return f'**{currentGame.warhammerAbility['Anka'].user.mention}**, you have been demoted!'
        
    def getKitzMessage(currentGame):
        return f'Y-y-y-y-you there, **{currentGame.kitzTarget.user.mention}**, fight in my stead!'
    
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

            

