import os
import time

import telegram
from dotenv import load_dotenv
from telegram.ext import Updater

from fetch_nasa import fetch_nasa_imgs
from fetch_spacex import fetch_spacex_imgs

DIR = f'images'


if __name__ == '__main__':
    load_dotenv()
    NASA_KEY = os.environ['NASA_KEY']
    TG_TOKEN = os.environ['TG_TOKEN']
    TG_CHAT_ID = os.environ['TG_CHAT_ID']
    TIME_SLEEP = os.getenv('TIME_SLEEP', default='86400')
    fetch_spacex_imgs()
    fetch_nasa_imgs(NASA_KEY)
    bot = telegram.Bot(token=TG_TOKEN)
    print(bot.get_me())
    imgs_paths = []
    for root, dirs, files in os.walk(DIR, topdown=False):
        for name in files:
            imgs_paths.append(os.path.join(root, name))
    updater = Updater(TG_TOKEN)
    updater.start_polling()
    bot.send_message(
        chat_id=TG_CHAT_ID,
        text="Hi! In this channel we post NASA photos of the space",
    )
    pause = int(TIME_SLEEP)
    for img_path in imgs_paths:
        bot.send_document(chat_id=TG_CHAT_ID, document=open(img_path, 'rb'))
        time.sleep(pause)
    updater.idle()

