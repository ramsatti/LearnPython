n = int(input("How many numbers? "))
num = []
count = 0

for i in range(n):
    num.append(int(input('Enter ' + str(n) + ' numbers: ')))

for num in num:
    if num % 2 != 0:
        count += 1

if count == 0:
    print("There are no odd numbers.")
else:
    print("Count of odd numbers is:", count)
