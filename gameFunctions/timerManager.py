import asyncio
import discord
from discord.ext import commands

from gameFunctions.searchFunctions import searchFunctions

class timerManager:
    async def setTimer(currentGame, home, currentTheme, context, funcs=[]):
        timerVariables = await timerManager.getContext(currentGame, currentTheme, context)
        timerValue = timerVariables['timerValue']
        breakoutCondition = timerVariables['breakoutCondition']
        timerMessage = timerVariables['timerMessage']
        timeout = True
        args = []
        Onyankopon = await searchFunctions.roleIDToPlayer(currentGame, 'Onyankopon')
        if Onyankopon != None and Onyankopon.role.abilityActive:
            args.append(True)
        else:
            args.append(False)
        i = 0
        while i < timerValue:
            if currentGame.online == False:
                return 
            check = await breakoutCondition(currentGame, args)
            if check == True:
                timeout = False
            elif check == 'Plane':
                if currentGame.currentExpo.playerFlown is not None and currentGame.currentExpo.playerFlown != False and not currentGame.currentExpo.flownIn:
                    await funcs[0](currentGame)
                    i = 0
                else:
                    timeout = False
            if not timeout:
                break
            if (timerValue-i) == 600:
                await home.send(f'{currentTheme.timeoutCoreStart}**10 minutes**{currentTheme.timeoutCoreEnd}{timerMessage}')
            if (timerValue-i) == 300:
                await home.send(f'{currentTheme.timeoutCoreStart}**5 minutes**{currentTheme.timeoutCoreEnd}{timerMessage}')
            if (timerValue-i) == 120:
                await home.send(f'{currentTheme.timeoutCoreStart}**2 minutes**{currentTheme.timeoutCoreEnd}{timerMessage}')
            if (timerValue-i) == 60:
                await home.send(f'{currentTheme.timeoutCoreStart}**1 minute**{currentTheme.timeoutCoreEnd}{timerMessage}')
            if (timerValue-i) == 30:
                await home.send(f'{currentTheme.timeoutCoreStart}**30 seconds**{currentTheme.timeoutCoreEnd}{timerMessage}')
            await asyncio.sleep(1)
            i += 1
        return timeout

    async def getContext(currentGame, currentTheme, context):
        if context == 'Pick':
            timerValue = currentGame.currentRules.pickExpeditionTimer
            breakoutCondition = timerManager.pickWillBreakOut
            timerMessage = currentTheme.timeoutPick
        
        elif context == 'Vote':
            timerValue = currentGame.currentRules.voteExpeditionTimer
            breakoutCondition = timerManager.voteWillBreakOut
            if currentGame.currentExpo.pyxisTrial != None or (type(currentGame.currentExpo.warhammerActivated) == dict and 'Pyxis' in currentGame.currentExpo.warhammerActivated):
                timerMessage = currentTheme.timeoutExecution
            else:
                timerMessage = currentTheme.timeoutVote

        elif context == 'Scan':
            timerValue = currentGame.currentRules.voteExpeditionTimer
            breakoutCondition = timerManager.scanWillBreakOut
            timerMessage = currentTheme.timeoutScan

        elif context == 'Expo':
            timerValue = currentGame.currentRules.actExpeditionTimer
            breakoutCondition = timerManager.expoWillBreakOut
            timerMessage = currentTheme.timeoutExpo
        
        elif context == 'Kidnap':
            timerValue = currentGame.currentRules.kidnapTimer
            breakoutCondition = timerManager.kidnapWillBreakOut
            timerMessage = currentTheme.timeoutKidnap

        elif context == 'Multikidnap':
            timerValue = currentGame.currentRules.kidnapTimer
            breakoutCondition = timerManager.multiKidnapWillBreakout
            timerMessage = currentTheme.timeoutKidnap

        elif context == 'RumblingFight':
            timerValue = currentGame.currentRules.rumblingFightTimer
            breakoutCondition = timerManager.rumblingFightWillBreakout
            timerMessage = currentTheme.timeoutRumblingFight
        
        return {'timerValue' : timerValue, 'breakoutCondition' : breakoutCondition, 'timerMessage' : timerMessage}
    
    async def pickWillBreakOut(currentGame, args=[]):
        if len(currentGame.currentExpo.expeditionMembers) == currentGame.currentExpo.size or currentGame.currentExpo.passed or currentGame.currentExpo.erwinActivated or currentGame.currentExpo.kitzActivated or currentGame.currentExpo.warhammerActivated == 'Erwin' or (currentGame.porcoGagged == currentGame.currentExpo.commander and currentGame.currentExpo.erwinActivated == False) or (currentGame.currentExpo.commander not in currentGame.commanderOrder) or currentGame.currentExpo.pyxisTrial != None or (type(currentGame.currentExpo.warhammerActivated) == dict and 'Pyxis' in currentGame.currentExpo.warhammerActivated) or currentGame.exposOver:
            return True
        return False
    
    async def voteWillBreakOut(currentGame, args=[]):
        if len(currentGame.currentExpo.eligibleVoters) == len(currentGame.currentExpo.voted) or currentGame.exposOver:
            return True
        return False
    
    async def scanWillBreakOut(currentGame, args=[]):
        if len(currentGame.currentExpo.scanVoted) == len(currentGame.livingPlayers):
            return True
        return False
    
    async def expoWillBreakOut(currentGame, args=[False]):
        if args[0]:
            if currentGame.currentExpo.playerFlown is not None:
                return 'Plane'
        else:
            if len(currentGame.currentExpo.expeditioned) == len(currentGame.currentExpo.expeditionMembers) or currentGame.exposOver:
                return True
        return False
    
    async def kidnapWillBreakOut(currentGame, args=[]):
        if currentGame.kidnappedPlayer != None:
            return True
        return False
    
    async def multiKidnapWillBreakout(currentGame, args=[]):
        if len(currentGame.multikidnapRecord) == len(currentGame.warriors):
            return True
        return False
    
    async def rumblingFightWillBreakout(currentGame, args=[]):
        if currentGame.attackedPlayer != None:
            return True
        return False