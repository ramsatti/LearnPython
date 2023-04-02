def harshardCheck(num):
    digitSum = sum(int(d) for d in str(num))
    return num % digitSum == 0

num = int(input('Type a number: '))
if harshardCheck(num):
    print(num, "is a Harshad Number!")
else:
    print(num, "is not a Harshad Number Unfortunately.")
