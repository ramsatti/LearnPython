num = 54
total = 0

while num>0:
    remaining = num % 10
    num = num // 10
    total = total + remaining
    print('total = ', total,'num = ', num)
print(total)     