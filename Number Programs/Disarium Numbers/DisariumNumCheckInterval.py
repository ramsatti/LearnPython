def checkDisarium(num):
    total = 0
    for i in range(len(str(num))):
        total = total + int(str(num)[i])**(i+1)
    if total == num:
        return True
    else:
        return False

print("Disarium numbers between 1 and 100 are:")
for i in range(1, 101):
    if checkDisarium(i):
        print(i)