from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as ureq

my_url = "https://www.walmart.com/search?q=Samsung"

uClient = ureq(my_url)
page_html = uClient.read()
uClient.close()
page_soup = soup(page_html, "html.parser")

containers = page_soup.findAll("div", {"class": "_3O0U0u"})
print(len(containers))

