import requests
from bs4 import BeautifulSoup
import os

url = 'https://improvado.io'
response = requests.get(url+'/blog')
soup = BeautifulSoup(response.text, 'lxml')

blog_posts = soup.find(class_='blog-posts')

for link in blog_posts.findAll('a', class_="link-block-12"):
    # print(type(link),link)
    filename = url+link.get('href')
    filename = filename.split('/')[-1]+'.txt'
    # print(filename)
    response = requests.get(url+link.get('href'))
    soup = BeautifulSoup(response.text, 'lxml')
    p = soup.find('div', class_='blog-body-block').find_all('p')
    os.makedirs('texts', exist_ok=True)
    with open(f'texts/{filename}', 'w') as f:
        for i in p:
            f.write(i.text+'\n')

