#Nesting: A list of dictionaries

alien_0 = {
    'color': 'grey',
    'points': 10
}
alien_1 = {
    'color': 'white',
    'points': 40
}
alien_2 = {
    'color': 'green',
    'points': 120
}

aliens = [alien_0, alien_1, alien_2]

for alien in aliens:
    print(alien)