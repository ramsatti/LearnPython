array = [3, 2, 1, 0]
anotherArray = []

print('Before Forloop: anotherArray = ', anotherArray)
for i in range(0, len(array)):
    print('In ForLoop: i = ', i)
    anotherArray.append(array[i-1])
print('Outside Forloop: anotherArray = ', anotherArray)
print(anotherArray)