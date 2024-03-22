import discord
from discord.ext import commands

from dataFunctions.databaseManager import databaseManager

from gameFunctions.searchFunctions import searchFunctions

from gameObjects.Player import Player

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
        else:
            if author.startswith('{ALTERNATE}'):
                foundRole = await searchFunctions.roleIDToRoleFromLoadedRoles(currentGame.loadedRoles, author.split('{ALTERNATE}')[1])
                if foundRole != None:
                    if type(foundRole.secondaryEmoji) == str:
                        authorAvatar = foundRole.secondaryImageURL
                    else:
                        authorAvatar = foundRole.secondaryEmoji.url
            else:
                foundRole = await searchFunctions.roleIDToRoleFromLoadedRoles(currentGame.loadedRoles, author)
                if foundRole != None:
                    if type(foundRole.emoji) == str:
                        authorAvatar = foundRole.imageURL
                    else:
                        authorAvatar = foundRole.emoji.url
            if foundRole != None:
                authorName = foundRole.name
        await ourWebhook.send(message, embed=embed, username= authorName, avatar_url = authorAvatar, wait = True)

    async def processExpoVoteWebhooks(currentGame, currentTheme, home, client):
        Hitch = await searchFunctions.roleIDToPlayer(currentGame, 'Hitch')
        if Hitch != None:
            hitchInfo = {}
        if currentGame.currentExpo.falcoActivated and Hitch != None:
            Falco = await searchFunctions.roleIDToPlayer(currentGame, 'Falco')
            hitchInfo['Falco'] = Falco
        if currentGame.currentExpo.jeanActivated:
            await webhookManager.sendWebhook(currentGame, currentTheme, home, currentTheme.jeanMessage, 'Jean', client)
            if Hitch != None:
                Jean = await searchFunctions.roleIDToPlayer(currentGame, 'Jean')
                hitchInfo['Jean'] = Jean
        if currentGame.currentExpo.zacharyActivated:
            await webhookManager.sendWebhook(currentGame, currentTheme, home, currentTheme.zacharyMessage, 'Zachary', client)
            if currentGame.currentExpo.jeanActivated:
                await home.send(currentTheme.conflictJeanZacharyMessage)
            if Hitch != None:
                Zachary = await searchFunctions.roleIDToPlayer(currentGame, 'Zachary')
                hitchInfo['Zachary'] = Zachary
        if currentGame.currentExpo.pieckActivated:
            if currentGame.currentExpo.jeanActivated and currentGame.currentExpo.zacharyActivated == False:
                msg = currentTheme.pieckMessageJean
            elif currentGame.currentExpo.zacharyActivated and currentGame.currentExpo.jeanActivated == False:
                msg = currentTheme.pieckMessageZachary
            else:
                msg = currentTheme.pieckMessage
            await webhookManager.sendWebhook(currentGame, currentTheme, home, msg, '{ALTERNATE}Pieck', client)
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
        Hitch = await searchFunctions.roleIDToPlayer(currentGame, 'Hitch')
        if Hitch != None:
            hitchInfo = {}
        if currentGame.currentExpo.arminActivated:
            await webhookManager.sendWebhook(currentGame, currentTheme, home, currentTheme.arminMessage, '{ALTERNATE}Armin', client)
            if Hitch != None:
                Armin = await searchFunctions.roleIDToPlayer(currentGame, 'Armin')
                hitchInfo['Armin'] = Armin
        if currentGame.currentExpo.bertholdtCloaked:
            await webhookManager.sendWebhook(currentGame, currentTheme, home, currentTheme.bertholdtMessage, '{ALTERNATE}Bertholdt', client)
            if Hitch != None:
                Bertholdt = await searchFunctions.roleIDToPlayer(currentGame, 'Bertholdt')
                hitchInfo['Bertholdt'] = Bertholdt
        if currentGame.currentExpo.leviAttacked:
            Levi = await searchFunctions.roleIDToPlayer(currentGame, 'Levi')
            await webhookManager.sendWebhook(currentGame, currentTheme, home, currentTheme.leviAttackMessage, '{ALTERNATE}Levi', client)
            for player in currentGame.warriors:
                user = databaseManager.searchForUser(player.user)
                userChannel = client.get_channel(user['channelID'])
                await webhookManager.sendWebhook(currentGame, currentTheme, userChannel, f'{player.user.mention}\n\n{currentTheme.getLeviRevealMessage(Levi)}', '{ALTERNATE}Zeke', client)
            if Hitch != None:
                Levi = await searchFunctions.roleIDToPlayer(currentGame, 'Levi')
                hitchInfo['Levi'] = Levi
        if currentGame.currentExpo.leviDefended and len(currentGame.currentExpo.sabotagedExpedition) > 0:
            Levi = await searchFunctions.roleIDToPlayer(currentGame, 'Levi')
            await webhookManager.sendWebhook(currentGame, currentTheme, home, currentTheme.leviDefendMessage, 'Levi', client)
            for player in currentGame.warriors:
                user = databaseManager.searchForUser(player.user)
                userChannel = client.get_channel(user['channelID'])
                await webhookManager.sendWebhook(currentGame, currentTheme, userChannel, f'{player.user.mention}\n\n{currentTheme.getLeviRevealMessage(Levi)}', '{ALTERNATE}Zeke', client)
            if Hitch != None:
                Levi = await searchFunctions.roleIDToPlayer(currentGame, 'Levi')
                hitchInfo['Levi'] = Levi
        if currentGame.currentExpo.petraWatched != None and currentGame.currentExpo.petraWatched in currentGame.currentExpo.sabotagedExpedition:
            Petra = await searchFunctions.roleIDToPlayer(currentGame, 'Petra')
            await webhookManager.sendWebhook(currentGame, currentTheme, home, currentTheme.petraMessage, 'Petra', client)
            if Hitch != None:
                hitchInfo['Petra'] = Petra
        if currentGame.currentExpo.kennyMurdered != None:
            Kenny = await searchFunctions.roleIDToPlayer(currentGame, 'Kenny')
            kennyMsg = currentTheme.kennyMessage
            if currentGame.currentExpo.kennyMurdered == Kenny:
                kennyMsg = currentTheme.kennySuicideMessage
            await webhookManager.sendWebhook(currentGame, currentTheme, home, kennyMsg, 'Kenny', client)
            if Hitch != None:
                hitchInfo['Kenny'] = Kenny
        Sasha = await searchFunctions.roleIDToPlayer(currentGame, 'Sasha')
        if Sasha != None and currentGame.sashaTargeted in currentGame.currentExpo.expeditionMembers and Sasha not in currentGame.currentExpo.expeditionMembers and Sasha.role.abilityActive:
            await webhookManager.sendWebhook(currentGame, currentTheme, home, currentTheme.sashaMessage, 'Sasha', client)
            if Hitch != None:
                Sasha = await searchFunctions.roleIDToPlayer(currentGame, 'Sasha')
                hitchInfo['Sasha'] = Sasha
        Gabi = await searchFunctions.roleIDToPlayer(currentGame, 'Gabi')
        if Gabi !=None and currentGame.gabiTargeted != None and currentGame.gabiTargeted not in currentGame.deadPlayers:
            await webhookManager.sendWebhook(currentGame, currentTheme, home, currentTheme.gabiMessage, 'Gabi', client)
            if Hitch != None:
                hitchInfo['Gabi'] = Gabi
        if currentGame.currentExpo.annieMessage != None:
            await webhookManager.sendWebhook(currentGame, currentTheme, home, currentTheme.annieMessage, '{ALTERNATE}Annie', client)
            for player in currentGame.warriors:
                    user = databaseManager.searchForUser(player.user)
                    userChannel = client.get_channel(user['channelID'])
                    await webhookManager.sendWebhook(currentGame, currentTheme, userChannel, f'{player.user.mention}\n\n{currentGame.currentExpo.annieMessage}', '{ALTERNATE}Annie', client)
            if Hitch != None:
                Annie = await searchFunctions.roleIDToPlayer(currentGame, 'Annie')
                hitchInfo['Annie'] = Annie
        if Hitch != None and Hitch in currentGame.livingPlayers and hitchInfo != {}:
            user = databaseManager.searchForUser(Hitch.user)
            userChannel = client.get_channel(user['channelID'])
            hitchMessage = currentTheme.getHitchInfo(currentGame, Hitch, hitchInfo)
            embed = await embedBuilder.infoUpdate(currentTheme, Hitch, hitchMessage)
            await webhookManager.sendWebhook(currentGame, currentTheme, userChannel, f'{Hitch.user.mention}', 'Hitch', client, embed)
        Nile = await searchFunctions.roleIDToPlayer(currentGame, 'Nile')
        if Nile != None and Nile in currentGame.livingPlayers and len(currentGame.currentExpo.sabotagedExpedition) > 0:
            user = databaseManager.searchForUser(Nile.user)
            userChannel = client.get_channel(user['channelID'])
            embed = await embedBuilder.nileEmbed(currentGame, currentTheme, Nile)
            await webhookManager.sendWebhook(currentGame, currentTheme, userChannel, f'{Nile.user.mention}', 'Nile', client, embed)
        Connie = await searchFunctions.roleIDToPlayer(currentGame, 'Connie')
        if Connie != None and Connie in currentGame.livingPlayers and Connie in currentGame.currentExpo.expeditionMembers and len(currentGame.currentExpo.sabotagedExpedition) == 0:
            connieFlag = False
            for player in currentGame.currentExpo.expeditionMembers:
                if player in currentGame.warriors:
                    connieFlag = True
                    break
            if connieFlag:
                user = databaseManager.searchForUser(Connie.user)
                userChannel = client.get_channel(user['channelID'])
                embed = await embedBuilder.infoUpdate(currentTheme, Connie, currentTheme.connieMessage)
                await webhookManager.sendWebhook(currentGame, currentTheme, userChannel, f'{Connie.user.mention}', 'Connie', client, embed)
                Connie.stats.connieAlert()


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
        Hitch = await searchFunctions.roleIDToPlayer(currentGame, 'Hitch')
        if Hitch != None:
            Daz = await searchFunctions.roleIDToPlayer(currentGame, 'Daz')
            hitchInfo = {'Daz': Daz}
            user = databaseManager.searchForUser(Hitch.user)
            userChannel = client.get_channel(user['channelID'])
            hitchMessage = currentTheme.getHitchInfo(currentGame, Hitch, hitchInfo)
            embed = await embedBuilder.infoUpdate(currentTheme, Hitch, hitchMessage)
            await webhookManager.sendWebhook(currentGame, currentTheme, userChannel, f'{Hitch.user.mention}', 'Hitch', client)
            await webhookManager.sendWebhook(currentGame, currentTheme, userChannel, '', 'Hitch', client, embed)

    async def mikasaWebhook(currentGame, currentTheme, home, client):
        await webhookManager.sendWebhook(currentGame, currentTheme, home, currentTheme.mikasaMessage, 'Mikasa', client)

    async def reinerWebhook(currentGame, currentTheme, home, client):
        await webhookManager.sendWebhook(currentGame, currentTheme, home, currentTheme.reinerMessage, '{ALTERNATE}Reiner', client)

    async def basementSkipWebhook(currentGame, currentTheme, home, client):
        await webhookManager.sendWebhook(currentGame, currentTheme, home, currentTheme.retreatMessage, '{ALTERNATE}Zeke', client)

    async def erenFrecklemirWebhook(currentGame, currentTheme, channel, msg, embed, client):
        await webhookManager.sendWebhook(currentGame, currentTheme, channel, msg, 'Eren', client, embed)

    async def ymirWebhook(currentGame, currentTheme, channel, msg, embed, client):
        await webhookManager.sendWebhook(currentGame, currentTheme, channel, msg, 'Ymir', client, embed)
    
    async def ymirMessageWebhook(currentGame, currentTheme, channel, embed, client):
        await webhookManager.sendWebhook(currentGame, currentTheme, channel, currentGame.ymirGuiding.user.mention, 'Ymir', client, embed)

    async def ymirRevivalWebhook(currentGame, currentTheme, home, msg, client):
        await webhookManager.sendWebhook(currentGame, currentTheme, home, msg, 'Ymir', client)

    async def ymirBlessingGrantedWebook(currentGame, currentTheme, client):
        Ymir = await searchFunctions.roleIDToPlayer(currentGame, 'Ymir')
        await webhookManager.sendWebhook(currentGame, currentTheme, currentGame.home, f'{currentGame.blessedPlayer.user.mention}, you have been granted {Ymir.role.shortName}\'s Blessing. Use `{currentGame.prefix}check @player` to determine what team they are on.', 'Ymir', client)

    async def ymirBlessingCheckWebhook(currentGame, currentTheme, channel, embed):
        await webhookManager.sendWebhook(currentGame, currentTheme, channel, currentGame.blessedPlayer.user.mention, 'Ymir', currentGame.client, embed)
    
