num = int(input('What is the number? '))
prime = True
i = 2

while i < num:
    if num % i == 0:
        prime = False
        print(num, 'is Composite!')
        break
    i += 1

if prime == True:
    print(num, 'is Prime!')