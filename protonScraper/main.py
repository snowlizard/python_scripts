import csv, json

arrays = []

with open('proton.txt') as tsv:
    for line in csv.reader(tsv, dialect='excel-tab'):
        arrays.append(line)

gamesDict = {}

for game in arrays:
    for x in range(len(game) -1 ):
        gamesDict[game[0]] = game[1]

games = open('protondb.json', 'w')
games.write(json.dumps(gamesDict, indent=4, sort_keys=True))
games.close()
