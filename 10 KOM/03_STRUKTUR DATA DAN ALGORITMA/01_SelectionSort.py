def find_greatest(list):
	largeval = list[0]
	largeind = 0

	for i in range(1, len(list)):
		if list[i] > largeval:
			largeval = list[i]
			largeind = i

	return largeind


def selectsort(list):
	new_list = []
	for i in range (len(list)):
		great_index = find_greatest(list)
		new_list.append(list.pop(great_index))
	return new_list	

numList = [10, 4, 8, 6, 9, 2]
print(selectsort(numList))

#selection_sort(list, "asc")
#punya fitur asc dan desc, dan punya default sort		