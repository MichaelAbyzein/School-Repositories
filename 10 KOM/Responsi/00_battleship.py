lists = [ [0, 1, 2], [3, 4, 5]]
for list in lists:
	for item in list:
		print(item, end=" ")
	print()

"""
texts = []
text = "X" * 3
for i in range(3):
	texts.append(text)
"""

texts = [ "X" * 3 for i in range(3)]

#print(texts)
"""
texts = ["XXX", "XXX", "XXX"]
for text in texts:
	for char in text:
		print(char, end=" ")
	print()
"""
for text in texts:
	print(" ".join(text))
