import json

with open('dat.json', 'w') as jsfile:
    #json.dump(100, jsfile)
    #json.dump("Wow", jsfile)
    num = [3, 1, 2, 5, 6, 7, 8]
    json.dump(num, jsfile)
    #with json please, move data from numbers to file (dat.json)