num = 54
product = 1

while num > 0:
    remaining = num % 10
    num = num // 10
    product = product * remaining
    print('product = ', product,'num = ', num)
print(product)  