array = [2,8,14,13]
anotherArray = []
#array[0]= 2, array[1] = 8 array[2] = 14 array[3] = 13;  len(array)=4
#step1: append last element of array to anotherArray => anotherArray = [13]
anotherArray.append(array[len(array)-1])

#step2: append rest of elements of array to anotherArray => anotherArray = [13,2,8,14]
print(range(0,len(array)))
for i in range(len(array)-1):
    # print('[Line 10] i = ', i, "anotherArray= ", anotherArray)
    anotherArray.append(array[i])
    # print('[Line 12] i = ', i, "anotherArray=", anotherArray)

print(anotherArray)