from themeData.defaultGameTheme import *
import discord
from discord.ext import commands

class Theme:

    def __init__(self):
        #Change this to the default theme you want the bot to initialize on
        defaultTheme = defaultGameTheme
        print(defaultTheme)
        self.setTheme(defaultTheme)

    def setTheme(self, theme):
        #Changing the basic theme strings
        self.themeName = theme.themeName
        self.gameName = theme.gameName
        self.soldierSingle = theme.soldierSingle
        self.soldierPlural = theme.soldierPlural
        self.emojiSoldier = theme.emojiSoldier
        self.warriorSingle = theme.warriorSingle
        self.warriorPlural = theme.warriorPlural
        self.emojiWarrior = theme.emojiWarrior
        self.wallSingle = theme.wallSingle
        self.wallPlural = theme.wallPlural

        #Changing Some Team Aesthetics
        self.soldierThumbnail = theme.soldierThumbnail
        self.warriorThumbnail = theme.warriorThumbnail
        self.wildcardThumbnail = theme.wildcardThumbnail
        self.soldierColor = theme.soldierColor
        self.warriorColor = theme.warriorColor
        self.wildcardColor = theme.wildcardColor

        #Changing some expedition embed aesthetics
        self.winningColor = theme.winningColor
        self.neutralColor = theme.neutralColor
        self.losingColor = theme.losingColor
        self.lostColor = theme.lostColor
        self.statusProgress = theme.statusProgress
        self.statusWalls = theme.statusWalls
        self.statusExpeditions = theme.statusExpeditions
        self.expeditionName = theme.expeditionName
        self.expoMembersName = theme.expoMembersName
        self.emojiWinMarkerOne = theme.emojiWinMarkerOne
        self.emojiWinMarkerTwo = theme.emojiWinMarkerTwo
        self.emojiWinMarkerThree = theme.emojiWinMarkerThree
        self.emojiSpacer = theme.emojiSpacer
        self.emojiRoundVictoryMarker = theme.emojiRoundVictoryMarker
        self.emojiVictoryMarker = theme.emojiVictoryMarker
        self.emojiMariaExterior = theme.emojiMariaExterior
        self.emojiMariaInterior = theme.emojiMariaInterior
        self.emojiRoseExterior = theme.emojiRoseExterior
        self.emojiRoseInterior = theme.emojiRoseInterior
        self.emojiSinaExterior = theme.emojiSinaExterior
        self.emojiSinaInterior = theme.emojiSinaInterior
        self.emojiWinMarker = theme.emojiWinMarker
        self.emojiFailMarker = theme.emojiFailMarker
        self.emojiCurrentMarker = theme.emojiCurrentMarker

        #Changing some roles embed aesthetics
        self.rolesEmbedColor = theme.rolesEmbedColor

        #Changing Some Role Intro Messages
        self.soldierDefaultMessage = theme.soldierDefaultMessage
        self.warriorDefaultMessage = theme.warriorDefaultMessage
        self.wildcardDefaultMessage = theme.wildcardDefaultMessage


        #Changing the Soldier Role Themes
        self.Eren = theme.Eren.roleDict
        self.Soldier = theme.Soldier.roleDict

        #Changing the Warrior Role Themes
        self.Zeke = theme.Zeke.roleDict
        self.Warrior = theme.Warrior.roleDict

        #Changing info getter functions
        self.getErenInfo = theme.getErenInfo
        self.getWarriorInfo = theme.getWarriorInfo

    async def resolveEmojis(self, client):
        for key, value in vars(self).items():
            if key.startswith('emoji'):
                resolvedEmoji = value
                if type(value) == int:
                    resolvedEmoji = client.get_emoji(value)
                setattr(self, key, resolvedEmoji)





