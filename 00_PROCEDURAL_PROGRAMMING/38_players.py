
players = ["Alex", "Hans", "Robert"]

for player in players:
    print(player)
    
foods = ["Muffins", "Dregnout", "Pizza"]
for food in foods:
    print(food)
    
for number in range(2, 21, 2): #start, stop, step
    print(number, end=" ")
print()

#nested for
for i in range(1, 11):
    for j in range(1, 11):
        print("*", end=" ")
    print()