import discord
from discord.ext import commands
from gameObjects.Lobby import Lobby
from embedBuilder import embedBuilder

from discordViewBuilder import discordViewBuilder


class lobbyFunctions:
    async def host(ctx, currentLobby, currentGame, currentTheme, prefix, noMentions, home, currentRules):
        if home == ctx.channel:
            if currentLobby.online:     
                if ctx.message.author in currentLobby.users:
                    if ctx.message.author == currentLobby.host:
                        await ctx.message.reply(f"You are already hosting a lobby. use `{prefix}reset` to close it to start a new one.")
                    else:
                        await ctx.message.reply("Hey stinky, there's already a lobby! You're even in it!")
                else:
                    await ctx.message.reply(f'There is already a lobby! Why not `{prefix}join` instead?')
            else:
                if currentGame.online == False:
                    currentLobby.openLobby(ctx.message.author, currentRules)
                    embed = await embedBuilder.buildLobby(currentLobby, currentTheme, prefix)
                    await home.send(embed=embed, allowed_mentions= noMentions)
                    await home.send('Lobby Created.')
                else:
                    await ctx.message.reply(f'There is already an active game! Please wait for it to finish before trying to host a new one.')
            
    async def join(ctx, currentLobby, currentGame, currentTheme, prefix, noMentions, home):
        if home == ctx.channel:
            if currentLobby.online:
                if ctx.message.author in currentLobby.users:
                    await ctx.message.reply('Hey stinky, you are already in the lobby!')
                else:
                    if currentGame.online == False:
                        currentLobby.addUser(ctx.message.author)
                        embed = await embedBuilder.buildLobby(currentLobby, currentTheme, prefix)
                        await home.send(embed=embed, allowed_mentions= noMentions)
                        await home.send(f'**{ctx.message.author.name}** has joined the Lobby.')
                    else:
                        await ctx.message.reply('You may not join a currently active game! Please wait for the game to finish and a new one to begin.')
            else:
                await ctx.message.reply(f'There is no active lobby. Why not create one using `{prefix}host`?')

    #Test Command Only
    async def forceJoin(ctx, bozos, currentLobby, currentGame, currentTheme, prefix, noMentions, home):
        for bozo in bozos:
            currentLobby.addUser(bozo)
        embed = await embedBuilder.buildLobby(currentLobby, currentTheme, prefix)
        await home.send(embed=embed, allowed_mentions= noMentions)
        await home.send('Force Join Executed.')

    async def leave(ctx, currentLobby, currentGame, currentTheme, prefix, noMentions, home):
        if home == ctx.channel:
            if currentLobby.online:
                if ctx.message.author in currentLobby.users:
                    if currentLobby.host != ctx.message.author:
                        if currentGame.online == False:
                            currentLobby.removeUser(ctx.message.author)
                            embed = await embedBuilder.buildLobby(currentLobby, currentTheme, prefix)
                            await home.send(embed=embed, allowed_mentions= noMentions)
                            await home.send(f'**{ctx.message.author.name}** has left the Lobby.')
                        else:
                            await ctx.message.reply('~~Cannot run from trainer battles~~ You can\'t leave an active game, you cowardly quitter!')
                    else:
                        await ctx.message.reply(f'Hey stinky, you can\'t leave the lobby as a host! Instead, use `{prefix}reset`.')
                else:
                    await ctx.message.reply(f'Hey stinky, you\'re not in the active lobby! You may join it using `{prefix}join`.')
            else:
                await ctx.message.reply(f'You can\'t leave a lobby that doesn\'t exist! There is no active lobby. You may create one using `{prefix}host`.')
    
    async def kick(ctx, currentLobby, currentGame, currentTheme, prefix, noMentions, home, kicked):
        if home == ctx.channel:
            if kicked == None:
                await ctx.message.reply(f'You didn\'t specify who to kick, so you kick the air! You hurt your hamstring doing so. Good job. Proper command usage is `{prefix}kick @guyYouWannaKick`.')
            else:
                if currentLobby.online:
                    if ctx.message.author == currentLobby.host:
                        if kicked in currentLobby.users:
                            if currentGame.online == False:
                                currentLobby.removeUser(kicked)
                                embed = await embedBuilder.buildLobby(currentLobby, currentTheme, prefix)
                                await home.send(embed=embed, allowed_mentions= noMentions)
                                await home.send(f'**{kicked.name}** has been kicked back to where they came from.')
                            else:
                                await ctx.message.reply('Hey, you meanie! You can\'t kick someone midgame! Please kindly refrain from delivering them your boot of justice until after the game has finished.')
                        else:
                            await ctx.message.reply(f'Hey, you bully! You can\'t kick a player out of a lobby that they are not a part of! You may only kick {kicked.name} if they joined the lobby.')
                    else:
                        await ctx.message.reply(f'Hey, you bully! You can\'t kick a player out of a lobby that you\'re not the host of! Only the host may punt {kicked.name} out of here.')
                else:
                    await ctx.message.reply(f'Hey, you bully! You can\'t kick a player out of a lobby that doesn\'t exist! At least have the decency to create a lobby using `{prefix}host` before kicking poor {kicked.name}.')

    async def kickAll(ctx, currentLobby, currentGame, currentTheme, prefix, noMentions, home):
        if home == ctx.channel:
            if currentLobby.online:
                if ctx.message.author == currentLobby.host:
                    if currentGame.online == False:
                        currentLobby.clearUsers()
                        embed = await embedBuilder.buildLobby(currentLobby, currentTheme, prefix)
                        await home.send(embed=embed, allowed_mentions= noMentions)
                        await home.send('The lobby has been rumbled.')
                    else:
                        await ctx.message.reply('You can\'t ~~rumble the world~~ clear a lobby in the middle of a game!')
                else:
                    await ctx.message.reply('Only the ~~founding titan~~ host can rumble the lobby!')
            else:
                await ctx.message.reply(f'You can\'t ~~rumble a world~~ kick players from a lobby that doesn\'t exist! Use `{prefix}host` to create the lobby before you flatten it!')

    async def lobby(ctx, home, currentLobby, currentTheme, currentGame, prefix, noMentions):
        if currentLobby.online:
            embed = await embedBuilder.buildLobby(currentLobby, currentTheme, prefix)
            await home.send(embed=embed, allowed_mentions=noMentions)
        else:
            await ctx.reply(f'There is no lobby! Use `{prefix}host` from within <#{home.id}> to create one.')

    async def options(ctx, home, currentLobby, currentGame, currentTheme, prefix, noMentions, client, loadedRoles):
        if home == ctx.channel:
            if currentLobby.online:
                if ctx.message.author == currentLobby.host:
                    if currentGame.online == False:
                        embed = await embedBuilder.buildLobby(currentLobby, currentTheme, prefix)
                        view = await discordViewBuilder.basicOptionsView(currentTheme, client, currentLobby, currentGame, prefix, loadedRoles)
                        await home.send(embed=embed, allowed_mentions= noMentions, view = view)
                    else:
                        await ctx.message.reply('You cannot change options mid-game.')
                else:
                    await ctx.message.reply('Only the host may change game options.')
            else:
                await ctx.message.reply(f'There is no open lobby! Use `{prefix}host` to create one!')