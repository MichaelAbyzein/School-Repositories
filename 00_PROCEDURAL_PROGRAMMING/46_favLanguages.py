favorite_lang = {
    'louis' : 'italian',
    'cody' : 'spanish',
    'andrew' : 'english',
    'anna' : 'russian',
    'joseph' : 'english'
}
#lists, dict, dict_keys, dict_values, tuple, set
#print(list(favorite_lang.keys()))
#print(tuple(favorite_lang.values()))

rgb_color = (255, 255, 255) #rgb
position = (100, 200) #xy
screen_size = (1280, 860)


#for name, lang in favorite_lang.items():
    #print(f"{name.title()}'s favorite language is {lang.title()}.")

for name in sorted(favorite_lang.keys()):
    print(f"{name.title()}, thank you for taking the poll.")

print("The Following language have been mentioned: ")

for lang in sorted(set(favorite_lang.values())):
    print(lang)