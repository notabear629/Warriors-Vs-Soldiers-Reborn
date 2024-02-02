from dataFunctions.databaseManager import databaseManager

from embedBuilder import embedBuilder

from discordViewBuilder import discordViewBuilder

from gameFunctions.timerManager import timerManager
from gameFunctions.webhookManager import webhookManager
from gameFunctions.searchFunctions import searchFunctions
from gameFunctions.endGameFunctions import endGameFunctions


import random
import asyncio

class rumblingFunctions:
    async def rumblingStart(currentGame, currentTheme, home, client, prefix):
        await home.send(currentTheme.allianceFormMessage)
        yeageristVictory = False
        while True:
            nextYeagerist = await rumblingFunctions.getNextYeagerist(currentGame)
            if nextYeagerist == False:
                await rumblingFunctions.processRumblingEnd('Alliance', currentGame, currentTheme, home)
                return
            if nextYeagerist == None:
                return
            else:
                while True:
                    nextAllianceMember = await rumblingFunctions.getNextAllianceMember(currentGame)
                    if nextAllianceMember == False:
                        await rumblingFunctions.processRumblingEnd('Yeagerists', currentGame, currentTheme, home)
                        return
                    else:
                        if yeageristVictory:
                            losingTeam = 'Alliance'
                        else:
                            losingTeam = 'Yeagerists'
                        yeageristVictory = await rumblingFunctions.yeageristFight(currentGame, currentTheme, home, client, nextYeagerist, nextAllianceMember, losingTeam, prefix)
                        if yeageristVictory != None:
                            embed = await embedBuilder.rumblingStatusEmbed(currentGame, currentTheme, currentGame.expoProjections)
                            await home.send(embed=embed)
                        if yeageristVictory:
                            continue
                        else:
                            break
                        

            
    async def getNextYeagerist(currentGame):
        for yeagerist in currentGame.yeageristFighters:
            if yeagerist in currentGame.livingYeagerists:
                return yeagerist
        return False
    
    async def getNextAllianceMember(currentGame):
        for allianceMember in currentGame.allianceFighters:
            if allianceMember in currentGame.livingAlliance:
                return allianceMember
        return False

    async def yeageristFight(currentGame, currentTheme, home, client, nextYeagerist, nextAllianceMember, newFighterCase, prefix):
        currentGame.setRumblingFight(nextYeagerist, nextAllianceMember)
        if newFighterCase == 'Yeagerists':
            if nextYeagerist.role.id == 'Eren':
                coreMsg = currentTheme.ErenInTheWay
            elif nextYeagerist.role.id == 'Zeke':
                coreMsg = currentTheme.ZekeInTheWay
            else:
                coreMsg = currentTheme.yeageristInTheWay
            await home.send(f'{coreMsg}\n\n**{nextYeagerist.role.emoji}{nextYeagerist.role.name} has Risen to Fight!{nextYeagerist.role.emoji}**')
        else:
            await home.send(currentTheme.allianceMemberSlain)
        await home.send(f'{nextYeagerist.user.mention},\n\n{currentTheme.newFightPrompt}\n\nUse `{prefix}attack @mention` to attack the {currentTheme.allianceSingle} you believe to be **{nextAllianceMember.role.emoji}{nextAllianceMember.role.name}{nextAllianceMember.role.emoji}**')
        timeout = await timerManager.setTimer(currentGame, home, currentTheme, 'RumblingFight')
        if timeout == None:
            return
        elif timeout:
            await home.send(f'{nextYeagerist.user.mention}, \n\nYou did not choose who to attack!\n\nBecause of your indecisiveness, you have been killed by **{nextAllianceMember.role.emoji}{nextAllianceMember.role.name}{nextAllianceMember.role.emoji}**')
            currentGame.rumblingKill(nextYeagerist, nextAllianceMember)
            currentGame.resetRumblingFight()
            return False
        else:
            if currentGame.attackedPlayer == nextAllianceMember:
                await home.send(f'{nextYeagerist.user.mention}, \n\n{nextYeagerist.role.emoji}You have chosen correctly!{nextYeagerist.role.emoji}\n\nYou have killed **{nextAllianceMember.role.emoji}{nextAllianceMember.role.name}{nextAllianceMember.role.emoji}**')
                currentGame.rumblingKill(nextAllianceMember, nextYeagerist)
                currentGame.resetRumblingFight()
                return True
            else:
                await home.send(f'{nextYeagerist.user.mention}, \n\n{nextAllianceMember.role.emoji}You did NOT choose correctly!{nextAllianceMember.role.emoji}\n\nYou have been killed by **{nextAllianceMember.role.emoji}{nextAllianceMember.role.name}{nextAllianceMember.role.emoji}**')
                currentGame.rumblingKill(nextYeagerist, nextAllianceMember)
                currentGame.resetRumblingFight()
                return False
            
    async def processRumblingEnd(winningTeam, currentGame, currentTheme, home):
        if winningTeam == 'Yeagerists':
            await rumblingFunctions.processYeageristVictory(currentGame, currentTheme, home)
        else:
            await rumblingFunctions.processAllianceVictory(currentGame, currentTheme, home)
        currentGame.setWinCondition(winningTeam)
        await endGameFunctions.processEndgame(currentGame, currentTheme, home)

            
    async def processYeageristVictory(currentGame, currentTheme, home):
        await home.send(f'{currentTheme.genericYeageristWin}')
        if currentGame.dominantYeagerist != False and currentGame.dominantYeagerist != None:
            if currentGame.dominantYeagerist.role.id == 'Floch':
                await home.send(f'{currentTheme.flochDominationWin}')
            elif currentGame.dominantYeagerist.role.id == 'Zeke':
                await home.send(f'{currentTheme.zekeDominationWin}')
            elif currentGame.dominantYeagerist.role.id == 'Eren':
                await home.send(f'{currentTheme.erenDominationWin}')
        else:
            await home.send(f'{currentTheme.standardYeageristWin}')

    async def processAllianceVictory(currentGame, currentTheme, home):
        await home.send(f'{currentTheme.genericAllianceWin}')
        if currentGame.allianceDomination:
            await home.send(f'{currentTheme.dominantAlliancewin}')
        else:
            await home.send(f'{currentTheme.standardAllianceWin}')

    async def attack(ctx, attackedUser, currentGame, currentTheme, home):
        if ctx.message.channel == home and currentGame.online and currentGame.fightingYeagerist != None:
            attackingUser = await searchFunctions.userToPlayer(currentGame, ctx.message.author)
            if attackingUser != currentGame.fightingYeagerist:
                await ctx.reply(f'Only **{currentGame.fightingYeagerist.role.emoji}{currentGame.fightingYeagerist.role.name}{currentGame.fightingYeagerist.role.emoji}** can make this decision!')
            else:
                attackedPlayer = await searchFunctions.userToPlayer(currentGame, attackedUser)
                if attackedPlayer == None:
                    await ctx.reply(f'You can only choose somebody playing the game!')
                else:
                    currentGame.attackPlayer(attackedPlayer)


        




        