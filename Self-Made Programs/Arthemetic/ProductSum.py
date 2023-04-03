howManyNum = input("How many Numbers? ")
howManyNum = int(howManyNum)
productOfEven = 1
sumOfOdd = 0

for x in range(howManyNum):
    num = int(input('What number? '))

    if num % 2 == 0:
        productOfEven = productOfEven * num
    elif num % 2 != 0:
        sumOfOdd = sumOfOdd + num
    else:
        print('Unknown')
        
if sumOfOdd == 0:
    print('No odd numbers entered')
else:
    print('Odd numbers Sum: ' + str(sumOfOdd))
    
if productOfEven == 1:
    print('No even numbers entered')
else:
    print('Even numbers Product: ' + str(productOfEven))