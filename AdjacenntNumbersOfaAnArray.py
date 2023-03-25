aLength = input('Enter array length: ')
aLength = int(aLength)
array = []  # [4, 1, 7] 
otherArray = [] #[5, 8]

for i in range(aLength):
    print("Enter " + str(i) + ' numbers: ')
    value = int(input(''))
    array.append(value)

for i in range(0, len(array)-1):  # (0, 2) => i = 0, 1
    otherArray.append(array[i]+array[i+1])
    print("i=", i, ";otherArray[i]=", otherArray[i])
   
# otherNum = False
# for x in array:
#     if otherNum == False:
#         otherNum = x
#     else:
#         otherArray.append(otherNum+x)
#         otherNum = x
print(otherArray)
