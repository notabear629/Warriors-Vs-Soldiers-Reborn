import pymongo
import bson
from bson import ObjectId, binary, BSON
import os
from dotenv import load_dotenv
import discord
from discord.ext import commands

class databaseManager:
    load_dotenv()

    DATABASE_NAME = os.getenv('DATABASE_NAME')
    host = "mongodb://localhost:27017/"
    client = pymongo.MongoClient(host)
    database = client[DATABASE_NAME]
    
    @staticmethod
    def addUser(userData):
        databaseManager.database['users'].insert_one(userData)

    @staticmethod
    def searchForUser(user):
        returnedUser = databaseManager.database['users'].find_one({"userID": user.id})
        return returnedUser
    
    @staticmethod
    def updateUserInformation(user, userData):
        databaseManager.database['users'].update_one({'userID' : user.id}, {'$set' : userData})

