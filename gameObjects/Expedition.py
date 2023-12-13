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
        self.voted = []

    def voteExpo(self, player, voteCase):
        self.voted.append(player)
        if voteCase == 'y':
            self.accepted.append(player)
        elif voteCase == 'n':
            self.rejected.append(player)
        elif voteCase == 'a':
            self.abstained.append(player)
        if len(self.voted) == len(self.eligibleVoters):
            self.currentlyVoting = False

        