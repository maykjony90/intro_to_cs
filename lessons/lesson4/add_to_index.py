# Define a procedure, add_to_index,
# that takes 3 inputs:

# - an index: [[<keyword>,[<url>,...]],...]
# - a keyword: String
# - a url: String

# If the keyword is already
# in the index, add the url
# to the list of urls associated
# with that keyword.

# If the keyword is not in the index,
# add an entry to the index: [keyword,[url]]

### Solution with while loop (primitive)###
'''
index = []

def add_to_index(index,keyword,url):
    if index == []:
        index.append([keyword, [url]])
        return index
    else:
        n = 0
        while n < len(index):
            if keyword in index[n][0]:
                if url not in index[n][1]:
                    return index[n][1].append(url)
                else:
                    return index
            n += 1
        return index.append([keyword, [url]])
'''

### Solution with for loop (more efficient) ###

index = []

def add_to_index(index,keyword,url):
    for entry in index: # iterate each item in index
        if keyword in entry[0]: # iterate only first items for efficiency
            if url not in entry[1]: # if url not exist append it and return
                return entry[1].append(url)
            else:
                return index # if url exists return index as it was before
    return index.append([keyword, [url]]) # if keyword not exist append it with url
            
'''
add_to_index(index,'udacity','http://udacity.com')
print index
add_to_index(index,'computing','http://acm.org')
print index
add_to_index(index,'udacity','http://npr.org')
print index
add_to_index(index,'udacity','http://osman.org')
print index
add_to_index(index,'dhamet','http://dhamet.org')
print index
add_to_index(index,'computing','http://acm.org')
print index
#>>> [['udacity', ['http://udacity.com', 'http://npr.org']], 
#>>> ['computing', ['http://acm.org']]]
'''

