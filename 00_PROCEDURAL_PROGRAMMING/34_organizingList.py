

cars = ["bmw", "audi", "toyota", "subaru"]

#Sorting
cars.sort()
print(cars)

cars.sort(reverse=True)
print(cars)

print(sorted(cars)) #temporary sorted list


#Searching
item = "toyota"
index_item = cars.index(item)
print(index_item)

isExist = item in cars # True
print(isExist)

item = "datsun"

if item in cars:
    index = cars.index(item)
    print(index)
else:
    print(f"{item} does not exist")
    

#Number of items in list
full_name = "Derren Rizandi" #str
print(len(full_name))

print(len(cars))
