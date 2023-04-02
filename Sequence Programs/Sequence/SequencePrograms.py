#input: startinNum = 0, delta = 2, endingNum = 10
#output 0,2,4,6,8,10
startinNum = 0#int(input('What number do you want to start with? '))
delta = 2#int(input('What is the difference? '))
endinNum = 10#int(input('What is the ending number? '))

for i in range(startinNum, endinNum, delta):
    print(i, end=' ')