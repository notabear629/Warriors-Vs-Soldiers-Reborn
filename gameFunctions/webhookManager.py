import discord
from discord.ext import commands

from dataFunctions.databaseManager import databaseManager

from gameFunctions.searchFunctions import searchFunctions

from embedBuilder import embedBuilder

class webhookManager:
    
    async def sendWebhook(currentGame, currentTheme, channel, message, author, client, embed=None):
        findWebhooks = await channel.webhooks()
        ourWebhook = None
        for webhook in findWebhooks:
            if webhook.user == client.user:
                ourWebhook = webhook
                break
        if ourWebhook == None:
            ourWebhook = await channel.create_webhook(name = 'WvS Bot Webhook')
        if author == 'PATHS':
            pass
        elif author.startswith('{ALTERNATE}'):
            foundPlayer = await searchFunctions.roleIDToPlayer(currentGame, author.split('{ALTERNATE}')[1])
            if foundPlayer != None:
                authorName = foundPlayer.role.name
                if type(foundPlayer.role.secondaryEmoji) == str:
                    authorAvatar = foundPlayer.secondaryImageURL
                else:
                    authorAvatar = foundPlayer.role.secondaryEmoji.url
        else:
            foundPlayer = await searchFunctions.roleIDToPlayer(currentGame, author)
            if foundPlayer != None:
                authorName = foundPlayer.role.name
                if type(foundPlayer.role.emoji) == str:
                    authorAvatar = foundPlayer.role.imageURL
                else:
                    authorAvatar = foundPlayer.role.emoji.url

        await ourWebhook.send(message, embed=embed, username= authorName, avatar_url = authorAvatar, wait = True)

    async def processExpoVoteWebhooks(currentGame, currentTheme, home, client):
        Hitch = await searchFunctions.roleIDToPlayer(currentGame, 'Hitch')
        if Hitch != None:
            hitchInfo = {}
        if currentGame.currentExpo.jeanActivated:
            await webhookManager.sendWebhook(currentGame, currentTheme, home, currentTheme.jeanMessage, 'Jean', client)
            if Hitch != None:
                Jean = await searchFunctions.roleIDToPlayer(currentGame, 'Jean')
                hitchInfo['Jean'] = Jean
        if currentGame.currentExpo.pieckActivated and currentGame.currentExpo.jeanActivated == False:
            await webhookManager.sendWebhook(currentGame, currentTheme, home, currentTheme.pieckMessageWithoutJean, 'Pieck', client)
        if currentGame.currentExpo.pieckActivated and currentGame.currentExpo.jeanActivated:
            await webhookManager.sendWebhook(currentGame, currentTheme, home, currentTheme.pieckMessageWithJean, 'Pieck', client)
        if currentGame.currentExpo.pieckActivated and Hitch != None:
            Pieck = await searchFunctions.roleIDToPlayer(currentGame, 'Pieck')
            hitchInfo['Pieck'] = Pieck
        if Hitch != None and Hitch in currentGame.livingPlayers and hitchInfo != {}:
            user = databaseManager.searchForUser(Hitch.user)
            userChannel = client.get_channel(user['channelID'])
            hitchMessage = currentTheme.getHitchInfo(currentGame, Hitch, hitchInfo)
            embed = await embedBuilder.infoUpdate(currentTheme, Hitch, hitchMessage)
            await webhookManager.sendWebhook(currentGame, currentTheme, userChannel, f'{Hitch.user.mention}', 'Hitch', client)
            await webhookManager.sendWebhook(currentGame, currentTheme, userChannel, '', 'Hitch', client, embed)

    async def processResultsWebhooks(currentGame, currentTheme, home, client):
        if currentGame.currentExpo.arminActivated:
            await webhookManager.sendWebhook(currentGame, currentTheme, home, currentTheme.arminMessage, 'Armin', client)
        if currentGame.currentExpo.bertholdtCloaked:
            await webhookManager.sendWebhook(currentGame, currentTheme, home, currentTheme.bertholdtMessage, 'Bertholdt', client)
        if currentGame.currentExpo.leviAttacked:
            Levi = await searchFunctions.roleIDToPlayer(currentGame, 'Levi')
            if Levi.killed != []:
                await webhookManager.sendWebhook(currentGame, currentTheme, home, currentTheme.leviAttackMessage, '{ALTERNATE}Levi', client)
                for player in currentGame.warriors:
                    user = databaseManager.searchForUser(player.user)
                    userChannel = client.get_channel(user['channelID'])
                    await webhookManager.sendWebhook(currentGame, currentTheme, userChannel, f'{player.user.mention}', 'Zeke', client)
                    await webhookManager.sendWebhook(currentGame, currentTheme, userChannel, currentTheme.getLeviRevealMessage(Levi), 'Zeke', client)
        if currentGame.currentExpo.leviDefended and len(currentGame.currentExpo.sabotagedExpedition) > 0:
            Levi = await searchFunctions.roleIDToPlayer(currentGame, 'Levi')
            await webhookManager.sendWebhook(currentGame, currentTheme, home, currentTheme.leviDefendMessage, 'Levi', client)
            for player in currentGame.warriors:
                user = databaseManager.searchForUser(player.user)
                userChannel = client.get_channel(user['channelID'])
                await webhookManager.sendWebhook(currentGame, currentTheme, userChannel, f'{player.user.mention}', 'Zeke', client)
                await webhookManager.sendWebhook(currentGame, currentTheme, userChannel, currentTheme.getLeviRevealMessage(Levi), 'Zeke', client)
        Sasha = await searchFunctions.roleIDToPlayer(currentGame, 'Sasha')
        if Sasha != None and currentGame.sashaTargeted in currentGame.currentExpo.expeditionMembers and Sasha not in currentGame.currentExpo.expeditionMembers and Sasha.role.abilityActive:
            await webhookManager.sendWebhook(currentGame, currentTheme, home, currentTheme.sashaMessage, 'Sasha', client)


    async def processNewRoundWebhooks(currentGame, currentTheme, home, client):
        Hange = await searchFunctions.roleIDToPlayer(currentGame, 'Hange')
        if Hange != None and Hange in currentGame.livingPlayers:
            user = databaseManager.searchForUser(Hange.user)
            userChannel = client.get_channel(user['channelID'])
            await Hange.role.hangeProcess(currentGame)
            hangeInfo = currentTheme.getHangeInfo(currentGame, Hange)
            embed = await embedBuilder.infoUpdate(currentTheme, Hange, hangeInfo)
            await webhookManager.sendWebhook(currentGame, currentTheme, userChannel, f'{Hange.user.mention}', 'Hange', client)
            await webhookManager.sendWebhook(currentGame, currentTheme, userChannel, '', 'Hange', client, embed)

    async def erwinWebhook(currentGame, currentTheme, home, client):
        Erwin = await searchFunctions.roleIDToPlayer(currentGame, 'Erwin')
        if Erwin != None and currentGame.currentExpo.erwinActivated:
            user = databaseManager.searchForUser(Erwin.user)
            userChannel = client.get_channel(user['channelID'])
            erwinMessage = currentTheme.getErwinMessage(Erwin)
            await webhookManager.sendWebhook(currentGame, currentTheme, home, erwinMessage, 'Erwin', client)

    async def dazWebhook(currentGame, currentTheme, home, client):
        await webhookManager.sendWebhook(currentGame, currentTheme, home, currentTheme.dazMessage, 'Daz', client)

    async def mikasaWebhook(currentGame, currentTheme, home, client):
        await webhookManager.sendWebhook(currentGame, currentTheme, home, currentTheme.mikasaMessage, 'Mikasa', client)

    async def reinerWebhook(currentGame, currentTheme, home, client):
        await webhookManager.sendWebhook(currentGame, currentTheme, home, currentTheme.reinerMessage, 'Reiner', client)


    
