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
    soldierGroupAbility = ['Jean']

    #Combine all optional Soldier Roles
    soldierGroupOptional = soldierGroupInfo + soldierGroupAbility

    #We combine all the previous groups to create a complete list of soldier roles
    soldierRoles = soldierGroupCoordinate + soldierGroupOptional + soldierGroupDefault

    #The Warchief roles. Same business as the Coordinate roles, but for the Warriors.
    warriorGroupWarchief = ['Zeke']

    #The group of all option Warriors with one-time special abilities
    warriorGroupAbility = ['Pieck']

    #The default Warrior classes.
    warriorGroupDefault = ['Warrior']

    #Combine all optional Warrior Roles
    warriorGroupOptional = warriorGroupAbility

    #Combine all warrior groups to make a complete warrior list
    warriorRoles = warriorGroupWarchief + warriorGroupOptional + warriorGroupDefault

    #Combine all roles into one
    allRoles = soldierRoles + warriorRoles

    #Combine all Roles with getInfo functions to one list
    infoMessageRoles = soldierGroupCoordinate + warriorRoles + soldierGroupInfo

    def __init__(self, roleInfo):
        self.id = roleInfo['roleID']
        self.name = roleInfo['name']
        self.shortName = roleInfo['shortName']
        self.team = roleInfo['team']
        self.isTitan = roleInfo['isTitan']
        self.emoji = roleInfo['emoji']
        self.imageURL = roleInfo['imageURL']
        self.roleMessage = roleInfo['roleMessage']
        self.gameRole = roleInfo['gameRole']
        self.helpInfo = roleInfo['helpInfo']
        self.abilityActive = True

    def disableAbility(self):
        self.abilityActive = False

    def loadRoles(currentTheme, client):
        roleList = []
        for role in Role.allRoles:
            getRole = getattr(currentTheme, role)
            newRole = Role(getRole)
            if type(newRole.emoji) == int:
                newRole.emoji = client.get_emoji(newRole.emoji)
            roleList.append(newRole)
        return roleList
    
    def update(self, currentTheme, client):
        roleInfo = getattr(currentTheme, self.id)
        self.id = roleInfo['roleID']
        self.name = roleInfo['name']
        self.shortName = roleInfo['shortName']
        self.team = roleInfo['team']
        self.isTitan = roleInfo['isTitan']
        self.emoji = roleInfo['emoji']
        self.imageURL = roleInfo['imageURL']
        self.roleMessage = roleInfo['roleMessage']
        self.gameRole = roleInfo['gameRole']
        self.helpInfo = roleInfo['helpInfo']
        if type(self.emoji) == int:
            self.emoji = client.get_emoji(self.emoji)
