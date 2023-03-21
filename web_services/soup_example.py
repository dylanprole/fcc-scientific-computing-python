import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup

# User inpur the desired URL address
url = input('Enter - ') # 'http://www.dr-chuck.com/page1.htm'



# Return the website data in bytes
html = urllib.request.urlopen(url).read() # Read entire file
# Have beautiful soup read the file and parse it using html
# HTML has many strange formats, so beautiful soup takes care of this for us
soup = BeautifulSoup(html, 'html.parser')

# Retrieve all of the anchor tags <a> <a/>
# e.g. <a href="https://www.w3schools.com">Visit W3Schools.com!</a>
tags = soup('a')
for tag in tags:
  # Find all hypertext links on the page
  print(tag.get('href', None))
