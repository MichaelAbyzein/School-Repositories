
def describe_pet(pet_name, animal_type="Dog"):
    print(f"\nI have a {animal_type}")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet('harry', 'hamster')
describe_pet(pet_name='molly', animal_type='pig')
describe_pet('willie')

#.upper(), .lower(), .title() # Method Default dari Ob. Str
#Equivalent Function


describe_pet('adolf', 'wolf')
describe_pet(animal_type= 'wolf', pet_name='adolf')
describe_pet(pet_name='adolf', animal_type='wolf')
