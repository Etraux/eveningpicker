#doing that evening planner thing

from random import choice
from jikanpy import Jikan

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
if mood == 'vidya' :
    vidya = choice(games)
    print('you\'ll play ' + vidya[0] + ' ' +vidya[2])
#but what about anime?
elif mood == 'animay':
    jikan1 = Jikan()
    animay = jikan1.search('anime', 'Jojo',
    parameters={
        'type': 'tv', 
        'min_score': '8',
        'max_score': '10', 
        'status': 'complete', 
        'limit': 5,
        })   
    for keys,values in animay.items():
        print(keys)
        print(values)