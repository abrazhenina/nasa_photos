import os
import time

import telegram
from dotenv import load_dotenv
from telegram.ext import Updater

from fetch_nasa import fetch_nasa
from fetch_spacex import fetch_spacex


load_dotenv()
NASA_KEY = os.environ['NASA_KEY']
TG_TOKEN = os.environ['TG_TOKEN']
TG_CHAT_ID = os.environ['TG_CHAT_ID']
TIME_SLEEP = os.getenv('TIME_SLEEP', default='86400')

DIR = f'images'


def post_to_telegram(api_key, tg_token, chat_id, dir):
    fetch_spacex()
    fetch_nasa(api_key)
    bot = telegram.Bot(token=tg_token)
    print(bot.get_me())
    imgs_paths = []
    for root, dirs, files in os.walk(DIR, topdown=False):
        for name in files:
            imgs_paths.append(os.path.join(root, name))
    updater = Updater(tg_token)
    updater.start_polling()
    bot.send_message(
        chat_id=chat_id,
        text="Hi! In this channel we post NASA photos of the space",
    )
    pause = int(TIME_SLEEP)
    for img_path in imgs_paths:
        bot.send_document(chat_id=chat_id, document=open(img_path, 'rb'))
        time.sleep(pause)
    updater.idle()


def main():
    post_to_telegram(NASA_KEY, TG_TOKEN, TG_CHAT_ID, DIR)


if __name__ == '__main__':
    main()
