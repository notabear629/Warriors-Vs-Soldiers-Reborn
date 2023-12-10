from themeData.defaultGameTheme import *

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
        self.warriorSingle = theme.warriorSingle
        self.warriorPlural = theme.warriorPlural
        self.wallSingle = theme.wallSingle
        self.wallPlural = theme.wallPlural


        #Changing the Soldier Role Themes
        self.Eren = theme.Eren.roleDict
        self.Soldier = theme.Soldier.roleDict

        #Changing the Warrior Role Themes
        self.Zeke = theme.Zeke.roleDict
        self.Warrior = theme.Warrior.roleDict






