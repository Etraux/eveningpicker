#doing that evening planner thing

from random import choice
from random import randrange
import requests
import json
import time

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
    test = []
    page_url = f'https://api.jikan.moe/v4/random/anime'
    response = requests.get(page_url)
    json_data = json.loads(response.text)
    test.append(json_data)
    print (*test)
    