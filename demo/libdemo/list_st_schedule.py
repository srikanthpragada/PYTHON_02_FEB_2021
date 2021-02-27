import requests
from bs4 import BeautifulSoup

resp = requests.get("http://www.srikanthtechnologies.com")
bs = BeautifulSoup(resp.text,"html.parser")
table = bs.find(id = "ctl00_ContentPlaceHolder1_GridView2")
#print(table)
rows = table.find_all("tr")
for row in rows[1:]:
    cols = row.find_all('td')
    print(f"{cols[0].text:40} {cols[2].text:15} {cols[1].text}")

