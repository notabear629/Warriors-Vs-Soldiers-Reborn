class Lobby:
    def __init__(self):
        self.online = False

    def openLobby(self, host, currentRules):
        self.online = True
        self.host = host
        self.users = [host]
        self.currentRules = currentRules

    def turnOffline(self):
        self.online = False

    def addUser(self, user):
        self.users.append(user)

    def removeUser(self, user):
        self.users.remove(user)

    def clearUsers(self):
        self.users = [self.host]