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
                    if foundRole.secondaryEmoji == None or type(foundRole.secondaryEmoji) == str:
                        authorAvatar = foundRole.secondaryImageURL
                    else:
                        authorAvatar = foundRole.secondaryEmoji.url
            else:
                foundRole = await searchFunctions.roleIDToRoleFromLoadedRoles(currentGame.loadedRoles, author)
                if foundRole != None:
                    if foundRole.emoji == None or type(foundRole.emoji) == str:
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
        if currentGame.currentExpo.magathActivated:
            await webhookManager.sendWebhook(currentGame, currentTheme, home, currentTheme.magathMessage, 'Magath', client)
            Magath = await searchFunctions.roleIDToPlayer(currentGame, 'Magath')
            if Magath != None:
                await currentGame.killPlayer(Magath, Magath, 'Magath')
                deathMessage = currentTheme.getMagathDeathMessage(currentGame, currentTheme, Magath)
                if deathMessage != '':
                    await home.send(deathMessage)
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
        if currentGame.currentExpo.warhammerActivated == 'Zachary':
            await webhookManager.sendWebhook(currentGame, currentTheme, home, currentTheme.zacharyMessage, 'Zachary', client)
            if currentGame.currentExpo.jeanActivated:
                await home.send(currentTheme.conflictJeanZacharyMessage)
            if Hitch != None:
                Warhammer = await searchFunctions.roleIDToPlayer(currentGame, 'Warhammer')
                hitchInfo['Warhammer'] = Warhammer
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
        if currentGame.currentExpo.yelenaStolen != None and Hitch != None:
            Yelena = await searchFunctions.roleIDToPlayer(currentGame, 'Yelena')
            hitchInfo['Yelena'] = Yelena
        if currentGame.currentExpo.samuelActivated and Hitch != None:
            Samuel = await searchFunctions.roleIDToPlayer(currentGame, 'Samuel')
            hitchInfo['Samuel'] = Samuel
        if currentGame.currentExpo.warhammerActivated == 'Samuel' and Hitch != None:
            Warhammer = await searchFunctions.roleIDToPlayer(currentGame, 'Warhammer')
            hitchInfo['Warhammer'] = Warhammer
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
        if currentGame.currentExpo.hannesActivated != None:
            Hannes = await searchFunctions.roleIDToPlayer(currentGame, 'Hannes')
            await webhookManager.sendWebhook(currentGame, currentTheme, home, currentTheme.hannesMessage, 'Hannes', client)
            await home.send(f'**{Hannes.user.name}** was spotted fleeing the {currentTheme.expeditionName}!')
        if currentGame.currentExpo.warhammerActivated == 'Hannes':
            Warhammer = await searchFunctions.roleIDToPlayer(currentGame, 'Warhammer')
            await webhookManager.sendWebhook(currentGame, currentTheme, home, currentTheme.hannesMessage, 'Hannes', client)
            await home.send(f'**{Warhammer.user.name}** was spotted fleeing the {currentTheme.expeditionName}!')
        if currentGame.currentExpo.arminActivated:
            await webhookManager.sendWebhook(currentGame, currentTheme, home, currentTheme.arminMessage, '{ALTERNATE}Armin', client)
            if Hitch != None:
                Armin = await searchFunctions.roleIDToPlayer(currentGame, 'Armin')
                hitchInfo['Armin'] = Armin
        if currentGame.currentExpo.warhammerActivated == 'Armin':
            await webhookManager.sendWebhook(currentGame, currentTheme, home, currentTheme.arminMessage, '{ALTERNATE}Armin', client)
            if Hitch != None:
                Warhammer = await searchFunctions.roleIDToPlayer(currentGame, 'Warhammer')
                hitchInfo['Warhammer'] = Warhammer
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
        if currentGame.currentExpo.warhammerActivated == 'LeviAttack':
            Warhammer = await searchFunctions.roleIDToPlayer(currentGame, 'Warhammer')
            await webhookManager.sendWebhook(currentGame, currentTheme, home, currentTheme.leviAttackMessage, '{ALTERNATE}Levi', client)
            for player in currentGame.warriors:
                user = databaseManager.searchForUser(player.user)
                userChannel = client.get_channel(user['channelID'])
                await webhookManager.sendWebhook(currentGame, currentTheme, userChannel, f'{player.user.mention}\n\n{currentTheme.warhammerApologyMessage}', 'Warhammer', client)
            if Hitch != None:
                Warhammer = await searchFunctions.roleIDToPlayer(currentGame, 'Warhammer')
                hitchInfo['Warhammer'] = Warhammer    
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
        if currentGame.currentExpo.warhammerActivated == 'LeviDefend' and len(currentGame.currentExpo.sabotagedExpedition) > 0:
            Warhammer = await searchFunctions.roleIDToPlayer(currentGame, 'Warhammer')
            await webhookManager.sendWebhook(currentGame, currentTheme, home, currentTheme.leviDefendMessage, 'Levi', client)
            for player in currentGame.warriors:
                user = databaseManager.searchForUser(player.user)
                userChannel = client.get_channel(user['channelID'])
                await webhookManager.sendWebhook(currentGame, currentTheme, userChannel, f'{player.user.mention}\n\n{currentTheme.warhammerApologyMessage}', 'Warhammer', client)
            if Hitch != None:
                hitchInfo['Warhammer'] = Warhammer
        if currentGame.ricoTargeted in currentGame.currentExpo.expeditionMembers and not currentGame.ricoFired:
            Rico = await searchFunctions.roleIDToPlayer(currentGame, 'Rico')
            await webhookManager.sendWebhook(currentGame, currentTheme, home, currentTheme.ricoMessage, 'Rico', client)
            currentGame.ricoFire()
            if Hitch != None:
                hitchInfo['Rico'] = Rico
        if type(currentGame.warhammerAbility) == dict and 'Rico' in currentGame.warhammerAbility and currentGame.warhammerAbility['Rico'] in currentGame.currentExpo.expeditionMembers:
            Warhammer = await searchFunctions.roleIDToPlayer(currentGame, 'Warhammer')
            if Warhammer != None and Warhammer.role.abilityActive:
                await webhookManager.sendWebhook(currentGame, currentTheme, home, currentTheme.ricoMessage, 'Rico', client)
                Warhammer.role.disableAbility()
                if Hitch != None:
                    hitchInfo['Warhammer'] = Warhammer
        if currentGame.currentExpo.petraWatched != None and currentGame.currentExpo.petraWatched in currentGame.currentExpo.sabotagedExpedition:
            Petra = await searchFunctions.roleIDToPlayer(currentGame, 'Petra')
            await webhookManager.sendWebhook(currentGame, currentTheme, home, currentTheme.petraMessage, 'Petra', client)
            if Hitch != None:
                hitchInfo['Petra'] = Petra
        if type(currentGame.currentExpo.warhammerActivated) == dict and 'Petra' in currentGame.currentExpo.warhammerActivated and currentGame.currentExpo.warhammerActivated['Petra'] in currentGame.currentExpo.sabotagedExpedition:
            Warhammer = await searchFunctions.roleIDToPlayer(currentGame, 'Warhammer')
            await webhookManager.sendWebhook(currentGame, currentTheme, home, currentTheme.petraMessage, 'Petra', client)
            if Hitch != None:
                hitchInfo['Warhammer'] = Warhammer
        if currentGame.currentExpo.kennyMurdered != None:
            Kenny = await searchFunctions.roleIDToPlayer(currentGame, 'Kenny')
            kennyMsg = currentTheme.kennyMessage
            if currentGame.currentExpo.kennyMurdered == Kenny:
                kennyMsg = currentTheme.kennySuicideMessage
            await webhookManager.sendWebhook(currentGame, currentTheme, home, kennyMsg, 'Kenny', client)
            if Hitch != None:
                hitchInfo['Kenny'] = Kenny
        if currentGame.currentExpo.willyBombed != None:
            willyMsg = currentTheme.willyMessage
            await webhookManager.sendWebhook(currentGame, currentTheme, home, willyMsg, '{ALTERNATE}Willy', client)
        Sasha = await searchFunctions.roleIDToPlayer(currentGame, 'Sasha')
        if Sasha != None and currentGame.sashaTargeted in currentGame.currentExpo.expeditionMembers and Sasha not in currentGame.currentExpo.expeditionMembers and Sasha.role.abilityActive:
            await webhookManager.sendWebhook(currentGame, currentTheme, home, currentTheme.sashaMessage, 'Sasha', client)
            if Hitch != None:
                Sasha = await searchFunctions.roleIDToPlayer(currentGame, 'Sasha')
                hitchInfo['Sasha'] = Sasha
        Warhammer = await searchFunctions.roleIDToPlayer(currentGame, 'Warhammer')
        if Warhammer != None and type(currentGame.warhammerAbility) == dict and 'Sasha' in currentGame.warhammerAbility and currentGame.warhammerAbility['Sasha'] in currentGame.currentExpo.expeditionMembers and Warhammer not in currentGame.currentExpo.expeditionMembers and Warhammer.role.abilityActive:
            await webhookManager.sendWebhook(currentGame, currentTheme, home, currentTheme.sashaMessage, 'Sasha', client)
            if Hitch != None:
                hitchInfo['Warhammer'] = Warhammer
        Gabi = await searchFunctions.roleIDToPlayer(currentGame, 'Gabi')
        if Gabi !=None and currentGame.gabiTargeted != None and currentGame.gabiTargeted not in currentGame.deadPlayers:
            await webhookManager.sendWebhook(currentGame, currentTheme, home, currentTheme.gabiMessage, 'Gabi', client)
            if Hitch != None:
                hitchInfo['Gabi'] = Gabi
        Annie = await searchFunctions.roleIDToPlayer(currentGame, 'Annie')
        if currentGame.annieMessage != None and Annie != None and Annie in currentGame.livingPlayers:
            await webhookManager.sendWebhook(currentGame, currentTheme, home, currentTheme.annieMessage, '{ALTERNATE}Annie', client)
            for player in currentGame.warriors:
                    user = databaseManager.searchForUser(player.user)
                    userChannel = client.get_channel(user['channelID'])
                    await webhookManager.sendWebhook(currentGame, currentTheme, userChannel, f'{player.user.mention}\n\n{currentGame.annieMessage}', '{ALTERNATE}Annie', client)
            Annie.role.disableAbility()
            if currentGame.currentRules.casual == False:
                Annie.stats.annieScream()
            currentGame.changeAnnieMessage(None)
            if Hitch != None:
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
        pass

    async def processHangeWebhook(currentGame, currentTheme, arg):
        client = currentGame.client
        Hange = await searchFunctions.roleIDToPlayer(currentGame, 'Hange')
        if currentGame.currentExpo.hangeActivated == False and Hange != None and Hange in currentGame.livingPlayers:
            user = databaseManager.searchForUser(Hange.user)
            userChannel = client.get_channel(user['channelID'])
            msg = ''
            if arg in ['Accept', 'Reject', 'Abstain']:
                msg = f'**{currentGame.hangeWiretapped.user.name}** has submitted a vote to {arg}!'
            elif arg not in ['Pass', 'Sabotage']:
                msg = f'❗An ability of {currentGame.hangeWiretapped.role.emoji}{currentGame.hangeWiretapped.role.name}{currentGame.hangeWiretapped.role.emoji} has been detected❗'
            if msg != '':
                embed = await embedBuilder.hangeEmbed(currentGame, currentTheme, msg)
                await webhookManager.sendWebhook(currentGame, currentTheme, userChannel, f'{Hange.user.mention}', 'Hange', client, embed)
        if currentGame.currentRules.casual == False:
            Hange.stats.processWiretap(currentGame)

    async def processColtWebhook(currentGame, currentTheme, arg, warrior):
        client = currentGame.client
        Colt = await searchFunctions.roleIDToPlayer(currentGame, 'Colt')
        if Colt in currentGame.livingPlayers:
            user = databaseManager.searchForUser(Colt.user)
            userChannel = client.get_channel(user['channelID'])
            msg = ''
            if arg in ['Accept', 'Reject', 'Abstain']:
                msg = f'Your comrade, **{warrior.user.name}** has submitted a vote to {arg}!'
            elif arg not in ['Pass', 'Sabotage']:
                msg = f'❗Your comrade **{warrior.role.emoji}{warrior.role.name}{warrior.role.emoji}** has used their special ability❗'
            if msg != '':
                embed = await embedBuilder.coltEmbed(currentGame, currentTheme, msg)
                await webhookManager.sendWebhook(currentGame, currentTheme, userChannel, f'{Colt.user.mention}', 'Colt', client, embed)
            if currentGame.currentRules.casual == False:
                Colt.stats.processWire()

    async def erwinWebhook(currentGame, currentTheme, home, client):
        if currentGame.currentExpo.erwinActivated:
            Erwin = await searchFunctions.roleIDToPlayer(currentGame, 'Erwin')
            erwinMessage = currentTheme.getErwinMessage(Erwin)
        if currentGame.currentExpo.warhammerActivated == 'Erwin':
            Warhammer = await searchFunctions.roleIDToPlayer(currentGame, 'Warhammer')
            erwinMessage = currentTheme.getErwinMessage(Warhammer)
        await webhookManager.sendWebhook(currentGame, currentTheme, home, erwinMessage, 'Erwin', client)

    async def friedaWebhook(currentGame, currentTheme, home, client):
        friedaMessage = currentTheme.getFriedaMessage(currentGame)
        await webhookManager.sendWebhook(currentGame, currentTheme, home, friedaMessage, 'Frieda', client)
        Frieda = await searchFunctions.roleIDToPlayer(currentGame, 'Frieda')
        Hitch = await searchFunctions.roleIDToPlayer(currentGame, 'Hitch')
        if Hitch != None:
            hitchInfo = {'Frieda':Frieda}
            user = databaseManager.searchForUser(Hitch.user)
            userChannel = client.get_channel(user['channelID'])
            hitchMessage = currentTheme.getHitchInfo(currentGame, Hitch, hitchInfo)
            embed = await embedBuilder.infoUpdate(currentTheme, Hitch, hitchMessage)
            await webhookManager.sendWebhook(currentGame, currentTheme, userChannel, f'{Hitch.user.mention}', 'Hitch', client, embed)

    async def pyxisWebhook(currentGame, currentTheme, home, client):
        Pyxis = await searchFunctions.roleIDToPlayer(currentGame, 'Pyxis')
        Warhammer = await searchFunctions.roleIDToPlayer(currentGame, 'Warhammer')
        if Pyxis != None and currentGame.currentExpo.pyxisTrial != None:
            await webhookManager.sendWebhook(currentGame, currentTheme, home, currentTheme.pyxisMessage, 'Pyxis', client)
            Hitch = await searchFunctions.roleIDToPlayer(currentGame, 'Hitch')
            if Hitch != None:
                hitchInfo = {'Pyxis':Pyxis}
                user = databaseManager.searchForUser(Hitch.user)
                userChannel = client.get_channel(user['channelID'])
                hitchMessage = currentTheme.getHitchInfo(currentGame, Hitch, hitchInfo)
                embed = await embedBuilder.infoUpdate(currentTheme, Hitch, hitchMessage)
                await webhookManager.sendWebhook(currentGame, currentTheme, userChannel, f'{Hitch.user.mention}', 'Hitch', client, embed)
        if type(currentGame.currentExpo.warhammerActivated) == dict and 'Pyxis' in currentGame.currentExpo.warhammerActivated:
            await webhookManager.sendWebhook(currentGame, currentTheme, home, currentTheme.pyxisMessage, 'Pyxis', client)
            Hitch = await searchFunctions.roleIDToPlayer(currentGame, 'Hitch')
            if Hitch != None:
                hitchInfo = {'Warhammer':Warhammer}
                user = databaseManager.searchForUser(Hitch.user)
                userChannel = client.get_channel(user['channelID'])
                hitchMessage = currentTheme.getHitchInfo(currentGame, Hitch, hitchInfo)
                embed = await embedBuilder.infoUpdate(currentTheme, Hitch, hitchMessage)
                await webhookManager.sendWebhook(currentGame, currentTheme, userChannel, f'{Hitch.user.mention}', 'Hitch', client, embed)

    async def dazWebhook(currentGame, currentTheme, home, client):
        if currentGame.currentExpo.dazActivated:
            await webhookManager.sendWebhook(currentGame, currentTheme, home, currentTheme.dazMessage, 'Daz', client)
        if currentGame.currentExpo.warhammerActivated == 'Daz':
            await webhookManager.sendWebhook(currentGame, currentTheme, home, currentTheme.dazMessage, 'Daz', client)
        Hitch = await searchFunctions.roleIDToPlayer(currentGame, 'Hitch')
        if Hitch != None:
            hitchInfo = {}
            if currentGame.currentExpo.dazActivated:
                Daz = await searchFunctions.roleIDToPlayer(currentGame, 'Daz')
                hitchInfo['Daz'] = Daz
            if currentGame.currentExpo.warhammerActivated == 'Daz':
                Warhammer = await searchFunctions.roleIDToPlayer(currentGame, 'Warhammer')
                hitchInfo['Warhammer'] = Warhammer
            user = databaseManager.searchForUser(Hitch.user)
            userChannel = client.get_channel(user['channelID'])
            hitchMessage = currentTheme.getHitchInfo(currentGame, Hitch, hitchInfo)
            embed = await embedBuilder.infoUpdate(currentTheme, Hitch, hitchMessage)
            await webhookManager.sendWebhook(currentGame, currentTheme, userChannel, f'{Hitch.user.mention}', 'Hitch', client, embed)

    async def mikasaWebhook(currentGame, currentTheme, home, client):
        await webhookManager.sendWebhook(currentGame, currentTheme, home, currentTheme.mikasaMessage, 'Mikasa', client)
        Hitch = await searchFunctions.roleIDToPlayer(currentGame, 'Hitch')
        if Hitch != None:
            Mikasa = await searchFunctions.roleIDToPlayer(currentGame, 'Mikasa')
            hitchInfo = {'Mikasa':Mikasa}
            user = databaseManager.searchForUser(Hitch.user)
            userChannel = client.get_channel(user['channelID'])
            hitchMessage = currentTheme.getHitchInfo(currentGame, Hitch, hitchInfo)
            embed = await embedBuilder.infoUpdate(currentTheme, Hitch, hitchMessage)
            await webhookManager.sendWebhook(currentGame, currentTheme, userChannel, f'{Hitch.user.mention}', 'Hitch', client, embed)

    async def marcoWebhook(currentGame, currentTheme, home, client):
        if currentGame.currentExpo.marcoActivated:
            await webhookManager.sendWebhook(currentGame, currentTheme, home, currentTheme.marcoMessage, '{ALTERNATE}Marco', client)
        if currentGame.currentExpo.warhammerActivated == 'Marco':
            await webhookManager.sendWebhook(currentGame, currentTheme, home, currentTheme.marcoMessage, '{ALTERNATE}Marco', client)

    async def reinerWebhook(currentGame, currentTheme, home, client):
        await webhookManager.sendWebhook(currentGame, currentTheme, home, currentTheme.reinerMessage, '{ALTERNATE}Reiner', client)

    async def basementSkipWebhook(currentGame, currentTheme, home, client):
        await webhookManager.sendWebhook(currentGame, currentTheme, home, currentTheme.retreatMessage, '{ALTERNATE}Zeke', client)

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
    
