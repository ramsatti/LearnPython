howManyNum = input("How many Numbers should be printed? ")
howManyNum = int(howManyNum)
list = []

for x in range(howManyNum):
    question = input ('What is the number? ')
    list.append(question)
print(list)

for i in list: 
    print(i)

#input/output sample1

# How many numbers you wanna enter?
# 3
# Enter 3 numbers:
# 2
# 3
# 5
# Here are the numbers you have entered:
# 2
# 3
# 5


#input/output sample1

# How many numbers you wanna enter?
# 7
# Enter 7 numbers:
# 1
# 2
# 3
# 2
# 5
# 6
# 7
# You've entered: 1 2 3 2 5 6 7