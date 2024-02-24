import discord
from discord.ext import commands

from dataFunctions.databaseManager import databaseManager

from embedBuilder import embedBuilder

from gameObjects.Role import Role

class userInfoManager:
    async def userRegistration(ctx, user, homeServer, userCategory, currentTheme, prefix):
        userValidation = databaseManager.searchForUser(user)
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
        gameValidation = databaseManager.searchForWvsPlayer(user)
        if gameValidation == None:
            userInformation = {'userID' : user.id, 'userName' : user.name}
            databaseManager.addWvsPlayer(userInformation)
            gameValidation = databaseManager.searchForWvsPlayer(user)
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
        if updateNeeded:
            databaseManager.updateWvsPlayer(newDB)


    async def getDefaultUserDatabase():
        db = {}
        savedRulesets = []
        while len(savedRulesets) < 25:
            savedRulesets.append(None)
        db['savedRulesets'] = savedRulesets
        db['stats'] = await userInfoManager.getDefaultStatistics()
        return db
    
    async def getDefaultStatistics():
        stats = {'GamesPlayed': 0, 'GamesWon' : 0, 'SoldiersPlayed': 0, 'SoldiersWon': 0, 'SoldiersKidnaps': 0, 'SoldiersKidnapWins': 0, 'WarriorsPlayed' : 0, 'WarriorsWon': 0, 'WarriorsKidnaps': 0, 'WarriorsKidnapWins': 0, 'Kills' : 0, 'Deaths': 0, 'MVPS':0, 'SoldiersMVPS': 0, 'WarriorsMVPS':0}
        for role in Role.allRoles:
            roleStats = {f'{role}Played': 0, f'{role}Won' :0, f'{role}Kidnaps': 0, f'{role}KidnapWins' : 0}
            stats.update(roleStats)
        for role in Role.allLethal:
            roleStats = {f'{role}Kills' : 0, f'{role}KillWins' :0}
            stats.update(roleStats)
        abilityStats = {'JeanForces':0, 'JeanForceWins':0, 'ErwinFlaresFired': 0, 'DazChickens':0, 'DazChickenWins': 0, 'LeviAttacks':0, 'LeviKills':0, 'LeviDefends':0, 'LeviDefendWins':0,  'MikasaGuards': 0, 'MikasaSaved': 0, 'MikasaSaveWins':0, 'ArminNukes': 0, 'SashaFires': 0, 'PieckFlipAccepts' : 0, 'PieckFlipRejects' : 0, 'PieckFlipAcceptWins': 0, 'PieckFlipRejectWins': 0, 'PorcoGags': 0, 'PorcoCommanderSkips':0, 'FalcoUses' :0, 'FalcoVoteWins':0, 'ReinerSaves': 0, 'BertholdtCloaks': 0, 'BertholdtDoubleCloaks': 0}
        stats.update(abilityStats)
        extraSoldierStats = {'SoldiersWallsBroken': 0, 'SoldiersPasses': 0, 'PassCommanders': 0, 'PassVotes': 0, 'PassAssists': 0, 'PassExpeditions': 0, 'PassesResponsible': 0, 'ExposCommanded': 0, 'AcceptedCommand':0, 'ExposVoted':0, 'SoldiersExpeditionsOn':0}
        stats.update(extraSoldierStats)
        extraWarriorStats = {'WarriorsWallsBroken': 0, 'WarriorsPasses':0, 'BreakCommanders': 0, 'BreakVotes': 0, 'BreakAssists':0, 'BreakExpeditions':0, 'BreaksResponsible': 0, 'WarriorsExpeditionsOn':0}
        stats.update(extraWarriorStats)
        return stats

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






            
