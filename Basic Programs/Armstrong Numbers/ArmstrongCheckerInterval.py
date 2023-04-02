lower = int(input("Please enter the lowest: "))
upper = int(input("Please enter the higher: "))

def armStrongChecker(question):
    total = 0
    numDigits = len(str(question))
    orgNum = question
    while question > 0:
        remaining = question % 10
        total = total + remaining ** numDigits
        question = question // 10
    if total == orgNum:
        print(orgNum, "is an Armstrong number")
    else:
        print(orgNum, "is not an Armstrong number")

for i in range(lower, upper+1):
    armStrongChecker(i)