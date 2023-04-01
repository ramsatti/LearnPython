num = int(input('What Number do you want to Check? '))

def primeCheck(num):
    prime = True
    for i in range(2, num):
        if num % i == 0:
            prime = False
            print(num, 'is Composite!')
            break
    if prime == True:
        print(num, 'is Prime!')
        
primeCheck(num)