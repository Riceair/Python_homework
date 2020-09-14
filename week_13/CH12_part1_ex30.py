from bs4 import BeautifulSoup
soup = BeautifulSoup("<c>Tag C</c>","html.parser")
print("Original Markup:")
print(soup.c)
tag = soup.new_tag('n')
tag.string = "New Tag"
print("\nNew Markup, after inserting the text:")
soup.c.string.insert_after(tag)
print(soup.c)
