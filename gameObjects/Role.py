from itertools import combinations

class Role:
    #DO NOT EDIT ANY OF THESE GROUPS!
    #The names within these lists should match with their corresponding class name.

    #Group of Coordinate roles (Mostly useless because it's just Eren, but if we want to add an alternative Coordinate in the future, it could be nice to have this)
    soldierGroupCoordinate = ['Eren']

    #Kind of same thing as Eren, there's only 1 basic soldier, but whatever
    soldierGroupDefault = ['Soldier']

    #A group of all optional Soldier roles that have power through information
    soldierGroupInfo = ['Historia']

    #A group of all optional Soldiers with one-time special abilities
    soldierGroupAbility = ['Jean', 'Erwin', 'Daz', 'Keith', 'Zachary', 'Hange', 'Hannes', 'Samuel', 'Frieda']

    #Group of all optional soldiers that are Defender class
    soldierGroupDefender = ['Levi', 'Mikasa']

    #A group of all Lethal Soldiers
    soldierGroupLethal = ['Armin', 'Sasha', 'Petra', 'Pyxis', 'Rico']

    #A group of all Analytical Soldiers
    soldierGroupAnalyst = ['Mike', 'Hitch', 'Floch', 'Nile', 'Connie', 'Marlowe', 'Moblit']

    #A group of Soldiers with passive abilities that assist the Soldiers
    soldierGroupPassive = ['Niccolo', 'Marco']

    #List of roles banned in noEren rulesets
    soldierBannedNoEren = ['Historia', 'Mike', 'Floch', 'Keith']

    #List of roles banned in no zeke rulesets
    soldierBannedNoZeke = ['Historia', 'Keith']

    #Combine all optional Soldier Roles
    soldierGroupOptional = soldierGroupInfo + soldierGroupAbility + soldierGroupDefender + soldierGroupLethal + soldierGroupAnalyst + soldierGroupPassive

    #We combine all the previous groups to create a complete list of soldier roles
    soldierRoles = soldierGroupCoordinate + soldierGroupOptional + soldierGroupDefault

    #The Warchief roles. Same business as the Coordinate roles, but for the Warriors.
    warriorGroupWarchief = ['Zeke']

    #The group of all option Warriors with one-time special abilities
    warriorGroupAbility = ['Pieck', 'Annie', 'Porco', 'Falco', 'Magath', 'Gabi', 'Yelena', 'Warhammer']

    #The group of all option Warriors with multi-use perks
    warriorGroupPerk = ['Reiner', 'Bertholdt', 'Colt', 'Marcel']

    #The group of all option Warriors that are lethal
    warriorGroupLethal = ['Willy']

    #The default Warrior classes.
    warriorGroupDefault = ['Warrior']

    #Combine all optional Warrior Roles
    warriorGroupOptional = warriorGroupAbility + warriorGroupPerk + warriorGroupLethal

    #Combine all warrior groups to make a complete warrior list
    warriorRoles = warriorGroupWarchief + warriorGroupOptional + warriorGroupDefault

    #List of Wildcard Roles
    wildcardRoles = ['Kenny', 'PureTitan', 'Ymir']

    #Combine all roles into one
    allRoles = soldierRoles + warriorRoles + wildcardRoles

    #All Lethal Roles in one
    allLethal = soldierGroupLethal

    #Combine all Roles with getInfo functions to one list
    infoMessageRoles = soldierGroupCoordinate + warriorRoles + soldierGroupInfo

    #Define prime roles for intelligent selection
    primeRoles = ['Historia', 'Jean', 'Daz', 'Moblit', 'Frieda', 'Rico', 'Keith', 'Zachary', 'Hange', 'Samuel', 'Levi', 'Petra', 'Pyxis', 'Mike', 'Floch', 'Nile', 'Connie', 'Niccolo', 'Annie', 'Porco', 'Falco', 'Gabi', 'Yelena', 'Warhammer', 'Bertholdt', 'Willy', 'Magath', 'Colt']

    #Now define role dependencies for intelligent selection
    roleDependencies = {'Erwin':{'soldierCount':4}, 'Hannes':{'soldierCount':4}, 'Mikasa':{'requiredRoles':['Armin', 'Sasha', 'Pyxis', 'Willy']}, 'Armin':{'soldierCount':4}, 'Sasha':{'soldierCount':4}, 'Hitch':{'requiredRoles':['Jean', 'Daz', 'Keith', 'Zachary', 'Hange', 'Samuel', 'Levi', 'Mikasa', 'Sasha', 'Petra', 'Pyxis', 'Pieck', 'Annie', 'Falco', 'Gabi', 'Yelena', 'Warhammer', 'Bertholdt', 'Frieda', 'Rico']}, 'Marlowe':{'requiredRoles':['Levi', 'Armin', 'Sasha', 'Petra', 'Pyxis', 'Willy', 'Rico']}, 'Marco':{'soldierCount':4}, 'Reiner':{'requiredRoles':['Levi', 'Armin', 'Sasha', 'Petra', 'Pyxis', 'Rico']}, 'Colt':{'requiredRoles':['Niccolo'], 'warriorCount':3}, 'Pieck':{'requiredRoles':['Zachary', 'Erwin', 'Daz']}, 'Marcel':{'requiredRoles':['Armin', 'Sasha', 'Pyxis', 'Willy']}}
    

    def __init__(self, roleInfo):
        self.id = roleInfo['roleID']
        self.name = roleInfo['name']
        self.shortName = roleInfo['shortName']
        self.team = roleInfo['team']
        self.rumblingTeam = roleInfo['rumblingTeam']
        self.isTitan = roleInfo['isTitan']
        self.emoji = roleInfo['emoji']
        self.secondaryEmoji = roleInfo['secondaryEmoji']
        self.imageURL = roleInfo['imageURL']
        self.roleMessage = roleInfo['roleMessage']
        self.gameRole = roleInfo['gameRole']
        self.helpInfo = roleInfo['helpInfo']
        self.abilityActive = True

    def disableAbility(self):
        self.abilityActive = False

    def refundAbility(self):
        self.abilityActive = True

    def loadRoles(currentTheme, client):
        roleList = []
        for role in Role.allRoles:
            getRole = getattr(currentTheme, role)
            newRole = Role(getRole)
            if type(newRole.emoji) == int:
                newRole.emoji = client.get_emoji(newRole.emoji)
            if type(newRole.secondaryEmoji) == int:
                newRole.secondaryEmoji = client.get_emoji(newRole.secondaryEmoji)
            roleList.append(newRole)
        return roleList
    
    def update(self, currentTheme, client):
        roleInfo = getattr(currentTheme, self.id)
        self.id = roleInfo['roleID']
        self.name = roleInfo['name']
        self.shortName = roleInfo['shortName']
        self.team = roleInfo['team']
        self.rumblingTeam = roleInfo['rumblingTeam']
        self.isTitan = roleInfo['isTitan']
        self.emoji = roleInfo['emoji']
        self.secondaryEmoji = roleInfo['secondaryEmoji']
        self.imageURL = roleInfo['imageURL']
        self.secondaryImageURL = roleInfo['secondaryImageURL']
        self.roleMessage = roleInfo['roleMessage']
        self.gameRole = roleInfo['gameRole']
        self.helpInfo = roleInfo['helpInfo']
        if type(self.emoji) == int:
            self.emoji = client.get_emoji(self.emoji)
        if type(self.secondaryEmoji) == int:
            self.secondaryEmoji = client.get_emoji(self.secondaryEmoji)

    def copy(self, currentTheme, client):
        roleInfo = getattr(currentTheme, self.id)
        newRole = Role(roleInfo)
        if self.abilityActive == False:
            newRole.disableAbility()
        newRole.resolveEmojis(client)
        return newRole
    
    def resolveEmojis(self, client):
        if type(self.emoji) == int:
            self.emoji = client.get_emoji(self.emoji)
        if type(self.secondaryEmoji) == int:
            self.secondaryEmoji = client.get_emoji(self.secondaryEmoji)
                

                




