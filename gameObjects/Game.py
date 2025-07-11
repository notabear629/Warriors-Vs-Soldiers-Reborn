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


    def start(self, lobby, players, currentRules, loadedRoles, gagRole, loadedBadges, currentTheme):
        self.currentTheme = currentTheme
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
        self.ymirGuiding = None
        self.ymirRevival = None
        self.blessedPlayer = None
        self.woundedPlayer = None
        self.healedPlayer = None
        self.summonedRole = None
        self.niccoloDecoy = None
        self.hangeWiretapped = None
        self.playersOnExpos = []
        self.mikasaGuarded = None
        self.annieRounds = []
        self.warhammerAbility = None
        self.moblitPlayer = None
        self.moblitRole = None
        self.friedaVowedPlayer = None
        self.ricoTargeted = None
        self.ricoFired = False
        self.ricoTrapped = False
        self.demotedPlayer = None
        self.greenFired = False
        self.redFired = False
        self.blackFired = False
        self.sevenBalance = False
        self.blackoutRound = None
        self.kitzTarget = None
        self.kitzRound = None

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

        if currentRules.playerCountBalance:
            if len(self.warriors) + 1 == len(self.soldiers) and len(self.players) >= 7:
                self.sevenBalance = True

    
    def turnOffline(self):
        self.online = False

    def turnOnline(self):
        self.online = True

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
        if Erwin in oldCommanderOrder:
            oldCommanderOrder.remove(Erwin)
        self.commanderOrder = [Erwin] + oldCommanderOrder
        self.currentExpo.changeCommander(Erwin)

    def pyxisOrderFix(self):
        oldCommanderOrder = self.commanderOrder.copy()
        lastCommander = oldCommanderOrder[len(oldCommanderOrder)-1]
        oldCommanderOrder.remove(lastCommander)
        self.commanderOrder = [lastCommander] + oldCommanderOrder

    def friedaVow(self, vowedPlayer):
        self.friedaVowedPlayer = vowedPlayer

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

    async def killPlayer(self, killedPlayer, killerPlayer, causeOfDeath):
        if self.mikasaGuarded == killedPlayer and (killedPlayer.role.id != 'Marco' or self.currentExpo.marcoActivated == False):
            self.updateMikasaTarget(killedPlayer, causeOfDeath)
            Mikasa = await searchFunctions.roleIDToPlayer(self, 'Mikasa')
            if self.currentRules.casual == False:
                Mikasa.stats.mikasaSave()
                if killedPlayer in self.soldiers:
                    Mikasa.stats.mikasaSoldierSave()
        elif killedPlayer.role.id == 'Reiner':
            self.updateReinerDefense(killedPlayer, causeOfDeath)
            self.exposedReiner = killedPlayer
            Reiner = await searchFunctions.roleIDToPlayer(self, 'Reiner')
            if self.currentRules.casual == False:
                Reiner.stats.reinerSave()
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
        self.mikasaGuarded = {target: causeOfDeath}

    def guardPlayer(self, guard):
        self.mikasaGuarded = guard

    def executeAnka(self, Anka, player):
        if player in self.commanderOrder:
            self.commanderOrder.remove(player)
        Anka.role.disableAbility()
        if Anka.role.id == 'Anka':
            self.demotedPlayer = player
        else:
            self.warhammerAbility = {'Anka':player}

    def fireColor(self, color):
        if color.lower() == 'green':
            self.greenFired = True
        elif color.lower() == 'red':
            self.redFired = True
        elif color.lower() == 'black':
            self.blackFired = True

    def updateReinerDefense(self,Reiner, causeOfDeath):
        self.currentExpo.reinerBlocked = {Reiner: causeOfDeath}

    def sashaTarget(self, Sasha, target):
        if Sasha.role.id == 'Sasha':
            self.sashaTargeted = target
        if Sasha.role.id == 'Warhammer':
            self.warhammerAbility = {'Sasha':target}

    def ricoTarget(self, Rico, target):
        if Rico.role.id == 'Rico':
            self.ricoTargeted = target
        if Rico.role.id == 'Warhammer':
            self.warhammerAbility = {'Rico':target}

    def ricoFire(self):
        self.ricoFired = True

    def ricoTrap(self):
        self.ricoTrapped = True

    def setMoblitPlayer(self, target):
        self.moblitPlayer = target

    def setMoblitRole(self, role):
        self.moblitRole = role

    def gabiFire(self, Gabi, target):
        self.gabiTargeted = target

    def porcoGag(self, gaggedPlayer):
        self.porcoGagged = gaggedPlayer

    def wiretapPlayer(self, wiretappedPlayer):
        self.hangeWiretapped = wiretappedPlayer

    def removeGag(self):
        self.porcoGagged = None

    def setBlackoutRound(self):
        self.blackoutRound = self.currentRound + 1
        
    def advanceRound(self):
        self.currentRound += 1
        self.friedaVowedPlayer = None

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

    def updateExpoPlayers(self):
        for player in self.currentExpo.expeditionMembers:
            if player not in self.playersOnExpos:
                self.playersOnExpos.append(player)


    def clearWarhammmerAbility(self):
        self.warhammerAbility = None

    def annieScream(self):
        self.annieRounds.append(self.currentRound)

    def setKitz(self, player):
        self.kitzTarget = player
        if player == None:
            self.kitzRound = None
        else:
            self.kitzRound = self.currentRound
        self.currentExpo.activateKitz()

                    
        