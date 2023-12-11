import discord
from discord.ext import commands
import random


from gameObjects.Lobby import Lobby
from gameObjects.Player import Player
from gameObjects.Game import Game
from gameObjects.Role import Role

from dataFunctions.databaseManager import databaseManager

from embedBuilder import embedBuilder

class expoFunctions:
    async def getExpeditionSize(currentGame):
        if currentGame.currentRound == 1:
            expeditionNumber = 2
        elif currentGame.currentRound == 2:
            expeditionNumber = 3
        elif currentGame.currentRound > 2 and (len(currentGame.players) < 7):
            if (currentGame.currentRound == 3 and currentGame.players == 5):
                expeditionNumber = 2
            elif (currentGame.players == 5 and (currentGame.currentRound>3)) or (currentGame.players == 6 and currentGame.currentRound == 4):
                expeditionNumber = 3
            else:
                expeditionNumber = 4
        elif currentGame.currentRound > 2 and (len(currentGame.players) >= 7):
            dynamicOffset = currentGame.currentRoundWins
            if 1 in currentGame.passedRounds:
                dynamicOffset -= 1
            expeditionNumber = 3 + dynamicOffset
        if expeditionNumber > len(currentGame.livingSoldiers):
            expeditionNumber = len(currentGame.livingSoldiers)
        return expeditionNumber
    
    async def getExpeditionPrediction(currentGame):
        roundsToPredict = 5 - (currentGame.currentRound)
        if len(currentGame.players) == 5 or len(currentGame.players) == 6:
            roundNumbers = [2, 3, 2, 3, 3]
            if len(currentGame.players) == 6:
                roundNumbers = [2, 3, 4, 3, 4]
            while len(roundNumbers) > roundsToPredict:
                roundNumbers.pop(0)
            index = 0
            for round in roundNumbers:
                if roundNumbers[index] > len(currentGame.livingSoldiers):
                    roundNumbers[index] = len(currentGame.livingSoldiers)
                roundNumbers[index] = str(roundNumbers[index])
                index += 1
        else:
            sampleDict = {'low': 3, 'high': 5}
            roundNumbers = [2, 3, sampleDict, sampleDict, sampleDict]
            while len(roundNumbers) > roundsToPredict:
                roundNumbers.pop(0)
            index = 0
            for round in roundNumbers:
                roundPredicted = 5 - roundsToPredict + index + 1
                if type(round) == int:
                    if roundNumbers[index] > len(currentGame.livingSoldiers):
                        roundNumbers[index] = len(currentGame.livingSoldiers)
                    roundNumbers[index] = str(roundNumbers[index])
                else:
                    dynamicOffset = currentGame.currentRoundWins
                    if 1 in currentGame.passedRounds:
                        dynamicOffset -= 1
                    chancesRemaining = 3 - currentGame.currentRoundFails - 1
                    floor = currentGame.currentExpo.size + (roundPredicted - currentGame.currentRound) - chancesRemaining
                    if floor > len(currentGame.livingSoldiers):
                        floor = len(currentGame.livingSoldiers)
                    delaysRemaining = 3 - currentGame.currentRoundWins - 1
                    ceiling = currentGame.currentExpo.size + (roundPredicted - currentGame.currentRound) - delaysRemaining
                    if ceiling > len(currentGame.livingSoldiers):
                        ceiling = len(currentGame.livingSoldiers)
                    if floor == ceiling:
                        roundNumbers[index] = str(floor)
                    else:
                        roundNumbers[index] = f'({floor}-{ceiling})'
                index += 1

        return roundNumbers



