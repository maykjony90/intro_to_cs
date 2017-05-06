# Modify the get_next_target procedure so that
# if there is a link it behaves as before, but
# if there is no link tag in the input string,
# it returns None, 0.

# Note that None is not a string and so should
# not be enclosed in quotes.

# Also note that your answer will appear in
# parentheses if you print it.

def get_next_target(page):
    start_link = page.find('<a href=')
    #print 'start link is', start_link

    #Insert your code below here
    if start_link == -1:
        return None, 0
        
    start_quote = page.find('"', start_link)
        #print 'start quote is', start_quote
    end_quote = page.find('"', start_quote + 1)
        #print 'end_quote is', end_quote
    url = page[start_quote + 1:end_quote]
        #print 'url is', url
    
    return url, end_quote
                 

#print get_next_target('asdf asdf asldfkj a href="hhttp">lilnk</a>')
url, endpos = get_next_target('asdf asdf asldfkj a href="hhttp">lilnk</a>')
#print url
