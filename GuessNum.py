while True:
    import random
    numGuess = random.randint(1, 10)
    guess = int(input('Guess a number between 1 - 10: '))


    if guess == numGuess:
        print('Congratulations, That is correct!')
        break
    elif guess > numGuess:
        print('Too High')
    elif guess < numGuess:
        print('Too Low')