import os

import datetime
import requests
import telegram
import time

from dotenv import load_dotenv
from pathlib import Path
from telegram.ext import Updater


url_img1 = 'https://upload.wikimedia.org/wikipedia/commons/3/3f/HST-SM4.jpeg'
url_spacex = 'https://api.spacexdata.com/v4/launches/'
url_nasa = 'https://api.nasa.gov/planetary/apod'
url_nasa_epic_data = 'https://api.nasa.gov/EPIC/api/natural/images'
url_nasa_epic_img = 'https://api.nasa.gov/EPIC/archive/natural/'


def download_img(url, dir, img_name):
    response = requests.get(url)
    response.raise_for_status()
    dir = f'{dir}/{img_name}'
    with open(dir, 'wb') as img:
        img.write(response.content)


def get_img_ext_from_url(url):
    filename = os.path.split(url)[1]
    ext = os.path.splitext(filename)[1]
    if ext:
        return ext


def fetch_spacex_imgs(url, dir):
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


def fetch_nasa_imgs(url, api_key, dir):
    params = {
        'api_key': api_key,
        'count': 30,
    }
    response = requests.get(url, params=params)
    response.raise_for_status()
    img_urls = []
    for img_data in response.json():
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


def fetch_nasa_epic_imgs(url_data, url_img, api_key, dir):
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


if __name__ == '__main__':
    load_dotenv()
    API_KEY = os.environ['API_KEY']
    img_name = 'hubble.jpg'
    dir = f'images'
    Path(dir).mkdir(parents=True, exist_ok=True)
    download_img(url_img1, dir, img_name)
    dir = f'images'
    Path(dir).mkdir(parents=True, exist_ok=True)
    fetch_spacex_imgs(url_spacex, dir)
    dir = f'images/nasa'
    Path(dir).mkdir(parents=True, exist_ok=True)
    fetch_nasa_imgs(url_nasa, API_KEY, dir)
    dir = f'images/nasa/epic'
    Path(dir).mkdir(parents=True, exist_ok=True)
    fetch_nasa_epic_imgs(url_nasa_epic_data, url_nasa_epic_img, API_KEY, dir)

    tg_token = os.environ['TG_TOKEN']
    bot = telegram.Bot(token=tg_token)
    print(bot.get_me())
    chat_id = '@nasa_cosmos_photos'

    imgs_paths = []
    for root, dirs, files in os.walk("images", topdown=False):
        for name in files:
            imgs_paths.append(os.path.join(root, name))

    updater = Updater(tg_token)
    dispatcher = updater.dispatcher
    updater.start_polling()
    bot.send_message(
        chat_id=chat_id,
        text="Hi! In this channel we'll post NASA photos of the space",
    )

    pause = int(os.getenv('TIME_SLEEP', default='86400'))
    img_num = 0
    while True:
        if img_num < (len(imgs_paths)-1):
            img_path = imgs_paths[img_num]
            bot.send_document(chat_id=chat_id, document=open(img_path, 'rb'))
            time.sleep(pause)
            img_num += 1
    updater.idle()
