class Role:
    #DO NOT EDIT ANY OF THESE GROUPS!
    #The names within these lists should match with their corresponding class name.

    #Group of Coordinate roles (Mostly useless because it's just Eren, but if we want to add an alternative Coordinate in the future, it could be nice to have this)
    soldierGroupCoordinate = ['Eren']

    #Kind of same thing as Eren, there's only 1 basic soldier, but whatever
    soldierGroupDefault = ['Soldier']

    #Combine all optional Soldier Roles
    soldierGroupOptional = []

    #We combine all the previous groups to create a complete list of soldier roles
    soldierRoles = soldierGroupCoordinate + soldierGroupDefault

    #The Warchief roles. Same business as the Coordinate roles, but for the Warriors.
    warriorGroupWarchief = ['Zeke']

    #The default Warrior classes.
    warriorGroupDefault = ['Warrior']

    #Combine all optional Warrior Roles
    warriorGroupOptional = []

    #Combine all warrior groups to make a complete warrior list
    warriorRoles = warriorGroupWarchief + warriorGroupDefault

    #Combine all Roles with getInfo functions to one list
    infoMessageRoles = soldierGroupCoordinate + warriorRoles

    def __init__(self, roleInfo):
        self.id = roleInfo['roleID']
        self.name = roleInfo['name']
        self.shortName = roleInfo['shortName']
        self.team = roleInfo['team']
        self.isTitan = roleInfo['isTitan']
        self.emoji = roleInfo['emoji']
        self.roleMessage = roleInfo['roleMessage']
        self.gameRole = roleInfo['gameRole']
        self.helpInfo = roleInfo['helpInfo']
