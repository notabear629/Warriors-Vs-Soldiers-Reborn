from gameObjects.Stats import Stats

class Player:
    def __init__(self, user, role):
        self.user = user
        self.role = role
        self.killed = {}
        self.killedBy = {}
        self.mvpPoints = 0

    def getKilledBy(self, killer, causeOfDeath):
        self.killedBy[killer] = causeOfDeath

    def killPlayer(self, killedPlayer, causeOfDeath):
        self.killed[killedPlayer] = causeOfDeath

    def addStats(self, role, defaultStats):
        self.stats = Stats(role, defaultStats)

    def addMVPPoints(self, points):
        self.mvpPoints += points