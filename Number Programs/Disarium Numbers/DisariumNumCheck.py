def checkDisarium(num):
    total = 0
    for i in range(len(str(num))):
        total = total + int(str(num)[i])**(i+1)
    if total == num:
        return True
    else:
        return False

num = input('Type a number: ')
if checkDisarium(num):
    print(num, 'is a Disarium Number.')
else:
    print(num, 'is Not a Disarium Number Unfortunately.')