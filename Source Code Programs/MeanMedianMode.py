def meanCalc():
    numAmount = int(input("How many numbers do you want to calculate the average of? "))
    storage = []

    for i in range(numAmount):
        num = float(input(f"Enter number {i+1}: "))
        storage.append(num)

    average = sum(storage) / numAmount

    print(f"You entered {numAmount} numbers.")
    print(f"The average of those {numAmount} numbers is {average}.")

    return average

def medianCalc():
    numbs = []
    n = int(input("How many numbers do you want to calculate the median for? "))

    for i in range(n):
        num = float(input("Enter number: "))
        numbs.append(num)

    numbs.sort()

    if n % 2 == 0:
        leftNum = numbs[n//2 - 1]
        rightNum = numbs[n//2]
        median = (leftNum + rightNum) / 2
    else:
        median = numbs[n//2]

    return median

def modeCalc():
    numbs = []
    n = int(input("How many numbers do you want to calculate the mode for? "))

    for i in range(n):
        num = float(input("Enter number: "))
        numbs.append(num)

    countDict = {}
    for num in numbs:
        if num in countDict:
            countDict[num] += 1
        else:
            countDict[num] = 1

    mode = max(countDict, key=countDict.get)
    return mode

question = input("Enter if you want to Calculate [Mean, Median, Mode]: ")
question = question.lower()

if question == 'mean':
    ans = meanCalc()
elif question == 'median':
    ans = medianCalc()
elif question == 'mode':
    ans = modeCalc()
else:
    print('Unknown or Misstyped')
    exit()

question = question.capitalize()
print(f'The {question} is {ans}')