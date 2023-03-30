array1 = [1, 3, 4]
array2 = [6, 3, 9]
result = []

for i in range(0, len(array1)):
    result.append(array1[i] + array2[i])
    i = i + 1
print(result)