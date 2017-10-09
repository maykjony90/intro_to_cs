#########################################################################
#                 10-row School abacus
#                         by
#                      Michael H
#########################################################################
#       Description partially extracted from from wikipedia 
#
#  Around the world, abaci have been used in pre-schools and elementary
#
# In Western countries, a bead frame similar to the Russian abacus but
# with straight wires and a vertical frame has been common (see image).
# Helps schools as an aid in teaching the numeral system and arithmetic
#
#         |00000*****   |     row factor 1000000000
#         |00000*****   |     row factor 100000000
#         |00000*****   |     row factor 10000000 
#         |00000*****   |     row factor 1000000
#         |00000*****   |     row factor 100000
#         |00000*****   |     row factor 10000
#         |00000*****   |     row factor 1000
#         |00000****   *|     row factor 100     * 1
#         |00000***   **|     row factor 10      * 2
#         |00000**   ***|     row factor 1       * 3
#                                        -----------    
#                             Sum                123 
#
# Each row represents a different row factor, starting with x1 at the
# bottom, ascending up to x1000000000 at the top row.     
######################################################################

# TASK:
# Define a procedure print_abacus(integer) that takes a positive integer
# and prints a visual representation (image) of an abacus setup for a 
# given positive integer value.
abacus = '|00000*****|'

def print_abacus(v):
    ''' <int> -> <str>
    Takes an integer as an input and returns its value on
    row abacus(functions between 1 - 10^9 digits)
    '''
    # d for decimals to start with
    d = 10 ** 9
    # start from 10^9 digits and check every digits till 1.
    while d >= 1:
        # If the input has no value on digit, print value of 0
        # on abacus.
        if v // d == 0:
            print(abacus[:11] + ' ' * 3 + abacus[11])
        else:
            print(abacus[:int(10 - v // d) + 1] + ' ' * 3
                  + abacus[int(10 - v // d) + 1:])
            # after printing a digit remove it 
            v %= d
        # Step to the next digit by 10^-1
        d /= 10

