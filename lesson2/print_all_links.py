def get_next_target(page):
    start_link = page.find('<a href=')
    #print 'start link is', start_link
    if start_link == -1:
        return None, 0
        
    start_quote = page.find('"', start_link)
        #print 'start quote is', start_quote
    end_quote = page.find('"', start_quote + 1)
        #print 'end_quote is', end_quote
    url = page[start_quote + 1:end_quote]
        #print 'url is', url
    
    return url, end_quote

def print_all_links(page):
    while True:
        url, endpos = get_next_target(page)
        if url:
            print url
            page = page[endpos:]
        else:
            break
