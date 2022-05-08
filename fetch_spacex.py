import os

import requests

from save_img import save_img


def fetch_spacex_imgs(
        url='https://api.spacexdata.com/v4/launches/',
        dir=f'images',
    ):
    response = requests.get(url)
    response.raise_for_status()
    urls = response.json()[13]['links']['flickr']['original']
    for img_url in urls:
        img_name = os.path.split(img_url)[1]
        save_img(img_url, dir, img_name)


if __name__ == '__main__':
    fetch_spacex_imgs()
