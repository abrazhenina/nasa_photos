import os

import datetime
import requests

from dotenv import load_dotenv
from pathlib import Path


url_nasa = 'https://api.nasa.gov/planetary/apod'
url_nasa_epic_data = 'https://api.nasa.gov/EPIC/api/natural/images'
url_nasa_epic_img = 'https://api.nasa.gov/EPIC/archive/natural/'


def get_img_ext_from_url(url):
    filename = os.path.split(url)[1]
    ext = os.path.splitext(filename)[1]
    if ext:
        return ext


def fetch_nasa_imgs(dir, api_key, url=url_nasa):
    Path(dir).mkdir(parents=True, exist_ok=True)
    params = {
        'api_key': api_key,
        'count': 1,
    }
    response = requests.get(url, params=params)
    response.raise_for_status()
    img_urls = []
    for img_data in response.json():
        if img_data['url']:
            img_urls.append(img_data['url'])
    if img_urls[0]:
        for img_url in img_urls:
            img_dir = ''
            if '.jpg' or '.gif' in img_url:
                try:
                    img_name = os.path.split(img_url)[1]
                    img_response = requests.get(img_url)
                    img_response.raise_for_status()
                    img_dir = f'{dir}/{img_name}'
                    print
                    with open(img_dir, 'wb') as img:
                        img.write(img_response.content)
                except:
                    print('Error with url')
                    img_name = ''
            else:
                print('Error with url')
                img_name = ''


def fetch_nasa_epic_imgs(url_data, url_img, dir, api_key):
    Path(dir).mkdir(parents=True, exist_ok=True)
    params = {
        'api_key': api_key,
    }
    response = requests.get(url_data, params=params)
    response.raise_for_status()
    for epic_img in response.json():
        img_name = epic_img['image']
        img_name = f'{img_name}.png'
        img_date = epic_img['date']
        date_time = datetime.datetime.fromisoformat(img_date)
        date = date_time.strftime('%Y/%m/%d')
        url_get_img = f'{url_img}{date}/png/{img_name}'
        response = requests.get(url_get_img, params=params)
        img_dir = f'{dir}/{img_name}'
        with open(img_dir, 'wb') as img:
            img.write(response.content)


def fetch_all_nasa_imgs(api_key):
    dir = f'images/nasa'
    fetch_nasa_imgs(dir, api_key, url_nasa)
    dir = f'images/nasa/epic'
    fetch_nasa_epic_imgs(url_nasa_epic_data, url_nasa_epic_img, dir, api_key)


if __name__ == '__main__':
    load_dotenv()
    API_KEY = os.environ['API_KEY']
    fetch_all_nasa_imgs(API_KEY)

    
    
