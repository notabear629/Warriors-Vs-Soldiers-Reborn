from rulesData.defaultRules import defaultRules
from gameObjects.Role import Role

class Rules:

    def __init__(self):
        default = defaultRules
        self.setRules(default)

    def setRules(self, rules):
        for key, value in vars(rules).items():
            if key.startswith('__'):
                continue
            else:
                setattr(self, key, value)

    def changeRoles(self, roles, enabledArg):

        if roles[0] in Role.soldierGroupOptional:
            team = 'Soldiers'
        elif roles[0] in Role.warriorGroupOptional:
            team = 'Warriors'
        else:
            team = 'Wildcards'


        enableCopy = getattr(self, f'enabled{team}').copy()
        disableCopy = getattr(self, f'disabled{team}').copy()

        if enabledArg == 'Enable':
            for role in roles:
                if role not in enableCopy:
                    enableCopy.append(role)
                if role in disableCopy:
                    disableCopy.remove(role)

        elif enabledArg == 'Neutral':   
            for role in roles:
                if role in enableCopy:
                    enableCopy.remove(role)
                if role in disableCopy:
                    disableCopy.remove(role)

        else:
            for role in roles:
                if role in enableCopy:
                    enableCopy.remove(role)
                if role not in disableCopy:
                    disableCopy.append(role)

        
        setattr(self, f'enabled{team}', enableCopy)
        setattr(self, f'disabled{team}', disableCopy)
            


    def clearRoles(self, team):
        if team == 'Soldiers':
            self.disabledSoldiers = []
            self.enabledSoldiers = []
        elif team == 'Warriors':
            self.enabledWarriors = []
            self.disabledWarriors = []
        elif team == 'Wildcards':
            self.enabledWildcards = []
            self.disabledWildcards = []
    
    def toggleMultikidnap(self, toggle):
        self.multikidnap = toggle

    def toggleRumbling(self, toggle):
        self.rumbling = toggle

    def toggleCasual(self, toggle):
        self.casual = toggle

    def toggleCaptains(self, erenKey, zekeKey):
        self.noCoordinate = not erenKey
        self.noWarchief = not zekeKey

    def toggleIntelligentRoles(self):
        self.intelligentRoles = not self.intelligentRoles
        
    def toggleWildcards(self):
        self.wildcards = not self.wildcards

    def loadRules(self, rules):
        for key, value in rules.items():
            setattr(self, key, value)


    






