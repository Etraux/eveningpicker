#doing that evening planner thing

from random import choice

#do the list
#games = ['FFXIV', 'Tekken', 'GGST', 'Pathfinder', 'SFV', 'Rimworld', 'Hunt: Showdown']
#we're gonna need a bigger list
games = [['FFXIV', 'mumorpeger', 'Tank'],
    ['FFXIV', 'mumorpeger', 'deeps'],
    ['FFXIV', 'mumorpeger', 'healslut'],
    ['Tekken', 'Fightan', 'Leo'],
    ['Tekken', 'Fightan', 'Armor King'],
    ['GGST', 'Fightan', 'Sol'],
    ['GGST', 'Fightan', 'Ky'],
    ['GGST', 'Fightan', 'Gio'],
    ['Pathfinder', 'CRPG', 'Continue'],
    ['SFV', 'Fightan', 'Ken'],
    ['SFV', 'Fightan', 'Ed'],
    ['Rimworld', 'Chill', 'Continue'],
    ['Kenshi', 'CRPG', 'Continue'],
    ['Hunt', 'Dakka', 'Meta'],
    ['Hunt', 'Dakka', 'Cheapo']]

#but what if i'm not THAT indecisive?
print('any preferences?')
mood = input()

#print a random game
nah = choice(games)
print('you\'ll play ' + nah[0] + ' ' +nah[2])
