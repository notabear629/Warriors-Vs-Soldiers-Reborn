import discord
from discord.ext import commands
from discord import ui
from discord.ui import *
from discord.utils import *

from dataFunctions.databaseManager import databaseManager

from gameObjects.Role import Role

class statBuilder:

    async def getPercentage(db, input1, input2):
        try:
            percentage = round(db[input1]/db[input2]*100, 1)
        except:
            percentage = 0.0
        return percentage
    
    async def getAltPercentage(db, input1, input2):
        try:
            percentage = round(input1/db[input2]*100, 1)
        except:
            percentage = 0.0
        return percentage
    
    async def getDivider(db, input1, input2):
        try:
            per = round(db[input1]/db[input2], 1)
        except:
            per = 0.0
        return per

    async def profileEmbed(currentTheme, user, loadedRoles, embedType):
        if user == 'GLOBAL':
            rootDB = databaseManager.getGlobal()
            thumbnail = currentTheme.globalThumbnail
            name = 'Global'
        else:
            rootDB = databaseManager.searchForWvsPlayer(user)
            thumbnail = user.avatar.url
            name = user.name
        globalDB = databaseManager.getGlobal()
        if embedType == 'Main':
            return await statBuilder.mainProfileEmbed(currentTheme, user, name, thumbnail, rootDB, globalDB)
        elif embedType == 'Soldier Overview':
            return await statBuilder.soldierOverviewEmbed(currentTheme, user, name,  thumbnail, rootDB, globalDB)
        elif embedType == 'Warrior Overview':
            return await statBuilder.warriorOverviewEmbed(currentTheme, user, name, thumbnail, rootDB, globalDB)
        elif embedType == 'Soldier Roles':
            return await statBuilder.soldierRolesEmbed(currentTheme, user, name, thumbnail, rootDB, globalDB, loadedRoles)
        elif embedType == 'Warrior Roles':
            return await statBuilder.warriorRolesEmbed(currentTheme, user, name, thumbnail, rootDB, globalDB, loadedRoles)
        elif type(embedType) == dict:
            if 'Soldier Role' in embedType:
                return await statBuilder.soldierSpecificRoleEmbed(currentTheme, user, name, thumbnail, rootDB, globalDB, loadedRoles, embedType['Soldier Role'])
            elif 'Warrior Role' in embedType:
                return await statBuilder.warriorSpecificRoleEmbed(currentTheme, user, name, thumbnail, rootDB, globalDB, loadedRoles, embedType['Warrior Role'])
    
    async def mainProfileEmbed(currentTheme, user, name, thumbnail, rootDB, rootGlobalDB, role=None):
        db = rootDB['stats']
        globalDB = rootGlobalDB['stats']
        if user == 'GLOBAL':
            title = 'Global Stats'
            description = None
        else:
            title = f'{user.name}\'s Profile'
            description = 'Legacy Points: **0**'
        returnedEmbed = discord.Embed(title = title, description = description, color = currentTheme.helpEmbedColor)
        if user != 'GLOBAL':
            returnedEmbed.add_field(name = 'Rank', value = 'not implemented', inline= True)
            if len(rootDB['titles']) > 0:
                returnedEmbed.add_field(name = 'Titles', value = 'not implemented', inline= True)
        returnedEmbed.add_field(name = 'Games Played', value = db['GamesPlayed'], inline= True)
        returnedEmbed.add_field(name = 'Games Won', value = f'{db['GamesWon']} ({await statBuilder.getPercentage(db, 'GamesWon', 'GamesPlayed')}%)', inline=True)
        if user != 'GLOBAL':
            returnedEmbed.add_field(name = 'Wins Over Replacement Player(WORP)', value = 'not implemented', inline=True)
            returnedEmbed.add_field(name = 'True Winning Percentage (TW%)', value= 'not implemented', inline=True)
            returnedEmbed.add_field(name = 'MVPs', value= f'{db['MVPS']} ({await statBuilder.getPercentage(db, 'MVPS', 'GamesPlayed')}% of Games, {await statBuilder.getPercentage(db, 'MVPS', 'GamesWon')}% of Wins)')
        returnedEmbed.add_field(name = 'Kills', value = f'{db['Kills']} ({await statBuilder.getDivider(db, 'Kills', 'GamesPlayed')} per Game)')
        returnedEmbed.add_field(name = 'Deaths', value= f'{db['Deaths']}', inline=True)
        returnedEmbed.set_thumbnail(url=thumbnail)
        returnedEmbed.set_footer(icon_url=thumbnail, text = f'{name} Stats')
        return returnedEmbed
    

    
    async def soldierOverviewEmbed(currentTheme, user, name, thumbnail, rootDB, rootGlobalDB):
        db = rootDB['stats']
        globalDB = rootGlobalDB['stats']
        returnedEmbed = discord.Embed(title = f'{currentTheme.soldierSingle} Overview', color = currentTheme.soldierColor)
        returnedEmbed.add_field(name = f'{currentTheme.soldierSingle} Games Played', value=db['SoldiersPlayed'], inline=True)
        returnedEmbed.add_field(name = f'{currentTheme.soldierSingle} Games Won', value = f'{db['SoldiersWon']} ({await statBuilder.getPercentage(db, 'SoldiersWon', 'SoldiersPlayed')}%)', inline=True)
        if user != 'GLOBAL':
            returnedEmbed.add_field(name = f'{currentTheme.soldierSingle} WORP', value= 'not implemented', inline=True)
            returnedEmbed.add_field(name = f'{currentTheme.soldierSingle} TW%', value = 'not implemented', inline=True)
            returnedEmbed.add_field(name = f'{currentTheme.soldierSingle} MVPs', value = f'{db['SoldiersMVPS']} ({await statBuilder.getPercentage(db, 'SoldiersMVPS', 'SoldiersPlayed')}% of Games, {await statBuilder.getPercentage(db, 'SoldiersMVPS', 'SoldiersWon')}% of Wins)')
        returnedEmbed.add_field(name = f'Made to Kidnap Phase', value = f'{db['SoldiersKidnaps']} ({await statBuilder.getPercentage(db, 'SoldiersKidnaps', 'SoldiersPlayed')}% of Games)', inline= True)
        returnedEmbed.add_field(name = 'Protected Coordinate', value = f'{db['SoldiersKidnapWins']} ({await statBuilder.getPercentage(db, 'SoldiersKidnapWins', 'SoldiersKidnaps')}% of Kidnap Phases)', inline=True)
        returnedEmbed.add_field(name = f'{currentTheme.expeditionName} Passes', value = f'{db['SoldiersPasses']} ({await statBuilder.getDivider(db, 'SoldiersPasses', 'SoldiersPlayed')} per Game)', inline=True)
        returnedEmbed.add_field(name = f'{currentTheme.expeditionName} Fails', value = f'{db['SoldiersWallsBroken']} ({await statBuilder.getDivider(db, 'SoldiersWallsBroken', 'SoldiersPlayed')} per Game)', inline= True)
        returnedEmbed.add_field(name = f'Commanded {currentTheme.expeditionName}', value = f'{db['ExposCommanded']}', inline= True)
        returnedEmbed.add_field(name = f'{currentTheme.expeditionName} Proposals Passed', value = f'{db['AcceptedCommand']} ({await statBuilder.getPercentage(db, 'AcceptedCommand', 'ExposCommanded')}% of Commanded {currentTheme.expeditionName})', inline= True)
        returnedEmbed.add_field(name = f'{currentTheme.expeditionName} Rounds Passed as Commander', value = f'{db['PassExpeditions']} ({await statBuilder.getPercentage(db, 'PassExpeditions', 'AcceptedCommand')}% of Passed Proposals, {await statBuilder.getDivider(db, 'PassExpeditions', 'SoldiersPlayed')} per Game)')
        returnedEmbed.add_field(name = f'{currentTheme.expeditionName} Rounds Accepted', value = db['ExposVoted'], inline=True)
        returnedEmbed.add_field(name = f'{currentTheme.expeditionName} Passed Rounds Accepted', value= f'{db['PassVotes']} ({await statBuilder.getPercentage(db, 'PassVotes', 'ExposVoted')}% Vote Success Rate, {await statBuilder.getDivider(db, 'PassVotes', 'SoldiersPlayed')} per Game)')
        returnedEmbed.add_field(name = f'On {currentTheme.expeditionName}', value = f'{db['SoldiersExpeditionsOn']} ({await statBuilder.getDivider(db, 'SoldiersExpeditionsOn', 'SoldiersPlayed')} per Game)', inline= True)
        returnedEmbed.add_field(name = f'On Passed {currentTheme.expeditionName}', value = f'{db['PassExpeditions']} ({await statBuilder.getPercentage(db, 'PassExpeditions', 'SoldiersExpeditionsOn')}% Rounds Participated, {await statBuilder.getDivider(db, 'PassExpeditions', 'SoldiersPlayed')} per Game)', inline= True)
        returnedEmbed.add_field(name = f'Passed Round Assits', value = f'{db['PassAssists']} ({await statBuilder.getDivider(db, 'PassAssists', 'SoldiersPlayed')} per Game)')
        returnedEmbed.add_field(name = f'Passed Rounds Responsible For', value = f'{db['PassesResponsible']} ({await statBuilder.getDivider(db, 'PassesResponsible', 'SoldiersPlayed')} per Game)')
        returnedEmbed.set_thumbnail(url = currentTheme.soldierThumbnail)
        returnedEmbed.set_footer(icon_url=thumbnail, text = f'{name} Stats')
        return returnedEmbed
    
    async def soldierRolesEmbed(currentTheme, user, name, thumbnail, rootDB, rootGlobalDB, loadedRoles):
        db = rootDB['stats']
        globalDB = rootGlobalDB['stats']
        returnedEmbed = discord.Embed(title = f'{currentTheme.soldierSingle} Role Overview', color = currentTheme.soldierColor)
        for role in loadedRoles:
            if role.team == 'Soldiers':
                value = f'Played: {db[f'{role.id}Played']}'
                value += f'\nWon: {db[f'{role.id}Won']} ({await statBuilder.getPercentage(db, f'{role.id}Won', f'{role.id}Played')}%)'
                value += f'\nBasements: {db[f'{role.id}Kidnaps']} ({await statBuilder.getPercentage(db, f'{role.id}Kidnaps', f'{role.id}Played')}% Games)'
                value += f'\nBasement Wins: {db[f'{role.id}KidnapWins']} ({await statBuilder.getPercentage(db, f'{role.id}KidnapWins', f'{role.id}Kidnaps')}%)'
                returnedEmbed.add_field(name = f'{role.emoji}{role.shortName}{role.emoji}', value = value, inline = True)
        returnedEmbed.set_thumbnail(url = currentTheme.soldierThumbnail)
        returnedEmbed.set_footer(icon_url=thumbnail, text = f'{name} Stats')
        return returnedEmbed
    
    async def soldierSpecificRoleEmbed(currentTheme, user, name, thumbnail, rootDB, rootGlobalDB, loadedRoles, role):
        db = rootDB['stats']
        globalDB = rootGlobalDB['stats']
        returnedEmbed = discord.Embed(title = f'{role.shortName} Stats', color = currentTheme.soldierColor)
        returnedEmbed.add_field(name = 'Games Played', value=db[f'{role.id}Played'], inline=True)
        returnedEmbed.add_field(name = 'Games Won', value = f'{db[f'{role.id}Won']} ({await statBuilder.getPercentage(db, f'{role.id}Won', f'{role.id}Played')}%)', inline = True)
        if user != 'GLOBAL':
            returnedEmbed.add_field(name = 'Wins Over Replacement Player (WORP)', value = 'not implemented', inline=True)
            returnedEmbed.add_field(name = 'True Winning %', value = 'not implemented', inline = True)
        returnedEmbed.add_field(name = 'Made to Kidnap Phase', value = f'{db[f'{role.id}Kidnaps']} ({await statBuilder.getPercentage(db, f'{role.id}Kidnaps', f'{role.id}Played')}% of Games)', inline=True)
        returnedEmbed.add_field(name = 'Won Kidnap Phases', value= f'{db[f'{role.id}KidnapWins']} ({await statBuilder.getPercentage(db, f'{role.id}KidnapWins', f'{role.id}Kidnaps')}% of Kidnap Phases)', inline = True)
        if role.id == 'Armin':
            returnedEmbed.add_field(name = 'Nukes', value = db['ArminNukes'], inline=True)
            returnedEmbed.add_field(name = 'Kills', value = f'{db[f'{role.id}Kills']} ({await statBuilder.getDivider(db, f'ArminKills', 'ArminNukes')} per Nuke)', inline=True)
            returnedEmbed.add_field(name = f'{currentTheme.warriorPlural} Killed', value= f'{db[f'{role.id}KillWins']} ({await statBuilder.getPercentage(db, f'{role.id}KillWins', f'{role.id}Kills')}% of Kills, {await statBuilder.getDivider(db, 'ArminKillWins', 'ArminNukes')} per Nuke)', inline=True)
        elif role.id == 'Sasha':
            returnedEmbed.add_field(name = 'Players Targeted', value = db['SashaFires'], inline=True)
            returnedEmbed.add_field(name = 'Kills', value = f'{db[f'{role.id}Kills']} ({await statBuilder.getDivider(db, f'SashaKills', 'SashaFires')} per Player Targeted)', inline=True)
            returnedEmbed.add_field(name = f'{currentTheme.warriorPlural} Killed', value= f'{db[f'{role.id}KillWins']} ({await statBuilder.getPercentage(db, f'{role.id}KillWins', f'{role.id}Kills')}% of Kills, {await statBuilder.getDivider(db, 'SashaKillWins', 'SashaFires')} per Player Targeted)', inline=True)
        elif role.id == 'Jean':
            returnedEmbed.add_field(name = 'Proposals Secured', value = db['JeanForces'], inline=True)
            returnedEmbed.add_field(name = f'Forced Proposal {currentTheme.expeditionName} Passes', value= f'{db['JeanForceWins']} ({await statBuilder.getPercentage(db, 'JeanForceWins', 'JeanForces')}%)')
        elif role.id == 'Erwin':
            returnedEmbed.add_field(name = 'Flares Fired', value = db['ErwinFlaresFired'], inline=True)
        elif role.id == 'Daz':
            returnedEmbed.add_field(name = 'Chickened Out', value = db['DazChickens'], inline=True)
            returnedEmbed.add_field(name = f'Chicken {currentTheme.expeditionName} Saves', value = f'{db['DazChickenWins']} ({await statBuilder.getPercentage(db, 'DazChickenWins', 'DazChickens')}%)')
        elif role.id == 'Levi':
            returnedEmbed.add_field(name = 'Attacks', value = db['LeviAttacks'], inline=True)
            returnedEmbed.add_field(name = 'Kills', value = f'{db['LeviKills']} ({await statBuilder.getDivider(db, 'LeviKills', 'LeviAttacks')} per Attack)', inline = True)
            returnedEmbed.add_field(name = 'Defends', value = db['LeviDefends'], inline=True)
            returnedEmbed.add_field(name = f'Levi {currentTheme.expeditionName} Saves', value = f'{db['LeviDefendWins']} ({await statBuilder.getPercentage(db, 'LeviDefendWins', 'LeviDefends')}% of Defends)')
        elif role.id == 'Mikasa':
            returnedEmbed.add_field(name = 'Players Guarded', value = db['MikasaGuards'], inline=True)
            returnedEmbed.add_field(name = 'Players Saved', value = f'{db['MikasaSaved']} ({await statBuilder.getPercentage(db, 'MikasaSaved', 'MikasaGuards')}% of Guards)')
            returnedEmbed.add_field(name = f'{currentTheme.soldierPlural} Saved', value = f'{db['MikasaSaveWins']} ({await statBuilder.getPercentage(db, 'MikasaSaveWins', 'MikasaGuards')}% of Guards, {await statBuilder.getPercentage(db, 'MikasaSaveWins', 'MikasaSaved')}% of Saves)')
        if type(role.emoji) == str:
            returnedEmbed.set_thumbnail(url = role.imageURL)
        else:
            returnedEmbed.set_thumbnail(url = role.emoji.url)
        returnedEmbed.set_footer(icon_url=thumbnail, text = f'{name} Stats')
        return returnedEmbed

    async def warriorOverviewEmbed(currentTheme, user, name, thumbnail, rootDB, rootGlobalDB):
        db = rootDB['stats']
        globalDB = rootGlobalDB['stats']
        returnedEmbed = discord.Embed(title = f'{currentTheme.warriorSingle} Overview', color = currentTheme.warriorColor)
        returnedEmbed.add_field(name = f'{currentTheme.warriorSingle} Games Played', value=db['WarriorsPlayed'], inline=True)
        returnedEmbed.add_field(name = f'{currentTheme.warriorSingle} Games Won', value = f'{db['WarriorsWon']} ({await statBuilder.getPercentage(db, 'WarriorsWon', 'WarriorsPlayed')}%)', inline=True)
        if user != 'GLOBAL':
            returnedEmbed.add_field(name = f'{currentTheme.warriorSingle} WORP', value= 'not implemented', inline=True)
            returnedEmbed.add_field(name = f'{currentTheme.warriorSingle} TW%', value = 'not implemented', inline=True)
            returnedEmbed.add_field(name = f'{currentTheme.warriorSingle} MVPs', value = f'{db['WarriorsMVPS']} ({await statBuilder.getPercentage(db, 'WarriorsMVPS', 'WarriorsPlayed')}% of Games, {await statBuilder.getPercentage(db, 'WarriorsMVPS', 'WarriorsWon')}% of Wins)')
        sabVal = f'{db['WarriorsPlayed'] - db['WarriorsKidnaps']} ({await statBuilder.getAltPercentage(db, (db['WarriorsPlayed'] - db['WarriorsKidnaps']), 'WarriorsPlayed')}% of Games)'
        returnedEmbed.add_field(name = 'Sabotage Wins', value = sabVal, inline= True)
        returnedEmbed.add_field(name = f'Made to Kidnap Phase', value = f'{db['WarriorsKidnaps']} ({await statBuilder.getPercentage(db, 'WarriorsKidnaps', 'WarriorsPlayed')}% of Games)', inline= True)
        returnedEmbed.add_field(name = 'Identified Coordinate', value = f'{db['WarriorsKidnapWins']} ({await statBuilder.getPercentage(db, 'WarriorsKidnapWins', 'WarriorsKidnaps')}% of Kidnap Phases)', inline=True)
        returnedEmbed.add_field(name = f'{currentTheme.expeditionName} Fails', value = f'{db['WarriorsWallsBroken']} ({await statBuilder.getDivider(db, 'WarriorsWallsBroken', 'WarriorsPlayed')} per Game)', inline= True)
        returnedEmbed.add_field(name = f'{currentTheme.expeditionName} Passes', value = f'{db['WarriorsPasses']} ({await statBuilder.getDivider(db, 'WarriorsPasses', 'WarriorsPlayed')} per Game)', inline=True)
        returnedEmbed.add_field(name = f'Sabotaged {currentTheme.expeditionName} Commanded', value = f'{db['BreakCommanders']} ({await statBuilder.getDivider(db, 'BreakCommanders', 'WarriorsPlayed')} per Game)', inline=True)
        returnedEmbed.add_field(name = f'Voted for Sabotaged {currentTheme.expeditionName}', value = f'{db['BreakVotes']} ({await statBuilder.getDivider(db, 'BreakVotes', 'WarriorsPlayed')} per Game)')
        returnedEmbed.add_field(name = f'On {currentTheme.expeditionName}', value = f'{db['WarriorsExpeditionsOn']} ({await statBuilder.getDivider(db, 'WarriorsExpeditionsOn', 'WarriorsPlayed')} per Game)')
        returnedEmbed.add_field(name = f'On Sabotaged {currentTheme.expeditionName}', value = f'{db['BreakExpeditions']} ({await statBuilder.getPercentage(db, 'BreakExpeditions', 'WarriorsExpeditionsOn')}% Participated, {await statBuilder.getDivider(db, 'BreakExpeditions', 'WarriorsPlayed')} per Game)')
        returnedEmbed.add_field(name = f'Sabotaged {currentTheme.expeditionName} Assists', value = f'{db['BreakAssists']} ({await statBuilder.getDivider(db, 'BreakAssists', 'WarriorsPlayed')} per Game)')
        returnedEmbed.add_field(name = f'Sabotaged {currentTheme.expeditionName} Responsible For', value = f'{db['BreaksResponsible']} ({await statBuilder.getDivider(db, 'BreaksResponsible', 'WarriorsPlayed')} per Game)')
        returnedEmbed.set_thumbnail(url = currentTheme.warriorThumbnail)
        returnedEmbed.set_footer(icon_url=thumbnail, text = f'{name} Stats')
        return returnedEmbed
    
    async def warriorRolesEmbed(currentTheme, user, name, thumbnail, rootDB, rootGlobalDB, loadedRoles):
        db = rootDB['stats']
        globalDB = rootGlobalDB['stats']
        returnedEmbed = discord.Embed(title = f'{currentTheme.warriorSingle} Role Overview', color = currentTheme.warriorColor)
        for role in loadedRoles:
            if role.team == 'Warriors':
                value = f'Played: {db[f'{role.id}Played']}'
                value += f'\nWon: {db[f'{role.id}Won']} ({await statBuilder.getPercentage(db, f'{role.id}Won', f'{role.id}Played')}%)'
                value += f'\nSab Wins: {db[f'{role.id}Played'] - db[f'{role.id}Kidnaps']} ({await statBuilder.getAltPercentage(db, db[f'{role.id}Played'] - db[f'{role.id}Kidnaps'], f'{role.id}Played')}%)'
                value += f'\nKidnaps: {db[f'{role.id}Kidnaps']} ({await statBuilder.getPercentage(db, f'{role.id}Kidnaps', f'{role.id}Played')}% Games)'
                value += f'\nKidnap Wins: {db[f'{role.id}KidnapWins']} ({await statBuilder.getPercentage(db, f'{role.id}KidnapWins', f'{role.id}Kidnaps')}%)'
                returnedEmbed.add_field(name = f'{role.emoji}{role.shortName}{role.emoji}', value = value, inline = True)
        returnedEmbed.set_thumbnail(url = currentTheme.warriorThumbnail)
        returnedEmbed.set_footer(icon_url=thumbnail, text = f'{name} Stats')
        return returnedEmbed
    
    async def warriorSpecificRoleEmbed(currentTheme, user, name, thumbnail, rootDB, rootGlobalDB, loadedRoles, role):
        db = rootDB['stats']
        globalDB = rootGlobalDB['stats']
        returnedEmbed = discord.Embed(title = f'{role.shortName} Stats', color = currentTheme.warriorColor)
        returnedEmbed.add_field(name = 'Games Played', value=db[f'{role.id}Played'], inline=True)
        returnedEmbed.add_field(name = 'Games Won', value = f'{db[f'{role.id}Won']} ({await statBuilder.getPercentage(db, f'{role.id}Won', f'{role.id}Played')}%)', inline = True)
        if user != 'GLOBAL':
            returnedEmbed.add_field(name = 'Wins Over Replacement Player (WORP)', value = 'not implemented', inline=True)
            returnedEmbed.add_field(name = 'True Winning %', value = 'not implemented', inline = True)
        returnedEmbed.add_field(name = 'Sabotage Wins', value = f'{db[f'{role.id}Played'] - db[f'{role.id}Kidnaps']} ({await statBuilder.getAltPercentage(db, (db[f'{role.id}Played'] - db[f'{role.id}Kidnaps']), f'{role.id}Played')})% of Games')
        returnedEmbed.add_field(name = 'Made to Kidnap Phase', value = f'{db[f'{role.id}Kidnaps']} ({await statBuilder.getPercentage(db, f'{role.id}Kidnaps', f'{role.id}Played')}% of Games)', inline=True)
        returnedEmbed.add_field(name = 'Identified Coordinate', value= f'{db[f'{role.id}KidnapWins']} ({await statBuilder.getPercentage(db, f'{role.id}KidnapWins', f'{role.id}Kidnaps')}% of Kidnap Phases)', inline = True)
        if role.id == 'Pieck':
            returnedEmbed.add_field(name = 'Flip Accepts', value = db['PieckFlipAccepts'], inline=True)
            returnedEmbed.add_field(name = 'Flip Accept Wins', value = f'{db['PieckFlipAcceptWins']} ({await statBuilder.getPercentage(db, 'PieckFlipAcceptWins', 'PieckFlipAccepts')}% of Flips)', inline=True)
            returnedEmbed.add_field(name = 'Flip Rejects', value = db['PieckFlipRejects'], inline=True)
            returnedEmbed.add_field(name = 'Flip Reject Wins', value = f'{db['PieckFlipRejectWins']} ({await statBuilder.getPercentage(db, 'PieckFlipRejectWins', 'PieckFlipRejects')}% of Flips)', inline=True)
        elif role.id == 'Annie':
            returnedEmbed.add_field(name = 'Screams', value = db['AnnieScreams'], inline=True)
        elif role.id == 'Porco':
            returnedEmbed.add_field(name = 'Gags', value = db['PorcoGags'], inline=True)
            returnedEmbed.add_field(name = f'Gag {currentTheme.commanderName} Skips', value = f'{db['PorcoCommanderSkips']} ({await statBuilder.getDivider(db, 'PorcoCommanderSkips', 'PorcoPlayed')} per Game, {await statBuilder.getDivider(db, 'PorcoCommanderSkips', 'PorcoGags')} per Gag)')
        elif role.id == 'Falco':
            returnedEmbed.add_field(name = 'Vote Intercepts', value = db['FalcoUses'], inline=True)
            returnedEmbed.add_field(name = 'Vote Intercept Passes', value = f'{db['FalcoVoteWins']} ({await statBuilder.getPercentage(db, 'FalcoVoteWins', 'FalcoUses')}% of Intercepts)', inline=True)
        elif role.id == 'Reiner Saves':
            returnedEmbed.add_field(name = 'Armor Saves', value = f'{db['ReinerSaves']} ({await statBuilder.getDivider('ReinerSaves', 'ReinerPlayed')} per Game)')
        elif role.id == 'Bertholdt':
            returnedEmbed.add_field(name = f'{currentTheme.expeditionName} Cloaked', value = f'{db['BertholdtCloaks']} ({await statBuilder.getDivider(db, 'BertholdtCloaks', 'BertholdtPlayed')} per Game)', inline=True)
            returnedEmbed.add_field(name = f'{currentTheme.expeditionName} Doubles Cloaked', value = f'{db['BertholdtDoubleCloaks']} ({await statBuilder.getDivider(db, 'BertholdtDoubleCloaks', 'BertholdtCloaks')} per Cloak, {await statBuilder.getDivider(db, 'BertholdtDoubleCloaks', 'BertholdtPlayed')} per Game)')
        if type(role.emoji) == str:
            returnedEmbed.set_thumbnail(url = role.imageURL)
        else:
            returnedEmbed.set_thumbnail(url = role.emoji.url)
        returnedEmbed.set_footer(icon_url=thumbnail, text = f'{name} Stats')
        return returnedEmbed

    
    async def profileView(navigator, user, currentTheme, loadedRoles):
        returnedView = View()

        soldierRoles = []
        warriorRoles = []
        for role in loadedRoles:
            if role.team == 'Soldiers':
                soldierRoles.append(role)
            elif role.team == 'Warriors':
                warriorRoles.append(role)

        mainButton = Button(label = 'Main Profile', style=discord.ButtonStyle.grey, emoji=str('🪪'))
        async def processMainButton(interaction):
            if interaction.user == navigator:
                embed = await statBuilder.profileEmbed(currentTheme, user, loadedRoles, 'Main')
                await interaction.message.edit(embed=embed)
                await interaction.response.defer()
        mainButton.callback = processMainButton
        returnedView.add_item(mainButton)

        soldierOverviewButton = Button(label = f'{currentTheme.soldierSingle} Overview', style=discord.ButtonStyle.grey, emoji = currentTheme.emojiSoldier)
        async def processSoldierOverviewButton(interaction):
            if interaction.user == navigator:
                embed = await statBuilder.profileEmbed(currentTheme, user, loadedRoles, 'Soldier Overview')
                await interaction.message.edit(embed=embed)
                await interaction.response.defer()
        soldierOverviewButton.callback = processSoldierOverviewButton
        returnedView.add_item(soldierOverviewButton)

        soldierRoleButton = Button(label = f'{currentTheme.soldierSingle} Role Overview', style=discord.ButtonStyle.grey, emoji = str('🎭'))
        async def processSoldierRoleButton(interaction):
            if interaction.user == navigator:
                embed = await statBuilder.profileEmbed(currentTheme, user, loadedRoles, 'Soldier Roles')
                await interaction.message.edit(embed=embed)
                await interaction.response.defer()
        soldierRoleButton.callback = processSoldierRoleButton
        returnedView.add_item(soldierRoleButton)


        soldierSelect = Select(placeholder= f'Specific {currentTheme.soldierSingle} Role', min_values=1, max_values=1)
        for role in soldierRoles:
            soldierSelect.add_option(label = role.shortName, emoji=role.emoji)
        async def processSoldierSelect(interaction):
            if interaction.user == navigator: 
                if interaction.user == navigator:
                    selection = soldierSelect.values[0]
                    for role in soldierRoles:
                        if role.shortName == selection:
                            chosenRole = role
                            break
                    embed = await statBuilder.profileEmbed(currentTheme, user, loadedRoles, {'Soldier Role': chosenRole})
                    await interaction.message.edit(embed=embed)
                    await interaction.response.defer()
        soldierSelect.callback = processSoldierSelect
        returnedView.add_item(soldierSelect) 

        warriorOverviewButton = Button(label = f'{currentTheme.warriorSingle} Overview', style=discord.ButtonStyle.grey, emoji = currentTheme.emojiWarrior)
        async def processWarriorOverviewButton(interaction):
            if interaction.user == navigator:
                embed = await statBuilder.profileEmbed(currentTheme, user, loadedRoles, 'Warrior Overview')
                await interaction.message.edit(embed=embed)
                await interaction.response.defer()
        warriorOverviewButton.callback = processWarriorOverviewButton
        returnedView.add_item(warriorOverviewButton)

        warriorRoleButton = Button(label = f'{currentTheme.warriorSingle} Role Overview', style=discord.ButtonStyle.grey, emoji = str('🎭'))
        async def processWarriorRoleButton(interaction):
            if interaction.user == navigator:
                embed = await statBuilder.profileEmbed(currentTheme, user, loadedRoles, 'Warrior Roles')
                await interaction.message.edit(embed=embed)
                await interaction.response.defer()
        warriorRoleButton.callback = processWarriorRoleButton
        returnedView.add_item(warriorRoleButton)


        warriorSelect = Select(placeholder= f'Specific {currentTheme.warriorSingle} Role', min_values=1, max_values=1)
        for role in warriorRoles:
            warriorSelect.add_option(label = role.shortName, emoji=role.emoji)
        async def processWarriorSelect(interaction):
            if interaction.user == navigator: 
                if interaction.user == navigator:
                    selection = warriorSelect.values[0]
                    for role in warriorRoles:
                        if role.shortName == selection:
                            chosenRole = role
                            break
                    embed = await statBuilder.profileEmbed(currentTheme, user, loadedRoles, {'Warrior Role' : chosenRole})
                    await interaction.message.edit(embed=embed)
                    await interaction.response.defer()
        warriorSelect.callback = processWarriorSelect
        returnedView.add_item(warriorSelect)

        return returnedView




