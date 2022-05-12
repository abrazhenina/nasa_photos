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
    img_path = f'{dir}/{img_name}'
    with open(img_path, 'wb') as img:
        img.write(response.content)
