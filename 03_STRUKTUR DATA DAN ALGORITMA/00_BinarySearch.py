myNumbers = [1, 4, 5, 8, 9]

def binSearch(list, item):
	low = 0
	high = len(list) - 1

	while low <= high:
		mid = (low + high) // 2
		guess = list[mid]
		if guess == item:
			return mid
		elif guess > item:
			high = mid-1
		elif guess < item:
			low = mid+1
	return None

print(binSearch(myNumbers, 5))
print(binSearch(myNumbers, 11))