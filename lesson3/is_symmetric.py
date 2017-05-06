# A list is symmetric if the first row is the same as the first column,
# the second row is the same as the second column and so on. Write a
# procedure, symmetric, which takes a list as input, and returns the
# boolean True if the list is symmetric and False if it is not.

def is_symmetric(p):
    ''' <list> -> <Boolean>
    Takes a list, p, as input, and returns Boolean True if the list
    is symmetric, and False if it is not.
    '''
    zipped = zip(*p) # zip the list to compare
    count = 0 # create a variable to index
    for i in p:
        # check the rows and columns starting with the first ones,
        # and continue with the next.
        if i != list(zipped[count]):
            return False
        count += 1
    return True

#print is_symmetric([[1, 2, 3],
#                   [2, 3, 4],
#                   [3, 4, 1]])
#>>> True

#print symmetric([["cat", "dog", "fish"],
#                ["dog", "dog", "fish"],
#                ["fish", "fish", "cat"]])
#>>> True

#print symmetric([["cat", "dog", "fish"],
#                ["dog", "dog", "dog"],
#                ["fish","fish","cat"]])
#>>> False

#print symmetric([[1, 2],
#                [2, 1]])
#>>> True

#print symmetric([[1, 2, 3, 4],
#                [2, 3, 4, 5],
#                [3, 4, 5, 6]])
#>>> False

#print symmetric([[1,2,3],
#                 [2,3,1]])
#>>> False
