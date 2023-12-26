import random

from embedBuilder import embedBuilder

class Game:
    def __init__(self, client):
        self.online = False
        self.client = client


    def start(self, lobby, players, currentRules, loadedRoles):
        self.online = True
        self.lobby = lobby
        self.players = players
        self.soldiers = []
        self.warriors = []
        self.wildcards = []
        self.deadPlayers = []
        self.livingPlayers = []
        self.livingSoldiers = []
        self.deadSoldiers = []
        self.livingWarriors = []
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
        self.currentRules = currentRules
        self.temporaryMessage = None
        self.basementReached = False
        self.wallsBroken = False
        self.exposOver = False
        self.winCondition = None
        self.winners = []
        self.currentlyKidnapping = False
        self.kidnappedPlayer = None
        self.loadedRoles = loadedRoles
        self.sashaTargeted = None

        for player in players:
            self.livingPlayers.append(player)
            if player.role.team == 'Soldiers':
                self.soldiers.append(player)
                self.livingSoldiers.append(player)
            elif player.role.team == 'Warriors':
                self.warriors.append(player)
                self.livingWarriors.append(player)
            elif player.role.team == 'Wildcards':
                self.wildcards.append(player)
    
    def turnOffline(self):
        self.online = False

    def setExpedition(self, currentExpo):
        if self.currentExpo != None:
            self.expeditionHistory.append(self.currentExpo)
            self.previousExpeditionCounts.append(self.currentExpo.size)
        self.currentExpo = currentExpo

    def nextCommander(self):
        oldCommander = self.commanderOrder.pop(0)
        self.commanderOrder.append(oldCommander)
        for player in self.deadPlayers:
            if player in self.commanderOrder:
                self.commanderOrder.remove(player)
        self.currentExpo.changeCommander(self.commanderOrder[0])

    def erwinCommander(self, Erwin):
        oldCommanderOrder = self.commanderOrder.copy()
        oldCommanderOrder.remove(Erwin)
        self.commanderOrder = [Erwin] + oldCommanderOrder
        self.currentExpo.changeCommander(Erwin)

    async def sendTemporaryMessage(self, currentTheme, home):
        embed = await embedBuilder.temporaryMessage(self, currentTheme)
        try:
            await self.temporaryMessage.delete()
        except:
            pass
        if embed != None:
            self.temporaryMessage = await home.send(embed=embed)

    def processResult(self, result):
        if result == 'y':
            self.passedRounds.append(self.currentRound)
            self.roundWins += 1
        elif result == 'n' or result == 'Armin':
            self.failedRounds.append(self.currentRound)
            self.roundFails += 1
        if self.roundWins == 3:
            self.basementReached = True
            self.exposOver = True
        elif self.roundFails == 3:
            self.wallsBroken = True
            self.exposOver = True
        self.resultsAvailable = False

    def killPlayer(self, killedPlayer, killerPlayer, causeOfDeath):
        if self.currentExpo.mikasaGuarded == killedPlayer:
            self.updateMikasaTarget(killedPlayer, causeOfDeath)
        elif killedPlayer.role.id == 'Reiner':
            self.updateReinerDefense(killedPlayer, causeOfDeath)
        else:
            if killedPlayer not in self.deadPlayers:
                if killedPlayer in self.livingPlayers:
                    self.livingPlayers.remove(killedPlayer)
                    self.deadPlayers.append(killedPlayer)
                if killedPlayer in self.livingSoldiers:
                    self.livingSoldiers.remove(killedPlayer)
                    self.deadSoldiers.append(killedPlayer)
                if killedPlayer in self.livingWarriors:
                    self.livingWarriors.remove(killedPlayer)
                    self.deadWarriors.append(killedPlayer)
                killedPlayer.getKilledBy(killerPlayer, causeOfDeath)
                killerPlayer.killPlayer(killedPlayer, causeOfDeath)

    def updateMikasaTarget(self, target, causeOfDeath):
        self.currentExpo.mikasaGuarded = {target: causeOfDeath}

    def updateReinerDefense(self,Reiner, causeOfDeath):
        self.currentExpo.reinerBlocked = {Reiner: causeOfDeath}

    def sashaTarget(self, Sasha, target):
        self.sashaTargeted = target
        
    def advanceRound(self):
        self.currentRound += 1

    def activateKidnap(self):
        self.currentlyKidnapping = True

    def kidnapPlayer(self, player):
        self.kidnappedPlayer = player
        self.currentlyKidnapping = False

    def setWinCondition(self, condition):
        self.winCondition = condition

    def processWinners(self):
        if self.winCondition == 'wallBreaks':
            self.winners = self.warriors.copy()
        elif self.winCondition == 'kidnapTimeout':
            self.winners = self.soldiers.copy()
        elif self.winCondition == 'kidnapSuccess':
            self.winners = self.warriors.copy()
        elif self.winCondition == 'kidnapFail':
            self.winners = self.soldiers.copy()

    def refundAbilities(self):
        for player in self.currentExpo.usedExpoAbilities:
            player.role.refundAbility()
        