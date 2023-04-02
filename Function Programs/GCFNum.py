def GCD(num1, num2):
    while num1 % num2 != 0:
        r = num1 % num2
        num1 = num2
        num2 = r
    return num2

num1 = int(input('Enter Number 1: '))
num2 = int(input('Enter Number 2: '))

gcd = GCD(num1, num2)
print('The GCD is', gcd)