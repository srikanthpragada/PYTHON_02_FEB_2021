import requests
from bs4 import BeautifulSoup
from datetime import *
resp = requests.get("http://www.srikanthtechnologies.com/rss.xml")
bs = BeautifulSoup(resp.text,"lxml-xml")
items = bs.find_all("item")
for item in items:
    pubdate_text = item.pubDate.text.strip()
    pubdate = datetime.strptime(pubdate_text[5:16], '%d %b %Y')
    days = (datetime.today() - pubdate).days
    if  days < 200:
        print(item.title.text.strip())
        print(item.link.text.strip())
        print(f"{days} days old")
        print("-" * 50)

