# Import packages
import requests
from bs4 import BeautifulSoup

# Specify url: url
url = 'https://www.python.org/~guido/'

# Package the request, send the request and catch the response: r
r = requests.get(url)

# Extract the response as html: html_doc
html_doc = r.text

# Create a BeautifulSoup object from the HTML: soup
soup = BeautifulSoup(html_doc, "html.parser")

# Get Guido's text: guido_text
guido_text = soup.get_text()

# Print Guido's text to the shell
# print(guido_text)
print(soup.find_all('b'))
