class Stats:
    def __init__(self, role):
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

    def processKill(self, killer, killed):
        solKillRoles = ['Levi', 'Sasha', 'Armin']
        solKillWinRoles = ['Sasha', 'Armin']
        if killer.role.id in solKillRoles:
            killAttribute = getattr(self, f'{killer.role.id}Kills')
            if killAttribute == None:
                setattr(self, f'{killer.role.id}Kills', 0)
                killAttribute = 0
            setattr(self, f'{killer.role.id}Kills', killAttribute+1)
            if killer.role.id in solKillWinRoles and killed.role.team == 'Warriors':
                winAttribute = getattr(self, f'{killer.role.id}KillWins')
                if winAttribute == None:
                    setattr(self, f'{killer.role.id}KillWins', 0)
                    winAttribute = 0
                setattr(self, f'{killer.role.id}Kills', killAttribute+1)
            


