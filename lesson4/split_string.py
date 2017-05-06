# 1 Gold Star

# The built-in <string>.split() procedure works
# okay, but fails to find all the words on a page
# because it only uses whitespace to split the
# string. To do better, we should also use punctuation
# marks to split the page into words.

# Define a procedure, split_string, that takes two
# inputs: the string to split and a string containing
# all of the characters considered separators. The
# procedure should return a list of strings that break
# the source string up by the characters in the
# splitlist.


### MY SOLUTION ###
"""
def split_string(source, splitlist):
    '''  <string>, <string> -> <list>
    Takes two string, source and splitlist, as input and returns
    a list of strings that break the source string up by characters in
    the splitlist.
    '''
    splitted = source.split(splitlist[0])
    temp_list = []
    
    
    for seperator in splitlist:
        for n in splitted:
            temp_elements = n.split(seperator)
            for elm in temp_elements:
                temp_list.append(elm)
            
        splitted = temp_list
        temp_list = []
        
    for j in splitted:
        if "" in splitted:
            splitted.remove('')
    
    return splitted
"""

### BETTER SOLUTION ###

"""
def split_string(source, splitlist):
    '''  <string>, <string> -> <list>
    Takes two string, source and splitlist, as input and returns
    a list of strings that break the source string up by characters in
    the splitlist.
    '''
    seperator = splitlist[0]
    for char in splitlist:
        source = source.replace(char, seperator)
    result = source.split(seperator)
    
    for j in result:
        if "" in result:
            result.remove('')
    
    return result
"""
### WAY BETTER ONE ###

def split_string(source,splitlist):
    '''  <string>, <string> -> <list>
    Takes two string, source and splitlist, as input and returns
    a list of strings that break the source string up by characters in
    the splitlist.
    '''
    separator = splitlist[0]
    for character in splitlist:
        source = source.replace(character, separator)
        
    # below code is to eliminate any empty strings from the
    # list returned by source.split(separator).
    return [e for e in source.split(separator) if e]

            

        




#out = split_string("This is a test-of the,string separation-code!"," ,!-")
#print out
#>>> ['This', 'is', 'a', 'test', 'of', 'the', 'string', 'separation', 'code']

#out = split_string("After  the flood   ...  all the colors came out.", " .")
#print out
#>>> ['After', 'the', 'flood', 'all', 'the', 'colors', 'came', 'out']

#out = split_string("First Name,Last Name,Street Address,City,State,Zip Code",",")
#print out
#>>>['First Name', 'Last Name', 'Street Address', 'City', 'State', 'Zip Code']
