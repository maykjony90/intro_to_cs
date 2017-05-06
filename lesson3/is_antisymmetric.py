# By Dimitris_GR from forums
# Modify Problem Set 31's (Optional) Symmetric Square to return True 
# if the given square is antisymmetric and False otherwise. 
# An nxn square is called antisymmetric if A[i][j]=-A[j][i] 
# for each i=0,1,...,n-1 and for each j=0,1,...,n-1.

def antisymmetric(A):
    ''' <list> -> <Boolean>
    Takes a list, A, as input and returns Boolean True if the list
    is antisymmetric(An nxn square is called antisymmetric if A[i][j]=-A[j][i] 
    for each i=0,1,...,n-1 and for each j=0,1,...,n-1.),
    and False if it is not.
    '''
    if A == []: # if it is an empty list, return False
        return False
    for i in A:
        if len(A) != len(i): # if it is not a NxN square, return False
            return False
        for e in i:
            if isinstance(e, str): # if there is a string in list, return False
                return False
    for count_row in range(len(A)):
        for count_col in range(len(A)):
            if A[count_row][count_col] != -A[count_col][count_row]:
                return False
    return True

'''
# Test Cases:

print antisymmetric([[0, 1, 2], 
                     [-1, 0, 3], 
                     [-2, -3, 0]])   
#>>> True

print antisymmetric([[0, 0, 0],
                     [0, 0, 0],
                     [0, 0, 0]])
#>>> True

print antisymmetric([[0, 1, 2], 
                     [-1, 0, -2], 
                     [2, 2,  3]])
#>>> False

print antisymmetric([[1, 2, 5],
                     [0, 1, -9],
                     [0, 0, 1]])
#>>> False

print antisymmetric([])

print antisymmetric([[0, 1], 
                     [-1, 0]])

'''
