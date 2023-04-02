num = int(input('What is the number? '))
prime = True

for i in range(2, num):
    if num % i == 0:
        prime = False
        print(num, 'is Composite!')
        break

if prime == True: 
    print(num, 'is Prime')