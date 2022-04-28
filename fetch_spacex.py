import os

import requests

from pathlib import Path

url_img = 'https://upload.wikimedia.org/wikipedia/commons/3/3f/HST-SM4.jpeg'
url_spacex = 'https://api.spacexdata.com/v4/launches/'

def download_img(url=url_img, dir=f'images', img_name='h.jpg'):
    dir = f'{dir}/{img_name}'
    Path(dir).mkdir(parents=True, exist_ok=True)
    response = requests.get(url)
    response.raise_for_status()
    with open(dir, 'wb') as img:
        img.write(response.content)


def fetch_spacex_imgs(url=url_spacex, dir=f'images'):
    Path(dir).mkdir(parents=True, exist_ok=True)
    response = requests.get(url)
    response.raise_for_status()
    paths = response.json()[13]['links']['flickr']['original']
    for img_path in paths:
        img_dir = ''
        img_name = os.path.split(img_path)[1]
        img_response = requests.get(img_path)
        img_response.raise_for_status()
        img_dir = f'{dir}/{img_name}'
        with open(img_dir, 'wb') as img:
            img.write(img_response.content)


if __name__ == '__main__':
    fetch_spacex_imgs()