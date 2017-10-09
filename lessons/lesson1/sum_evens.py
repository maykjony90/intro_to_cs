# Define a procedure, sum_evens, that takes
# as an argument a list of numbers, and returns
# the sum of all the even integers from the list
#
# For example,
# sum_evens([1, 2, 3, 4, 5]) = 6
# sum_evens([7, 21, -9]) = 0
# sum_evens([0.5, 4]) = 4

def sum_evens(number_list):
    '''(list of numbers) -> (list of int(s))
    Check if the numbers in number_list are integers and
    then return the sum of the even numbers.

    >>> sum_evens([1, 2, 3, 4, 5])
    >>> 6
    >>> sum_evens([7, 21, -9])
    >>> 0
    >>> sum_evens([0.5, 4])
    >>> 4
    '''
    total = 0
    for n in number_list:
        if (n == int(n)) and (n % 2 == 0):
            total += n
    return total
        
