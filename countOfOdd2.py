# num = input('How many numbers? ')
# num = int(num)
# total = 0

# for count in range (num):
#     question = input ('Enter Numbers: ')
#     question = int(question)

#     if num % 2 != 0:
#         total = total + 1

# if total == 0:
#     print("There are no odd numbers.")
# else:
#     print("Count of odd numbers is: " + str(total))

n = input('How many numbers? ')
n = int(n)
countOfOddNumbers = 0

print ('Enter ', n, ' Numbers: ')

for i in range (n):  # i: 0, 1, ...., (n - 1)
    numI = input ('Enter num ' + str(i) + ': ')
    numI = int(numI)

    if numI % 2 != 0:
        countOfOddNumbers += 1

if countOfOddNumbers == 0:
    print("There are no odd numbers.")
else:
    print("Count of odd numbers is: " + str(countOfOddNumbers))