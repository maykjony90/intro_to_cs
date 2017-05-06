def get_next_target(page):
    ''' <string> -> <string>, <number>
    Takes a string as an argument and finds the first URL starting from
    beggining and returns the URL, url, and its ending position, endpos.
    '''
    start_link = page.find("<a href=")
    # If there isn't any return None, 0
    if start_link == -1:
        return None, 0
    start_quote = page.find('"', start_link)
    endpos = page.find('"', start_quote + 1)
    url = page[start_quote + 1:endpos]
    return url, endpos

def print_all_links(page):
    ''' <string> -> <string>
    Takes a string as an argument and prints all the links that
    appears in the given input. Helper precedure needed: get_next_page(page)
    '''
    while True:
        url, endpos = get_next_target(page)
        if url:
            print url
            page = page[endpos:]
        else:
            break
