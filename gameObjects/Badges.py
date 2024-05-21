import discord

class Badges:

    def __init__(self, client):
        emojiBronze = 1212269518097752124
        emojiSilver = 1212269519771537498
        emojiGold = 1212269834713169951
        emojiPlatinum = 1212269993836810270
        emojiRuby = 1212271085366804551
        emojiSapphire = 1212271196452691998
        emojiEmerald = 1212271369484505148
        emojiAmethyst = 1212271546673004564
        emojiDiamond = 1212271848390402088
        emojiDarkmatter = 1212273594617303091

        self.emojiBronze = client.get_emoji(emojiBronze)
        self.emojiSilver = client.get_emoji(emojiSilver)
        self.emojiGold = client.get_emoji(emojiGold)
        self.emojiPlatinum = client.get_emoji(emojiPlatinum)
        self.emojiRuby = client.get_emoji(emojiRuby)
        self.emojiSapphire = client.get_emoji(emojiSapphire)
        self.emojiEmerald = client.get_emoji(emojiEmerald)
        self.emojiAmethyst = client.get_emoji(emojiAmethyst)
        self.emojiDiamond = client.get_emoji(emojiDiamond)
        self.emojiDarkmatter = client.get_emoji(emojiDarkmatter)

        self.emojiLegacyPoints = str('🐐')
        self.emojiWORP = str('👑')
        self.emojiSoldierWORP = str('🛡️')
        self.emojiWarriorWORP = str('⚔️')
        self.emojiMVPS = str('🏆')
        self.emojiBadgePoints =  str('💍')
        self.emojiKills = str('🔪')
        self.emojiDeaths = str('☠️')
        self.emojiMostKidnappable = str('😳')
        self.emojiBiggestLoser = str('🇱')
        self.emojiMostWins = str('🏅')
        self.emojiELO = str('🌠')
        self.emojiMostKidnapWins = str('🎯')
        self.emojiSinaSmasher = str('💥')

        self.titleAnnouncements = {'LegacyPoints':'GOAT', 'WORP':'Greatest Winner', 'MostWins': 'Most Wins', 'ELO':'ELO Champion', 'MVPS': 'True Most Valuable Player', 'BadgePoints': 'Most Decorated Player', 'SoldierWORP' : 'Greatest Soldier', 'WarriorWORP': 'Greatest Warrior', 'Kills': 'Most Bloodthirsty', 'Deaths': 'The Grim Reaper\'s Favorite', 'MostKidnappable': 'Most Kidnappable', 'BiggestLoser': 'Biggest Loser', 'MostKidnapWins': 'The Kidnapping Marksman', 'SinaSmasher': 'Sina Smasher'}
        self.titleConditions = {'LegacyPoints': 'Player with most Legacy Points', 'WORP': 'Player with most Total WORP', 'SoldierWORP' : 'Soldier with most WORP', 'WarriorWORP': 'Warrior with most WORP', 'MVPS':  'Player with most MVPs', 'BadgePoints': 'Player with most Badge Points', 'Kills' : 'Player with most Kills', 'Deaths' : 'Player with most Deaths', 'MostKidnappable': 'Coordinate that lost the most Kidnaps', 'BiggestLoser': 'Player with most Losses', 'MostWins': 'Player with most Wins', 'ELO': 'Player with highest ELO Score', 'MostKidnapWins' : 'Warrior with the most successful Kidnaps', 'SinaSmasher': 'Warrior with the most Sabotage Wins'}

        self.groupXL = ['PassesResponsible', 'BreaksResponsible']
        self.groupL = ['GamesWon']
        self.groupM = ['SoldiersWon', 'WarriorsWon']
        self.groupS = ['MVPS', 'WarriorsKidnapWins']

        self.boundsXL = [10, 25, 50, 100, 500, 1000, 2000, 3000, 4000, 5000]
        self.boundsL = [5, 10, 25, 50, 100, 200, 300, 500, 750, 1000]
        self.boundsM = [1, 5, 10, 25, 50, 100, 200, 300, 400, 500]
        self.boundsS = [1, 5, 10, 25, 50, 75, 100, 150, 200, 250]

        self.pointsBronze = 5
        self.pointsSilver = 10
        self.pointsGold = 15
        self.pointsPlatinum = 20
        self.pointsRuby = 35
        self.pointsSapphire = 50
        self.pointsEmerald = 65
        self.pointsAmethyst = 80
        self.pointsDiamond = 100
        self.pointsDarkmatter = 125

        self.totalTiers = [self.pointsBronze*8, self.pointsSilver*8, self.pointsGold*8, self.pointsPlatinum*8, self.pointsRuby*8, self.pointsSapphire*8, self.pointsEmerald*8, self.pointsAmethyst*8, self.pointsDiamond*8, self.pointsDarkmatter*8]

        self.colorNoBadges = discord.Color.default()
        self.colorBronze = discord.Color.from_str('0xce5b1e')
        self.colorSilver = discord.Color.light_grey()
        self.colorGold = discord.Color.gold()
        self.colorPlatinum = discord.Color.from_str('0xb1dbdb')
        self.colorRuby = discord.Color.dark_red()
        self.colorSapphire = discord.Color.dark_blue()
        self.colorEmerald = discord.Color.dark_green()
        self.colorAmethyst = discord.Color.dark_purple()
        self.colorDiamond = discord.Color.from_str('0xcdeeee')
        self.colorDarkmatter = discord.Color.from_str('0xd53bb2')


        self.tierNames = ['Bronze', 'Silver', 'Gold', 'Platinum', 'Ruby', 'Sapphire', 'Emerald', 'Amethyst', 'Diamond', 'Darkmatter']

        self.badgeTitles = {'PassesResponsible' : 'Passes Responsible for as Soldier', 'BreaksResponsible' : 'Breaks Responsible for as Warrior', 'GamesWon' : 'Games Won', 'SoldiersWon' : 'Games Won as Soldier', 'WarriorsWon' : 'Games Won as Warrior', 'MVPS' : 'MVPs Awarded', 'WarriorsKidnapWins' : 'Warriors Successfully Kidnapped Coordinate'}

    def getBadgeOutput(self, badgeType, score):
        if badgeType in self.groupXL:
            tiers = self.boundsXL
        elif badgeType in self.groupL:
            tiers = self.boundsL
        elif badgeType in self.groupM:
            tiers = self.boundsM
        else:
            tiers = self.boundsS
        index = -1
        for tier in tiers:
            if score >= tier:
                index += 1
            else:
                break
        if index == -1:
            points = 0
            emoji = None
            progress = f'{score}/{tiers[0]}'
            color = self.colorNoBadges
            badge = 'No Badge Earned'
        else:
            badge = self.tierNames[index]
            points = getattr(self, f'points{badge}')
            if badgeType == 'GamesWon':
                points *= 2
            emoji = getattr(self, f'emoji{badge}')
            color = getattr(self, f'color{badge}')
            if index == 9:
                progress = 'MASTERED'
            else:
                progress = f'{score}/{tiers[index+1]}'
        
        return {'points':points, 'emoji':emoji, 'progress':progress, 'badge':badge, 'color':color, 'title': self.badgeTitles[badgeType]}
    
    def getTotalBadgeOutput(self, db):
        badgeTypes = []
        for key, value in db['badges'].items():
            badgeTypes.append(key)
        
        runningTotal = 0
        for badgeType in badgeTypes:
            if badgeType == 'Rank':
                continue
            runningTotal += self.getBadgeOutput(badgeType, db['stats'][badgeType])['points']
        
        tierIndex = -1
        for tier in self.totalTiers:
            if runningTotal >= tier:
                tierIndex += 1
            else:
                break

        if tierIndex == -1:
            tier = 'Noob'
            emoji = None
            color = self.colorNoBadges
        
        else:
            tier = self.tierNames[tierIndex]
            emoji = getattr(self, f'emoji{tier}')
            color = getattr(self, f'color{tier}')

        if tierIndex == 9:
            progress = ' (MASTERED)'

        else:
            progress = f' (Progress to Next Rank: {runningTotal}/{self.totalTiers[tierIndex+1]})'

        return {'points': runningTotal, 'emoji' :emoji, 'progress':progress, 'badge':tier, 'color':color}
        