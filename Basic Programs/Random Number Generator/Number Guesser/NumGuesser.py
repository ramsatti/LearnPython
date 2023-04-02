import random
ranNum = random.randint (1, 100)
print ('I will give you a number from 1 - 100 and you have to guess it')


while True:
    num = input ('What number do you guess? ')
    num = int(num)

    if num == ranNum:
        print ('You are correct, great job!')
        break
    elif num > ranNum:
        print('Too high')
    elif num < ranNum:
        print('Too Low')
    else:
        print('Unknown or Incorrect')