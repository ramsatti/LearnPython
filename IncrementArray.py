aLength = input('Enter array length: ')
aLength = int(aLength)
array = []

for i in range(aLength):
    print ("Enter " + str(i) + ' numbers: ')
    value = int(input (''))
    array.append(value)

for i in range(len(array)):
    array[i] += 1

print(array)