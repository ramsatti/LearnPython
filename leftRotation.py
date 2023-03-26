array = [1, 2, 3]
anotherArray = []
for i in range(0, len(array)):
	anotherArray.append(array[i-1])
print(anotherArray)