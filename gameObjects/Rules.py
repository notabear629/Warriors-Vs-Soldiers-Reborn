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


    






