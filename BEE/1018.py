money = int(input())
banknotes = [100, 50, 20, 10, 5, 2, 1]
print(money)
for banknote in banknotes:
	note = money // banknote
	money = money % banknote
	print(f"{note} nota(s) de R$ {banknote},00")