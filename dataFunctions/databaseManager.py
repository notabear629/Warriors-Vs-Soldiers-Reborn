import pymongo
import bson
from bson import ObjectId, binary, BSON
import os
from dotenv import load_dotenv
import discord
from discord.ext import commands

class databaseManager:
    load_dotenv()

    DATABASE_NAME_ROOT = os.getenv('DATABASE_NAME_ROOT')
    DATABASE_NAME_GAME = os.getenv('DATABASE_NAME_GAME')
    host = "mongodb://localhost:27017/"
    client = pymongo.MongoClient(host)
    gameDatabase = client[DATABASE_NAME_ROOT][DATABASE_NAME_GAME]
    rootDatabase = client[DATABASE_NAME_ROOT]
    
    @staticmethod
    def addUser(userData):
        databaseManager.rootDatabase['users'].insert_one(userData)

    @staticmethod
    def searchForUser(user):
        returnedUser = databaseManager.rootDatabase['users'].find_one({"userID": user.id})
        return returnedUser
    
    @staticmethod
    def searchForUserByName(userName):
        foundUsers = databaseManager.rootDatabase['users'].find()
        for user in foundUsers:
            if userName.lower() in user['userName'].lower():
                return user
    
    @staticmethod
    def returnAllUsers():
        return databaseManager.rootDatabase['users'].find()
    
    @staticmethod
    def getGlobal():
        globalDB = databaseManager.gameDatabase.find_one({'userID' : "GLOBAL"})
        return globalDB
    
    @staticmethod
    def searchForWvsPlayer(user):
        returnedPlayer = databaseManager.gameDatabase.find_one({"userID":user.id})
        if returnedPlayer == None:
            returnedPlayer = databaseManager.gameDatabase.find_one({"altID":user.id})
        return returnedPlayer
    
    @staticmethod
    def getWvsPlayerByID(userID):
        returnedPlayer = databaseManager.gameDatabase.find_one({"userID":userID})
        if returnedPlayer == None:
            returnedPlayer = databaseManager.gameDatabase.find_one({"altID":userID})
        return returnedPlayer
    
    @staticmethod
    def addWvsPlayer(userInfo):
        databaseManager.gameDatabase.insert_one(userInfo)

    @staticmethod
    def updateWvsPlayer(userInfo):
        nullCheck = databaseManager.gameDatabase.find_one({"userID":userInfo['userID']})
        if nullCheck != None:
            databaseManager.gameDatabase.update_one({'userID' : userInfo['userID']}, {'$set' : userInfo})
        else:
            databaseManager.gameDatabase.update_one({'altID' : userInfo['altID']}, {'$set' : userInfo})

    @staticmethod
    def getSortedWvsPlayer(calc):
        return databaseManager.gameDatabase.find({"userID":{"$ne":"GLOBAL"}}).sort(f'calcs.{calc}', -1)
    
    @staticmethod
    def getWorstWvsPlayer(calc):
        return databaseManager.gameDatabase.find({"userID":{"$ne":"GLOBAL"}}).sort(f'calcs.{calc}')[0]
    
    @staticmethod
    def getSortedLegacy():
        return databaseManager.gameDatabase.find({"userID":{"$ne":"GLOBAL"}}).sort(f'points.LegacyPoints', -1)
    
    @staticmethod
    def getSortedPoints(stat):
        return databaseManager.gameDatabase.find({"userID":{"$ne":"GLOBAL"}}).sort(f'points.{stat}', -1)
    
    @staticmethod
    def getSortedWvsStat(stat):
        return databaseManager.gameDatabase.find({"userID":{"$ne":"GLOBAL"}}).sort(f'stats.{stat}', -1)

    @staticmethod
    def tallyStatsByID(userID, stats):
        player = databaseManager.getWvsPlayerByID(userID)
        globalDB = databaseManager.getGlobal()
        newDB = player.copy()
        newGlobalDB = globalDB.copy()
        for key, value in player['stats'].items():
            newDB['stats'][key] += stats[key]
            newGlobalDB['stats'][key] += stats[key]
        databaseManager.updateWvsPlayer(newDB)
        databaseManager.updateWvsPlayer(newGlobalDB)

    @staticmethod
    def updateRuleset(userID, rules):
        databaseManager.gameDatabase.update_one({'userID' : userID}, {'$set' : {'savedRulesets':rules}})

    
    @staticmethod
    def updateUserInformation(user, userData):
        databaseManager.rootDatabase['users'].update_one({'userID' : user.id}, {'$set' : userData})

