# Define a procedure is_palindrome, that takes as input a string, and returns a
# Boolean indicating if the input string is a palindrome.

# Base Case: '' => True
# Recursive Case: if first and last characters don't match => False
# if they do match, is the middle a palindrome?

def is_palindrome(s):
    if s == '':
        return True
    elif s[0] != s[-1]:
        return False
    else:
        return is_palindrome(s.strip([0]))


# Udacity's answer:

def uda_is_palindrome(s):
    if s == '':
        return True
    else:
        if s[0] == s[1]:
            return is_palindrome(s[1:-1])


# Iterative way of solving the same problem:
def iter_palindrome(s):
    for in range(0, len(s) / 2):
        if s[i] != s[-(i + 1)]:
            return False
    return True


# print is_palindrome('')
# >>> True
# print is_palindrome('abab')
# >>> False
# print is_palindrome('abba')
# >>> True
