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
        self.pieckActivated = False
        self.arminActivated = False
        self.leviAttacked = False
        self.leviDefended = False
        self.sashaActivated = False
        self.erwinActivated = False
        self.dazActivated = False
        self.usedExpoAbilities = []

    def changeCommander(self, commander):
        self.commander = commander
        
    def resetExpo(self):
        self.expeditionMembers = []
        self.currentlyPicking = True
        self.passed = False
        self.jeanActivated = False
        self.pieckActivated = False
        self.erwinActivated = False
        self.dazActivated = False
    
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
        elif voteCase == 'PieckAccept':
            self.rejected.append(player)
            player.role.disableAbility()
            self.pieckActivated = True
        elif voteCase == 'PieckReject':
            self.accepted.append(player)
            player.role.disableAbility()
            self.pieckActivated = True
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
        elif actCase == 'y':
            self.passedExpedition.append(player)
        elif actCase == 'n':
            self.sabotagedExpedition.append(player)
        if len(self.expeditioned) == len(self.expeditionMembers):
            self.currentlyExpeditioning = False
            self.resultsAvailable = True

    def activateSasha(self):
        self.sashaActivated = True



        