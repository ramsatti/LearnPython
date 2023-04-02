def squareDigits(num):
    return sum(int(digit)**2 for digit in str(num))

def happyNumCheck(num):
    result = num
    while result != 1 and result != 4:
        result = squareDigits(result)
    return result == 1

num = int(input('Type a number: '))

if happyNumCheck(num):
    print(str(num) + " is a happy number")
else:
    print(str(num) + " is not a happy number")