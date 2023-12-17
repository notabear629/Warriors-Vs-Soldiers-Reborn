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
    soldierGroupAbility = ['Jean']

    #Group of all optional soldiers that are Defender class
    soldierGroupDefender = ['Levi']

    #A group of all Lethal Soldiers
    soldierGroupLethal = ['Armin', 'Sasha']

    #A group of all Analytical Soldiers
    soldierGroupAnalyst = ['Hange', 'Mike', 'Hitch']

    #Combine all optional Soldier Roles
    soldierGroupOptional = soldierGroupInfo + soldierGroupAbility + soldierGroupDefender + soldierGroupLethal + soldierGroupAnalyst

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
        self.secondaryEmoji = roleInfo['secondaryEmoji']
        self.imageURL = roleInfo['imageURL']
        self.roleMessage = roleInfo['roleMessage']
        self.gameRole = roleInfo['gameRole']
        self.helpInfo = roleInfo['helpInfo']
        self.abilityActive = True

    def disableAbility(self):
        self.abilityActive = False

    async def startHange(self, currentGame, Hange):
        self.confirmedSoldiers = [Hange]
        self.confirmedWarriors = []
        await self.generateAllTeams(currentGame)

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
        if type(self.secondaryEmoji) == int:
            self.secondaryEmoji = client.get_emoji(self.secondaryEmoji)

    async def generateAllTeams(self, currentGame):
        warriorAmount = len(currentGame.warriors)
        possibleWarriors = currentGame.players.copy()
        for soldier in self.confirmedSoldiers:
            if soldier in possibleWarriors:
                possibleWarriors.remove(soldier)
        self.possibleWarriorTeams = list(combinations(possibleWarriors, warriorAmount))

    async def confirmSoldier(self, soldier):
        self.confirmedSoldiers.append(soldier)

    async def confirmWarrior(self, warrior):
        self.confirmedWarriors.append(warrior)

    async def hangeProcess(self, currentGame):
        await self.identifyDeadPlayers(currentGame)
        await self.indictWarriors()
        await self.absolveSoldiers()
        await self.crossReference(currentGame)
        await self.confirmFromPossibilities(currentGame)

    async def identifyDeadPlayers(self, currentGame):
        for player in currentGame.deadPlayers:
            if player in currentGame.soldiers and player not in self.confirmedSoldiers:
                self.confirmedSoldiers.append(player)
            if player in currentGame.warriors and player not in self.confirmedWarriors:
                self.confirmedWarriors.append(player)

    async def indictWarriors(self):
        possibleTeams = self.possibleWarriorTeams.copy()
        for team in self.possibleWarriorTeams:
            for warrior in self.confirmedWarriors:
                if warrior not in team:
                    possibleTeams.remove(team)
        self.possibleWarriorTeams = possibleTeams

    async def absolveSoldiers(self):
        possibleTeams = self.possibleWarriorTeams.copy()
        for team in self.possibleWarriorTeams:
            for soldier in self.confirmedSoldiers:
                if soldier in team:
                    possibleTeams.remove(team)
        self.possibleWarriorTeams = possibleTeams

    async def crossReference(self, currentGame):
        possibleTeams = self.possibleWarriorTeams.copy()
        requirements = await self.getRequirements(currentGame)
        for requirement in requirements:
            expoTeam = requirement['expoTeam']
            minWarrior = requirement['minWarrior']
            benchSquad = requirement['benchSquad']
            maxWarriorBenched = requirement['maxWarriorBenched']

            for team in self.possibleWarriorTeams:
                memberOnExpo = []
                for member in team:
                    if member in expoTeam:
                        memberOnExpo.append(member)
                if len(memberOnExpo) < minWarrior:
                    possibleTeams.remove(team)
                    continue
                memberOnBench = []
                for member in team:
                    if member in benchSquad:
                        memberOnBench.append(member)
                if len(memberOnBench) > maxWarriorBenched:
                    possibleTeams.remove(team)
        self.possibleWarriorTeams = possibleTeams


    async def getRequirements(self, currentGame):
        requirements = []

        for expo in currentGame.expeditionHistory:
            newRequirement = {}
            shiftedExpo = expo.expeditionMembers.copy()
            for member in expo.expeditionMembers:
                if member in self.confirmedSoldiers:
                    shiftedExpo.remove(member)
            newRequirement['expoTeam'] = shiftedExpo
            newRequirement['minWarrior'] = len(expo.sabotagedExpedition)
            benchSquad = []
            for player in currentGame.players:
                if player not in expo.expeditionMembers:
                    benchSquad.append(player)
            newRequirement['benchSquad'] = benchSquad
            newRequirement['maxWarriorBenched'] = len(currentGame.warriors) - len(expo.sabotagedExpedition)
            requirements.append(newRequirement)
        return requirements

    async def confirmFromPossibilities(self, currentGame):
        for player in currentGame.players:
            if player in self.confirmedSoldiers or player in self.confirmedWarriors:
                continue
            mayBeWarrior = False
            definitelyWarrior = True
            for team in self.possibleWarriorTeams:
                if player in team:
                    mayBeWarrior = True
                if player not in team:
                    definitelyWarrior = False
                if definitelyWarrior == False and mayBeWarrior:
                    break
            if mayBeWarrior == False and player not in self.confirmedSoldiers:
                self.confirmedSoldiers.append(player)
            if definitelyWarrior and player not in self.confirmedWarriors:
                self.confirmedWarriors.append(player)

    def getProbabilities(self, currentGame):
        probabilities = {}
        for player in currentGame.players:
            if player in self.confirmedSoldiers:
                probabilities[player] = 0
            elif player in self.confirmedWarriors:
                probabilities[player] = 100
            else:
                scenariosWithPlayer = 0
                for team in self.possibleWarriorTeams:
                    if player in team:
                        scenariosWithPlayer += 1
                calculation = scenariosWithPlayer/len(self.possibleWarriorTeams)*100
                calculation = round(calculation, 2)
                probabilities[player] = calculation
        return probabilities
                

                




