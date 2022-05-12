import os

import requests

from save_img import save_img

LAUNCH_NUM = 13


def fetch_spacex_imgs(
        url=f'https://api.spacexdata.com/v4/launches',
        dir=f'images',
    ):
    response = requests.get(f'{url}/latest')
    response.raise_for_status()
    urls = response.json()['links']['flickr']['original']
    if not urls:
        response = requests.get(url)
        response.raise_for_status()
        urls = response.json()[LAUNCH_NUM]['links']['flickr']['original']
        for img_url in urls:
            path, img_name = os.path.split(img_url)
            save_img(img_url, dir, img_name)
    else:
        for img_url in urls:
            path, img_name = os.path.split(img_url)
            save_img(img_url, dir, img_name)


if __name__ == '__main__':
    fetch_spacex_imgs()
