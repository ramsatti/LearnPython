# input:
n = 4
startingNum = 2
delta = 3
array = []
# ROutput: [2, 5, 8, 11]
# Output: [11, 8, 5, 2]

for i in range(n):
    array.append(startingNum)
    startingNum = startingNum + delta

for i in range(n-1, -1, -1):
    print(array[i], end='')
    if i > 0:
        print(',', end=' ')