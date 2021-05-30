!pip install requests
!pip install bs4
!pip install html5lib

import requests
from bs4 import BeautifulSoup
url = "https://www.fabhotels.com/blog/cleanest-cities-in-india/"


r = requests.get(url)
htmlContent = r.content
# print(htmlContent)

soup = BeautifulSoup(htmlContent, 'html.parser')
print(soup.prettify)

paras = soup.find_all('p')
# print(paras)

anchors = soup.find_all('a')
all_links = set()
print (anchors)

anchors = soup.find_all('a')
all_links = set()
for link in anchors:
    if(link.get('href') != '#'):
        linkText = "https://www.fabhotels.com/blog/cleanest-cities-in-india/" +link.get('href')
        all_links.add(link)
        print(linkText)
