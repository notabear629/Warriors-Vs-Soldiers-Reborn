import asyncio
import discord
from discord.ext import commands

class timerManager:
    async def setTimer(currentGame, context):
        timerVariables = await timerManager.getContext(currentGame, context)
        timerValue = timerVariables['timerValue']
        breakoutCondition = timerVariables['breakoutCondition']
        timeout = True
        for i in range(timerValue):
            if currentGame.online == False:
                return 
            if await breakoutCondition(currentGame):
                timeout = False
            if not timeout:
                break
            await asyncio.sleep(1)
        return timeout

    async def getContext(currentGame, context):
        if context == 'Pick':
            timerValue = currentGame.currentRules.pickExpeditionTimer
            breakoutCondition = timerManager.pickWillBreakOut
        
        elif context == 'Vote':
            timerValue = currentGame.currentRules.voteExpeditionTimer
            breakoutCondition = timerManager.voteWillBreakOut
        
        elif context == 'Expo':
            timerValue = currentGame.currentRules.actExpeditionTimer
            breakoutCondition = timerManager.expoWillBreakOut
        
        elif context == 'Kidnap':
            timerValue = currentGame.currentRules.kidnapTimer
            breakoutCondition = timerManager.kidnapWillBreakOut
        
        return {'timerValue' : timerValue, 'breakoutCondition' : breakoutCondition}
    
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