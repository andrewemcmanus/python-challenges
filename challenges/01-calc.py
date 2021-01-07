# Use the `input()` function to prompt a user to enter something.
# input() always returns a string value. If you ever want someone
# to enter a number you have to use the `int()` function to convert
# what they typed in to a string.

user_function = input('What calculation would you like to do? (add, sub, mult, div) ')
number1 = input('What is number 1? ')
number2 = input('What is number 2? ')
int1 = float(number1)
int2 = float(number2)

def operator(function, a, b):
    if function == 'add':
        result = a + b
        return str(result)
    elif function == 'sub':
        result = a - b
        return str(result)
    elif function == 'mult':
        result = a * b
        return str(result)
    elif function == 'div':
        result = a / b
        return str(result)
    else:
        return 'error'

print('Your result is ' + operator(user_function, int1, int2))
