#dictionary -> store data in to model a variety of real world object accurately.

alien = {'color': 'red', 'skill': 'wallclimbing'}

print(alien['color']) #key=value
print(alien['skill'])

#adding more inforamation
alien['pos_x'] = 30
alien['pos_y'] = 100
print(alien)

#start with empty dictionary
player = {}
player['username'] = "Senor"
player['points'] = -320
player['skill'] = 'gun'

#Modifying
player['username'] = "Snoer420"
player['points'] += 420

del player['skill']

houses = ["rowan", "jword", "redtrd"]

fav_item = {
    'ranwon' : 'clock',
    'yroda' : 'book',
    'ashley' : 'pen'
}

contact = (
    'rick' : '088374537182',
    'aktish' : '07743271282'
}

print(f"The player {player['username']} has {player['points']} point(s).")