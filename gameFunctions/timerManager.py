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
            if currentGame.deleted:
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
        return {'timerValue' : timerValue, 'breakoutCondition' : timerManager.pickWillBreakOut}
    
    async def pickWillBreakOut(currentGame):
        if len(currentGame.currentExpo.expeditionMembers) == currentGame.currentExpo.size or currentGame.currentExpo.passed:
            return True
        return False