from bs4 import *
import requests as rq
import os

searchInput = input("Search: ")
r2 = rq.get('https://www.pexels.com/search/'+searchInput+'/')
soup2 = BeautifulSoup(r2.text, "html.parser")

links = []

x = soup2.select('img[src^="https://images.pexels.com/photos/"]')

for img in x:
    links.append(img['src'])

os.mkdir(str(searchInput))
imagesCount = int(input("How many images do you want: "))
i=1
for index, img_link in enumerate(links):
    if i<=imagesCount:
        img_data = rq.get(img_link).content
        with open(str(searchInput)+'/'+str(index+1)+'.jpg','wb+') as f:
            f.write(img_data)
        i+=1
    else:
        f.close()
        break