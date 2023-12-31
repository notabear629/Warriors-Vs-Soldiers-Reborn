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
    def updateUserInformation(user, userData):
        databaseManager.rootDatabase['users'].update_one({'userID' : user.id}, {'$set' : userData})

