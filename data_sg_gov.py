# Import packages
import requests

# Specify url: url
url = 'https://api.data.gov.sg/v1/environment/pm25'

# Package the request, send the request and catch the response: r
r = requests.get(url)

# Extract the response as html: html_doc
html_json = r.json()

info = html_json.get('api_info')
readings = html_json.get('items')[0].get('readings')

print(info)
print(readings)
