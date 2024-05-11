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

    def changeRoles(self, roles, enabled):
        if roles[0] in Role.soldierGroupOptional:
            primaryGroup = self.disabledSoldiers
            secondaryGroup = self.enabledSoldiers
            primaryAttribute = 'disabledSoldiers'
            secondaryAttribute = 'enabledSoldiers'
            if enabled:
                primaryGroup = self.enabledSoldiers
                secondaryGroup = self.disabledSoldiers
                primaryAttribute = 'enabledSoldiers'
                secondaryAttribute = 'disabledSoldiers'
        elif roles[0] in Role.warriorGroupOptional:
            primaryGroup = self.disabledWarriors
            secondaryGroup = self.enabledWarriors
            primaryAttribute = 'disabledWarriors'
            secondaryAttribute = 'enabledWarriors'
            if enabled:
                primaryGroup = self.enabledWarriors
                secondaryGroup = self.disabledWarriors
                primaryAttribute = 'enabledWarriors'
                secondaryAttribute = 'disabledWarriors'
        elif roles[0] in Role.wildcardRoles:
            primaryGroup = self.disabledWildcards
            secondaryGroup = self.enabledWildcards
            primaryAttribute = 'disabledWildcards'
            secondaryAttribute = 'enabledWildcards'
            if enabled:
                primaryGroup = self.enabledWildcards
                secondaryGroup = self.disabledWildcards
                primaryAttribute = 'enabledWildcards'
                secondaryAttribute = 'disabledWildcards'
        for role in roles:
            if role in secondaryGroup:
                secondaryGroup.remove(role)
        primaryGroup = roles
        setattr(self, primaryAttribute, primaryGroup)
        setattr(self, secondaryAttribute, secondaryGroup)

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


    






