# THREE GOLD STARS
# Question 3-star: Elementary Cellular Automaton

# Please see the video for additional explanation.

# A one-dimensional cellular automata takes in a string, which in our
# case, consists of the characters '.' and 'x', and changes it according
# to some predetermined rules. The rules consider three characters, which
# are a character at position k and its two neighbours, and determine
# what the character at the corresponding position k will be in the new
# string.

# For example, if the character at position k in the string  is '.' and
# its neighbours are '.' and 'x', then the pattern is '..x'. We look up
# '..x' in the table below. In the table, '..x' corresponds to 'x' which
# means that in the new string, 'x' will be at position k.

# Rules:
#          pattern in         position k in        contribution to
# Value    current string     new string           pattern number
#                                                  is 0 if replaced by '.'
#                                                  and value if replaced
#                                                  by 'x'
#   1       '...'               '.'                        1 * 0
#   2       '..x'               'x'                        2 * 1
#   4       '.x.'               'x'                        4 * 1
#   8       '.xx'               'x'                        8 * 1
#  16       'x..'               '.'                       16 * 0
#  32       'x.x'               '.'                       32 * 0
#  64       'xx.'               '.'                       64 * 0
# 128       'xxx'               'x'                      128 * 1
#                                                      ----------
#                                                           142

# To calculate the patterns which will have the central character x, work
# out the values required to sum to the pattern number. For example,
# 32 = 32 so only pattern 32 which is x.x changes the central position to
# an x. All the others have a . in the next line.

# 23 = 16 + 4 + 2 + 1 which means that 'x..', '.x.', '..x' and '...' all
# lead to an 'x' in the next line and the rest have a '.'

# For pattern 142, and starting string
# ...........x...........
# the new strings created will be
# ..........xx...........  (generations = 1)
# .........xx............  (generations = 2)
# ........xx.............  (generations = 3)
# .......xx..............  (generations = 4)
# ......xx...............  (generations = 5)
# .....xx................  (generations = 6)
# ....xx.................  (generations = 7)
# ...xx..................  (generations = 8)
# ..xx...................  (generations = 9)
# .xx....................  (generations = 10)

# Note that the first position of the string is next to the last position
# in the string.

# Define a procedure, cellular_automaton, that takes three inputs:
#     a non-empty string,
#     a pattern number which is an integer between 0 and 255 that
# represents a set of rules, and
#     a positive integer, n, which is the number of generations.
# The procedure should return a string which is the result of
# applying the rules generated by the pattern to the string n times.

# SOLUTION:

# define an helper procedure to assign '.' or 'x' according to pattern number.
def initial_pattern(pattern_number):
    # create a list with default patterns.
    default_pattern = ['xxx', 'xx.', 'x.x', 'x..', '.xx', '.x.', '..x', '...']

    # format the pattern number into binary form to assign pattern relativly.
    bin_form_pat_num = format(pattern_number, '08b')
    # replace 1's to 'x' and 0's to '.'
    bin_form_pat_num = bin_form_pat_num.replace('1', 'x').replace('0', '.')
    # create a dict for rules
    rules = dict(zip(default_pattern, bin_form_pat_num))

    return rules


# define an helper procedure to create next generation.
def create_next_generation(genome_pattern, default_pattern):
    # add last item to the begining and first item to the ending and convert
    # it into a list.
    def_generations_list = [default_pattern[-1]] + list(default_pattern) + [default_pattern[0]]
    # turn the above list into a string.
    def_gen_pattern = ''.join(i for i in def_generations_list)

    new_gen = ''
    for i in range(0, len(default_pattern)):
        new_gen += ''.join(genome_pattern[def_gen_pattern[i:i+3]])

    return new_gen


def cellular_automaton(default_pattern, pattern_number, num_of_generations):
    # determine next generation's pattern
    genome_pattern = initial_pattern(pattern_number)

    for i in range(0, num_of_generations):
        next_generation = create_next_generation(genome_pattern, default_pattern)
        # update the default generation pattern
        default_pattern = next_generation
    # if it is required to print all the generations to nth generation
    # use below code:
    """
    for i in range(0, num_of_generations):
        next_generation = create_next_generation(genome_pattern, default_pattern)
        print(next_generation)
        # update the default generation pattern
        default_pattern = next_generation
    # if it is required to print all the generations to nth generation
    """
    return next_generation


# Udacity's SOLUTION:

def cellular_automaton_U(string, pattern_number, generations):
    patterns = {}
    pattern_list = ['...', '..x', '.x.', '.xx', 'x..', 'x.x', 'xx.', 'xxx']
    n = len(string)

    # build my patterns dictionary
    for i in range(7, -1, -1):
        if pattern_number // (2**i) == 1:
            patterns[pattern_list[i]] = 'x'
            pattern_number = pattern_number - 2**i
        else:
            patterns[pattern_list[i]] = '.'

    # make a new string by applying pattern to string
    # generations times1as
    for j in range(0, generations):
        new_string = ''
        for i in range(0, n): 
            pattern = string[i-1] + string[i] + string[(i+1)%n]
            new_string = new_string + patterns[pattern]
        string = new_string
    return new_string





"""
print(cellular_automaton('.x.x.x.x.', 17, 2))
#>>> xxxxxxx..
print cellular_automaton('.x.x.x.x.', 249, 3)
#>>> .x..x.x.x
print cellular_automaton('...x....', 125, 1)
#>>> xx.xxxxx
print cellular_automaton('...x....', 125, 2)
#>>> .xxx....
print cellular_automaton('...x....', 125, 3)
#>>> .x.xxxxx
print cellular_automaton('...x....', 125, 4)
#>>> xxxx...x
print cellular_automaton('...x....', 125, 5)
#>>> ...xxx.x
print cellular_automaton('...x....', 125, 6)
#>>> xx.x.xxx
print cellular_automaton('...x....', 125, 7)
#>>> .xxxxx..
print cellular_automaton('...x....', 125, 8)
#>>> .x...xxx
print cellular_automaton('...x....', 125, 9)
#>>> xxxx.x.x
print cellular_automaton('...x....', 125, 10)
#>>> ...xxxxx
"""

