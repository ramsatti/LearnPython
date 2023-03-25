# array = [1, 2, 3]
# anotherArray = []
# for i in range(0, len(array)):
# 	anotherArray.append(array[i-1])
# print(anotherArray)

array = [1,4,5,4]
array2 = [] #output 4

for i in range(0, len(array)):
    for j in range (i+1, len(array)):
        if array[i] == array[j]:
            print(j+1)