import datetime
import os

import requests
from dotenv import load_dotenv

from save_img import save_img


DIR_NASA = f'images/nasa'
DIR_EPIC = f'images/nasa/epic'
URL_NASA = 'https://api.nasa.gov/planetary/apod'
URL_EPIC_DATA = 'https://api.nasa.gov/EPIC/api/natural/images'
URL_EPIC_IMG = 'https://api.nasa.gov/EPIC/archive/natural/'
NUM_NASA_PHOTOS = 1


def fetch_nasa_today_imgs(dir, nasa_key, url=URL_NASA):
    params = {'api_key': nasa_key, 'count': NUM_NASA_PHOTOS}
    response = requests.get(url, params=params)
    response.raise_for_status()
    img_urls = []
    for img_data in response.json():
        if img_data['media_type'] == 'image':
            img_urls.append(img_data['url'])
    for img_url in img_urls:
            path, img_name = os.path.split(img_url)
            save_img(img_url, dir, img_name, params=params)


def fetch_nasa_epic_imgs(url_data, url_img, dir, nasa_key):
    params = {'api_key': nasa_key}
    response = requests.get(url_data, params=params)
    response.raise_for_status()
    for epic_img in response.json():
        img_name = epic_img['image']
        img_name = f'{img_name}.png'
        img_date = epic_img['date']
        date_time = datetime.datetime.fromisoformat(img_date)
        date = date_time.strftime('%Y/%m/%d')
        url_get_img = f'{url_img}{date}/png/{img_name}'
        save_img(url_get_img, dir, img_name, params=params)


def fetch_nasa_imgs(nasa_key):
    fetch_nasa_today_imgs(DIR_NASA, nasa_key, URL_NASA)
    fetch_nasa_epic_imgs(URL_EPIC_DATA, URL_EPIC_IMG, DIR_EPIC, nasa_key)


if __name__ == '__main__':
    load_dotenv()
    nasa_key = os.environ['NASA_KEY']
    fetch_nasa_imgs(nasa_key)
