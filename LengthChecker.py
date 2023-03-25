num = int(input('How many numbers? '))
count = 0

for x in range(num):
    print('Type number ' + str(x) + ': ')
    int(x)
    value = input('')
    count = count + 1

print('You typed: ' + count)