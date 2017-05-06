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
<h1>Hello bitches</h1>
It is a good idea to 
<a href="http://www.udacity.com/cs101x/crawling.html">learn to crawl</a>
before you try to 
<a href="http://www.udacity.com/cs101x/walking.html">walk</a> or 
<a href="http://www.udacity.com/cs101x/flying.html">fly</a>.
</p>
</body>
</html>

"""
        elif url == "http://www.udacity.com/cs101x/crawling.html":
            return """<html>
<body>
This is a test page for learning to crawl!
<p>
<a href="https://www.udacity.com/cs101x/index.html">
<h1>Hi there sexy bitches</h1>
It is a good idea to 
</p>
</body>
</html>"""
    except:
        return ""
    return ""
    
def add_to_index(index, keyword, url):
    for entry in index:
        if entry[0] == keyword:
            if entry[1] != url: # WARNING!if this line throws error, remove it!!!
                entry[1].append(url)
                return
    index.append([keyword, [url]])

def lookup(index, keyword):
    for entry in index:
        if entry[0] == keyword:
            return entry[1]
    return []

def add_page_to_index(index, url, content):
    words = content.split()
    for word in words:
        add_to_index(index, word, url)

def get_next_h1(page):
    start_h1 = page.find('<h1>') #find starting of the h1
    if start_h1 == -1:
        return None,0
    end_h1 = page.find('</h1>', start_h1) #find ending of h1
    title = page[start_h1 + 4:end_h1]
    return title, end_h1



def get_all_h1(page):
    titles = ''
    while True: #while there is more URL to find continue iterating
        title, end_h1 = get_next_h1(page) #take the URL ann endpos
        if title: #If next URL found append it to links list
            titles += " " + title
            page = page[end_h1:] #update page value
        else:
            break
    return titles
    

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
    index = []
    while tocrawl:
        # remove last element and assign it into to crawl
        page = tocrawl.pop() 
        if page not in crawled:
            # as it is expensive to web request, assign it into a variable
            content = get_page(page)
            titles = get_all_h1(content)
            # update index to reflect all the words found on the page
            add_page_to_index(index, page, titles)
            # get each URL from page and if they aren't in tocrawl list
            # put them into tocrawl 
            union(tocrawl, get_all_links(content))
            crawled.append(page) # append page into crawled list
    return index


crawl_web("https://www.udacity.com/cs101x/index.html")
