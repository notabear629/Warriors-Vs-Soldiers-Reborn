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
    emojiTheme = 685785857609039873
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
    emojiSpacer = 686015611985461307
    emojiRoundVictoryMarker = str('✅')
    emojiVictoryMarker = str('🏁')
    emojiMariaExterior = str('🏠')
    emojiMariaInterior = 686009957233066004
    emojiRoseExterior = str('🏦')
    emojiRoseInterior = 686009957123883056
    emojiSinaExterior = str('🏰')
    emojiSinaInterior = 686009957509758996
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

    #Expedition DM aesthetics
    expeditionDMColor = discord.Color.blue()

    #Temporary Message Aesthetics
    temporaryMessageColor = discord.Color.blue()

    #Expedition results aesthetics
    expoPassedColor = discord.Color.green()
    expoSabotagedColor = discord.Color.red()
    expoSecuredColor = discord.Color.blue()
    arminNukeColor = discord.Color.default()
    wallMariaBreakMessage = str('💥Wall Maria has Fallen!💥')
    wallRoseBreakMessage = str('💥Wall Rose has Fallen!💥')
    wallSinaBreakMessage = str('💥Wall Sina has Fallen!💥')

    #Game over Aesthetics
    wallBreakMessage = str('⚔️All the Walls have Fallen and Paradis has been destroyed!⚔️\n\n⚔️Warriors Win!⚔️')
    basementMessage = str(f'The Soldiers have reached the Basement. The Warriors still have one final chance to win! Use `{prefix}kidnap @mention` to kidnap who you think is the Coordinate for one final chance at victory!')
    kidnapTimeoutMessage = str(f'The Warriors have failed to identify the Coordinate in time...\n\n🛡️Soldiers Win!🛡️')
    kidnapSuccessMessage = str('⚔️The Warriors have successfully identified the Coordinate!⚔️\n\n⚔️Warriors Win!⚔️')
    kidnapFailMessage = str('🛡️The Warriors did not manage to successfully identify the Coordinate and Eren\'s identity was kept secret.🛡️\n\n🛡️Soldiers Win!🛡️')
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

        #isTitan is used for stuff like the Pure Titan (may or may not be implemented yet) and Mike (may or may not be implemented yet). You may actually edit these to being True or False depending on the logic for the "Titan" you use in your theme.
        #For example, if you were making a Fate Stay/Night based theme, you may decide that the "titan" logic should instead work on the basis of "Servants".
        #Under this system, if the character is a servant, you would keep this as info['isTitan'] = True, and if they aren't, you would set this to info['isTitan'] = False.
        #Please keep in mind that removing isTitan from the coordinate equivalent will make very Mike overpowered in games with many Warriors as Titans.
        roleDict['isTitan'] = True

        #If you are using a custom emoji, just make this the integer emoji ID you wish to use. It is important your bot is in the server that the emoji is hosted in, or they will not be able to use the emoji and your game will break.
        #If you are using a default emoji, like the crown emoji, you can just put a String ':crown:' and it will work fine. The code will check if the type is an integer or String so dont worry about mixing types.
        roleDict['emoji'] = 685785857609039873


        #Not all roles actually use secondary emojis. If this is None, it's fine. Should be an int or emoji string like any other emoji.
        roleDict['secondaryEmoji'] = None

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

        roleDict['isTitan'] = False

        roleDict['emoji'] = 695886874937524275

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

        roleDict['isTitan'] = False

        roleDict['emoji'] = 1185201738815393833

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

        roleDict['isTitan'] = False

        roleDict['emoji'] = 686525460607401989

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

        roleDict['isTitan'] = False

        roleDict['emoji'] = 686833146787921940

        roleDict['secondaryEmoji'] = 686528354886877253

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

        roleDict['isTitan'] = False

        roleDict['emoji'] = 696620790833217546

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

        roleDict['isTitan'] = True

        roleDict['emoji'] = 686831164102541314

        roleDict['secondaryEmoji'] = 934886285254987846

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

        roleDict['isTitan'] = False

        roleDict['emoji'] = 696271784777089024

        roleDict['secondaryEmoji'] = str('🏹')

        roleDict['imageURL'] = None

        roleDict['secondaryImageURL'] = None

        roleDict['roleMessage'] = f'You have the ability to attack from long range! You can set a target to fire at using `{prefix}target`, and the next time they are on an expedition that you are not, you\'ll fire an arrow at them and kill them! Be careful: This does NOT stop them from breaking the walls, and if you attack a soldier, they will still die!\n\n'

        roleDict['gameRole'] = ':bow_and_arrow:Sniper:bow_and_arrow:'

        roleDict['helpInfo'] = 'Sasha is a master at long range weapons! She is able to choose a target, and the next time they are in an expedition that goes through that she is NOT in, she will send an arrow to them, killing them! You can use this to eliminate someone you know is a warrior, but be careful, this will NOT stop them from sabotaging the walls!'


    class Soldier:
        roleDict = {'roleID' : 'Soldier'}

        roleDict['name'] = 'Soldier'

        roleDict['shortName'] = 'Soldier'

        roleDict['team'] = 'Soldiers'

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

        roleDict['isTitan'] = True

        roleDict['emoji'] = 685785857617035327

        roleDict['secondaryEmoji'] = None

        roleDict['imageURL'] = None

        roleDict['secondaryImageURL'] = None

        roleDict['roleMessage'] = f'Eren does not see you as a Warrior, in fact, you are the only Warrior to be hidden in this matter. Be mindful of this when deciding if you want to be flagrant about your identity as a Warrior or not. You also may `{prefix}kidnap @mention` Eren at any time, but be warned, this will end the game just like a regular kidnap! In order to unlock this ability, first use `{prefix}unlock` in this DM, then you will be able to kidnap Eren.'

        roleDict['gameRole'] = ':man_supervillain:Warchief:man_supervillain:'

        roleDict['helpInfo'] = f'Zeke is the warchief and team captain for the Warriors! He will not be seen as a Wall by Eren, and is a mandatory role that appears every game. He is more important than just being invisible to the Coordinate, however. He alone has the ability to choose to kidnap in the middle of the game to stop all of the Warriors from being killed if the situation looks grim!'  
    

    class Pieck:
        roleDict = {'roleID' : 'Pieck'}

        roleDict['name'] = 'Pieck Finger'

        roleDict['shortName'] = 'Pieck'

        roleDict['team'] = 'Warriors'

        roleDict['isTitan'] = True

        roleDict['emoji'] = 1015918467167293440

        roleDict['secondaryEmoji'] = None

        roleDict['imageURL'] = None
        
        roleDict['secondaryImageURL'] = None

        roleDict['roleMessage'] = f'You are an expert inflitrator! As such, you have the ability to drop into the expedition voting and flip the results once. When properly used, this ability is incredibly powerful, so be wise in your use of it!\n\n'

        roleDict['gameRole'] = ':detective:Spy:detective:'

        roleDict['helpInfo'] = 'Pieck is great at inflitrating enemy lines undetected. Thanks to this spying ability, she has the ability to mess with the votes for an expedition once and flip them all! This is an incredibly powerful ability when used properly, as it can turn a rejected expo into a free wall for the Warriors!'


    class Warrior:
        roleDict = {'roleID' : 'Warrior'}

        roleDict['name'] = 'Warrior'

        roleDict['shortName'] = 'Warrior'

        roleDict['team'] = 'Warriors'

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
    
    def getArminDeathMessages(currentGame, currentTheme, Armin):
        arminDeathMessages = ''
        for killedPlayer, causeOfDeath in Armin.killed.items():
            if causeOfDeath == 'Armin':
                arminDeathMessages += f'**{killedPlayer.user.name}** perished in the Blast!\n'
                if killedPlayer in currentGame.soldiers:
                    arminDeathMessages += f'They were a {currentTheme.emojiSoldier}**{currentTheme.soldierSingle}**{currentTheme.emojiSoldier}!\n\n'
                elif killedPlayer in currentGame.warriors:
                    arminDeathMessages += f'They were a {currentTheme.emojiWarrior}**{currentTheme.warriorSingle}**{currentTheme.emojiWarrior}!\n\n'
        return arminDeathMessages
    
    def getLeviDeathMessages(currentGame, currentTheme, Levi):
        leviDeathMessages = ''
        for killedPlayer, causeOfDeath in Levi.killed.items():
            if causeOfDeath == 'Levi':
                leviDeathMessages += f'**{killedPlayer.user.name}** was slain by Levi!\n'
                if killedPlayer in currentGame.soldiers:
                    leviDeathMessages += f'They were a {currentTheme.emojiSoldier}**{currentTheme.soldierSingle}**{currentTheme.emojiSoldier}!\n\n'
                elif killedPlayer in currentGame.warriors:
                    leviDeathMessages += f'They were a {currentTheme.emojiWarrior}**{currentTheme.warriorSingle}**{currentTheme.emojiWarrior}!\n\n'
        return leviDeathMessages
            

