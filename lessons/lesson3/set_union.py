# Define a procedure, union,
# that takes as inputs two lists.
# It should modify the first input
# list to be the set union of the two
# lists. You may assume the first list
# is a set, that is, it contains no 
# repeated elements.


def union(s,p):
    for e in p:
        if e not in s:
            s.append(e)
    # return statement isn't really neccesary in 
    # this precedure.
    return s 



# To test, uncomment all lines 
# below except those beginning with >>>.

a = [1,2,3]
b = [2,4,6]
union(a,b)
print a 
#>>> [1,2,3,4,6]
print b
#>>> [2,4,6]
print union([],[1])
