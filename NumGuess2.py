#number == 89
#input == 78
#output == too Low
# input == 100
#output == your answer is too high
#input == 89
#output == That is Correct
import random
targetNumber = random.randint(1, 100)

while True:
    guess = input ('Guess The Target Number: ')
    guess = int (guess)
    if guess == targetNumber:
        print('That is Correct')
        break
    elif guess > targetNumber:
        print('Your Guess is too High')
    elif guess < targetNumber:
        print('Your Guess is too Low')
    else:
        print('Unknown or Misstyped')