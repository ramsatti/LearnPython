# input: startinNum = 0, delta = 2, n = 4
# output: 0,2,4,6
startinNum = 0  # int(input('What number do you want to start with? '))
delta = 2  # int(input('What is the difference? '))
n = 4  # (input('What is the ending number? '))

for i in range(n):
    print('#', i + 1, ':', startinNum, end=', ')
    if i < n - 1:
        print(',', end=' ')
    startinNum = startinNum + delta