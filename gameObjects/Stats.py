from dataFunctions.databaseManager import databaseManager

class Stats:
    def __init__(self, role, defaultStats):
        for key, value in defaultStats.items():
            setattr(self, key, value)
        self.GamesPlayed = 1
        setattr(self, f'{role.team}Played', 1)
        setattr(self, f'{role.id}Played', 1)

    def changeRole(self, role):
        setattr(self, f'{role.id}Played', 1)

    def processEndgame(self, player, currentGame):
        if player in currentGame.winners:
            self.GamesWon = 1
            setattr(self, f'{player.role.team}Won', 1)
            setattr(self, f'{player.role.id}Won', 1)
            if player.originalKeith:
                setattr(self, 'KeithWon', 1)
                if player.role.id == 'Keith':
                    setattr(self, 'KeithFinishedWon', 1)
        if 'kidnap' in currentGame.winCondition:
            setattr(self, f'{player.role.team}Kidnaps', 1)
            setattr(self, f'{player.role.id}Kidnaps', 1)
            if player.originalKeith:
                setattr(self, 'KeithKidnaps', 1)
                if player.role.id == 'Keith':
                    setattr(self, 'KeithFinishedKidnaps', 1)
            if player in currentGame.winners:
                setattr(self, f'{player.role.team}KidnapWins', 1)
                setattr(self, f'{player.role.id}KidnapWins', 1)
                if player.originalKeith:
                    setattr(self, 'KeithKidnapWins', 1)
                    if player.role.id == 'Keith':
                        setattr(self, 'KeithFinishedKidnapWins', 1)
        setattr(self, f'{player.role.team}WallsBroken', currentGame.roundFails)
        setattr(self, f'{player.role.team}Passes', currentGame.roundWins)
        if player.role.id == 'Keith':
            setattr(self, 'KeithFinishedPlayed', 1)
        if player.role.id == 'Warhammer' and player.role.abilityActive == False:
            setattr(self, 'WarhammerAbilities', 1)
        if player.role.id == 'Rico' and player.role.abilityActive == False:
            setattr(self, 'RicoTraps', 1)
            if currentGame.ricoFired:
                setattr(self, 'RicoTrapsFired', 1)
        if player.role.id == 'Marcel':
            setattr(self, 'MarcelGags', len(currentGame.deadSoldiers))
        

    def processKill(self, killer, killed):
        solKillRoles = ['Levi', 'Sasha', 'Armin', 'Petra', 'Pyxis', 'Rico']
        solKillWinRoles = ['Sasha', 'Armin', 'Pyxis']
        totalKills = getattr(killer.stats, 'Kills')
        totalDeaths = getattr(killed.stats, 'Deaths')
        if killer != killed:
            setattr(killer.stats, 'Kills', totalKills+1)
        setattr(killed.stats, 'Deaths', totalDeaths+1)
        if killer.role.id == 'Willy':
            if killed.role.id == 'Willy':
                setattr(killer.stats, 'WillyDeaths', 1)
            else:
                setattr(killer.stats, 'WillyKills', 1)
        if killed.role.id == 'Marco':
            setattr(killed.stats, 'MarcoDeaths', 1)
            if killer.role.id == 'Marco':
                setattr(killed.stats, 'MarcoSuicides', 1)
        if killer.role.id in solKillRoles:
            killAttribute = getattr(self, f'{killer.role.id}Kills')
            setattr(self, f'{killer.role.id}Kills', killAttribute+1)
            if killer.role.id in solKillWinRoles and killed.role.team == 'Warriors':
                winAttribute = getattr(self, f'{killer.role.id}KillWins')
                setattr(self, f'{killer.role.id}KillWins', winAttribute+1)

    def fireFlare(self):
        self.ErwinFlaresFired = 1

    def activateGag(self):
        self.PorcoGags = 1

    def smellTitans(self, num):
        self.MikeSmells += num

    def detectEren(self):
        self.FlochDetects += 1

    def hitchDiscover(self):
        self.HitchDiscovers += 1

    def nileSighting(self):
        self.NileSightings += 1

    def connieAlert(self):
        self.ConnieAlerts += 1

    def moblitAnalyze(self, success):
        self.MoblitAnalyzes += 1
        if success:
            self.MoblitAnalyzeWins += 1
    
    def friedaVow(self, currentGame, vowedPlayer):
        self.FriedaVows += 1
        if vowedPlayer in currentGame.warriors:
            self.FriedaWarriorVows += 1


    def gagSkip(self):
        currentGags = getattr(self, 'PorcoCommanderSkips')
        setattr(self, 'PorcoCommanderSkips', currentGags + 1)

    @staticmethod
    async def processVoteStats(currentGame, voteResult, searchFunctions):
        expo = currentGame.currentExpo
        if expo.yelenaStolen != None and expo.yelenaStolen not in expo.abstained:
            Yelena = await searchFunctions.roleIDToPlayer(currentGame, 'Yelena')
            setattr(Yelena.stats, 'YelenaSteals', 1)
        if expo.samuelActivated:
            Samuel = await searchFunctions.roleIDToPlayer(currentGame, 'Samuel')
            setattr(Samuel.stats, 'SamuelClowns', 1)
            if Samuel in expo.accepted:
                setattr(Samuel.stats, 'SamuelClownAccepts', 1)
        if expo.jeanActivated:
            Jean = await searchFunctions.roleIDToPlayer(currentGame, 'Jean')
            setattr(Jean.stats, 'JeanForces', 1)
        if expo.zacharyActivated:
            Zachary = await searchFunctions.roleIDToPlayer(currentGame, 'Zachary')
            setattr(Zachary.stats, 'ZacharyVetoes', 1)
            for player in currentGame.currentExpo.expeditionMembers:
                if player in currentGame.warriors:
                    setattr(Zachary.stats, 'ZacharyVetoWins', 1)
                    break
        if expo.pieckActivated:
            Pieck = await searchFunctions.roleIDToPlayer(currentGame, 'Pieck')
            if Pieck in expo.accepted:
                setattr(Pieck.stats, 'PieckFlipRejects', 1)
                if voteResult == False:
                    setattr(Pieck.stats, 'PieckFlipRejectWins', 1)
            else:
                setattr(Pieck.stats, 'PieckFlipAccepts', 1)
                if voteResult:
                    setattr(Pieck.stats, 'PieckFlipAcceptWins', 1)
        if expo.falcoActivated:
            Falco = await searchFunctions.roleIDToPlayer(currentGame, 'Falco')
            setattr(Falco.stats, 'FalcoUses', 1)
            if voteResult:
                setattr(Falco.stats, 'FalcoVoteWins', 1)
        if expo.magathActivated:
            Magath = await searchFunctions.roleIDToPlayer(currentGame, 'Magath')
            setattr(Magath.stats, 'MagathFinalOrders', 1)
        if expo.commander in currentGame.soldiers:
            commandCount = getattr(expo.commander.stats, 'ExposCommanded')
            setattr(expo.commander.stats, 'ExposCommanded', commandCount + 1)
        Marco = await searchFunctions.roleIDToPlayer(currentGame, 'Marco')
        if Marco != None and Marco in currentGame.deadPlayers:
            marcoRoundCount = getattr(Marco.stats, 'MarcoRounds')
            setattr(Marco.stats, 'MarcoRounds', marcoRoundCount+1)
            if Marco in expo.accepted or Marco in expo.rejected:
                marcoVoteCount = getattr(Marco.stats, 'MarcoVoted')
                setattr(Marco.stats, 'MarcoVoted', marcoVoteCount+1)

    @staticmethod
    async def processResults(currentGame, result, searchFunctions):
        expo = currentGame.currentExpo
        if expo.dazActivated:
            Daz = await searchFunctions.roleIDToPlayer(currentGame, 'Daz')
            setattr(Daz.stats, 'DazChickens', 1)
            if result == 'n':
                setattr(Daz.stats, 'DazChickenWins', 1)
        else:
            if expo.hannesActivated != None:
                Hannes = await searchFunctions.roleIDToPlayer(currentGame, 'Hannes')
                setattr(Hannes.stats, 'HannesEscapes', 1)
            if expo.petraWatched != None:
                Petra = await searchFunctions.roleIDToPlayer(currentGame, 'Petra')
                setattr(Petra.stats, 'PetraWatches', 1)
            if expo.hangeActivated:
                Hange = await searchFunctions.roleIDToPlayer(currentGame, 'Hange')
                setattr(Hange.stats, 'HangeWiretaps', 1)
            if expo.jeanActivated and result == 'y':
                Jean = await searchFunctions.roleIDToPlayer(currentGame, 'Jean')
                setattr(Jean.stats, 'JeanForceWins', 1)
            if expo.leviAttacked or expo.leviDefended:
                Levi = await searchFunctions.roleIDToPlayer(currentGame, 'Levi')
                if expo.leviAttacked:
                    setattr(Levi.stats, 'LeviAttacks', 1)
                if expo.leviDefended:
                    setattr(Levi.stats, 'LeviDefends', 1)
                    if len(expo.sabotagedExpedition) > 0 and result == 'y':
                        setattr(Levi.stats, 'LeviDefendWins', 1)
            if expo.arminActivated:
                Armin = await searchFunctions.roleIDToPlayer(currentGame, 'Armin')
                setattr(Armin.stats, 'ArminNukes', 1)
            if expo.sashaActivated:
                Sasha = await searchFunctions.roleIDToPlayer(currentGame, 'Sasha')
                setattr(Sasha.stats, 'SashaFires', 1)
            if expo.gabiActivated:
                Gabi = await searchFunctions.roleIDToPlayer(currentGame, 'Gabi')
                setattr(Gabi.stats, 'GabiFires', 1)
                if currentGame.woundedPlayer in currentGame.soldiers:
                    setattr(Gabi.stats, 'GabiFireWins', 1)
            if expo.reinerBlocked != None:
                Reiner = await searchFunctions.roleIDToPlayer(currentGame, 'Reiner')
                setattr(Reiner.stats, 'ReinerSaves', 1)
            if expo.bertholdtCloaked and result == 'n':
                Bertholdt = await searchFunctions.roleIDToPlayer(currentGame, 'Bertholdt')
                cloakCount = getattr(Bertholdt.stats, 'BertholdtCloaks')
                setattr(Bertholdt.stats, 'BertholdtCloaks', cloakCount + 1)
                if len(expo.sabotagedExpedition) > 1:
                    doubleCount = getattr(Bertholdt.stats, 'BertholdtDoubleCloaks')
                    setattr(Bertholdt.stats, 'BertholdtDoubleCloaks', doubleCount + 1)
            if expo.commander in currentGame.soldiers:
                    commandCount = getattr(expo.commander.stats, 'AcceptedCommand')
                    setattr(expo.commander.stats, 'AcceptedCommand', commandCount + 1)
            for soldier in currentGame.soldiers:
                if soldier in expo.accepted or soldier in expo.rejected:
                    voteCount = getattr(soldier.stats, 'ExposVoted')
                    setattr(soldier.stats, 'ExposVoted', voteCount + 1)
                if soldier in expo.expeditionMembers:
                    expoCount = getattr(soldier.stats, 'SoldiersExpeditionsOn')
                    setattr(soldier.stats, 'SoldiersExpeditionsOn', expoCount + 1)
            for warrior in currentGame.warriors:
                if warrior in expo.expeditionMembers:
                        expoCount = getattr(warrior.stats, 'WarriorsExpeditionsOn')
                        setattr(warrior.stats, 'WarriorsExpeditionsOn', expoCount + 1)
                        if currentGame.currentExpo.magathActivated:
                            Magath = await searchFunctions.roleIDToPlayer(currentGame, 'Magath')
                            setattr(Magath.stats, 'MagathFinalOrderWins', 1)
            if result == 'y':
                for soldier in currentGame.soldiers:
                    if soldier == expo.commander or soldier in expo.accepted or soldier in expo.expeditionMembers:
                        passesResponsible = getattr(soldier.stats, 'PassesResponsible')
                        setattr(soldier.stats, 'PassesResponsible', passesResponsible + 1)
                        if soldier in expo.expeditionMembers:
                            expoWins = getattr(soldier.stats, 'PassExpeditions')
                            setattr(soldier.stats, 'PassExpeditions', expoWins + 1)
                        else:
                            expoAssists = getattr(soldier.stats, 'PassAssists')
                            setattr(soldier.stats, 'PassAssists', expoAssists + 1)
                        if soldier in expo.accepted:
                            passVotes = getattr(soldier.stats, 'PassVotes')
                            setattr(soldier.stats, 'PassVotes', passVotes + 1)
                        if expo.commander == soldier:
                            passCommands = getattr(soldier.stats, 'PassCommanders')
                            setattr(soldier.stats, 'PassCommanders', passCommands + 1)
            if result == 'n' or result == 'Armin':
                for warrior in currentGame.warriors:
                    if warrior == expo.commander or warrior in expo.accepted or warrior in expo.expeditionMembers:
                        breaksResponsible = getattr(warrior.stats, 'BreaksResponsible')
                        setattr(warrior.stats, 'BreaksResponsible', breaksResponsible + 1)
                        if warrior in expo.expeditionMembers:
                            expoWins = getattr(warrior.stats, 'BreakExpeditions')
                            setattr(warrior.stats, 'BreakExpeditions', expoWins + 1)
                        else:
                            expoAssists = getattr(warrior.stats, 'BreakAssists')
                            setattr(warrior.stats, 'BreakAssists', expoAssists + 1)
                        if warrior in expo.accepted:
                            breakVotes = getattr(warrior.stats, 'BreakVotes')
                            setattr(warrior.stats, 'BreakVotes', breakVotes + 1)
                        if expo.commander == warrior:
                            breakCommands = getattr(warrior.stats, 'BreakCommanders')
                            setattr(warrior.stats, 'BreakCommanders', breakCommands + 1)
                        
    @staticmethod
    async def processMVP(currentGame):

        soldierMVPGrading = {'ArminKills': -1, 'ArminKillWins': 2, 'SashaKills': -1, 'SashaKillWins':2, 'PetraKillWins': 1, 'RicoKillWins':1, 'FriedaVows':1, 'PyxisKills':-1, 'PyxisKillWins':2, 'JeanForces':-1, 'JeanForceWins':2, 'ZacharyVetoes':-1, 'ZacharyVetoWins':2, 'ErwinFlaresFired':-0.5, 'DazChickens':-1, 'DazChickenWins':2, 'LeviAttacks':-0.5, 'LeviKills':1, 'LeviDefends':1, 'MikasaSaved':-1, 'MikasaSaveWins':2, 'HangeWiretapsSoldier':0.5, 'HangeWiretapsWarrior':0.5, 'MarcoSuicides':-1, 'HannesEscapes':-0.5, 'ArminNukes':-1,'PassCommanders' : 2, 'AcceptedCommand' : -1, 'PassVotes' :2, 'ExposVoted' : -1, 'PassExpeditions' : 1}
        for soldier in currentGame.soldiers:
            for key, value in soldierMVPGrading.items():
                check = getattr(soldier.stats, key)
                if check != None:
                    score = check * value
                    soldier.addMVPPoints(score)
        warriorMVPGrading = {'GabiFires': -0.5, 'GabiFireWins':1.5, 'AnnieScreams': 0.5, 'PieckFlipAcceptWins': 1, 'PorcoCommanderSkips': 0.5, 'FalcoVoteWins':1, 'ReinerSaves': 0.5, 'BertholdtCloaks': 0.5, 'BertholdtDoubleCloaks':0.5, 'WillyKills':0.5, 'YelenaSteals': 0.5, 'WarhammerAbilities':0.5, 'BreakCommanders' : 1, 'BreakVotes' : 1, 'BreakExpeditions' : 1}
        for warrior in currentGame.warriors:
            for key, value in warriorMVPGrading.items():
                check = getattr(warrior.stats, key)
                if check != None:
                    score = check * value
                    warrior.addMVPPoints(score)
        mvp = [currentGame.winners[0]]
        for winner in currentGame.winners:
            if winner.mvpPoints > mvp[0].mvpPoints:
                mvp = [winner]
            elif winner.mvpPoints == mvp[0].mvpPoints:
                mvp.append(winner)
        currentGame.setMVP(mvp)
        for elem in mvp:
            setattr(elem.stats, 'MVPS', 1)
            setattr(elem.stats, f'{elem.role.team}MVPS', 1)

    @staticmethod
    async def processELO(currentGame):
        soldierELO = 0
        warriorELO = 0
        totalELO = 0
        for player in currentGame.players:
            db = databaseManager.searchForWvsPlayer(player.user)
            totalELO += db['calcs']['ELO']
            if player in currentGame.soldiers:
                soldierELO += db['calcs']['ELO']
            else:
                warriorELO += db['calcs']['ELO']
        if totalELO == 0:
            totalELO = 1
        for player in currentGame.players:
            db = databaseManager.searchForWvsPlayer(player.user)
            if player in currentGame.soldiers:
                eloOffset = (1-(soldierELO/totalELO)) * 50
            else:
                eloOffset = (1-(warriorELO/totalELO)) * 50
            if player not in currentGame.winners:
                eloOffset = eloOffset * -1
            db['calcs']['ELO'] += eloOffset
            if db['calcs']['ELO'] < 0:
                db['calcs']['ELO'] = 0
            if db['calcs']['ELO'] > 1000:
                db['calcs']['ELO'] = 1000
            db['calcs']['ELO'] = int(db['calcs']['ELO'])
            databaseManager.updateWvsPlayer(db)
    
    def processWiretap(self, currentGame):
        if currentGame.hangeWiretapped in currentGame.soldiers:
            setattr(self, 'HangeWiretapsSoldier', 1)
        else:
            setattr(self, 'HangeWiretapsWarrior', 1)

    def processWire(self):
        coltWires = getattr(self, 'ColtWires')
        setattr(self, 'ColtWires', coltWires+1)

    def processBodyID(self, currentGame):
        setattr(self, 'MarloweIdentified', len(currentGame.deadPlayers))

    def startTrial(self):
        setattr(self, 'PyxisTrials', 1)

    def trialWin(self):
        setattr(self, 'PyxisTrialWins', 1)

    def mikasaSave(self):
        setattr(self, 'MikasaSaved', 1)

    def mikasaSoldierSave(self):
        setattr(self, 'MikasaSaveWins', 1)

    def reinerSave(self):
        reinerSaves = getattr(self, 'ReinerSaves')
        setattr(self, 'ReinerSaves', reinerSaves+1)

    def guardPlayer(self):
        mikasaGuards = getattr(self, 'MikasaGuards')
        setattr(self, 'MikasaGuards', mikasaGuards+1)

    def annieScream(self):
        setattr(self, 'AnnieScreams', 1)


            

            


