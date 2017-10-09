# By Sam the Great from forums
# That freaking superhero has been frequenting Udacity
# as his favorite boss battle fight stage. The 'Udacity'
# banner keeps breaking, and money is being wasted on
# repairs. This time, we need you to proceduralize the
# fixing process by building a machine to automatically
# search through debris and return the 'Udacity' banner
# to the company, and be able to similarly fix other goods.

# Write a Python procedure fix_machine to take 2 string inputs
# and returns the 2nd input string as the output if all of its
# characters can be found in the 1st input string and "Give me
# something that's not useless next time." if it's impossible.
# Letters that are present in the 1st input string may be used
# as many times as necessary to create the 2nd string (you
# don't need to keep track of repeat usage).

# NOTE: # If you are experiencing difficulties taking
        # this problem seriously, please refer back to
        # "Superhero flyby", the prequel, in Problem Set 11.

# TOOLS: # if statement
         # while loop
         # string operations
         # Unit 1 Basics

# BONUS: # 
# 5***** #  If you've graduated from CS101,
#  Gold  #  try solving this in one debris.
# Stars! #

''' The most primitive way '''
# The following precedure can hold the value of the
# every item that is searched.
def fix_machine(debris, product):
    # the program should check every letter of the product argument 
    # one at a time to see if they appear in the debris argument.
    # If any of them doesn't, then it prints the value of the no_banner
    # variable.
    counter = 0
    letter = debris[debris.find(product[counter])]
    banner = ""
    no_banner = "Give me something that's not useless next time."
    if letter:
        while letter:
            banner += letter
            counter += 1
            if counter == len(product):
                if banner == product:
                    return banner
                return no_banner
            letter = debris[debris.find(product[counter])]
        return banner
    else:
        return no_banner


''' An improved way '''
# This precedure doesn't required as many memory as the first one.
def fix_machine(debris, product):
    counter = 0
    # while letter appears in the debris look for the next letter.
    while debris.find(product[counter]) >= 0:
        counter += 1
        # Check if all the letters are searched
        if counter >= len(product):
            # if so, return product to be compared
            return product
    # if a letter can't be found in debris return a statement
    # to be compared.
    return "Give me something that's not useless next time."

''' A better way '''
def fix_machine(debris, product):
    char = 0
    while char <= len (product) - 1:
        if product [char] in debris:
                char += 1
        else:
            return "Give me something that's not useless next time."
    return product

''' A sophisticated way '''
def fix_machine(debris, product):
    for p in product:
        if p not in debris:
            return "Give me something that's not useless next time."
    else:
        return product

''' The most elegant way '''
def fix_machine(debris, product):
    return product if set(product) <= set(debris) \
    else "Give me something that's not useless next time."

### TEST CASES ###
print "Test case 1: ", fix_machine('UdaciousUdacitee', 'Udacity') == "Give me something that's not useless next time."
print "Test case 2: ", fix_machine('buy me dat Unicorn', 'Udacity') == 'Udacity'
print "Test case 3: ", fix_machine('AEIOU and sometimes y... c', 'Udacity') == 'Udacity'
print "Test case 4: ", fix_machine('wsx0-=mttrhix', 't-shirt') == 't-shirt'
