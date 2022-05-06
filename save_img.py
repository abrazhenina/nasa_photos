import os
from pathlib import Path

import requests


def save_img(
        url='https://upload.wikimedia.org/wikipedia/commons/3/3f/HST-SM4.jpeg',
        dir=f'images',
        img_name='HST-SM4.jpeg', 
        params='',
    ):
    response = requests.get(url, params=params)
    response.raise_for_status()
    Path(dir).mkdir(parents=True, exist_ok=True)
    dir_img = f'{dir}/{img_name}'
    with open(dir_img, 'wb') as img:
        img.write(response.content)


if __name__ == '__main__':
    save_img()
