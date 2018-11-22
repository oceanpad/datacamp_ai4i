# Import packages
import requests
import urllib2
from bs4 import BeautifulSoup

# Specify url: url
url = 'http://www.sg--pr.appspot.com/'

# Package the request, send the request and catch the response: r
r = requests.get(url, timeout=5)

# Extract the response as html: html_doc
html_doc = r.text
print html_doc[:1000]

# Create a BeautifulSoup object from the HTML: soup
soup = BeautifulSoup(html_doc, "html.parser")

# Get Guido's text: guido_text
guido_text = soup.get_text()

# Print Guido's text to the shell
# print(guido_text)
trs = soup.find_all('tr')
print trs[1]
print len(trs)

response = urllib2.request.urlopen(url)
html = response.read()
print html[0:1000]
