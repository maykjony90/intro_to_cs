# Define a precedure, web_crawl, that takes a string, seed, as its input
# and returns a list that contains all the URLs reachable from this string.

### HELPER PRECEDURES ###
def get_next_target(page):
    ''' <string> -> <string>, <number>
    Takes a string as an argument and finds the first URL starting from
    beggining and returns the URL, url, and its ending position, endpos.
    '''
    # go to first appearence of the anchor tag: <a href='...'>
    start_link = page.find("<a href=")
    # If there isn't any return None, 0
    if start_link == -1:
        return None, 0
    # find where the quote starts
    start_quote = page.find('"', start_link)
    # find where the quote ends
    endpos = page.find('"', start_quote + 1)
    # assign the URL as a value into a variable
    url = page[start_quote + 1:endpos]
    # return the URL and its end position
    return url, endpos

def get_all_links(page):
    ''' <string> -> <list>
    Takes a string, page, as an argument and returns all the
    links present on this string.
    >>> get_all_links(www.mywebsite.com)
    >>> ['htttps://www.facebook.com/mikey','.../index.html']
    '''
    links = []
    while True:
        url, endpos = get_next_target(page)
        if url:
            links.append(url)
            page = page[endpos:]
        else:
            break
    return links

##########################


def web_crawl(seed):
    ''' <string> -> <list>
    Takes a string, seed, as an argument and returns a list, links, that
    contains all the URLs reachable from this string
    >>> web_crawl(www.mywebsite.com)
    >>> ['https://www.facebook.com/mayki', 'https://www.google.com']
    '''
    # assign all the links to be crawled that
    # appeats on the seed page to a variabl
    tocrawl = get_all_links(get_page(seed))
    # create a list to collect the links crawled
    crawled = []
    # while there are more links reachable continue to search
    while tocrawl != []:
        # create a variable, target, to collect all the
        # links in the indexing the last item in the list tocrawl.
        target = get_all_links(tocrawl[-1])
        # check target is not already
        # saved in the list crawled. 
        if target not in crawled:
            # check if target is an empty list. If so, add the last
            # item that page into crawled and remove it from tocrawl.
            # if not, assign links in target to tocrawl.
            if target != []:
                tocrawl = target
            else:
                crawled += target[-1]
                tocrawl.pop()
            # check if the new value of the tocrawl is equal to empty list.
            # if so, turn back to the seed page.
            if tocrawl == []:
                tocrawl = get_all_links(get_page(seed))
                # ALT: tocrawl = get_all_links(get_page(seed))
        # if a link is already in crawled, remove it from the searh precedure.
        else:
            tocrawl.pop()
    # return all the links crawled
    return crawled
    
