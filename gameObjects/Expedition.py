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
        self.mikasaGuarded = None
        self.reinerBlocked = None
        self.kennyMurdered = None
        self.petraWatched = None
        self.bertholdtCloaked = False
        self.annieMessage = None
        self.hangeActivated = False
        self.hannesActivated = None
        self.willyBombed = None
        self.yelenaStolen = None
        self.usedExpoAbilities = []
        self.filledUp = False

    def changeCommander(self, commander):
        self.commander = commander
        
    def resetExpo(self):
        self.expeditionMembers = []
        self.currentlyPicking = True
        self.passed = False
        self.jeanActivated = False
        self.zacharyActivated = False
        self.pieckActivated = False
        self.falcoActivated = False
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
        self.annieMessage = None
        self.hangeActivated = False
        self.hannesActivated = None
        self.yelenaStolen = None
        self.willyBombed = None
        self.filledUp = False

    def fillUp(self):
        self.filledUp = True
    
    def activateErwin(self, Erwin):
        self.erwinActivated = True
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

    def voteExpo(self, player, voteCase):
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
        elif voteCase == 'Zachary':
            self.rejected.append(player)
            player.role.disableAbility()
            self.zacharyActivated = True
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
            self.arminActivated = True
            player.role.disableAbility()
            self.usedExpoAbilities.append(player)
        elif actCase == 'LeviAttack':
            self.passedExpedition.append(player)
            self.leviAttacked = True
            player.role.disableAbility()
            self.usedExpoAbilities.append(player)
        elif actCase == 'LeviDefend':
            self.passedExpedition.append(player)
            self.leviDefended = True
            player.role.disableAbility()
            self.usedExpoAbilities.append(player)
        elif actCase == 'Daz':
            self.passedExpedition.append(player)
            self.dazActivated = True
            player.role.disableAbility()
        elif actCase == 'Bertholdt':
            self.sabotagedExpedition.append(player)
            self.bertholdtCloaked = True
        elif type(actCase) == dict and 'Mikasa' in actCase:
            self.passedExpedition.append(player)
            self.mikasaGuarded = actCase['Mikasa']
        elif type(actCase) == dict and 'Petra' in actCase:
            self.passedExpedition.append(player)
            self.petraWatched = actCase['Petra']
            player.role.disableAbility()
            self.usedExpoAbilities.append(player)
        elif type(actCase) == dict and 'Hange' in actCase:
            self.passedExpedition.append(player)
            self.hangeActivated = True
            player.role.disableAbility()
            self.usedExpoAbilities.append(player)
        elif actCase == 'Hannes':
            self.passedExpedition.append(player)
            self.hannesActivated = player
            player.role.disableAbility()
            self.usedExpoAbilities.append(player)
        elif type(actCase) == dict and 'Annie' in actCase:
            self.sabotagedExpedition.append(player)
            self.annieMessage = actCase['Annie']
            player.role.disableAbility()
            self.usedExpoAbilities.append(player)
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
        self.expeditioned.remove(Hannes)
        self.passedExpedition.remove(Hannes)
        self.expeditionMembers.remove(Hannes)



        