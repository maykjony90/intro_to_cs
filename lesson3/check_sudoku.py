# THREE GOLD STARS

# Sudoku [http://en.wikipedia.org/wiki/Sudoku]
# is a logic puzzle where a game
# is defined by a partially filled
# 9 x 9 square of digits where each square
# contains one of the digits 1,2,3,4,5,6,7,8,9.
# For this question we will generalize
# and simplify the game.

# Define a procedure, check_sudoku,
# that takes as input a square list
# of lists representing an n x n
# sudoku puzzle solution and returns the boolean
# True if the input is a valid
# sudoku square and returns the boolean False
# otherwise.

# A valid sudoku square satisfies these
# two properties:

#   1. Each column of the square contains
#       each of the whole numbers from 1 to n exactly once.

#   2. Each row of the square contains each
#       of the whole numbers from 1 to n exactly once.

# You may assume the the input is square and contains at
# least one row and column.

correct = [[1,2,3],
           [2,3,1],
           [3,1,2]]

incorrect = [[1,2,3,4],
             [2,3,1,3],
             [3,1,2,3],
             [4,4,4,4]]

incorrect2 = [[1,2,3,4],
             [2,3,1,4],
             [4,1,2,3],
             [3,4,1,2]]

incorrect3 = [[1,2,3,4,5],
              [2,3,1,5,6],
              [4,5,2,1,3],
              [3,4,5,2,1],
              [5,6,4,3,2]]

incorrect4 = [['a','b','c'],
              ['b','c','a'],
              ['c','a','b']]

incorrect5 = [ [1, 1.5],
               [1.5, 1]]
               
def check_sudoku(p):
    # iterate each element in the input list 
    for i in p:
        # check if all the child elements of the elements  
        # in the input list match
        if set(i) != set(p[0]):
            return False
            
        # If an element occures more than once, return false
        if p.count(i) > 1:
            return False
        
        # iterate each element of the main elements in the list
        for e in i:
            # if an element is less than 1 or is not a whole number
            # return false
            if (e < 1) or (isinstance(e, int) == False):
                return False
            # if an element of an elements in the list
            # occures more than once, return false
            if i.count(e) > 1:
                return False
                
            # if max value of the child list is bigger than 
            # length of the list, return false.
            if max(i) > len(i):
                return False
        
        # check if elements in the columns are repeated, return false        
        counter = counter_child = -len(p)
        while counter < 0:
            if p[counter][counter_child] != p[counter+1][counter_child]:
                while counter_child < 0:
                    # check each element of the possibles columns
                    # if there are elements with the same value. return false
                    if p[counter][counter_child] != p[counter+1][counter_child]:
                        counter_child += 1
                    else:
                        return False
                counter += 1
                counter_child = -len(p)
            
            # if input list has only one element that contains
            # one element, return True
            elif p.count(i) == 1:
                return True
            else:
                return False
    # if all cases are passed, return true
    return True
    
    
#print check_sudoku(incorrect)
#>>> False

print check_sudoku(correct)
#>>> True

print check_sudoku(incorrect2)
#>>> False

print check_sudoku(incorrect3)
#>>> False

print check_sudoku(incorrect4)
#>>> False

print check_sudoku(incorrect5)
#>>> False


