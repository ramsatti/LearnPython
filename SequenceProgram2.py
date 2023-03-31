#input: startinNum = 0, delta = 2, n = 4
#output 0,2,4,6
startinNum = int(input('What number do you want to start with? '))
delta = int(input('What is the difference? '))
n = int(input('What is the ending number? '))

for i in range(n):
    startinNum = startinNum + delta
    print(startinNum)