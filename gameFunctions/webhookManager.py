import discord
from discord.ext import commands

from gameFunctions.searchFunctions import searchFunctions

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
            foundPlayer = await searchFunctions.roleIDToPlayer(currentGame, author)
            if foundPlayer != None:
                authorName = foundPlayer.role.name
                if type(foundPlayer.role.emoji) == str:
                    authorAvatar = foundPlayer.role.imageURL
                else:
                    authorAvatar = foundPlayer.role.emoji.url

        await ourWebhook.send(message, embed=embed, username= authorName, avatar_url = authorAvatar, wait = True)

    async def processExpoVoteWebhooks(currentGame, currentTheme, home, client):
        if currentGame.currentExpo.jeanActivated:
            await webhookManager.sendWebhook(currentGame, currentTheme, home, currentTheme.jeanMessage, 'Jean', client)
        if currentGame.currentExpo.pieckActivated and currentGame.currentExpo.jeanActivated == False:
            await webhookManager.sendWebhook(currentGame, currentTheme, home, currentTheme.pieckMessageWithoutJean, 'Pieck', client)
        if currentGame.currentExpo.pieckActivated and currentGame.currentExpo.jeanActivated:
            await webhookManager.sendWebhook(currentGame, currentTheme, home, currentTheme.pieckMessageWithJean, 'Pieck', client)
    
