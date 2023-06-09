import requests
from bs4 import BeautifulSoup
import os

url = 'https://www.nytimes.com/2022/03/15/technology/ai-no-code.html'


def imagedl(url, folder):
    try:
        os.mkdir(os.path.join(os.getcwd(), folder))
    except:
        pass
    os.chdir(os.path.join(os.getcwd(), folder))
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    images = soup.find_all('img')
    for image in images:
        name = image['alt']
        link = image['src']
        with open(name.replace(' ', '-').replace('/', '') + '.jpg', 'wb') as f:
            im = requests.get(link)
            f.write(im.content)
            print('Writing: ', name)


imagedl('https://www.nytimes.com/2022/03/15/technology/ai-no-code.html', '')
