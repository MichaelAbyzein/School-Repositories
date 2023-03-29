
my_items = ['pen', 'drinking_bottle', 'books']

my_fav_items = my_items[0:2] # slicing string and list
# list[0]
# list[0:2] [start:stop:step]

print(my_items, "\n", my_fav_items)

#my_friend_items = my_items #alias : mereferensikan data
my_friend_items = my_items[:]

my_friend_items.append("ruler")
print(my_friend_items)

print(my_items)