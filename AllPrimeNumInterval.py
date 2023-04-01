lower = int(input("Please enter the lowest: "))
upper = int(input("Please enter the higher: "))
print("The prime numbers are: ")

i = lower
while i <= upper:
    if i > 1:
        prime = True
        j = 2
        while j < i:
            if i % j == 0:
                prime = False
                break
            j += 1
        if prime:
            print(i)
    i += 1