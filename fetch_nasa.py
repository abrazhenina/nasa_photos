import datetime
import os

from dotenv import load_dotenv

from download_img import download_img
from download_img import get_response


load_dotenv()
NASA_KEY = os.environ['NASA_KEY']


DIR_NASA = f'images/nasa'
DIR_EPIC = f'images/nasa/epic'
URL_NASA = 'https://api.nasa.gov/planetary/apod'
URL_EPIC_DATA = 'https://api.nasa.gov/EPIC/api/natural/images'
URL_EPIC_IMG = 'https://api.nasa.gov/EPIC/archive/natural/'
NUM_NASA_PHOTOS = 1


def fetch_nasa_imgs(dir, api_key, url=URL_NASA):
    params = {'api_key': NASA_KEY, 'count': NUM_NASA_PHOTOS}
    response = get_response(url, params=params)
    img_urls = []
    for img_data in response.json():
        if img_data['url']:
            img_urls.append(img_data['url'])
    if img_urls[0]:
        for img_url in img_urls:
            if '.jpg' or '.gif' in img_url:
                try:
                    img_name = os.path.split(img_url)[1]
                    img_response = get_response(img_url)
                    download_img(dir, img_name, img_response)
                except:
                    print('Error with url')
                    img_name = ''
            else:
                print('Error with url')
                img_name = ''


def fetch_nasa_epic_imgs(url_data, url_img, dir, api_key):
    params = {'api_key': NASA_KEY}
    response = get_response(url_data, params=params)
    for epic_img in response.json():
        img_name = epic_img['image']
        img_name = f'{img_name}.png'
        img_date = epic_img['date']
        date_time = datetime.datetime.fromisoformat(img_date)
        date = date_time.strftime('%Y/%m/%d')
        url_get_img = f'{url_img}{date}/png/{img_name}'
        response = get_response(url_get_img, params=params)
        download_img(dir, img_name, response)


def fetch_nasa(api_key):
    fetch_nasa_imgs(DIR_NASA, api_key, URL_NASA)
    fetch_nasa_epic_imgs(URL_EPIC_DATA, URL_EPIC_IMG, DIR_EPIC, api_key)


if __name__ == '__main__':
    fetch_nasa(NASA_KEY)
