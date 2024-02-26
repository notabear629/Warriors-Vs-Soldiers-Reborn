class Stats:
    def __init__(self, role, defaultStats):
        for key, value in defaultStats.items():
            setattr(self, key, value)
        self.GamesPlayed = 1
        setattr(self, f'{role.team}Played', 1)
        setattr(self, f'{role.id}Played', 1)

    def processEndgame(self, player, currentGame):
        if player in currentGame.winners:
            self.GamesWon = 1
            setattr(self, f'{player.role.team}Won', 1)
            setattr(self, f'{player.role.id}Won', 1)
        if 'kidnap' in currentGame.winCondition:
            setattr(self, f'{player.role.team}Kidnaps', 1)
            setattr(self, f'{player.role.id}Kidnaps', 1)
            if player in currentGame.winners:
                setattr(self, f'{player.role.team}KidnapWins', 1)
                setattr(self, f'{player.role.id}KidnapWins', 1)
        setattr(self, f'{player.role.team}WallsBroken', currentGame.roundFails)
        setattr(self, f'{player.role.team}Passes', currentGame.roundWins)
        

    def processKill(self, killer, killed):
        solKillRoles = ['Levi', 'Sasha', 'Armin']
        solKillWinRoles = ['Sasha', 'Armin']
        totalKills = getattr(killer.stats, 'Kills')
        totalDeaths = getattr(killed.stats, 'Deaths')
        setattr(killer.stats, 'Kills', totalKills+1)
        setattr(killed.stats, 'Deaths', totalDeaths+1)
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

    def gagSkip(self):
        currentGags = getattr(self, 'PorcoCommanderSkips')
        setattr(self, 'PorcoCommanderSkips', currentGags + 1)

    @staticmethod
    async def processVoteStats(currentGame, voteResult, searchFunctions):
        expo = currentGame.currentExpo
        if expo.jeanActivated:
            Jean = await searchFunctions.roleIDToPlayer(currentGame, 'Jean')
            setattr(Jean.stats, 'JeanForces', 1)
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
        if expo.commander in currentGame.soldiers:
            commandCount = getattr(expo.commander.stats, 'ExposCommanded')
            setattr(expo.commander.stats, 'ExposCommanded', commandCount + 1)

    @staticmethod
    async def processResults(currentGame, result, searchFunctions):
        expo = currentGame.currentExpo
        if expo.dazActivated:
            Daz = await searchFunctions.roleIDToPlayer(currentGame, 'Daz')
            setattr(Daz.stats, 'DazChickens', 1)
            if result == 'n':
                setattr(Daz.stats, 'DazChickenWins', 1)
        else:
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
            if expo.annieMessage != None:
                Annie = await searchFunctions.roleIDToPlayer(currentGame, 'Annie')
                setattr(Annie.stats, 'AnnieScreams', 1)
            if expo.mikasaGuarded != None:
                Mikasa = await searchFunctions.roleIDToPlayer(currentGame, 'Mikasa')
                guardCount = getattr(Mikasa.stats, 'MikasaGuards')
                setattr(Mikasa.stats, 'MikasaGuards', guardCount + 1)
                if type(expo.mikasaGuarded) == dict:
                    saveCount = getattr(Mikasa.stats, 'MikasaSaved')
                    setattr(Mikasa.stats, 'MikasaSaved', saveCount + 1)
                    for key, value in expo.mikasaGuarded.items():
                        if key in currentGame.soldiers:
                            saveWins = getattr(Mikasa.stats, 'MikasaSaveWins')
                            setattr(Mikasa.stats, 'MikasaSaveWins', saveWins + 1)
            if expo.arminActivated:
                Armin = await searchFunctions.roleIDToPlayer(currentGame, 'Armin')
                setattr(Armin.stats, 'ArminNukes', 1)
            if expo.sashaActivated:
                Sasha = await searchFunctions.roleIDToPlayer(currentGame, 'Sasha')
                setattr(Sasha.stats, 'SashaFires', 1)
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
                if soldier in expo.accepted:
                    voteCount = getattr(soldier.stats, 'ExposVoted')
                    setattr(soldier.stats, 'ExposVoted', voteCount + 1)
                if soldier in expo.expeditionMembers:
                    expoCount = getattr(soldier.stats, 'SoldiersExpeditionsOn')
                    setattr(soldier.stats, 'SoldiersExpeditionsOn', expoCount + 1)
            for warrior in currentGame.warriors:
                if warrior in expo.expeditionMembers:
                        expoCount = getattr(warrior.stats, 'WarriorsExpeditionsOn')
                        setattr(warrior.stats, 'WarriorsExpeditionsOn', expoCount + 1)
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
                            setattr(soldier.stats, 'PassCommanders', passVotes + 1)
                        if expo.commander == soldier:
                            passCommands = getattr(soldier.stats, 'PassCommanders')
                            setattr(soldier.stats, 'PassCommanders', passCommands + 1)
            if result == 'n':
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
                            setattr(warrior.stats, 'BreakCommanders', breakVotes + 1)
                        if expo.commander == warrior:
                            breakCommands = getattr(warrior.stats, 'BreakCommanders')
                            setattr(warrior.stats, 'BreakCommanders', breakCommands + 1)
                        
    @staticmethod
    async def processMVP(currentGame):
        soldierMVPGrading = {'ArminKills' : -1, 'SashaKills' : -1, 'ArminKillWins' : 2, 'SashaKillWins': 2, 'JeanForces' : -1, 'JeanForceWins' : 2, 'DazChickenWins' : 1, 'LeviKills': 1, 'LeviDefendWins' : 1, 'MikasaSaved' : -1, 'MikasaSaveWins': 2, 'PassCommanders' : 2, 'AcceptedCommand' : -1, 'PassVotes' :2, 'ExposVoted' : -1, 'PassExpeditions' : 1}
        for soldier in currentGame.soldiers:
            for key, value in soldierMVPGrading.items():
                check = getattr(soldier.stats, key)
                if check != None:
                    score = check * value
                    soldier.addMVPPoints(score)
        warriorMVPGrading = {'PieckFlipAcceptWins' : 1, 'PieckFlipRejectWins' : 0.5, 'PorcoCommanderSkips' : 0.5, 'FalcoVoteWins' : 1, 'ReinerSaves' : 0.5, 'BertholdtCloaks' : -0.5, 'BertholdtDoubleCloaks' : 1.5, 'BreakCommanders' : 1, 'BreakVotes' : 1, 'BreakExpeditions' : 1}
        for warrior in currentGame.warriors:
            for key, value in warriorMVPGrading.items():
                check = getattr(warrior.stats, key)
                if check != None:
                    score = check * value
                    warrior.addMVPPoints(score)
        mvp = currentGame.winners[0]
        for winner in currentGame.winners:
            if winner.mvpPoints > mvp.mvpPoints:
                mvp = winner
        currentGame.setMVP(mvp)
        setattr(mvp.stats, 'MVPS', 1)
        setattr(mvp.stats, f'{winner.role.team}MVPS', 1)


            

            


