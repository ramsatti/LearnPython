startinNum = 0
delta = 2
n = 4

for i in range(n):
    print('#', i + 1, ':', startinNum, end='')
    if i < n - 1:
        print(', ', end=' ')
    startinNum += delta
