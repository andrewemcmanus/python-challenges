# You'll need to use a couple of built in functions to alphabetize a string.
# Try to avoid looking up the exact answer and look at built in functions for
# lists and strings instead.

user_input = input("Give me a string to alphabetize:\n")

letters = list(user_input)
output = sorted(letters)
concat = ''.join(output)
print(concat)
