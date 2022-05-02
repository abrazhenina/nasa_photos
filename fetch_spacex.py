import os

from download_img import download_img
from download_img import get_response


url_spacex = 'https://api.spacexdata.com/v4/launches/'


def fetch_spacex(url=url_spacex, dir=f'images'):
    response = get_response(url)
    paths = response.json()[13]['links']['flickr']['original']
    for img_path in paths:
        img_name = os.path.split(img_path)[1]
        img_response = get_response(img_path)
        download_img(dir, img_name, img_response)


if __name__ == '__main__':
    fetch_spacex()
