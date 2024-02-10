#Please pay close attention to instructions when creating new theme classes.
#When creating new themes, you should only be trying to make COSMETIC changes. To truly add more roles or functionality to the game, you will need to do a lot more than change the theme.
#However, if you do create a new role, you will have to give them a theme in any themes you are using.
import os
from dotenv import load_dotenv
import discord
from discord.ext import commands
import random

#CHANGE THIS CLASS NAME. Your new file and your new class should NOT be named defaultGameTheme, each theme added should have different names.
class defaultGameTheme:
    global prefix

    prefix = os.getenv('BOT_PREFIX')


    #You have free reign to edit these as you please
    themeName = 'Default Warriors vs Soldiers'
    gameName = 'Warriors vs Soldiers'
    soldierSingle = 'Soldier'
    soldierPlural = 'Soldiers'
    emojiSoldier = str('🛡️')
    warriorSingle = 'Warrior'
    warriorPlural = 'Warriors'
    emojiWarrior = str('⚔️')
    wallSingle = 'Wall'
    wallPlural = 'Walls'
    #By Default is the same as Eren Emoji
    emojiTheme = 1205662731659780106
    titanSingle = 'Titan'
    titanPlural = 'Titans'
    emojiDead = '☠️'

    soldierThumbnail = 'https://cdn.discordapp.com/emojis/934488343343927367.webp?size=128&quality=lossless'
    warriorThumbnail = 'https://cdn.discordapp.com/emojis/934488802213384292.webp?size=128&quality=lossless'
    wildcardThumbnail ='https://cdn.discordapp.com/emojis/934489212277882932.webp?size=128&quality=lossless'

    soldierColor = discord.Color.blue()
    warriorColor = discord.Color.red()
    wildcardColor = discord.Color.gold()

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

    #Status Embed Aesthetics
    winningColor = discord.Color.green()
    neutralColor = discord.Color.gold()
    losingColor = discord.Color.red()
    lostColor = discord.Color.default()

    statusProgress = 'Progress towards Basement'
    statusWalls = 'Status of the Walls'
    statusExpeditions = 'Expedition Info'

    expeditionName = 'Expedition'
    expoMembersName = 'members'

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
    voteDMColor = discord.Color.blue()
    acceptedExpeditionColor = discord.Color.green()
    rejectedExpeditionColor = discord.Color.red()
    jeanedExpeditionColor = discord.Color.gold()
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
    endgameCardColor = discord.Color.blue()
    emojiWinner ='🏅'
    emojiLoser = '☠️'

    #Webhook Message Aesthetics
    jeanMessage = f'I\'m securing this Expedition!'
    pieckMessageWithJean = f'I tried to flip the votes, but I am not sure if I was able to successfully do so because of **Jean**!'
    pieckMessageWithoutJean = f'I flipped the votes!'
    arminMessage = f'I blew up the Expedition!'
    leviAttackMessage = f'I... Won\'t let a single one of you get away!'
    leviDefendMessage = f'I will defend this expedition at all costs!'
    sashaMessage = f'I have fired an arrow!'
    dazMessage = f'Waaaaaah! I\'m scared!'
    dazMessageFollowUp = 'The Expedition has been cancelled!'
    mikasaMessage = 'My guard is unbreakable...'
    reinerMessage = 'Marley\'s Shield is not broken so easily...'
    bertholdtMessage = 'I\'ll deploy a cloak of steam!'
    annieMessage = '***RAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA***'
    retreatMessage = 'I\'m ordering a retreat! Pull back from the assault on the walls, and allow the Soldiers to advance to the basement!'

    #Other role messages
    flochMessageEren = 'Eren Yeager is on the expedition team!'
    flochMessageNoEren = 'Eren Yeager is not on the expedition team.'

    #Timeout Messages
    timeoutCoreStart = 'You have '
    timeoutCoreEnd = ' left to'
    timeoutPick = ' pick your Expedition Team!'
    timeoutVote = ' vote on the Expedition Team!'
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

        roleDict['helpInfo'] = 'Historia is the queen of Paradis and has closer knowledge of the situation than most Soldiers due to being in communications with the Yeager brothers, but there was a mistake in the line! Now, she knows which 2 players are Eren and Zeke, but not which is which!'

    class Hange:
        roleDict = {'roleID' : 'Hange'}

        roleDict['name'] = 'Hange Zoë'

        roleDict['shortName'] = 'Hange'

        roleDict['team'] = 'Soldiers'

        roleDict['rumblingTeam'] = 'allianceFighter'

        roleDict['isTitan'] = False

        roleDict['emoji'] = 1205677240982183967

        roleDict['secondaryEmoji'] = None

        roleDict['imageURL'] = None

        roleDict['secondaryImageURL'] = None

        roleDict['roleMessage'] = f'At the end of each round, you will be given a statistical analysis on each player that can help you figure out who to trust! Be careful though, this statistical analysis is NOT 100% guaranteed, merely a game of probabilities, and it doesn\'t take into account more "human" sides to the game like who you think is lying.'

        roleDict['gameRole'] = ':bulb:Analyst:bulb:'

        roleDict['helpInfo'] = 'Hange is one of the more academically gifted members of the Survey Corps. Thanks to these abilities, it is very easy for her to identify statistical trends, and at the end of each round, will be given probabilities on each player being a Warrior.'
    
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

        roleDict['emoji'] = 1185512895094726756

        roleDict['secondaryEmoji'] = 1185515676392243302

        roleDict['imageURL'] = None

        roleDict['secondaryImageURL'] = None

        roleDict['roleMessage'] = 'You have the ability to secure the walls for an expedition! But be careful! If there are more titans than soldiers attempting to secure the walls, you will fail!\n\n'

        roleDict['gameRole'] = ':guard:Ackermann:guard:'

        roleDict['helpInfo'] = 'Levi is the strongest Soldier of all time! He has an ability to secure an expedition and ensure that it will pass, even if a warrior sabotages! However, Levi is not strong enough to beat TWO warriors, so if 2 or more warriors try to sabotage the expedition, he will fail! In addition, when you use the ability to secure the walls and the warriors sabotage, they will be alerted as to your identity which may make it easier for them to track down Eren.'


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

        roleDict['roleMessage'] = f'When voting for an expedition, you will be told if Eren is in the expedition or not.\n\n'

        roleDict['gameRole'] = ':punch:Coordinate\'s Fist:punch:'

        roleDict['helpInfo'] = 'Floch is the quintessential Yeagerist. He will follow a complete rumbling to the bitter end, and will help it come to fruition. In addition, he has the ability to gain intel from Eren. After every Expedition proposed, he will be informed by Eren if he is in the expo or not.'

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

        roleDict['roleMessage'] = 'You have the ability to act as a personal bodyguard to any **one** person on any expedition you are on (Inlcuding yourself if you choose yourself!) and prevent them from being killed. Use this ability wisely, only to protect yourself and Soldiers you really trust! If someone is saved by you, everyone will know Mikasa was in the expo and used the guard on them as well, so be careful about giving out role information!\n\n'

        roleDict['gameRole'] = ':fencer:Bodyguard:fencer:'

        roleDict['helpInfo'] = 'Mikasa is an extremely strong Soldier! Thanks to this and an unwavering ~~desire to be a pathetic fucking simp~~ loyal streak, every expedition she is on, she has the ability to protect 1 person on the expo INCLUDING herself to prevent them from being killed!'
    
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

        roleDict['helpInfo'] = f'Zeke is the warchief and team captain for the Warriors! He will not be seen as a Wall by Eren, and is a mandatory role that appears every game. He is more important than just being invisible to the Coordinate, however. He alone has the ability to choose to kidnap in the middle of the game to stop all of the Warriors from being killed if the situation looks grim!'  
    

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

        roleDict['roleMessage'] = f'Your titan has a unique screaming ability! In order to use it, use the scream option to send a message to all of your Warrior comrades! When you use this ability, an alert will be shown in the home channel.\n\n'

        roleDict['gameRole'] = ':speaking_head:Screaming Titan:speaking_head:'

        roleDict['helpInfo'] = 'Annie is the owner of the Female Titan! One of this titan\'s abilities is its scream can be used to attract titans. However, it can also be used to convey hidden messages! Once per game, Annie can send ONE message to all of the Warriors, and the Soldiers will only know that a message was sent, but not what it was!'

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

        roleDict['roleMessage'] = f'You are the "Shut-Your-Jaw" Titan! Use `{prefix}gag` to open the menu to choose to gag a player. When a player is gagged, they are not able to speak and their commander turn gets skipped! However, there is an important exception! A flared Erwin is ungaggable, and you are not allowed to gag players when there is 2 walls down with an active spy.\n\n'

        roleDict['gameRole'] = ':shushing_face:Gag Orderer:shushing_face:'

        roleDict['helpInfo'] =  'Porco, the owner of the "Shut-Your-Jaw" Titan ~~dear god I have fucking lost it please just end my misery~~ can gag a player so they are not able to speak for an entire round. Their turn in the commander order also gets skipped, so this ability can be quite powerful. However, there are important exceptions and wrinkles to understand. First, a flared Erwin is ungaggable, there is nothing you can do to contain him. Next, you are prohibited from gagging players when 2 walls are broken and the spy is active. Finally, a gagged player is NOT confirmed good, Porco has the ability to gag a Warrior or even himself to do a little trolling and trick the Soldiers.'

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
    
    def getHangeInfo(currentGame, Hange):
        hangeInfo = 'I have deduced that of all possible remaining scenarios, the following users are Warriors in this percentage of them.\n\n'
        getProbabilities = Hange.role.getProbabilities(currentGame)
        for player in currentGame.players:
            if player.role.id == 'Hange':
                continue
            hangeInfo += f'**{player.user.name}** - {getProbabilities[player]}%\n'
        return hangeInfo
    
    def getHitchInfo(currentGame, Hitch, hitchInfo):
        hitchMessage = ''
        for role, player in hitchInfo.items():
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
        warriorList = random.sample(warriorList, len(warriorList))
        for warrior in warriorList:
            if player.user.name != warrior.user.name:
                warriorInfo += f'**{warrior.user.name}**'
            if warriorList.index(warrior) != len(warriorList) - 1:
                warriorInfo += '\n'
        return warriorInfo
    
    def getLeviRevealMessage(Levi):
        return f'The identity of **Levi Ackermann** has been revealed to be **{Levi.user.name}**!'
    
    def getErwinMessage(Erwin):
        return f'I, {Erwin.user.mention}, am activating a signal flare!'
    
    def getArminDeathMessages(currentGame, currentTheme, Armin, Mikasa, Reiner):
        arminDeathMessages = ''
        for killedPlayer, causeOfDeath in Armin.killed.items():
            if causeOfDeath == 'Armin':
                arminDeathMessages += f'**{killedPlayer.user.name}** perished in the Blast!\n'
                if killedPlayer in currentGame.soldiers:
                    arminDeathMessages += f'They were a {currentTheme.emojiSoldier}**{currentTheme.soldierSingle}**{currentTheme.emojiSoldier}!\n\n'
                elif killedPlayer in currentGame.warriors:
                    arminDeathMessages += f'They were a {currentTheme.emojiWarrior}**{currentTheme.warriorSingle}**{currentTheme.emojiWarrior}!\n\n'
        if type(currentGame.currentExpo.mikasaGuarded) == dict:
            for key, value in currentGame.currentExpo.mikasaGuarded.items():
                if value == 'Armin':
                    arminDeathMessages += f'{Mikasa.role.emoji} Mikasa saved **{key.user.name}** from the Blast!{Mikasa.role.emoji}\n\n'
        if type(currentGame.currentExpo.reinerBlocked) == dict:
            for key, value in currentGame.currentExpo.reinerBlocked.items():
                if value == 'Armin':
                    arminDeathMessages += f'{Reiner.role.emoji}**{key.user.name}** Survived the Blast!{Reiner.role.emoji}\n\n'
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
        if type(currentGame.currentExpo.mikasaGuarded) == dict:
            for key, value in currentGame.currentExpo.mikasaGuarded.items():
                if value == 'Levi':
                    leviDeathMessages += f'**{key.user.name}** was attacked by Levi!\n{Mikasa.role.emoji}But was protected by Mikasa!{Mikasa.role.emoji}\n\n'
        if type(currentGame.currentExpo.reinerBlocked) == dict:
            for key, value in currentGame.currentExpo.reinerBlocked.items():
                if value == 'Levi':
                    leviDeathMessages += f'{Reiner.role.emoji}**{key.user.name}**\'s Armor protected them from Levi\'s onslaught!{Reiner.role.emoji}\n\n'
        return leviDeathMessages
    
    def getSashaDeathMessages(currentGame, currentTheme, Sasha, Mikasa, Reiner):
        sashaDeathMessages = ''
        for killedPlayer, causeOfDeath in Sasha.killed.items():
            if causeOfDeath == 'Sasha':
                sashaDeathMessages += f'{Sasha.role.secondaryEmoji}**{killedPlayer.user.name}** was struck by Sasha\'s Arrow!{Sasha.role.secondaryEmoji}\n'
                if killedPlayer in currentGame.soldiers:
                    sashaDeathMessages += f'They were a {currentTheme.emojiSoldier}**{currentTheme.soldierSingle}**{currentTheme.emojiSoldier}!\n\n'
                elif killedPlayer in currentGame.warriors:
                    sashaDeathMessages += f'They were a {currentTheme.emojiWarrior}**{currentTheme.warriorSingle}**{currentTheme.emojiWarrior}!\n\n'
        if type(currentGame.currentExpo.mikasaGuarded) == dict:
            for key, value in currentGame.currentExpo.mikasaGuarded.items():
                if value == 'Sasha':
                    sashaDeathMessages += f'{Mikasa.role.emoji}Mikasa deflected Sasha\'s Arrow away from **{key.user.name}**!{Mikasa.role.emoji}\n\n'
        if type(currentGame.currentExpo.reinerBlocked) == dict:
            for key, value in currentGame.currentExpo.reinerBlocked.items():
                if value == 'Sasha':
                    sashaDeathMessages += f'{Reiner.role.emoji}The Arrow merely bounced off **{key.user.name}**\'s Armor!{Reiner.role.emoji}\n\n'
        return sashaDeathMessages
    
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

            

