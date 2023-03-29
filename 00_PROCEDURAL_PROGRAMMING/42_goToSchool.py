
hadShower = True
hasBackpack = True
#or

hasMeal = False
hasMoney = True
#or

sunday = False

shouldGoToSchool = not sunday and (hadShower and hasBackpack and hasMeal or hasMoney)
#True and True and False

print(shouldGoToSchool)