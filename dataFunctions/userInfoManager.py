import discord
from discord.ext import commands

from dataFunctions.databaseManager import databaseManager

from embedBuilder import embedBuilder

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
            await channel.send(embed=embed)
            userInformation = {'userID' : user.id, 'userName': user.name, 'roleID' : newPersonalRole.id, 'channelID' : channel.id}
            databaseManager.addUser(userInformation)

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





            
