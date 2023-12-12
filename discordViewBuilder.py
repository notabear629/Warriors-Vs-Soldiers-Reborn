import discord
from discord.ext import commands
from discord import ui
from discord.ui import *

class discordViewBuilder:

    async def expeditionVoteView():
       returnedView = View()
       button1 = Button(label= 'fuck you')
       returnedView.add_item(button1)
       return returnedView