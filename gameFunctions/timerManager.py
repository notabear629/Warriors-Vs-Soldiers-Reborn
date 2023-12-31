import asyncio
import discord
from discord.ext import commands

class timerManager:
    async def setTimer(currentGame, home, currentTheme, context):
        timerVariables = await timerManager.getContext(currentGame, currentTheme, context)
        timerValue = timerVariables['timerValue']
        breakoutCondition = timerVariables['breakoutCondition']
        timerMessage = timerVariables['timerMessage']
        timeout = True
        for i in range(timerValue):
            if currentGame.online == False:
                return 
            if await breakoutCondition(currentGame):
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
        return timeout

    async def getContext(currentGame, currentTheme, context):
        if context == 'Pick':
            timerValue = currentGame.currentRules.pickExpeditionTimer
            breakoutCondition = timerManager.pickWillBreakOut
            timerMessage = currentTheme.timeoutPick
        
        elif context == 'Vote':
            timerValue = currentGame.currentRules.voteExpeditionTimer
            breakoutCondition = timerManager.voteWillBreakOut
            timerMessage = currentTheme.timeoutVote
        
        elif context == 'Expo':
            timerValue = currentGame.currentRules.actExpeditionTimer
            breakoutCondition = timerManager.expoWillBreakOut
            timerMessage = currentTheme.timeoutExpo
        
        elif context == 'Kidnap':
            timerValue = currentGame.currentRules.kidnapTimer
            breakoutCondition = timerManager.kidnapWillBreakOut
            timerMessage = currentTheme.timeoutKidnap
        
        return {'timerValue' : timerValue, 'breakoutCondition' : breakoutCondition, 'timerMessage' : timerMessage}
    
    async def pickWillBreakOut(currentGame):
        if len(currentGame.currentExpo.expeditionMembers) == currentGame.currentExpo.size or currentGame.currentExpo.passed or currentGame.currentExpo.erwinActivated:
            return True
        return False
    
    async def voteWillBreakOut(currentGame):
        if len(currentGame.currentExpo.eligibleVoters) == len(currentGame.currentExpo.voted):
            return True
        return False
    
    async def expoWillBreakOut(currentGame):
        if len(currentGame.currentExpo.expeditioned) == len(currentGame.currentExpo.expeditionMembers):
            return True
        return False
    
    async def kidnapWillBreakOut(currentGame):
        if currentGame.kidnappedPlayer != None:
            return True
        return False