# By Ashwath from forums
# Given a list of lists representing a n * n matrix as input, 
# define a  procedure that returns True if the input is an identity matrix 
# and False otherwise.

# An IDENTITY matrix is a square matrix in which all the elements 
# on the principal/main diagonal are 1 and all the elements outside 
# the principal diagonal are 0. 
# (A square matrix is a matrix in which the number of rows 
# is equal to the number of columns)

def is_identity_matrix(matrix):
    ''' <list> -> <Boolean>
    Takes a list, matrix, as input and returns True if the list
    is an identity list, and return False if it is not
    (An IDENTITY matrix is a square matrix in which all the elements 
    on the principal/main diagonal are 1 and all the elements outside 
    the principal diagonal are 0.
    '''
    for i in matrix:
        if len(matrix) != len(i): # if it is not a NxN square, return False
            return False
    for n in range(len(matrix)):
        for j in range(len(matrix)):
            if n == j: # if n equal to j, check if the element is 1, 
                if matrix[n][j] != 1: # if not, return False
                    return False
            elif matrix[n][j] != 0: # else, check if element is 0,
                return False        # if not, return False
    return True

'''

# Test Cases:

matrix1 = [[1,0,0,0],
           [0,1,0,0],
           [0,0,1,0],
           [0,0,0,1]]
print is_identity_matrix(matrix1)
#>>>True

matrix2 = [[1,0,0],
           [0,1,0],
           [0,0,0]]

print is_identity_matrix(matrix2)
#>>>False

matrix3 = [[2,0,0],
           [0,2,0],
           [0,0,2]]

print is_identity_matrix(matrix3)
#>>>False

matrix4 = [[1,0,0,0],
           [0,1,1,0],
           [0,0,0,1]]

print is_identity_matrix(matrix4)
#>>>False

matrix5 = [[1,0,0,0,0,0,0,0,0]]

print is_identity_matrix(matrix5)
#>>>False

matrix6 = [[1,0,0,0],  
           [0,1,0,1],  
           [0,0,1,0],  
           [0,0,0,1]]

print is_identity_matrix(matrix6)
#>>>False

matrix7 = [[1, -1, 1],
           [0, 1, 0],
           [0, 0, 1]]
print is_identity_matrix(matrix7)
#>>>False           
'''
           
