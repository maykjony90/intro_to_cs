#Finish crawl web

def get_page(url):
    # This is a simulated get_page procedure so that you can test your
    # code on two pages "http://xkcd.com/353" and "http://xkcd.com/554".
    # A procedure which actually grabs a page from the web will be
    # introduced in unit 4.
    try:
        if url == "https://www.udacity.com/cs101x/index.html":
            return """
<html>
<body>
This is a test page for learning to crawl!
<p>
It is a good idea to
<a href="http://www.udacity.com/cs101x/crawling.html">learn to crawl</a>
before you try to
<a href="http://www.udacity.com/cs101x/walking.html">walk</a> or
<a href="http://www.udacity.com/cs101x/flying.html">fly</a>.
</p>
</body>
</html>

"""
    except:
        return ""
    return ""


def get_next_target(page):
    start_link = page.find('<a href=') #find starting of the list
    if start_link == -1: #if there isn't return None, 0
        return None, 0
    start_quote = page.find('"', start_link) #find starting of the URL
    end_quote = page.find('"', start_quote + 1) #find ending of the URL
    url = page[start_quote + 1:end_quote] # save the URL
    return url, end_quote #return saved URL and ending pos. of URL

def union(p,q): # p = tocrawl, q = links
    for e in q:
        if e not in p:
            p.append(e)


def get_all_links(page):
    links = []
    while True: #while there is more URL to find continue iterating
        url,endpos = get_next_target(page) #take the URL ann endpos
        if url: #If next URL found append it to links list
            links.append(url)
            page = page[endpos:] #update page value
        else:
            break
    return links

# WARNING!: I didn't understand exatcly how below precedure functions!!!
# I'm getting into it gradually
def crawl_web(seed):
    tocrawl = [seed] # start with seed page
    crawled = []
    while tocrawl:
        # remove last element and assign it into to crawl
        page = tocrawl.pop()
        if page not in crawled:
            # get each URL from page and if they aren't in tocrawl list
            # put them into tocrawl
            union(tocrawl, get_all_links(get_page(page)))
            crawled.append(page) # append page into crawled list
    return crawled


crawl_web("https://www.udacity.com/cs101x/index.html")
