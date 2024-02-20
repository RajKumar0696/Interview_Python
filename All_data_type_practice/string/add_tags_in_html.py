#  Write a Python function to create an HTML string with tags around the word(s).
# Sample function and result :
# add_tags('i', 'Python') -> '<i>Python</i>'
# add_tags('b', 'Python Tutorial') -> '<b>Python Tutorial </b>'

def html_string(tag, value):
    return "<%s> %s </%s>" % (tag, value, tag)


print(html_string("i", "python"))
