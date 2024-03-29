class searchFunctions:
    async def roleIDToPlayer(currentGame, roleID):
        matchesFound = []
        for player in currentGame.players:
            if player.role.id == roleID:
                matchesFound.append(player)
        if matchesFound == []:
            return None
        elif len(matchesFound) == 1:
            return matchesFound[0]
        else:
            return matchesFound
        
    async def userToPlayer(currentGame, user):
        matchFound = None
        for player in currentGame.players:
            if player.user == user:
                matchFound = player
                break
        return matchFound
    
    async def roleIDToRoleFromLoadedRoles(loadedRoles, roleID):
        for role in loadedRoles:
            if role.id == roleID:
                return role
        return False
    
    async def stringToRole(loadedRoles, input):
        foundRoles = []
        for role in loadedRoles:
            if input.lower() in role.id.lower() or input.lower() in role.name.lower() or input.lower() in role.shortName.lower():
                foundRoles.append(role)
        if len(foundRoles) > 0:
            return foundRoles[0]