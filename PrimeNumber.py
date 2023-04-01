num = int(input('What is the number? '))

for i in range(2, num):
    if num % i == 0:
        print(num, 'is Composite')
        break
    else:
        print(num, 'is Prime!')
        break