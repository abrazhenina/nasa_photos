import os
from pathlib import Path

import requests


url_img = 'https://upload.wikimedia.org/wikipedia/commons/3/3f/HST-SM4.jpeg'


def get_response(url, params=''):
    if params:
        response = requests.get(url, params)
        response.raise_for_status()
        return response
    else:
        response = requests.get(url)
        response.raise_for_status()
        return response


def get_img_ext_from_url(url):
    filename = os.path.split(url)[1]
    ext = os.path.splitext(filename)[1]
    if ext:
        return ext


def download_img(dir, name, response):
    Path(dir).mkdir(parents=True, exist_ok=True)
    dir_img = f'{dir}/{name}'
    with open(dir_img, 'wb') as img:
        img.write(response.content)


def main(url=url_img, dir=f'images', img_name='h.jpg'):
    response = get_response(url)
    download_img('images', 'h.jpg', response)


if __name__ == '__main__':
    main()
