import os


import telegram
import time

from dotenv import load_dotenv
from fetch_nasa import fetch_all_nasa_imgs
from fetch_spacex import fetch_spacex_imgs
from pathlib import Path
from telegram.ext import Updater


def post_to_telegram(api_key, tg_token, chat_id, dir):
    fetch_spacex_imgs()
    fetch_all_nasa_imgs(api_key)
    bot = telegram.Bot(token=tg_token)
    print(bot.get_me())

    imgs_paths = []
    for root, dirs, files in os.walk("images", topdown=False):
        for name in files:
            imgs_paths.append(os.path.join(root, name))

    updater = Updater(tg_token)
    dispatcher = updater.dispatcher
    updater.start_polling()
    bot.send_message(
        chat_id=chat_id,
        text="Hi! In this channel we post NASA photos of the space",
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


if __name__ == '__main__':
    load_dotenv()
    API_KEY = os.environ['API_KEY']
    TG_TOKEN = os.environ['TG_TOKEN']
    CHAT_ID = os.environ['CHAT_ID']
    DIR = os.environ['DIR']
    dir = f'{DIR}'
    post_to_telegram(API_KEY, TG_TOKEN, CHAT_ID, dir=f'images')
