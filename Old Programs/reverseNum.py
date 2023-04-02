a = 947
reverse = 0
while a > 0:
    lastDigit = a % 10
    a = a // 10
    reverse = reverse * 10 + lastDigit
    print(a,lastDigit,reverse)
print(reverse)