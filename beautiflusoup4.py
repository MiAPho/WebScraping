from bs4 import BeautifulSoup
import urllib.request as req

url="http://codehobby.starfree.jp/about.html"
response=req.urlopen(url)

parse_html=BeautifulSoup(response,'html.parser')

print(parse_html)


divElem=parse_html.find('div',{'class':'col-md-10 col-md-offset-1 space'})

print(divElem)

pElem=[p.get_text() for p in divElem.select('div p')]

print(pElem)

fos=open('scraped.txt','a')
for line in pElem:
    fos.write(line)
fos.close()
