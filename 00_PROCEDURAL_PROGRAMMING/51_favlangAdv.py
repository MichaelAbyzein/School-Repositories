
favorite_languange = {
    'jen': ['python', 'javascript'],
    'sarah': ['c'],
    'edward' : ['go', 'typescript'],
    'billie' : ['python', 'haskel']
 }
 
for name, languages in favorite_languange.items():
    print(f"{name.title()}'s favorite languages are :")
    
    for language in languages:
        print(f"\t{language.upper()}")