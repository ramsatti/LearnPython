number = int(input("Which Number Table do you want to print? "))

def multiTable(number):
    print("The Multiplication Table of:", number)
    for count in range(1, 11):
        print(number, "x", count, "=", number * count)
multiTable(number)
