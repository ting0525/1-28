import urllib2
from bs4 import BeautifulSoup

# Fetch the html file
import urllib3
from bs4 import BeautifulSoup
# Fetch the html file
http = urllib3.PoolManager()
response = http.request('GET','http://localhost/startbootstrap-resume-gh-pages')
html_doc = response.data
# Parse the html file
soup = BeautifulSoup(html_doc, 'html.parser')
# Format the parsed html file
strhtm = soup.prettify()
# Print the first few characters
print (strhtm[:225])