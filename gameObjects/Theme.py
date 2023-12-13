from themeData.defaultGameTheme import *
from themeData.eggplant import *
import discord
from discord.ext import commands

from gameObjects.Role import Role

class Theme:

    def __init__(self):
        #Change this to the default theme you want the bot to initialize on
        defaultTheme = defaultGameTheme
        self.setTheme(defaultTheme)

    def setTheme(self, theme):
        for key, value in vars(theme).items():
            if key.startswith('__'):
                continue
            if key in Role.allRoles:
                setattr(self, key, value.roleDict)
            else:
                setattr(self, key, value)


    async def resolveEmojis(self, client):
        for key, value in vars(self).items():
            if key.startswith('emoji'):
                resolvedEmoji = value
                if type(value) == int:
                    resolvedEmoji = client.get_emoji(value)
                setattr(self, key, resolvedEmoji)





