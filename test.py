from mathematicians import simple_get
raw_html = simple_get('https://realpython.com/blog/')
len(raw_html)

no_html = simple_get('https://realpython.com/blog/nope-not-gonna-find-it')
no_html is None

print(raw_html)
print(no_html)