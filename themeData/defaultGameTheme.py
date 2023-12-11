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
    #You have free reign to edit these as you please
    themeName = 'Default Warriors vs Soldiers'
    gameName = 'Warriors vs Soldiers'
    soldierSingle = 'Soldier'
    soldierPlural = 'Soldiers'
    emojiSoldier = ':shield:'
    warriorSingle = 'Warrior'
    warriorPlural = 'Warriors'
    emojiWarrior = ':crossed_swords:'
    wallSingle = 'Wall'
    wallPlural = 'Walls'

    soldierThumbnail = 'https://cdn.discordapp.com/emojis/934488343343927367.webp?size=128&quality=lossless'
    warriorThumbnail = 'https://cdn.discordapp.com/emojis/934488802213384292.webp?size=128&quality=lossless'
    wildcardThumbnail ='https://cdn.discordapp.com/emojis/934489212277882932.webp?size=128&quality=lossless'

    soldierColor = discord.Color.blue()
    warriorColor = discord.Color.red()
    wildcardColor = discord.Color.gold()

    soldierDefaultMessage = 'Work with your fellow Soldiers to successfully complete 3 expeditions and reach the basement. Remember to conceal the true identity of Eren! Securing the walls is not enough, after the rounds of expeditions, the Warriors will have one last shot of winning if they can successfully identity Eren!'
    warriorDefaultMessage = 'Work with your fellow Warriors to try to knock down the walls before the Soldiers can reach the basement. Be mindful of how the Soldiers behave, even if you fail to destroy the walls, you will have one last chance of victory if you can successfully identify Eren!'
    wildcardDefaultMessage = 'Wildcards are neither Soldiers nor Warriors, so the roles behave much differently. Shoot for your personal objective to the best of your abilities so that you may bask in the eternal glory of winning your own way!'

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

    emojiWinMarkerOne = ':one:'
    emojiWinMarkerTwo = ':two:'
    emojiWinMarkerThree = ':three:'
    emojiSpacer = 686015611985461307
    emojiRoundVictoryMarker = ':white_check_mark'
    emojiVictoryMarker = ':checkered_flag:'
    emojiMariaExterior = ':house:'
    emojiMariaInterior = 686009957233066004
    emojiRoseExterior = ':bank:'
    emojiRoseInterior = 686009957123883056
    emojiSinaExterior = ':european_castle:'
    emojiSinaInterior = 686009957509758996
    emojiWinMarker = ':shield:'
    emojiFailMarker = ':crossed_swords:'
    emojiCurrentMarker = ':horse_racing:'

    #Roles embed aesthetics
    rolesEmbedColor = discord.Color.blue()

    global prefix

    prefix = os.getenv('BOT_PREFIX')


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

    class Soldier:
        roleDict = {'roleID' : 'Soldier'}

        roleDict['name'] = 'Soldier'

        roleDict['shortName'] = 'Soldier'

        roleDict['team'] = 'Soldiers'

        roleDict['isTitan'] = False

        roleDict['emoji'] = ':shield:'

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

        roleDict['roleMessage'] = f'Eren does not see you as a Warrior, in fact, you are the only Warrior to be hidden in this matter. Be mindful of this when deciding if you want to be flagrant about your identity as a Warrior or not. You also may `{prefix}kidnap @mention` Eren at any time, but be warned, this will end the game just like a regular kidnap! In order to unlock this ability, first use `{prefix}unlock` in this DM, then you will be able to kidnap Eren.'

        roleDict['gameRole'] = ':man_supervillain:Warchief:man_supervillain:'

        roleDict['helpInfo'] = f'Zeke is the warchief and team captain for the Warriors! He will not be seen as a Wall by Eren, and is a mandatory role that appears every game. He is more important than just being invisible to the Coordinate, however. He alone has the ability to choose to kidnap in the middle of the game to stop all of the Warriors from being killed if the situation looks grim!'  
    

    class Warrior:
        roleDict = {'roleID' : 'Warrior'}

        roleDict['name'] = 'Warrior'

        roleDict['shortName'] = 'Warrior'

        roleDict['team'] = 'Warriors'

        roleDict['isTitan'] = False

        roleDict['emoji'] = ':crossed_swords:'

        roleDict['roleMessage'] = f'You are an average Warrior. You do not possess any special abilities to aid you in breaking the walls.'

        roleDict['gameRole'] = ':crossed_swords:Default Warrior:crossed_swords:'

        roleDict['helpInfo'] = f'The Warrior role is merely just a default Warrior, they essentially have no role.'


    def getErenInfo(CurrentGame):
        erenInfo = 'The Warriors are:\n'
        warriorList = CurrentGame.warriors.copy()
        warriorList = random.sample(warriorList, len(warriorList))
        for warrior in warriorList:
            if warrior.role.id != 'Zeke':
                erenInfo += f'**{warrior.user.name}**'
            if warriorList.index(warrior) != len(warriorList) -1:
                erenInfo += '\n'
        return erenInfo
    
    def getWarriorInfo(CurrentGame, player):
        warriorInfo = 'Your fellow Warriors are:\n'
        warriorList = CurrentGame.warriors.copy()
        warriorList = random.sample(warriorList, len(warriorList))
        for warrior in warriorList:
            if player.user.name != warrior.user.name:
                warriorInfo += f'**{warrior.user.name}**'
            if warriorList.index(warrior) != len(warriorList) - 1:
                warriorInfo += '\n'
        return warriorInfo