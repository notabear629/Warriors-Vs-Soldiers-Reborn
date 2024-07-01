import discord
from discord.ext import commands
from discord import ui
from discord.ui import *
from discord.utils import *

from dataFunctions.databaseManager import databaseManager

from gameObjects.Role import Role

import math

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
    
    async def getRoleTW(db, globalDB, wins, plays):
        if wins.startswith('Keith'):
            if wins.startswith('Keith'):
                role = 'Keith'
            if globalDB[f'{role}FinishedPlayed'] == 0 or db[f'{role}FinishedWon'] == 0:
                return 0.0
            elif db[f'{role}FinishedWon'] == globalDB[f'{role}FinishedWon']:
                return 100.0
            g = globalDB[f'{role}FinishedWon']/globalDB[f'{role}FinishedPlayed']
            x = db[f'{role}FinishedWon']/db[f'{role}FinishedPlayed']
            return round((x ** (math.log(0.5,g))) * 100, 1)
        else:
            if globalDB[plays] == 0 or db[wins] == 0:
                return 0.0
            elif db[wins] == db[plays]:
                return 100.0
            #Let x = average win percentage of given role
            g = globalDB[wins]/globalDB[plays]
            #Let x = user's win percentage
            x = db[wins]/db[plays]
            #Return our TW% function calc
            return round((x ** (math.log(0.5,g))) * 100, 1)
    
    async def getTeamTW(db, globalDB, team, specialCase=False):
        playedDB = db['GamesPlayed']
        if team == 'Soldiers':
            roles = Role.soldierRoles.copy()
            if specialCase:
                playedDB = db['SoldiersPlayed']
        elif team == 'Warriors':
            roles = Role.warriorRoles.copy()
            if specialCase:
                playedDB = db['WarriorsPlayed']
        #initialize t = total
        t = 0
        for role in roles:
            specialRoles = ['Keith']
            if role in specialRoles:
                if globalDB[f'{role}FinishedPlayed'] == 0 or db[f'{role}FinishedWon'] == 0:
                    continue
                if db[f'{role}FinishedWon'] == db[f'{role}FinishedPlayed']:
                    t += (db[f'{role}FinishedPlayed']/playedDB)
                    continue
                #let g = average win percentage of given role
                g = globalDB[f'{role}FinishedWon']/globalDB[f'{role}FinishedPlayed']
                #let x = user's win percentage
                x = db[f'{role}FinishedWon']/db[f'{role}FinishedPlayed']
                #let y = the raw tw% calculation
                y = x ** (math.log(0.5, g))
                #let z = y times the proportion of the time they played as that role relative to playing as the team
                z = y * (db[f'{role}FinishedPlayed']/playedDB)
                #increment t by z
                t += z
            else:
                if globalDB[f'{role}Played'] == 0 or db[f'{role}Won'] == 0:
                    continue
                if db[f'{role}Won'] == db[f'{role}Played']:
                    t += (db[f'{role}Played']/playedDB)
                    continue
                #let g = average win percentage of given role
                g = globalDB[f'{role}Won']/globalDB[f'{role}Played']
                #let x = user's win percentage
                x = db[f'{role}Won']/db[f'{role}Played']
                #let y = the raw tw% calculation
                y = x ** (math.log(0.5, g))
                #let z = y times the proportion of the time they played as that role relative to playing as the team
                z = y * (db[f'{role}Played']/playedDB)
                #increment t by z
                t += z
        #Convert t to properly rounded percentage and return
        return round(t*100, 1)
    
    async def getTotalTW(db, globalDB):
        roles = Role.allRoles.copy()
        t = 0
        for role in roles:
            specialRoles = ['Keith']
            if role in specialRoles:
                if globalDB[f'{role}FinishedPlayed'] == 0 or db[f'{role}FinishedWon'] == 0:
                    continue
                if db[f'{role}FinishedWon'] == db[f'{role}FinishedPlayed']:
                    t += (db[f'{role}FinishedPlayed']/db[f'GamesPlayed'])
                    continue
                #let g = average win percentage of given role
                g = globalDB[f'{role}FinishedWon']/globalDB[f'{role}FinishedPlayed']
                #let x = user's win percentage
                x = db[f'{role}FinishedWon']/db[f'{role}FinishedPlayed']
                #let y = the raw tw% calculation
                y = x ** (math.log(0.5, g))
                #let z = y times the proportion of the time they played as that role relative to playing as the team
                z = y * (db[f'{role}FinishedPlayed']/db[f'GamesPlayed'])
                #increment t by z
                t += z
            else:
                if globalDB[f'{role}Played'] == 0 or db[f'{role}Won'] == 0:
                    continue
                if db[f'{role}Won'] == db[f'{role}Played']:
                    t += (db[f'{role}Played']/db[f'GamesPlayed'])
                    continue
                #let g = average win percentage of given role
                g = globalDB[f'{role}Won']/globalDB[f'{role}Played']
                #let x = user's win percentage
                x = db[f'{role}Won']/db[f'{role}Played']
                #let y = the raw tw% calculation
                y = x ** (math.log(0.5, g))
                #let z = y times the proportion of the time they played as that role relative to playing as the team
                z = y * (db[f'{role}Played']/db[f'GamesPlayed'])
                #increment t by z
                t += z
        #Convert t to properly rounded percentage and return
        return round(t*100, 1)
    
    async def getRoleWORP(db, globalDB, role, stackCase=False):
        specialRoles = ['Keith']
        if role in specialRoles:
            if globalDB[f'{role}FinishedPlayed'] == 0 or db[f'{role}FinishedWon'] == 0:
                return 0.0
            g = globalDB[f'{role}FinishedWon']/globalDB[f'{role}FinishedPlayed']
            x = db[f'{role}FinishedWon']/db[f'{role}FinishedPlayed']
            y = x - g
            z = y * db[f'{role}FinishedPlayed']
            if stackCase:
                return z
            else:
                return round(z, 1)
        else:
            if globalDB[f'{role}Played'] == 0 or db[f'{role}Won'] == 0:
                return 0.0
            #let g = average win percentage
            g = globalDB[f'{role}Won']/globalDB[f'{role}Played']
            #let x = player win percentage
            x = db[f'{role}Won']/db[f'{role}Played']
            #let y be the differential between these two values
            y = x - g
            #let z be the total WORP generated by multiplying differential times user games
            z = y * db[f'{role}Played']
            #If this function is being called to get a team/total value, then return without a round
            if stackCase:
                return z
            else:
                return round(z,1)
        
    async def getTeamWORP(db, globalDB, team, stackCase=False):
        if team == 'Soldiers':
            roles = Role.soldierRoles.copy()
        elif team == 'Warriors':
            roles = Role.warriorRoles.copy()
        #initialize t for total = 0
        t = 0
        for role in roles:
            t += await statBuilder.getRoleWORP(db, globalDB, role, True)
        if stackCase:
            return t
        else:
            return round(t,1)
        
    async def getTotalWORP(db, globalDB, stackCase=False):
        worp = await statBuilder.getTeamWORP(db, globalDB, 'Soldiers', True) + await statBuilder.getTeamWORP(db, globalDB, 'Warriors', True)
        if stackCase:
            return worp
        else:
            return round(worp, 1)


    async def profileEmbed(currentTheme, user, loadedRoles, color, loadedBadges, embedType):
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
            return await statBuilder.mainProfileEmbed(currentTheme, user, name, thumbnail, rootDB, globalDB, color, loadedBadges)
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
    
    async def mainProfileEmbed(currentTheme, user, name, thumbnail, rootDB, rootGlobalDB, color, loadedBadges):
        db = rootDB['stats']
        globalDB = rootGlobalDB['stats']
        if user == 'GLOBAL':
            title = 'Global Stats'
            description = None
        else:
            title = f'{user.name}\'s Profile'
            description = f'Legacy Points: **{rootDB['points']['LegacyPoints']}**'
        rankedPoints = databaseManager.getSortedLegacy()
        playerIndex = 0
        playerNumber = 0
        for player in rankedPoints:
            playerNumber += 1
            if rootDB['userID'] == player['userID']:
                playerIndex = playerNumber
        returnedEmbed = discord.Embed(title = title, description = description, color = color)
        if user != 'GLOBAL':
            returnedEmbed.add_field(name = 'Rank', value = f'{playerIndex}/{playerNumber}', inline= True)
            if len(rootDB['titles']) > 0:
                titles = ['LegacyPoints', 'WORP', 'MostWins', 'ELO', 'MVPS', 'BadgePoints', 'SoldierWORP', 'WarriorWORP', 'Kills', 'Deaths', 'MostKidnappable', 'BiggestLoser', 'MostKidnapWins', 'SinaSmasher']
                titleValue = ""
                for title in titles:
                    if title in rootDB['titles']:
                        titleValue += f'{getattr(loadedBadges, f'emoji{title}')}'
                returnedEmbed.add_field(name = 'Titles', value = titleValue, inline= True)
        returnedEmbed.add_field(name = 'Games Played', value = db['GamesPlayed'], inline= True)
        returnedEmbed.add_field(name = 'Games Won', value = f'{db['GamesWon']} ({await statBuilder.getPercentage(db, 'GamesWon', 'GamesPlayed')}%)', inline=True)
        if user != 'GLOBAL':
            returnedEmbed.add_field(name = 'Wins Over Replacement Player(WORP)', value = await statBuilder.getTotalWORP(db, globalDB), inline=True)
            returnedEmbed.add_field(name = 'True Winning Percentage (TW%)', value= f'{await statBuilder.getTotalTW(db, globalDB)}%', inline=True)
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
            returnedEmbed.add_field(name = f'{currentTheme.soldierSingle} WORP', value= await statBuilder.getTeamWORP(db, globalDB, 'Soldiers'), inline=True)
            returnedEmbed.add_field(name = f'{currentTheme.soldierSingle} TW%', value = f'{await statBuilder.getTeamTW(db, globalDB, 'Soldiers', True)}%', inline=True)
            returnedEmbed.add_field(name = f'{currentTheme.soldierSingle} MVPs', value = f'{db['SoldiersMVPS']} ({await statBuilder.getPercentage(db, 'SoldiersMVPS', 'SoldiersPlayed')}% of Games, {await statBuilder.getPercentage(db, 'SoldiersMVPS', 'SoldiersWon')}% of Wins)')
        returnedEmbed.add_field(name = f'Made to Kidnap Phase', value = f'{db['SoldiersKidnaps']} ({await statBuilder.getPercentage(db, 'SoldiersKidnaps', 'SoldiersPlayed')}% of Games)', inline= True)
        returnedEmbed.add_field(name = 'Protected Coordinate', value = f'{db['SoldiersKidnapWins']} ({await statBuilder.getPercentage(db, 'SoldiersKidnapWins', 'SoldiersKidnaps')}% of Kidnap Phases)', inline=True)
        returnedEmbed.add_field(name = f'{currentTheme.expeditionName} Passes', value = f'{db['SoldiersPasses']} ({await statBuilder.getDivider(db, 'SoldiersPasses', 'SoldiersPlayed')} per Game)', inline=True)
        returnedEmbed.add_field(name = f'{currentTheme.expeditionName} Fails', value = f'{db['SoldiersWallsBroken']} ({await statBuilder.getDivider(db, 'SoldiersWallsBroken', 'SoldiersPlayed')} per Game)', inline= True)
        returnedEmbed.add_field(name = f'Commanded {currentTheme.expeditionName}', value = f'{db['ExposCommanded']}', inline= True)
        returnedEmbed.add_field(name = f'{currentTheme.expeditionName} Proposals Passed', value = f'{db['AcceptedCommand']} ({await statBuilder.getPercentage(db, 'AcceptedCommand', 'ExposCommanded')}% of Commanded {currentTheme.expeditionName})', inline= True)
        returnedEmbed.add_field(name = f'{currentTheme.expeditionName} Rounds Passed as Commander', value = f'{db['PassExpeditions']} ({await statBuilder.getPercentage(db, 'PassCommanders', 'AcceptedCommand')}% of Passed Proposals, {await statBuilder.getDivider(db, 'PassExpeditions', 'SoldiersPlayed')} per Game)')
        returnedEmbed.add_field(name = f'{currentTheme.expeditionName} Rounds Accepted', value = db['ExposVoted'], inline=True)
        returnedEmbed.add_field(name = f'{currentTheme.expeditionName} Passed Rounds Accepted', value= f'{db['PassVotes']} ({await statBuilder.getPercentage(db, 'PassVotes', 'ExposVoted')}% Vote Success Rate, {await statBuilder.getDivider(db, 'PassVotes', 'SoldiersPlayed')} per Game)')
        returnedEmbed.add_field(name = f'On {currentTheme.expeditionName}', value = f'{db['SoldiersExpeditionsOn']} ({await statBuilder.getDivider(db, 'SoldiersExpeditionsOn', 'SoldiersPlayed')} per Game)', inline= True)
        returnedEmbed.add_field(name = f'On Passed {currentTheme.expeditionName}', value = f'{db['PassExpeditions']} ({await statBuilder.getPercentage(db, 'PassExpeditions', 'SoldiersExpeditionsOn')}% Rounds Participated, {await statBuilder.getDivider(db, 'PassExpeditions', 'SoldiersPlayed')} per Game)', inline= True)
        returnedEmbed.add_field(name = f'Passed Round Assists', value = f'{db['PassAssists']} ({await statBuilder.getDivider(db, 'PassAssists', 'SoldiersPlayed')} per Game)')
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
                value += f'\nWon: {db[f'{role.id}Won']} ({await statBuilder.getPercentage(db, f'{role.id}Won', f'{role.id}Played')}%, {await statBuilder.getRoleTW(db, globalDB, f'{role.id}Won', f'{role.id}Played')}TW%)'
                value += f'\nBasements: {db[f'{role.id}Kidnaps']} ({await statBuilder.getPercentage(db, f'{role.id}Kidnaps', f'{role.id}Played')}% Games)'
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
            returnedEmbed.add_field(name = 'Wins Over Replacement Player (WORP)', value = await statBuilder.getRoleWORP(db, globalDB, role.id), inline=True)
            returnedEmbed.add_field(name = 'True Winning %', value = f'{await statBuilder.getRoleTW(db, globalDB, f'{role.id}Won', f'{role.id}Played')}%', inline = True)
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
        elif role.id == 'Zachary':
            returnedEmbed.add_field(name = 'Proposals Vetoed', value = db['ZacharyVetoes'], inline=True)
            returnedEmbed.add_field(name = 'Bad Teams Vetoed', value = f'{db['ZacharyVetoWins']} ({await statBuilder.getPercentage(db, 'ZacharyVetoWins', 'ZacharyVetoes')}% of Vetoes)', inline=True)
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
        elif role.id == 'Petra':
            returnedEmbed.add_field(name = 'Players Watched', value = db['PetraWatches'], inline=True)
            returnedEmbed.add_field(name = 'Players Killed', value = f'{db['PetraKills']} ({await statBuilder.getPercentage(db, 'PetraKills', 'PetraWatches')}% of Watches)', inline=True)
        elif role.id == 'Mikasa':
            returnedEmbed.add_field(name = 'Players Guarded', value = db['MikasaGuards'], inline=True)
            returnedEmbed.add_field(name = 'Players Saved', value = f'{db['MikasaSaved']} ({await statBuilder.getPercentage(db, 'MikasaSaved', 'MikasaGuards')}% of Guards)', inline=True)
            returnedEmbed.add_field(name = f'{currentTheme.soldierPlural} Saved', value = f'{db['MikasaSaveWins']} ({await statBuilder.getPercentage(db, 'MikasaSaveWins', 'MikasaGuards')}% of Guards, {await statBuilder.getPercentage(db, 'MikasaSaveWins', 'MikasaSaved')}% of Saves)')
        elif role.id == 'Keith':
            returnedEmbed.add_field(name = f'Times Summoned', value = f'{db['KeithPlayed']-db['KeithFinishedPlayed']} ({round((100 - await statBuilder.getPercentage(db, 'KeithFinishedPlayed', 'KeithPlayed')),1)}% of Games Played)', inline=True)
            returnedEmbed.add_field(name = f'Games Finished as {role.shortName}', value = f'{db['KeithFinishedPlayed']}', inline=True)
            returnedEmbed.add_field(name = f'Games Won as {role.shortName}', value = f'{db['KeithFinishedWon']} ({await statBuilder.getPercentage(db, 'KeithFinishedWon', 'KeithFinishedPlayed')}% of Non-Summoning Games)', inline=True)
            returnedEmbed.add_field(name = f'Basements Reached as {role.shortName}', value = f'{db['KeithFinishedKidnaps']} ({await statBuilder.getPercentage(db, 'KeithFinishedKidnaps', 'KeithFinishedPlayed')}% of Non-Summoning Games)', inline=True)
            returnedEmbed.add_field(name = f'Coords Hidden as {role.shortName}', value = f'{db['KeithFinishedKidnapWins']} ({await statBuilder.getPercentage(db, 'KeithFinishedKidnapWins', 'KeithFinishedKidnaps')}% of Non-Summoning Basements)', inline=True)
        elif role.id == 'Mike':
            returnedEmbed.add_field(name = f'{currentTheme.titanPlural} Detected', value = f'{db['MikeSmells']} ({await statBuilder.getDivider(db, 'MikeSmells', 'MikePlayed')} per Game)', inline=True)   
        elif role.id == 'Floch':
            returnedEmbed.add_field(name = f'Coordinates Detected', value = f'{db['FlochDetects']} ({await statBuilder.getDivider(db, 'FlochDetects', 'FlochPlayed')} per Game)', inline=True)
        elif role.id == 'Hitch':
            returnedEmbed.add_field(name = f'{role.shortName} Discoveries', value = f'{db['HitchDiscovers']} ({await statBuilder.getDivider(db,'HitchDiscovers', 'HitchPlayed')} per Game)', inline=True)
        elif role.id == 'Nile':
            returnedEmbed.add_field(name = f'{role.shortName} Sightings', value = f'{db['NileSightings']} ({await statBuilder.getDivider(db, 'NileSightings', 'NilePlayed')} per Game)', inline=True)
        elif role.id == 'Connie':
            returnedEmbed.add_field(name = f'{role.shortName} Bait Alerts', value = f'{db['ConnieAlerts']} ({await statBuilder.getDivider(db, 'ConnieAlerts', 'ConniePlayed')} per Game)', inline=True)
        elif role.id == 'Hange':
            returnedEmbed.add_field(name = f'{role.shortName} Wiretaps', value = f'{db['HangeWiretaps']} ({await statBuilder.getPercentage(db, 'HangeWiretaps', 'HangePlayed')}% of Games)', inline=True)
            returnedEmbed.add_field(name = f'{currentTheme.soldierPlural} Wiretap Detected', value = f'{db['HangeWiretapsSoldier']} ({await statBuilder.getPercentage(db, 'HangeWiretapsSoldier', 'HangeWiretaps')}% of Wiretaps, {await statBuilder.getPercentage(db, 'HangeWiretapsSoldier', 'HangePlayed')}% of Games)', inline=True)
            returnedEmbed.add_field(name = f'{currentTheme.warriorPlural} Wiretap Detected', value = f'{db['HangeWiretapsWarrior']} ({await statBuilder.getPercentage(db, 'HangeWiretapsWarrior', 'HangeWiretaps')}% of Wiretaps, {await statBuilder.getPercentage(db, 'HangeWiretapsWarrior', 'HangePlayed')}% of Games)', inline=True)
        elif role.id == 'Marco':
            returnedEmbed.add_field(name = f'{role.shortName} Deaths', value = f'{db['MarcoDeaths']} ({await statBuilder.getPercentage(db, 'MarcoDeaths', 'MarcoPlayed')}% of Games)', inline=True)
            returnedEmbed.add_field(name = f'{role.shortName} Suicides', value = f'{db['MarcoSuicides']} ({await statBuilder.getPercentage(db, 'MarcoSuicides', 'MarcoPlayed')}% of Games, {await statBuilder.getPercentage(db, 'MarcoSuicides', 'MarcoDeaths')}% of Deaths)')
            returnedEmbed.add_field(name = f'{currentTheme.expeditionName} Proposals when Dead', value  = f'{db['MarcoRounds']} ({await statBuilder.getDivider(db, 'MarcoRounds', 'MarcoPlayed')} per Game, {await statBuilder.getDivider(db, 'MarcoRounds', 'MarcoDeaths')} per Death)', inline=True)
            returnedEmbed.add_field(name = f'{currentTheme.expeditionName} Voted when Dead', value = f'{db['MarcoVoted']} ({await statBuilder.getDivider(db, 'MarcoVoted', 'MarcoPlayed')} per Game, {await statBuilder.getDivider(db, 'MarcoVoted', 'MarcoDeaths')} per Death, {await statBuilder.getPercentage(db, 'MarcoVoted', 'MarcoRounds')}% of Dead Rounds)', inline=True)
        elif role.id == 'Marlowe':
            returnedEmbed.add_field(name = f'{role.shortName} Bodies Identified', value = f'{db['MarloweIdentified']} ({await statBuilder.getDivider(db, 'MarloweIdentified', 'MarlowePlayed')} per Game)')
        elif role.id == 'Hannes':
            returnedEmbed.add_field(name = f'{currentTheme.expeditionName} Escaped', value = f'{db['HannesEscapes']} ({await statBuilder.getPercentage(db, 'HannesEscapes', 'HannesPlayed')}% of Games)')
        elif role.id == 'Pyxis':
            returnedEmbed.add_field(name = f'Trials Started', value = f'{db['PyxisTrials']} ({await statBuilder.getPercentage(db, 'PyxisTrials', 'PyxisPlayed')}% of Games)', inline=True)
            returnedEmbed.add_field(name = f'Trials Won', value = f'{db['PyxisTrialWins']} ({await statBuilder.getPercentage(db, 'PyxisTrialWins', 'PyxisTrials')}% of Games)', inline=True)
            returnedEmbed.add_field(name = f'Trial Kills', value = f'{db['PyxisKills']} ({await statBuilder.getPercentage(db, 'PyxisKills', 'PyxisTrials')}% of Trials, {await statBuilder.getPercentage(db, 'PyxisKills', 'PyxisTrialWins')}% of Trial Wins)', inline=True)
            returnedEmbed.add_field(name = f'Trial Kill Wins', value = f'{db['PyxisKillWins']} ({await statBuilder.getPercentage(db, 'PyxisKillWins', 'PyxisKills')}% of Kills)', inline=True)
        elif role.id == 'Samuel':
            returnedEmbed.add_field(name = f'Clowneries', value = f'{db['SamuelClowns']} ({await statBuilder.getPercentage(db, 'SamuelClowns', 'SamuelPlayed')}% of Games)', inline=True)
            returnedEmbed.add_field(name = f'Accepted Clowneries', value = f'{db['SamuelClownAccepts']} ({await statBuilder.getPercentage(db, 'SamuelClownAccepts', 'SamuelClowns')}% of Clowneries)', inline=True)
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
            returnedEmbed.add_field(name = f'{currentTheme.warriorSingle} WORP', value= await statBuilder.getTeamWORP(db, globalDB, 'Warriors'), inline=True)
            returnedEmbed.add_field(name = f'{currentTheme.warriorSingle} TW%', value = f'{await statBuilder.getTeamTW(db, globalDB, 'Warriors', True)}%', inline=True)
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
                value += f'\nWon: {db[f'{role.id}Won']} ({await statBuilder.getPercentage(db, f'{role.id}Won', f'{role.id}Played')}%, {await statBuilder.getRoleTW(db, globalDB, f'{role.id}Won', f'{role.id}Played')}TW%)'
                value += f'\nSab Wins: {db[f'{role.id}Played'] - db[f'{role.id}Kidnaps']} ({await statBuilder.getAltPercentage(db, db[f'{role.id}Played'] - db[f'{role.id}Kidnaps'], f'{role.id}Played')}%)'
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
            returnedEmbed.add_field(name = 'Wins Over Replacement Player (WORP)', value = await statBuilder.getRoleWORP(db, globalDB, role.id), inline=True)
            returnedEmbed.add_field(name = 'True Winning %', value = f'{await statBuilder.getRoleTW(db, globalDB, f'{role.id}Won', f'{role.id}Played')}%', inline = True)
        returnedEmbed.add_field(name = 'Sabotage Wins', value = f'{db[f'{role.id}Played'] - db[f'{role.id}Kidnaps']} ({await statBuilder.getAltPercentage(db, (db[f'{role.id}Played'] - db[f'{role.id}Kidnaps']), f'{role.id}Played')})% of Games')
        returnedEmbed.add_field(name = 'Made to Kidnap Phase', value = f'{db[f'{role.id}Kidnaps']} ({await statBuilder.getPercentage(db, f'{role.id}Kidnaps', f'{role.id}Played')}% of Games)', inline=True)
        returnedEmbed.add_field(name = 'Identified Coordinate', value= f'{db[f'{role.id}KidnapWins']} ({await statBuilder.getPercentage(db, f'{role.id}KidnapWins', f'{role.id}Kidnaps')}% of Kidnap Phases)', inline = True)
        if role.id == 'Pieck':
            returnedEmbed.add_field(name = 'Flip Accepts', value = db['PieckFlipAccepts'], inline=True)
            returnedEmbed.add_field(name = 'Flip Accept Wins', value = f'{db['PieckFlipAcceptWins']} ({await statBuilder.getPercentage(db, 'PieckFlipAcceptWins', 'PieckFlipAccepts')}% of Flips)', inline=True)
            returnedEmbed.add_field(name = 'Flip Rejects', value = db['PieckFlipRejects'], inline=True)
            returnedEmbed.add_field(name = 'Flip Reject Wins', value = f'{db['PieckFlipRejectWins']} ({await statBuilder.getPercentage(db, 'PieckFlipRejectWins', 'PieckFlipRejects')}% of Flips)', inline=True)
        elif role.id == 'Annie':
            returnedEmbed.add_field(name = 'Screams', value = f'{db['AnnieScreams']} ({await statBuilder.getPercentage(db, 'AnnieScreams', 'AnniePlayed')}% of Games)', inline=True)
        elif role.id == 'Porco':
            returnedEmbed.add_field(name = 'Gags', value = db['PorcoGags'], inline=True)
            returnedEmbed.add_field(name = f'Gag {currentTheme.commanderName} Skips', value = f'{db['PorcoCommanderSkips']} ({await statBuilder.getDivider(db, 'PorcoCommanderSkips', 'PorcoPlayed')} per Game, {await statBuilder.getDivider(db, 'PorcoCommanderSkips', 'PorcoGags')} per Gag)')
        elif role.id == 'Falco':
            returnedEmbed.add_field(name = 'Vote Intercepts', value = db['FalcoUses'], inline=True)
            returnedEmbed.add_field(name = 'Vote Intercept Passes', value = f'{db['FalcoVoteWins']} ({await statBuilder.getPercentage(db, 'FalcoVoteWins', 'FalcoUses')}% of Intercepts)', inline=True)
        elif role.id == 'Reiner':
            returnedEmbed.add_field(name = 'Armor Saves', value = f'{db['ReinerSaves']} ({await statBuilder.getDivider(db, 'ReinerSaves', 'ReinerPlayed')} per Game)')
        elif role.id == 'Bertholdt':
            returnedEmbed.add_field(name = f'{currentTheme.expeditionName} Cloaked', value = f'{db['BertholdtCloaks']} ({await statBuilder.getDivider(db, 'BertholdtCloaks', 'BertholdtPlayed')} per Game)', inline=True)
            returnedEmbed.add_field(name = f'{currentTheme.expeditionName} Doubles Cloaked', value = f'{db['BertholdtDoubleCloaks']} ({await statBuilder.getDivider(db, 'BertholdtDoubleCloaks', 'BertholdtCloaks')} per Cloak, {await statBuilder.getDivider(db, 'BertholdtDoubleCloaks', 'BertholdtPlayed')} per Game)')
        elif role.id == 'Gabi':
            returnedEmbed.add_field(name = 'Fires', value = f'{db['GabiFires']} ({await statBuilder.getDivider(db, 'GabiFires', 'GabiPlayed')} per Game)', inline=True)
            returnedEmbed.add_field(name = f'{currentTheme.soldierPlural} Fired Upon', value = f'{db['GabiFireWins']} ({await statBuilder.getPercentage(db, 'GabiFireWins', 'GabiFires')}% of Fires, {await statBuilder.getDivider(db, 'GabiFireWins', 'GabiPlayed')} per Game)', inline=True)
        elif role.id == 'Willy':
            returnedEmbed.add_field(name = f'{role.shortName} Deaths', value = f'{db['WillyDeaths']} ({await statBuilder.getPercentage(db, 'WillyDeaths', 'WillyPlayed')}% of Games)', inline=True)
            returnedEmbed.add_field(name = f'{role.shortName} Kills', value = f'{db['WillyKills']} ({await statBuilder.getPercentage(db, 'WillyKills', 'WillyPlayed')}% of Games, {await statBuilder.getPercentage(db, 'WillyKills', 'WillyDeaths')}% of Deaths)', inline=True)
        elif role.id == 'Yelena':
            returnedEmbed.add_field(name = f'{role.shortName} Vote Steals', value = f'{db['YelenaSteals']} ({await statBuilder.getPercentage(db, 'YelenaSteals', 'YelenaPlayed')}% of Games)', inline=True)
        elif role.id == 'Warhammer':
            returnedEmbed.add_field(name = f'{currentTheme.soldierSingle} Abilities Used', value = f'{db['WarhammerAbilities']} ({await statBuilder.getPercentage(db, 'WarhammerAbilities', 'WarhammerPlayed')}% of Games Played)')
        if type(role.emoji) == str:
            returnedEmbed.set_thumbnail(url = role.imageURL)
        else:
            returnedEmbed.set_thumbnail(url = role.emoji.url)
        returnedEmbed.set_footer(icon_url=thumbnail, text = f'{name} Stats')
        return returnedEmbed

    
    async def profileView(navigator, user, currentTheme, loadedRoles, color, loadedBadges):
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
                embed = await statBuilder.profileEmbed(currentTheme, user, loadedRoles, color, loadedBadges, 'Main')
                await interaction.message.edit(embed=embed)
                await interaction.response.defer()
        mainButton.callback = processMainButton
        returnedView.add_item(mainButton)

        soldierOverviewButton = Button(label = f'{currentTheme.soldierSingle} Overview', style=discord.ButtonStyle.grey, emoji = currentTheme.emojiSoldier)
        async def processSoldierOverviewButton(interaction):
            if interaction.user == navigator:
                embed = await statBuilder.profileEmbed(currentTheme, user, loadedRoles, color, loadedBadges, 'Soldier Overview')
                await interaction.message.edit(embed=embed)
                await interaction.response.defer()
        soldierOverviewButton.callback = processSoldierOverviewButton
        returnedView.add_item(soldierOverviewButton)

        soldierRoleButton = Button(label = f'{currentTheme.soldierSingle} Role Overview', style=discord.ButtonStyle.grey, emoji = str('🎭'))
        async def processSoldierRoleButton(interaction):
            if interaction.user == navigator:
                embed = await statBuilder.profileEmbed(currentTheme, user, loadedRoles, color, loadedBadges, 'Soldier Roles')
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
                    embed = await statBuilder.profileEmbed(currentTheme, user, loadedRoles, color, loadedBadges, {'Soldier Role': chosenRole})
                    await interaction.message.edit(embed=embed)
                    await interaction.response.defer()
        soldierSelect.callback = processSoldierSelect
        returnedView.add_item(soldierSelect) 

        warriorOverviewButton = Button(label = f'{currentTheme.warriorSingle} Overview', style=discord.ButtonStyle.grey, emoji = currentTheme.emojiWarrior)
        async def processWarriorOverviewButton(interaction):
            if interaction.user == navigator:
                embed = await statBuilder.profileEmbed(currentTheme, user, loadedRoles, color, loadedBadges, 'Warrior Overview')
                await interaction.message.edit(embed=embed)
                await interaction.response.defer()
        warriorOverviewButton.callback = processWarriorOverviewButton
        returnedView.add_item(warriorOverviewButton)

        warriorRoleButton = Button(label = f'{currentTheme.warriorSingle} Role Overview', style=discord.ButtonStyle.grey, emoji = str('🎭'))
        async def processWarriorRoleButton(interaction):
            if interaction.user == navigator:
                embed = await statBuilder.profileEmbed(currentTheme, user, loadedRoles, color, loadedBadges, 'Warrior Roles')
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
                    embed = await statBuilder.profileEmbed(currentTheme, user, loadedRoles, color, loadedBadges, {'Warrior Role' : chosenRole})
                    await interaction.message.edit(embed=embed)
                    await interaction.response.defer()
        warriorSelect.callback = processWarriorSelect
        returnedView.add_item(warriorSelect)

        return returnedView



    async def badgesEmbed(user, currentTheme, loadedBadges):
        thumbnailIMG = user.avatar.url

        db = databaseManager.getWvsPlayerByID(user.id)

        badgeStats = []
        for key, value in db['badges'].items():
            badgeStats.append(key)

        playerTotal = loadedBadges.getTotalBadgeOutput(db)

        description = f'Badge Points (BP): {playerTotal['points']}'

        if playerTotal['badge'] != 'Noob':
            description += f'\n{playerTotal['emoji']}Rank: {playerTotal['badge']} {playerTotal['progress']}'
        else:
            description += f'\nRank: {playerTotal['badge']} {playerTotal['progress']}'

        returnedEmbed = discord.Embed(title = f'{user.name}\'s Badges', description= f'**{description}**', color = playerTotal['color'])
        for badgeStat in badgeStats:
            if badgeStat == 'Rank':
                continue
            badgeOutput = loadedBadges.getBadgeOutput(badgeStat, db['stats'][f'{badgeStat}'])
            fieldName = f'{badgeOutput['title']} ({badgeOutput['progress']})'
            if badgeOutput['badge'] != 'No Badge Earned':
                fieldValue = f'{badgeOutput['emoji']} `{badgeOutput['badge']}` (+**{badgeOutput['points']}** BP)'
            else:
                fieldValue = f'`{badgeOutput['badge']}`'
            returnedEmbed.add_field(name=fieldName, value=fieldValue, inline=True)
        returnedEmbed.set_thumbnail(url = thumbnailIMG)
        return returnedEmbed
    
    async def leaderboardEmbed(client, homeServer, loadedBadges, currentTheme, statType, page):
        titles = {'LegacyPoints': 'Overall Leaderboard', 'WORP' : 'WORP Leaderboard', 'SoldierWORP' : 'Soldier WORP Leaderboard', 'WarriorWORP' : 'Warrior WORP Leaderboard', 'MVPS': 'MVP Leaderboard', 'BadgePoints' : 'Badge Point Leaderboard', 'ELO' : 'ELO Leaderboard', 'MostWins': 'Total Wins Leaderboard', 'Kills':'Kills Leaderboard', 'Deaths':'Deaths Leaderboard', 'MostKidnappable': 'Kidnapped as Coord Leaderboard', 'BiggestLoser':'Losses Leaderboard', 'MostKidnapWins':'Correct Kidnaps Leaderboard', 'SinaSmasher': 'Sabotage Wins Leaderboard'}

        scoredTitles = ['LegacyPoints', 'WORP', 'MVPS', 'BadgePoints', 'ELO', 'MostWins']

        startingIndex = (page * 10) - 10
        finalIndex = startingIndex + 9
        index = 0

        gatheredPlayers = []

        numberEmojis = [str('🥇'), str('🥈'), str('🥉'), str('4️⃣'), str('5️⃣'), str('6️⃣'), str('7️⃣'), str('8️⃣'), str('9️⃣'), str('🔟')]
        
        if type(statType) == str and statType in titles:
            if statType == 'LegacyPoints':
                allPlayers = databaseManager.getSortedLegacy()
            else:
                allPlayers = databaseManager.getSortedWvsPlayer(statType)
        else:
            if type(statType) == list:
                playerList = databaseManager.getSortedPoints('LegacyPoints')
                sorterDict = {}
                for player in playerList:
                    if statType[1] == '%':
                        sorterDict[player['userID']] = await statBuilder.getPercentage(player['stats'], statType[0], statType[2])
                    elif statType[1] == '/':
                        sorterDict[player['userID']] = await statBuilder.getDivider(player['stats'], statType[0], statType[2])
                    else:
                        sorterDict[player['userID']] = player['stats'][statType[0]] - player['stats'][statType[2]]
                allPlayers = []
                while len(sorterDict) > 0:
                    largestValue = None
                    for key, value in sorterDict.items():
                        if largestValue == None:
                            largestValue = {key: value}
                            continue
                        for key2, value2 in largestValue.items():
                            if value > value2:
                                largestValue = {key: value}
                                break
                    for key,value in largestValue.items():
                        allPlayers.append(databaseManager.getWvsPlayerByID(key))
                        del sorterDict[key]
            else:
                allPlayers = databaseManager.getSortedWvsStat(statType)
        for player in allPlayers:
            if index == 0:
                leader = player
            if index >= startingIndex and index <= finalIndex:
                gatheredPlayers.append(player)
            index += 1

        leader = databaseManager.searchForUser(client.get_user(leader['userID']))
        roleID = leader['roleID']
        role = homeServer.get_role(roleID)
        color = role.color
        if color == discord.Color.default():
            color = currentTheme.helpEmbedColor

        playerList = ''
        for player in gatheredPlayers:
            if page == 1:
                if gatheredPlayers.index(player) == 0 and statType in player['titles']:
                    playerList += f'{getattr(loadedBadges, f'emoji{statType}')}'
                else:
                    playerList += numberEmojis[gatheredPlayers.index(player)]
            else:
                playerList += f'{gatheredPlayers.index(player) + 1 + (10*(page-1))}. '
            user = client.get_user(player['userID'])
            if user != None:
                playerList += f'{user.mention}\n'
            else:
                playerList += f'<@{player['userID']}>\n'
        
        valueList = ''
        if type(statType) == str and 'Points' not in statType:
            for player in gatheredPlayers:
                if statType in titles:
                    valueList += f'{round(player['calcs'][statType], 1)}\n'
                else:
                    valueList += f'{player['stats'][statType]}\n'
        elif type(statType) == list:
            for player in gatheredPlayers:
                if statType[1] == '%':
                    valueList += f'{await statBuilder.getPercentage(player['stats'], statType[0], statType[2])}%\n'
                elif statType[1] == '/':
                    valueList += f'{await statBuilder.getDivider(player['stats'], statType[0], statType[2])}\n'
                else:
                    valueList += f'{player['stats'][statType[0]] - player['stats'][statType[2]]}\n'

        pointList = ''
        if type(statType) == str and statType in scoredTitles:
            for player in gatheredPlayers:
                pointList += f'{player['points'][statType]}\n'

        if type(statType) == str and statType in titles:
            title = titles[statType]
        elif type(statType) == str:
            title = f'{statType} Leaderboard'
        else:
            title = f'{statType[0]} {statType[1]} {statType[2]} Leaderboard'
        returnedEmbed = discord.Embed(title = title, color = color)
        returnedEmbed.add_field(name = 'Players', value=playerList, inline=True)
        if 'Points' not in statType:
            returnedEmbed.add_field(name = 'True Value', value = valueList, inline=True)
        if pointList != '':
            returnedEmbed.add_field(name = 'Legacy Points(LP)', value = pointList, inline=True)
        returnedEmbed.set_thumbnail(url = client.get_user(leader['userID']).avatar.url)
        return returnedEmbed
    
    async def leaderboardView(navigator, client, homeServer, loadedBadges, currentTheme, statType, page):
        returnedView = View()

        async def processChange(interaction, navigator, client, homeServer, loadedBadges, currentTheme, statType, page):
            if interaction.user == navigator:
                newView = await statBuilder.leaderboardView(navigator, client, homeServer, loadedBadges, currentTheme, statType, page)
                newEmbed = await statBuilder.leaderboardEmbed(client, homeServer, loadedBadges, currentTheme, statType, page)
                await interaction.message.edit(view = newView, embed=newEmbed)
                await interaction.response.defer()

        nameDict = {'LegacyPoints':'Main', 'WORP':'WORP', 'MostWins': 'Total Wins', 'ELO':'ELO', 'MVPS': 'MVP', 'BadgePoints':'Badges', 'SoldierWORP':'Soldier', 'WarriorWORP':'Warrior', 'Kills':'Kills', 'Deaths':'Deaths', 'MostKidnappable':'Kidnapped', 'BiggestLoser':'Losses', 'MostKidnapWins':'Coord Kidnapped', 'SinaSmasher': 'Sab Wins'}
        lbSelect = Select(placeholder = 'Change Leaderboard', max_values=1, min_values=1)
        for key, value in nameDict.items():
            lbSelect.add_option(label = f'{value} LB', emoji = getattr(loadedBadges, f'emoji{key}'))
        async def processLBSelection(interaction):
            if interaction.user == navigator:
                for key,value in nameDict.items():
                    if str(lbSelect.values[0]).split(' LB')[0] == value:
                        newLB = key
                        break
                await processChange(interaction, navigator, client, homeServer, loadedBadges, currentTheme, newLB, page)
        lbSelect.callback = processLBSelection
        returnedView.add_item(lbSelect)

        pageSelection = Select(placeholder= 'Select Page', min_values=1, max_values=1)
        
        allPlayers = databaseManager.getSortedPoints(statType)
        index = 0
        for player in allPlayers:
            index += 1
        pageLimit = math.ceil(index/10)
        index = 1
        while index <= pageLimit:
            pageSelection.add_option(label = f'{index}')
            index += 1

        async def processPageSelection(interaction):
            await processChange(interaction, navigator, client, homeServer, loadedBadges, currentTheme, statType, int(pageSelection.values[0]))
        pageSelection.callback = processPageSelection
        returnedView.add_item(pageSelection)

        return returnedView
    
    async def leaderboardAltView(navigator, client, homeServer, loadedBadges, currentTheme, statType, page):
        returnedView = View()

        pageSelection = Select(placeholder= 'Select Page', min_values=1, max_values=1)
        
        allPlayers = databaseManager.getSortedPoints(statType)
        index = 0
        for player in allPlayers:
            index += 1
        pageLimit = math.ceil(index/10)
        index = 1
        while index <= pageLimit:
            pageSelection.add_option(label = f'{index}')
            index += 1

        async def processPageSelection(interaction):
            if interaction.user == navigator:
                newView = await statBuilder.leaderboardAltView(navigator, client, homeServer, loadedBadges, currentTheme, statType, int(pageSelection.values[0]))
                newEmbed = await statBuilder.leaderboardEmbed(client, homeServer, loadedBadges, currentTheme, statType, int(pageSelection.values[0]))
                await interaction.message.edit(view=newView, embed=newEmbed)
                await interaction.response.defer()
        pageSelection.callback = processPageSelection
        returnedView.add_item(pageSelection)
        return returnedView
    
    async def advantageEmbed(currentGame, currentTheme):
        globalDB = databaseManager.getGlobal()['stats']
        soldierCalc = 0
        warriorCalc = 0
        for soldier in currentGame.soldiers:
            if globalDB[f'{soldier.role.id}Played'] == 0:
                soldierCalc += 0.5 / len(currentGame.soldiers)
            else:
                soldierCalc += (globalDB[f'{soldier.role.id}Won']/globalDB[f'{soldier.role.id}Played']/len(currentGame.soldiers))
        for warrior in currentGame.warriors:
            if globalDB[f'{warrior.role.id}Played'] == 0:
                warriorCalc += 0.5 / len(currentGame.warriors)
            else:
                warriorCalc += (globalDB[f'{warrior.role.id}Won']/globalDB[f'{warrior.role.id}Played']/len(currentGame.warriors))
        if soldierCalc == 0 and warriorCalc == 0:
            soldierCalc = 0.5
            warriorCalc = 0.5
        totalCalc = soldierCalc + warriorCalc

        if soldierCalc > warriorCalc:
            color = currentTheme.soldierColor
            msg = f'{currentTheme.emojiSoldier}{currentTheme.soldierPlural} with a {round(soldierCalc/totalCalc*100,1)}% Chance to Win{currentTheme.emojiSoldier}'
        elif warriorCalc > soldierCalc:
            color = currentTheme.warriorColor
            msg = f'{currentTheme.emojiWarrior}{currentTheme.warriorPlural} with a {round(warriorCalc/totalCalc*100,1)}% Chance to Win{currentTheme.emojiWarrior}'
        else:
            color = currentTheme.wildcardColor
            msg = f'⚖️Perfectly Balanced⚖️'
        returnedEmbed = discord.Embed(title = 'Advantage Calculation', color = color)
        returnedEmbed.add_field(name = f'{currentTheme.emojiSoldier}Average {currentTheme.soldierPlural} Win Percentage{currentTheme.emojiSoldier}', value = f'{round(soldierCalc*100, 1)}%', inline=False)
        returnedEmbed.add_field(name = f'{currentTheme.emojiWarrior}Average {currentTheme.warriorPlural} Win Percentage{currentTheme.emojiWarrior}', value = f'{round(warriorCalc*100, 1)}%', inline=False)
        returnedEmbed.add_field(name = 'Advantage', value = msg, inline=False)
        return returnedEmbed
    
    async def titlesEmbed(currentTheme, loadedBadges):
        returnedEmbed = discord.Embed(title = 'Possible Titles', color=currentTheme.helpEmbedColor)
        for key,value in loadedBadges.titleAnnouncements.items():
            fieldName = f'{getattr(loadedBadges, f'emoji{key}')}{value}'
            returnedEmbed.add_field(name = fieldName, value=f'Awarded to {loadedBadges.titleConditions[key]}', inline=True)
        return returnedEmbed




