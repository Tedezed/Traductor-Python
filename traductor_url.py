import urllib2
import re
from BeautifulSoup import BeautifulSoup

#<div itemprop="articleBody">

url_search = "http://docs.godotengine.org"
url_body = "/en/latest/"
url_obj = "index.html"
url = url_search + url_body + url_obj

html = urllib2.urlopen(url)
htmlread = html.read()
html.close()

html_soup = BeautifulSoup(htmlread)
soup = html_soup.find('div', { "itemprop" : "articleBody" })

print soup
