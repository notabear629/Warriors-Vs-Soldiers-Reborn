class Expedition:
    def __init__(self, commander, size, players):
        self.commander = commander
        self.size = size
        self.expeditionMembers = []
        self.currentlyPicking = True
        self.passed = False
        self.currentlyVoting = False
        self.eligibleVoters = []
        self.accepted = []
        self.rejected = []
        self.abstained = []

    def changeCommander(self, commander):
        self.commander = commander
        self.expeditionMembers = []
        self.currentlyPicking = True
        self.passed = False

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
        