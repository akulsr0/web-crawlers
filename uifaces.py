from bs4 import *
import requests as rq
import os

print("Choose Gender: 1) Male  2) Female  3) Both")
genderInput = int(input())
if genderInput==1:
    r2 = rq.get('https://uifaces.co/?from_age=18&to_age=40&gender%5B%5D=male')
elif genderInput==2:
    r2 = rq.get('https://uifaces.co/?from_age=18&to_age=40&gender%5B%5D=female')
else:
    r2 = rq.get('https://uifaces.co/')

soup2 = BeautifulSoup(r2.text, "html.parser")
links = []

x = soup2.select('img[data-original^="https://images.pexels.com/photos/"]')
y = soup2.select('img[data-original^="https://images.unsplash.com/"]')
z = soup2.select('img[data-original^="https://randomuser.me/api/portraits/"]')
a = soup2.select('img[data-original^="https://tinyfac.es/data/avatars/"]')
b = soup2.select('img[data-original^="https://images-na.ssl-images-amazon.com/images/"]')

for img in x:
    links.append(img['data-original'])

for img in y:
    links.append(img['data-original'])

for img in z:
    links.append(img['data-original'])

for img in a:
    links.append(img['data-original'])

for img in b:
    links.append(img['data-original'])


path = "Downloads/"

os.mkdir(str(path))
imagesCount = int(input("How many images do you want: "))
if imagesCount>len(links):
    imagesCount=len(links)
i=1
for index, img_link in enumerate(links):
    if i<=imagesCount:
        img_data = rq.get(img_link).content
        with open(str(path)+'/'+str(index+1)+'.jpg','wb+') as f:
            f.write(img_data)
        i+=1
    else:
        f.close()
        break