def primeCheck(num):
    prime = True
    for i in range(2, num):
        if num % i == 0:
            prime = False
            print(num, 'is Composite!')
            break
    if prime == True:
        print(num, 'is Prime!')

lower = int(input("Please enter the lowest: "))
upper = int(input("Please enter the higher: "))
print("The prime numbers are: ")

i = lower
while i <= upper:
    primeCheck(i)
    i += 1