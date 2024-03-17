import discord
from discord.ext import commands

from dataFunctions.databaseManager import databaseManager

from embedBuilder import embedBuilder

from gameObjects.Role import Role

from statBuilder import statBuilder

class userInfoManager:
    async def userRegistration(ctx, user, homeServer, userCategory, currentTheme, prefix, idCase=None):
        if idCase == None:
            userValidation = databaseManager.searchForUser(user)
        else:
            userValidation = idCase
        if userValidation == None:
            newPersonalRole = await homeServer.create_role(name = f'role-{user.name}')
            await user.add_roles(newPersonalRole)
            overwrites = {
                homeServer.default_role: discord.PermissionOverwrite(read_messages=False),
                newPersonalRole: discord.PermissionOverwrite(read_messages=True)
            }
            channel = await homeServer.create_text_channel(name = f'channel-{user.name}', overwrites = overwrites, category = userCategory)
            embed = await embedBuilder.buildRegistrationWelcome(user, homeServer, currentTheme, prefix)
            await channel.send(user.mention)
            await channel.send(embed=embed)
            userInformation = {'userID' : user.id, 'userName': user.name, 'roleID' : newPersonalRole.id, 'channelID' : channel.id}
            databaseManager.addUser(userInformation)
        if idCase == None:
            gameValidation = databaseManager.searchForWvsPlayer(user)
        else:
            gameValidation = databaseManager.getWvsPlayerByID(idCase['userID'])
        if gameValidation == None:
            if idCase == None:
                userInformation = {'userID' : user.id, 'userName' : user.name}
                databaseManager.addWvsPlayer(userInformation)
                gameValidation = databaseManager.searchForWvsPlayer(user)
            else:
                userInformation = {'userID' : idCase['userID'], 'userName' : idCase['userName']}
                databaseManager.addWvsPlayer(userInformation)
                gameValidation = databaseManager.getWvsPlayerByID(idCase['userID'])
        defaultDB = await userInfoManager.getDefaultUserDatabase()
        newDB = gameValidation.copy()
        updateNeeded = False
        for key, value in defaultDB.items():
            if key not in newDB:
                updateNeeded = True
                newDB[key] = value
            elif type(value) == dict:
                for key2, value2 in value.items():
                    if key2 not in newDB[key]:
                        updateNeeded = True
                        newDB[key][key2] = value2
        statsToRemove = []
        for key, value in newDB['stats'].items():
            if key not in defaultDB['stats']:
                statsToRemove.append(key)
                updateNeeded = True
        for stat in statsToRemove:
            del newDB['stats'][stat]
        if updateNeeded:
            databaseManager.updateWvsPlayer(newDB)


    async def fixDatabase(ctx, homeServer, userCategory, currentTheme, prefix, loadedBadges):

        globalDB = databaseManager.getGlobal()
        if globalDB == None:
            defaultDB = {'userID' : "GLOBAL", 'userName': 'GLOBAL'}
            defaultDB.update(await userInfoManager.getDefaultUserDatabase())
            databaseManager.addWvsPlayer(defaultDB)
            globalDB = databaseManager.getGlobal()
        await userInfoManager.userRegistration(ctx, globalDB, homeServer, userCategory, currentTheme, prefix, globalDB)


        allUsers = databaseManager.returnAllUsers()
        for user in allUsers:
            await userInfoManager.userRegistration(ctx, user, homeServer, userCategory, currentTheme, prefix, user)
            player = databaseManager.getWvsPlayerByID(user['userID'])
            databaseManager.updateWvsPlayer(await userInfoManager.calculateBadges(player, loadedBadges))
            player = databaseManager.getWvsPlayerByID(user['userID'])
            databaseManager.updateWvsPlayer(await userInfoManager.calculateCalcs(player, loadedBadges))
        await userInfoManager.calculateRanks()

        

    async def getDefaultUserDatabase():
        db = {}
        savedRulesets = []
        while len(savedRulesets) < 25:
            savedRulesets.append(None)
        db['savedRulesets'] = savedRulesets
        db['stats'] = await userInfoManager.getDefaultStatistics()
        db['titles'] = []
        db['badges'] = {'GamesWon': 'No Badge Earned', 'SoldiersWon': 'No Badge Earned', 'WarriorsWon': 'No Badge Earned', 'WarriorsKidnapWins': 'No Badge Earned', 'MVPS':'No Badge Earned', 'PassesResponsible':'No Badge Earned', 'BreaksResponsible':'No Badge Earned', 'Rank': 'Noob'}
        db['calcs'] = {'WORP' : 0, 'SoldierWORP' : 0, 'WarriorWORP': 0, 'MVPS': 0, 'BadgePoints':0}
        db['points'] = {'LegacyPoints': 0, 'WORP':0, 'SoldierWORP' : 0, 'WarriorWORP': 0, 'MVPS' :0 , 'BadgePoints':0}
        return db
    
    async def getDefaultStatistics():
        stats = {'GamesPlayed': 0, 'GamesWon' : 0, 'SoldiersPlayed': 0, 'SoldiersWon': 0, 'SoldiersKidnaps': 0, 'SoldiersKidnapWins': 0, 'WarriorsPlayed' : 0, 'WarriorsWon': 0, 'WarriorsKidnaps': 0, 'WarriorsKidnapWins': 0, 'Kills' : 0, 'Deaths': 0, 'MVPS':0, 'SoldiersMVPS': 0, 'WarriorsMVPS':0}
        for role in Role.allRoles:
            roleStats = {f'{role}Played': 0, f'{role}Won' :0, f'{role}Kidnaps': 0, f'{role}KidnapWins' : 0}
            stats.update(roleStats)
        for role in Role.allLethal:
            roleStats = {f'{role}Kills' : 0, f'{role}KillWins' :0}
            stats.update(roleStats)
        abilityStats = {'JeanForces':0, 'JeanForceWins':0, 'ErwinFlaresFired': 0, 'DazChickens':0, 'DazChickenWins': 0, 'LeviAttacks':0, 'LeviKills':0, 'LeviDefends':0, 'LeviDefendWins':0,  'MikasaGuards': 0, 'MikasaSaved': 0, 'MikasaSaveWins':0, 'ArminNukes': 0, 'SashaFires': 0, 'KeithFinishedPlayed': 0, 'KeithFinishedWon': 0, 'KeithFinishedKidnaps': 0, 'KeithFinishedKidnapWins':0,'GabiFires' : 0,  'GabiFireWins': 0, 'AnnieScreams' : 0, 'PieckFlipAccepts' : 0, 'PieckFlipRejects' : 0, 'PieckFlipAcceptWins': 0, 'PieckFlipRejectWins': 0, 'PorcoGags': 0, 'PorcoCommanderSkips':0, 'FalcoUses' :0, 'FalcoVoteWins':0, 'ReinerSaves': 0, 'BertholdtCloaks': 0, 'BertholdtDoubleCloaks': 0}
        stats.update(abilityStats)
        extraSoldierStats = {'SoldiersWallsBroken': 0, 'SoldiersPasses': 0, 'PassCommanders': 0, 'PassVotes': 0, 'PassAssists': 0, 'PassExpeditions': 0, 'PassesResponsible': 0, 'ExposCommanded': 0, 'AcceptedCommand':0, 'ExposVoted':0, 'SoldiersExpeditionsOn':0}
        stats.update(extraSoldierStats)
        extraWarriorStats = {'WarriorsWallsBroken': 0, 'WarriorsPasses':0, 'BreakCommanders': 0, 'BreakVotes': 0, 'BreakAssists':0, 'BreakExpeditions':0, 'BreaksResponsible': 0, 'WarriorsExpeditionsOn':0}
        stats.update(extraWarriorStats)
        return stats
    
    async def calculateBadges(db, loadedBadges):
        newDB = db.copy()
        for badgeType, badge in db['badges'].items():
            if badgeType == 'Rank':
                continue
            newDB['badges'][badgeType] = loadedBadges.getBadgeOutput(badgeType, db['stats'][badgeType])['badge']
        newDB['badges']['Rank'] = loadedBadges.getTotalBadgeOutput(db)['badge']
        return newDB
    
    async def calculateCalcs(db, loadedBadges):
        newDB = db.copy()
        globalDB = databaseManager.getGlobal()
        newDB['calcs']['WORP'] = await statBuilder.getTotalWORP(db['stats'], globalDB['stats'], True)
        newDB['calcs']['SoldierWORP'] = await statBuilder.getTeamWORP(db['stats'], globalDB['stats'], 'Soldiers', True)
        newDB['calcs']['WarriorWORP'] = await statBuilder.getTeamWORP(db['stats'], globalDB['stats'], 'Warriors', True)
        newDB['calcs']['MVPS'] = db['stats']['MVPS']
        newDB['calcs']['BadgePoints'] = loadedBadges.getTotalBadgeOutput(db)['points']
        return newDB
    
    async def calculateRanks():
        calcStats = ['WORP', 'SoldierWORP', 'WarriorWORP', 'MVPS', 'BadgePoints']
        allUsers = databaseManager.returnAllUsers()
        for user in allUsers:
            player = databaseManager.getWvsPlayerByID(user['userID'])
            newDB = player.copy()
            newDB['titles'] = []
            databaseManager.updateWvsPlayer(newDB)
        for stat in calcStats:
            sortedDB = databaseManager.getSortedWvsPlayer(stat)
            maxValue = sortedDB[0]['calcs'][stat]
            minValue = databaseManager.getWorstWvsPlayer(stat)['calcs'][stat]
            scaleValue = maxValue - minValue
            index = 0
            for player in sortedDB:
                newDB = player.copy()
                if index == 0 and player['calcs'][stat] != 0:
                    newDB['titles'].append(stat)
                if 'WORP' in stat:
                    if scaleValue== 0:
                        newDB['points'][stat] = 0
                    else:
                        newDB['points'][stat] = round((player['calcs'][stat] - minValue)/scaleValue*1000)
                elif 'MVPS' in stat:
                    if maxValue == 0:
                        newDB['points'][stat] = 0
                    else:
                        newDB['points'][stat] = round(player['calcs'][stat]/maxValue*1000)
                else:
                    newDB['points'][stat] = player['calcs'][stat]
                databaseManager.updateWvsPlayer(newDB)
                index += 1
        allUsers = databaseManager.returnAllUsers()
        for user in allUsers:
            player = databaseManager.getWvsPlayerByID(user['userID'])
            newDB = player.copy()
            newDB['points']['LegacyPoints'] = 0
            for stat in calcStats:
                newDB['points']['LegacyPoints'] += player['points'][stat]
            databaseManager.updateWvsPlayer(newDB)
        sortedDB = databaseManager.getSortedLegacy()
        pointWinner = sortedDB[0]
        newDB = pointWinner.copy()
        newDB['titles'].append('LegacyPoints')
        databaseManager.updateWvsPlayer(newDB)




    async def changeColor(ctx, user, homeServer, color):
        userValidation = databaseManager.searchForUser(user)
        userRoleID = userValidation['roleID']
        userRole = homeServer.get_role(userRoleID)
        if color != None:
            colorBuilderString = '0x' + color.lower()
            try:
                newColor = int(colorBuilderString, 16)
                await userRole.edit(color = discord.Color(newColor))
                await ctx.reply(f'Your color has been changed to {color}.')
            except:
                await ctx.reply('This is not a valid hex color!')
        else:
            await userRole.edit(color = discord.Color.default())
            await ctx.reply(f'Your color has been cleared.')

    async def changeChannelName(ctx, client, user, homeServer, channelName):
        userValidation = databaseManager.searchForUser(user)
        userChannelID = userValidation['channelID']
        userChannel = client.get_channel(userChannelID)
        if channelName != None:
            try:
                await userChannel.edit(name=channelName)
                await userChannel.send(f'{user.mention}, your channel name has been successfully updated.')
            except:
                await userChannel.send(f'{user.mention}, your channel name could not be updated at this time, please try a different name.')
        else:
            await userChannel.edit(name=f'channel-{user.name}')
            await userChannel.send(f'{user.mention}, your channel name has been successfully updated to its default name.')

    async def changeRoleName(ctx, user, homeServer, roleName):
        userValidation = databaseManager.searchForUser(user)
        userRoleID = userValidation['roleID']
        userRole = homeServer.get_role(userRoleID)
        if roleName != None:
            try:
                await userRole.edit(name=roleName)
                await ctx.reply(f'Your role name has been successfully updated.')
            except:
                await ctx.reply(f'Your role name could not be updated at this time, please try a different name.')
        else:
            await userRole.edit(name=f'role-{user.name}')
            await ctx.reply(f'{user.mention}, your role name has been successfully updated to its default name.')
    
    async def fixUser(ctx, client, user, homeServer, userCategory, currentTheme, prefix):
        userValidation = databaseManager.searchForUser(user)
        userRoleID = userValidation['roleID']
        userRole = homeServer.get_role(userRoleID)
        if userRole == None:
            userRole = await homeServer.create_role(name = f'role-{user.name}')
            await user.add_roles(userRole)
        overwrites = {
            homeServer.default_role: discord.PermissionOverwrite(read_messages=False),
            userRole: discord.PermissionOverwrite(read_messages=True)
        }
        if userRole not in user.roles:
            await user.add_roles(userRole)
        userChannelID = userValidation['channelID']
        userChannel = client.get_channel(userChannelID)
        if userChannel == None:
            userChannel = await homeServer.create_text_channel(name = f'channel-{user.name}', overwrites = overwrites, category = userCategory)
            embed = await embedBuilder.buildRegistrationWelcome(user, homeServer, currentTheme, prefix)
            await userChannel.send(embed=embed)
        else:
            await userChannel.edit(overwrites=overwrites)
        userInformation = {'userName': user.name, 'roleID' : userRole.id, 'channelID' : userChannel.id}
        databaseManager.updateUserInformation(user, userInformation)
        await ctx.reply('Your Data has successfully been fixed.')

    async def toggleAdmin(ctx, home, adminRole):
        if adminRole in ctx.message.author.roles:
            permissions = adminRole.permissions
            permissions.administrator = not permissions.administrator
            await adminRole.edit(permissions = permissions)
            await home.send('ADMIN ACCESS TOGGLED!')
            if ctx.message.channel != home:
                await ctx.reply('Admin access has been toggled.')






            
