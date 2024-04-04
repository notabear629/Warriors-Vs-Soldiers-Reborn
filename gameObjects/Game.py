import random

from embedBuilder import embedBuilder

from gameFunctions.searchFunctions import searchFunctions

from gameObjects.Player import Player

class Game:
    def __init__(self, client, homeServer, prefix, userCategory, home):
        self.online = False
        self.client = client
        self.homeServer = homeServer
        self.prefix = prefix
        self.userCategory = userCategory
        self.home = home


    def start(self, lobby, players, currentRules, loadedRoles, gagRole, loadedBadges):
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
        self.livingWildcards = []
        self.deadWildcards = []
        self.currentRound = 1
        self.passedRounds = []
        self.failedRounds = []
        self.previousExpeditionCounts = []
        self.roundWins = 0
        self.roundFails = 0
        self.commanderOrder = random.sample(players, len(players))
        self.currentExpo = None
        self.expoProjections = []
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
        self.multikidnapRecord = {}
        self.loadedRoles = loadedRoles
        self.sashaTargeted = None
        self.gabiTargeted = None
        self.exposedReiner = None
        self.porcoGagged = None
        self.gagRole = gagRole
        self.rumblingActivated = False
        self.yeagerists = []
        self.deadYeagerists = []
        self.livingYeagerists = []
        self.alliance = []
        self.deadAlliance = []
        self.livingAlliance = []
        self.rumblingFighters = []
        self.yeageristFighters = []
        self.allianceFighters = []
        self.yeageristBench = []
        self.allianceBench = []
        self.attackedPlayer = None
        self.fightingYeagerist = None
        self.fightingAllianceMember = None
        self.dominantYeagerist = None
        self.allianceDomination = True
        self.MVP = None
        self.badges = loadedBadges
        self.kennyDisplayedKills = []
        self.frecklemirTeam = None
        self.ymirGuiding = None
        self.ymirRevival = None
        self.blessedPlayer = None
        self.woundedPlayer = None
        self.healedPlayer = None
        self.summonedRole = None
        self.niccoloDecoy = None
        self.hangeWiretapped = None
        

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
                self.livingWildcards.append(player)

        for player in players:
            if player.role.id == 'Ymir':
                self.commanderOrder.remove(player)
                ymirChoices = self.commanderOrder.copy()
                self.ymirGuiding = random.choice(ymirChoices)
            if player.role.id == 'Niccolo':
                self.niccoloDecoy = random.choice(self.soldiers)

    
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
            self.exposedReiner = killedPlayer
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
                if killedPlayer in self.livingWildcards:
                    self.livingWildcards.remove(killedPlayer)
                    self.deadWildcards.append(killedPlayer)
                killedPlayer.getKilledBy(killerPlayer, causeOfDeath)
                killerPlayer.killPlayer(killedPlayer, causeOfDeath)
                killerPlayer.stats.processKill(killerPlayer, killedPlayer)
                

    def updateMikasaTarget(self, target, causeOfDeath):
        self.currentExpo.mikasaGuarded = {target: causeOfDeath}

    def updateReinerDefense(self,Reiner, causeOfDeath):
        self.currentExpo.reinerBlocked = {Reiner: causeOfDeath}

    def sashaTarget(self, Sasha, target):
        self.sashaTargeted = target

    def gabiFire(self, Gabi, target):
        self.gabiTargeted = target

    def porcoGag(self, gaggedPlayer):
        self.porcoGagged = gaggedPlayer

    def wiretapPlayer(self, wiretappedPlayer):
        self.hangeWiretapped = wiretappedPlayer

    def removeGag(self):
        self.porcoGagged = None
        
    def advanceRound(self):
        self.currentRound += 1

    def activateKidnap(self):
        self.currentlyKidnapping = True

    def kidnapPlayer(self, player):
        self.kidnappedPlayer = player
        self.currentlyKidnapping = False

    def multikidnapPlayer(self, warrior, player):
        self.multikidnapRecord[warrior] = player
        if len(self.multikidnapRecord) == len(self.warriors):
            self.currentlyKidnapping = False


    def setWinCondition(self, condition):
        self.winCondition = condition

    async def processWinners(self):
        if self.winCondition == 'wallBreaks':
            self.winners = self.warriors.copy()
        elif self.winCondition == 'kidnapTimeout':
            self.winners = self.soldiers.copy()
        elif self.winCondition == 'kidnapSuccess':
            self.winners = self.warriors.copy()
        elif self.winCondition == 'kidnapFail':
            self.winners = self.soldiers.copy()
        elif self.winCondition == 'noCoordinateWin':
            self.winners = self.soldiers.copy()
        elif self.winCondition == 'multikidnapSuccess' or self.winCondition == 'multikidnapFail':
            if self.winCondition == 'multikidnapFail':
                self.winners = self.soldiers.copy()
            for warrior, target in self.multikidnapRecord.items():
                if target.role.id == 'Eren':
                    self.winners.append(warrior)
        elif self.winCondition == 'Yeagerists':
            self.winners = self.yeagerists.copy()
        elif self.winCondition == 'Alliance':
            self.winners = self.alliance.copy()
        Kenny = await searchFunctions.roleIDToPlayer(self, 'Kenny')
        if Kenny != None:
            kennyCount = 0
            for killedPlayer, causeOfDeath in Kenny.killed.items():
                if killedPlayer != Kenny:
                    kennyCount += 1
            if kennyCount >= 2:
                self.winners.append(Kenny)
        Ymir = await searchFunctions.roleIDToPlayer(self, 'Ymir')
        if Ymir != None:
            if self.ymirGuiding in self.winners:
                self.winners.append(Ymir)

    def setMVP(self, MVP):
        self.MVP = MVP

    def refundAbilities(self):
        for player in self.currentExpo.usedExpoAbilities:
            player.role.refundAbility()

    def skipExpos(self):
        self.exposOver = True
        if self.currentExpo != None:
            self.currentExpo.resultsAvailable = False
            self.currentExpo.currentlyPicking = False
            self.currentExpo.currentlyVoting = False
            self.currentExpo.currentlyExpeditioning = False

    def displayKennyKill(self, killedPlayer):
        self.kennyDisplayedKills.append(killedPlayer)

    def activateRumbling(self):
        self.exposOver = True
        self.rumblingActivated = True
        yeageristCandidates = []
        allianceCandidates = []
        for player in self.players:
            if player.role.rumblingTeam.startswith('yeagerist'):
                yeageristCandidates.append(player)
            else:
                allianceCandidates.append(player)
            if player.role.rumblingTeam.endswith('Fighter'):
                self.rumblingFighters.append(player)

        self.alliance = random.sample(allianceCandidates, len(allianceCandidates))
        yeageristCandidates = random.sample(yeageristCandidates, len(yeageristCandidates))
        supportingCast = []
        zeke = []
        eren = []
        for yeagerist in yeageristCandidates:
            if yeagerist.role.id == 'Eren':
                eren = [yeagerist]
            elif yeagerist.role.id == 'Zeke':
                zeke = [yeagerist]
            else:
                supportingCast.append(yeagerist)
        returnedYeagerists = supportingCast + zeke + eren
        self.yeagerists = returnedYeagerists
        for yeagerist in self.yeagerists:
            if yeagerist.role.rumblingTeam.endswith('Fighter'):
                self.yeageristFighters.append(yeagerist)
            else:
                self.yeageristBench.append(yeagerist)
            if yeagerist in self.livingPlayers:
                self.livingYeagerists.append(yeagerist)
            else:
                self.deadYeagerists.append(yeagerist)
        for allianceMember in self.alliance:
            if allianceMember.role.rumblingTeam.endswith('Fighter'):
                self.allianceFighters.append(allianceMember)
            else:
                self.allianceBench.append(allianceMember)
            if allianceMember in self.livingPlayers:
                self.livingAlliance.append(allianceMember)
            else:
                self.deadAlliance.append(allianceMember)

    def setExpoProjections(self, projections):
        self.expoProjections = projections

    def rumblingKill(self, player, killer):
        if player in self.livingPlayers:
            self.livingPlayers.remove(player)
            self.deadPlayers.append(player)
        if player in self.livingSoldiers:
            self.livingSoldiers.remove(player)
            self.deadSoldiers.append(player)
        if player in self.livingWarriors:
            self.livingWarriors.remove(player)
            self.deadWarriors.append(player)
        if player in self.livingAlliance:
            self.livingAlliance.remove(player)
            self.deadAlliance.append(player)
        if player in self.livingYeagerists:
            self.livingYeagerists.remove(player)
            self.deadYeagerists.append(player)
        player.getKilledBy(killer, 'rumblingFight')
        killer.killPlayer(player, 'rumblingFight')
        if killer in self.yeagerists and self.dominantYeagerist == None:
            self.dominantYeagerist = killer
        if self.dominantYeagerist == player:
            self.dominantYeagerist = False
        if player in self.alliance:
            self.allianceDomination = False

    def setRumblingFight(self, yeagerist, allianceMember):
        self.attackedPlayer = None
        self.fightingYeagerist = yeagerist
        self.fightingAllianceMember = allianceMember

    def resetRumblingFight(self):
        self.attackedPlayer = None
        self.fightingYeagerist = None
        self.fightingAllianceMember = None

    def attackPlayer(self, player):
        self.attackedPlayer = player

    def setFrecklemirTeam(self, team):
        self.frecklemirTeam = team

    async def applyFrecklemirTeam(self):
        Frecklemir = await searchFunctions.roleIDToPlayer(self, 'Frecklemir')
        if Frecklemir != None:
            if self.frecklemirTeam == 'Soldiers':
                if Frecklemir in self.wildcards:
                    self.wildcards.remove(Frecklemir)
                    self.soldiers.append(Frecklemir)
                if Frecklemir in self.deadWildcards:
                    self.deadWildcards.remove(Frecklemir)
                    self.deadSoldiers.append(Frecklemir)
                if Frecklemir in self.livingWildcards:
                    self.livingWildcards.remove(Frecklemir)
                    self.livingSoldiers.append(Frecklemir)
            elif self.frecklemirTeam == 'Warriors':
                if Frecklemir in self.wildcards:
                    self.wildcards.remove(Frecklemir)
                    self.warriors.append(Frecklemir)
                if Frecklemir in self.deadWildcards:
                    self.deadWildcards.remove(Frecklemir)
                    self.deadWarriors.append(Frecklemir)
                if Frecklemir in self.livingWildcards:
                    self.livingWildcards.remove(Frecklemir)
                    self.livingWarriors.append(Frecklemir)
    
    def eatPlayer(self, PureTitan, eatenPlayer, currentTheme, client):
        pureRole = PureTitan.role.copy(currentTheme, client)
        eatenRole = eatenPlayer.role.copy(currentTheme, client)

        if PureTitan in self.wildcards:
            self.wildcards.remove(PureTitan)
            if eatenPlayer in self.soldiers:
                self.soldiers.append(PureTitan)
                if PureTitan in self.livingWildcards:
                    self.livingWildcards.remove(PureTitan)
                    self.livingSoldiers.append(PureTitan)
                if PureTitan in self.deadWildcards:
                    self.deadWildcards.remove(PureTitan)
                    self.deadSoldiers.append(PureTitan)
            elif eatenPlayer in self.warriors:
                self.warriors.append(PureTitan)
                if PureTitan in self.livingWildcards:
                    self.livingWildcards.remove(PureTitan)
                    self.livingWarriors.append(PureTitan)
                if PureTitan in self.deadWildcards:
                    self.deadWildcards.remove(PureTitan)
                    self.deadWarriors.append(PureTitan)

        self.wildcards.append(eatenPlayer)
        if eatenPlayer in self.warriors:
            self.warriors.remove(eatenPlayer)
        if eatenPlayer in self.soldiers:
            self.soldiers.remove(eatenPlayer)
        if eatenPlayer in self.livingSoldiers:
            self.livingSoldiers.remove(eatenPlayer)
            self.livingWildcards.append(eatenPlayer)
        if eatenPlayer in self.deadSoldiers:
            self.deadSoldiers.remove(eatenPlayer)
            self.deadWildcards.append(eatenPlayer)
        if eatenPlayer in self.livingWarriors:
            self.livingWarriors.remove(eatenPlayer)
            self.livingWildcards.append(eatenPlayer)
        if eatenPlayer in self.deadWarriors:
            self.deadWarriors.remove(eatenPlayer)
            self.deadWildcards.append(eatenPlayer)

        PureTitan.changeRole(eatenRole)
        eatenPlayer.changeRole(pureRole)

    def ymirRevive(self, player):
        self.ymirRevival = player

    def revivePlayer(self, player):
        if player in self.deadPlayers:
            self.deadPlayers.remove(player)
            self.livingPlayers.append(player)
        if player in self.deadWarriors:
            self.deadWarriors.remove(player)
            self.livingWarriors.append(player)
        if player in self.deadSoldiers:
            self.deadSoldiers.remove(player)
            self.livingSoldiers.append(player)
        if player in self.deadWildcards:
            self.deadWildcards.remove(player)
            self.livingWildcards.append(player)
        if player not in self.commanderOrder:
            self.commanderOrder.append(player)
        self.ymirRevival = {player:True}

    def ymirBless(self, player):
        self.blessedPlayer = player

    def removeBlessing(self):
        self.blessedPlayer = None

    def woundPlayer(self, player):
        self.woundedPlayer = player
        self.healedPlayer = player
        self.gabiTargeted = None
    
    def healPlayers(self):
        if self.woundedPlayer != None:
            self.woundedPlayer = None
            return True
        return False
    
    def keithSummon(self, roleID):
        self.summonedRole = roleID

                    
        