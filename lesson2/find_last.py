# Define a procedure, find_last, that takes as input
# two strings, a search string and a target string,
# and returns the last position in the search string
# where the target string appears, or -1 if there
# are no occurrences.
#
# Example: find_last('aaaa', 'a') returns 3

# Make sure your procedure has a return statement.

def find_last(page, target):
    # check if target occurs in the given string
    target_occur = page.find(target)
    # while target occurs, update the value of target_occur
    # and add one to index(to find next occurance)
    while page.find(target, target_occur+1) != -1:
        target_occur = page.find(target, target_occur+1)
    return target_occur

# Another way to solve this problem:

'''
def find_last(s,t):
    last_pos = s.find(t)
    while True:
        pos = s.find(t, last_pos+1)
        if pos == -1:
            return last_pos
        last_pos = pos
'''
    





#print find_last('aaaa', 'a')
#>>> 3

#print find_last('aaaaa', 'aa')
#>>> 3

#print find_last('aaaa', 'b')
#>>> -1

#print find_last("111111111", "1")
#>>> 8

#print find_last("222222222", "")
#>>> 9

#print find_last("", "3")
#>>> -1

#print find_last("", "")
#>>> 0




