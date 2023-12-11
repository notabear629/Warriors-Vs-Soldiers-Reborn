import random

class Game:
    def __init__(self, lobby, players):
        self.lobby = lobby
        self.players = players
        self.soldiers = []
        self.warriors = []
        self.wildcards = []
        self.deadPlayers = []
        self.livingPlayers = players
        self.livingSoldiers = self.soldiers
        self.deadSoldiers = []
        self.livingWarriors = self.warriors
        self.deadWarriors = []
        self.currentRound = 1
        self.passedRounds = []
        self.failedRounds = []
        self.previousExpeditionCounts = []
        self.roundWins = 0
        self.roundFails = 0
        self.commanderOrder = random.sample(players, len(players))
        self.currentExpo = None
        self.expeditionHistory = []

        for player in players:
            if player.role.team == 'Soldiers':
                self.soldiers.append(player)
            elif player.role.team == 'Warriors':
                self.warriors.append(player)
            elif player.role.team == 'Wildcards':
                self.wildcards.append(player)

    def setExpedition(self, currentExpo):
        if self.currentExpo != None:
            self.expeditionHistory.append(self.currentExpo)
        self.currentExpo = currentExpo