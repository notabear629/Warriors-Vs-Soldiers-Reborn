class Expedition:
    def __init__(self, commander, size, players):
        self.commander = commander
        self.size = size
        self.expeditionMembers = []
        self.currentlyPicking = True
        self.passed = False
        self.currentlyVoting = False
        self.eligibleVoters = []
        self.voted = []
        self.accepted = []
        self.rejected = []
        self.abstained = []
        self.currentlyExpeditioning = False
        self.expeditioned = []
        self.passedExpedition = []
        self.sabotagedExpedition = []
        self.resultsAvailable = False
        self.jeanActivated = False
        self.zacharyActivated = False
        self.pieckActivated = False
        self.arminActivated = False
        self.leviAttacked = False
        self.leviDefended = False
        self.sashaActivated = False
        self.gabiActivated = False
        self.erwinActivated = False
        self.dazActivated = False
        self.falcoActivated = False
        self.magathActivated = False
        self.mikasaGuarded = None
        self.reinerBlocked = None
        self.kennyMurdered = None
        self.petraWatched = None
        self.bertholdtCloaked = False
        self.hangeActivated = False
        self.hannesActivated = None
        self.willyBombed = None
        self.yelenaStolen = None
        self.usedExpoAbilities = []
        self.filledUp = False
        self.pyxisTrial = None
        self.samuelActivated = False
        self.marcoActivated = False
        self.warhammerActivated = None
        self.displaySize = None
        self.playerFlown = None
        self.flownIn = False
        self.frecklemirMauled = None
        self.ksaverBlackout = False
        self.kitzActivated = False

    def changeCommander(self, commander):
        self.commander = commander
        
    def resetExpo(self, currentGame):
        self.expeditionMembers = []
        self.currentlyPicking = True
        self.passed = False
        self.jeanActivated = False
        self.zacharyActivated = False
        self.pieckActivated = False
        self.falcoActivated = False
        self.magathActivated = False
        self.erwinActivated = False
        self.dazActivated = False
        self.sashaActivated = False
        self.gabiActivated = False
        self.leviAttacked = False
        self.leviDefended = False
        self.mikasaGuarded = None
        self.kennyMurdered = None
        self.arminActivated = False
        self.reinerBlocked = None
        self.bertholdtCloaked = False
        self.petraWatched = None
        self.hangeActivated = False
        self.hannesActivated = None
        self.yelenaStolen = None
        self.willyBombed = None
        self.filledUp = False
        self.pyxisTrial = None
        self.samuelActivated = False
        self.displaySize = None
        self.marcoActivated = False
        self.warhammerActivated = None
        self.playerFlown = None
        self.flownIn = False
        self.frecklemirMauled = None
        self.ksaverBlackout = False
        self.kitzActivated = False

        if currentGame.kitzRound == currentGame.currentRound and currentGame.kitzTarget in currentGame.livingPlayers:
            self.addMember(currentGame.kitzTarget)

    def fillUp(self):
        self.filledUp = True
    
    def activateErwin(self, Erwin):
        if Erwin.role.id == 'Erwin':
            self.erwinActivated = True
        if Erwin.role.id == 'Warhammer':
            self.warhammerActivated = 'Erwin'
        Erwin.role.disableAbility()
        

    def addMember(self, member):
        self.expeditionMembers.append(member)
        if len(self.expeditionMembers) >= self.size:
            self.currentlyPicking = False

    def passExpo(self):
        self.passed = True

    def clearExpedition(self):
        self.expeditionMembers = []

    def beginVoting(self, currentGame):
        self.currentlyVoting = True
        self.eligibleVoters = currentGame.livingPlayers.copy()
        for player in currentGame.deadPlayers:
            if player.role.id == 'Marco':
                self.eligibleVoters.append(player)
        self.accepted = []
        self.rejected = []
        self.abstained = []
        self.voted = []

    def voteExpo(self, currentGame, player, voteCase):
        self.voted.append(player)
        if voteCase == 'y':
            self.accepted.append(player)
        elif voteCase == 'n':
            self.rejected.append(player)
        elif voteCase == 'a':
            self.abstained.append(player)
        elif voteCase == 'Jean':
            self.accepted.append(player)
            player.role.disableAbility()
            self.jeanActivated = True
        elif voteCase == 'Samuel':
            player.role.disableAbility()
            if player.role.id == 'Samuel':
                self.samuelActivated = True
            else:
                self.warhammerActivated = 'Samuel'
            isWarriorInExpo = False
            for expeditioner in self.expeditionMembers:
                if expeditioner in currentGame.warriors:
                    isWarriorInExpo = True
                    break
            if self.pyxisTrial != None:
                if isWarriorInExpo:
                    self.rejected.append(player)
                else:
                    self.accepted.append(player)
            else:
                if isWarriorInExpo:
                    self.accepted.append(player)
                else:
                    self.rejected.append(player)
        elif voteCase == 'Zachary':
            self.rejected.append(player)
            player.role.disableAbility()
            if player.role.id == 'Zachary':
                self.zacharyActivated = True
            else:
                self.warhammerActivated = 'Zachary'
        elif voteCase == 'PieckAccept':
            self.rejected.append(player)
            player.role.disableAbility()
            self.pieckActivated = True
        elif voteCase == 'PieckReject':
            self.accepted.append(player)
            player.role.disableAbility()
            self.pieckActivated = True
        elif voteCase == 'Falco':
            self.falcoActivated = True
            player.role.disableAbility()
        elif voteCase == 'Magath':
            self.magathActivated = True
            player.role.disableAbility()
            self.accepted.append(player)
        elif type(voteCase) == dict and 'Yelena' in voteCase:
            self.abstained.append(player)
            player.role.disableAbility()
            self.yelenaStolen = voteCase['Yelena']
        if len(self.voted) == len(self.eligibleVoters):
            self.currentlyVoting = False

    def beginExpeditioning(self):
        self.currentlyExpeditioning = True
        self.expeditioned = []
        self.passedExpedition = []
        self.sabotagedExpedition = []
        self.resultsAvailable = False

    def actExpo(self, player, actCase):
        self.expeditioned.append(player)
        if actCase == 'Armin':
            self.passedExpedition.append(player)
            if player.role.id == 'Armin':
                self.arminActivated = True
            if player.role.id == 'Warhammer':
                self.warhammerActivated = 'Armin'
            player.role.disableAbility()
            self.usedExpoAbilities.append(player)
        elif actCase == 'LeviAttack':
            self.passedExpedition.append(player)
            if player.role.id == 'Levi':
                self.leviAttacked = True
            if player.role.id == 'Warhammer':
                self.warhammerActivated = 'LeviAttack'
            player.role.disableAbility()
            self.usedExpoAbilities.append(player)
        elif actCase == 'LeviDefend':
            self.passedExpedition.append(player)
            if player.role.id == 'Levi':
                self.leviDefended = True
            if player.role.id == 'Warhammer':
                self.warhammerActivated = 'LeviDefend'
            player.role.disableAbility()
            self.usedExpoAbilities.append(player)
        elif actCase == 'Daz':
            self.passedExpedition.append(player)
            if player.role.id == 'Daz':
                self.dazActivated = True
            else:
                self.warhammerActivated = 'Daz'
            player.role.disableAbility()
        elif actCase == 'Rico':
            self.passedExpedition.append(player)
            player.role.disableAbility()
            self.usedExpoAbilities.append(player)
        elif actCase == 'Bertholdt':
            self.sabotagedExpedition.append(player)
            self.bertholdtCloaked = True
        elif actCase == 'Ksaver':
            self.sabotagedExpedition.append(player)
            player.role.disableAbility()
            self.usedExpoAbilities.append(player)
            self.ksaverBlackout = True
        elif type(actCase) == dict and 'Mikasa' in actCase:
            self.passedExpedition.append(player)
            self.mikasaGuarded = actCase['Mikasa']
        elif type(actCase) == dict and 'Petra' in actCase:
            self.passedExpedition.append(player)
            if player.role.id == 'Petra':
                self.petraWatched = actCase['Petra']
            if player.role.id == 'Warhammer':
                self.warhammerActivated = {'Petra':actCase['Petra']}
            player.role.disableAbility()
            self.usedExpoAbilities.append(player)
        elif type(actCase) == dict and 'Frecklemir' in actCase:
            self.passedExpedition.append(player)
            if player.role.id == 'Frecklemir':
                self.frecklemirMauled = actCase['Frecklemir']
            if player.role.id == 'Warhammer':
                self.warhammerActivated = {'Frecklemir':actCase['Frecklemir']}
                player.role.disableAbility()
                self.usedExpoAbilities.append(player)
        elif type(actCase) == dict and 'Hange' in actCase:
            self.passedExpedition.append(player)
            self.hangeActivated = True
            player.role.disableAbility()
            self.usedExpoAbilities.append(player)
        elif actCase == 'Hannes':
            self.passedExpedition.append(player)
            if player.role.id == 'Hannes':
                self.hannesActivated = player
            if player.role.id == 'Warhammer':
                self.warhammerActivated = 'Hannes'
            player.role.disableAbility()
            self.usedExpoAbilities.append(player)
        elif actCase == 'Marco':
            self.passedExpedition.append(player)
            if player.role.id == 'Marco':
                self.marcoActivated = True
            if player.role.id == 'Warhammer':
                self.warhammerActivated = 'Marco'
        elif type(actCase) == dict and 'Willy' in actCase:
            self.sabotagedExpedition.append(player)
            self.willyBombed = actCase['Willy']
            player.role.disableAbility()
            self.usedExpoAbilities.append(player)
        elif type(actCase) == dict and 'Kenny' in actCase:
            self.passedExpedition.append(player)
            self.kennyMurdered = actCase['Kenny']
        elif actCase == 'y':
            self.passedExpedition.append(player)
        elif actCase == 'n':
            self.sabotagedExpedition.append(player)
        if player.role.id == 'Onyankopon' and self.playerFlown is None:
            self.playerFlown = False
        if len(self.expeditioned) == len(self.expeditionMembers):
            self.currentlyExpeditioning = False
            self.resultsAvailable = True

    def activateSasha(self):
        self.sashaActivated = True

    def activateGabi(self):
        self.gabiActivated = True

    def processFalco(self, Falco):
        if len(self.accepted) >= len(self.rejected):
            self.accepted.append(Falco)
        else:
            self.rejected.append(Falco)

    def processMagath(self, currentGame):
        for warrior in currentGame.livingWarriors:
            if warrior in self.rejected:
                self.rejected.remove(warrior)
            if warrior not in self.accepted:
                self.accepted.append(warrior)

    def processYelena(self, Yelena):
        if self.yelenaStolen not in self.abstained:
            self.abstained.remove(Yelena)
            if self.yelenaStolen in self.accepted:
                self.accepted.append(Yelena)
                self.accepted.remove(self.yelenaStolen)
                self.rejected.append(self.yelenaStolen)
            else:
                self.rejected.append(Yelena)
                self.rejected.remove(self.yelenaStolen)
                self.accepted.append(self.yelenaStolen)

    def ejectPlayer(self, Hannes):
        if Hannes in self.expeditioned:
            self.expeditioned.remove(Hannes)
        if Hannes in self.passedExpedition:
            self.passedExpedition.remove(Hannes)
        if Hannes in self.expeditionMembers:
            self.expeditionMembers.remove(Hannes)

    def flyIn(self, player):
        if player not in self.expeditionMembers:
            self.expeditionMembers.append(player)
            self.currentlyExpeditioning = True
            self.flownIn = True

    def fly(self, Onyankopon, player):
        self.playerFlown = player
        Onyankopon.role.disableAbility()

    def noFly(self):
        self.playerFlown = False

    def trialPlayer(self, Pyxis, player):
        if Pyxis.role.id == 'Pyxis':
            self.pyxisTrial = player
        if Pyxis.role.id == 'Warhammer':
            self.warhammerActivated = {'Pyxis':player}

    def deactivatePyxis(self):
        self.pyxisTrial = None
        self.warhammerActivated = None

    def prepareExpoForPyxis(self):
        self.displaySize = None
        self.size = 1
        self.expeditionMembers = [self.pyxisTrial]
        self.currentlyPicking = False


    def prepareExpoForFakePyxis(self):
        self.displaySize = None
        self.size = 1
        self.expeditionMembers = [self.warhammerActivated['Pyxis']]
        self.currentlyPicking = False

    
    def changeExpoSize(self, newSize):
        self.size = newSize
        self.displaySize = None

    def changeWarhammerAbility(self, ability):
        self.warhammerActivated = ability

    def activateKitz(self):
        self.kitzActivated = True


        