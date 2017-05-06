# Write Python code that assigns to the 
# variable url a string that is the value 
# of the first URL that appears in a link 
# tag in the string page.
# Your code should print http://udacity.com
# Make sure that if page were changed to

# page = '<a href="http://udacity.com">Hello world</a>'

# that your code still assigns the same value to the variable 'url', 
# and therefore still prints the same thing.

# page = contents of a web page
page =('<div id="top_bin"><div id="top_content" class="width960">'
'<div class="udacity float-left"><a href="http://udacity.com">')
start_link = page.find('<a href=')

# look for a double quote to find out where the url begins.
start_quote = page.find('"', start_link)
# look for a double quote again to find out where the url
# ends. But this time add 1 to start_quote to begin searching
# after first double quote.
end_quote = page.find('"', start_quote + 1)

# assign the value of string between start_quote + 1, because we
# want to start after the first double quote and add it end_quote,
# by using index, to the variable url then print it.
url = page[start_quote + 1:end_quote]
print(url)
