print ('We are going to Play Rock, Paper, Scissors')
rock = 'Rock'
paper = 'Paper'
scissors = 'Scissor'
handInput = input ('What do you choose? ' + rock + ', ' + paper + ', or ' + scissors + '? ')
rock = rock.lower()
paper = paper.lower()
scissors = scissors.lower()

#Random Rock, Paper, Scissors Generator
import random
handSigns = ['Rock', 'Paper', 'Scissors']
random_handSigns = random.choice (handSigns)

if handInput == rock and random_handSigns == 'Rock':
    print ('I chose Rock too. Tie.')
elif handInput == paper and random_handSigns == 'Rock':
    print ('I chose Rock which means... You won! Great job!.')
elif handInput == scissors and random_handSigns == 'Rock':
    print ('I chose Rock which means... You Lost. Try again!.')
elif handInput == rock and random_handSigns == 'Paper':
    print ('I chose Paper which means... You Lost. Try again!.')
elif handInput == paper and random_handSigns == 'Paper':
    print ('I chose Paper too. Tie.')
elif handInput == scissors and random_handSigns == 'Paper':
    print ('I chose Paper which means... You won! Great job!.')
elif handInput == rock and random_handSigns == 'Scissors':
    print ('I chose Scissors which means... You won! Great job!')
elif handInput == paper and random_handSigns == 'Scissors':
    print ('I chose Scissors which means... You Lost. Try again!')
elif handInput == scissors and random_handSigns == 'Scissors':
    print ('I chose Scissors too. Tie')
else:
    print ('Unknown or Typed Incorrectly.')