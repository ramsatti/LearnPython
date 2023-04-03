print('This is a Calculator')
add = "Add"
subtract = "Subtract"
multiply = "Multiply"
divide = "Divide"

question = input('Do you want to ' + add + ', ' + subtract +
                 ', ' + multiply + ', or ' + divide + ': ')
num1 = int(input('First Number: '))
num2 = int(input('Second Number: '))

add = add.lower()
subtract = subtract.lower()
multiply = multiply.lower()
divide = divide.lower()

if question == add:
    print(num1 + num2)
elif question == subtract:
    print(num1 - num2)
elif question == multiply:
    print(num1 * num2)
elif question == divide:
    print(num1 / num2)
else:
    print(' Unknown or Misspelled')
