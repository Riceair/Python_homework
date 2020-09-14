from bs4 import BeautifulSoup
import re

htmlfile = open('htmlfile.htm',encoding = 'utf-8').read()
soup = BeautifulSoup(htmlfile,'html.parser')

print(soup.title.string)
h1=re.split(' ',soup.h1.string)
h1[2]="A1065506"
soup.h1.string=" ".join(h1)

new_file = open('A1065506.htm','w')
new_file.write(str(soup))
new_file.close()
