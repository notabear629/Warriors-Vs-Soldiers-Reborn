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