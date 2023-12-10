class Game:
    def __init__(self, lobby, players):
        self.lobby = lobby
        self.players = players
        self.soldiers = []
        self.warriors = []
        self.wildcards = []
        self.dead = []
        self.livingPlayers = players

        for player in players:
            if player.role.team == 'Soldiers':
                self.soldiers.append(player)
            elif player.role.team == 'Warriors':
                self.warriors.append(player)
            elif player.role.team == 'Wildcards':
                self.wildcards.append(player)