def squareDigits(num):
    return sum(int(digit)**2 for digit in str(num))


def happyNumCheck(num):
    result = num
    while result != 1 and result != 4:
        result = squareDigits(result)
    return result == 1


for num in range(1, 101):
    if happyNumCheck(num):
        print(str(num), "is a Happy Number!")
    else:
        print(str(num), 'is not a Happy Number Unfortunately.')
