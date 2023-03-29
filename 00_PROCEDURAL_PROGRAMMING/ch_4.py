
pers_0 = {
    'Name': 'John',
    'Age': 21,
    'Hobby': "Watching Movie"
}
pers_1 = {
    'Name': 'Adam',
    'Age': 18,
    'Hobby': "Cycling"
}
pers_2 = {
    'Name': 'Sandra',
    'Age': 32,
    'Hobby': "Cooking"
}

persons = [pers_0, pers_1, pers_2]

for persdat in persons:
    print(f"Name: {persdat['Name']}")
    print(f"Age: {persdat['Age']}")
    print(f"Hobby: {persdat['Hobby']}")
    print()
    
cities = {
    'rome': {
        'landmark': "colosseum",
        'area': "1285"
    },
    'jakarta': {
        'landmark': "monas",
        'area': "661,5"
    }
}

for cityname, city_dat in cities.items():
    cityname = cityname.title()
    print(f"\nCities: {cityname}")
    area = city_dat['area']
    landmark = city_dat['landmark'].title()
    print(f"\tLandmark: {landmark}")
    print(f"\tArea: {area} km^2")
    
meds = {
    "paracetamol" : {
        "use" : ['relieve toothache', 'cure fever'],
        "sideeff" : ['stomach ache', 'rash'],
        "prize" : 1800
    },
    "naproxen" : {
        "use" : ['inflammation', 'relieve pain'],
        "sideeff" : ['nausea', 'drowsiness'],
        "prize" : 35000
    }
}

for med, data in meds.items():
    print(f"\n{med.title()}:")
    
    for a_data, info in data.items():
        print(f"\t{a_data}:")
        if type(info) == list:
            for obj in info:
                print(f"\t\t- {obj.title()}")
        else:
            print(f"\t\t{info}")
                
    print()