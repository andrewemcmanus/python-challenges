# Python offers several ways to reverse a String. This is a classic thing
# that lots of people want to do. It's probably easy to look up this
# answer on Stack Overflow.
#
# This website of 30 Python Tips and Tricks also happens to point out
# several ways to reverse a string, and it's a good read!
#
# http://www.techbeamers.com/essential-python-tips-tricks-programmers/?utm_source=mybridge&utm_medium=blog&utm_campaign=read_more#tip1

user_input = input('What string would you like to reverse? ')

def reverse_for_loop(s):
    s1 = ''
    for c in s:
        s1 = c + s1
    return s1

if __name__ == '__main__':
    print(reverse_for_loop(user_input))
