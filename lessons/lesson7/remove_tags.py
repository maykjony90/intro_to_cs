# Question 4: Remove Tags

# When we add our words to the index, we don't really want to include
# html tags such as <body>, <head>, <table>, <a href="..."> and so on.

# Write a procedure, remove_tags, that takes as input a string and returns
# a list of words, in order, with the tags removed. Tags are defined to be
# strings surrounded by < >. Words are separated by whitespace or tags.
# You may assume the input does not include any unclosed tags, that is,
# there will be no '<' without a following '>'.

# My Version by using recursive function:

def remove_tags_mV(page):
    untagged = ''
    start_tag = page.find('<')
    if start_tag != -1:
        end_tag = page.find('>', start_tag)
        tag = page[start_tag:end_tag+1]
        untagged = page.replace(tag, ' ')
        return remove_tags(untagged)
    else:
        return page.split()


# Udacity's answer by using iterative function:

def remove_tags(page):
    start = page.find('<')
    while start != -1:
        end = page.find('>', start)
        page = page[:start] + ' ' + page[end + 1:]
        start = page.find('<')
    return page.split()


print(remove_tags('''<h1>Title</h1><p>This is a
                    <a href="http://www.udacity.com">link</a>.<p>'''))
#>>> ['Title','This','is','a','link','.']

print(remove_tags('''<table cellpadding='3'>
                     <tr><td>Hello</td><td>World!</td></tr>
                     </table>'''))
#>>> ['Hello','World!']

print(remove_tags("<hello><goodbye>"))
#>>> []

print(remove_tags("This is plain text."))
#>>> ['This', 'is', 'plain', 'text.']
