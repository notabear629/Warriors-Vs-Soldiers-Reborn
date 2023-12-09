class Lobby:
    def __init__(self, host):
        self.host = host
        self.users = [host]

    def addUser(self, user):
        self.users.append(user)

    def removeUser(self, user):
        self.users.remove(user)

    def clearUsers(self):
        self.users = [self.host]