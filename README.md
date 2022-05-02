# Cosmic NASA photos publisher in Telegram channel

The script downloads NASA photos of the space and publishes them in a telegram channel through a telegram bot through a regulable period of time.

Set a period of time in the variable `TIME_SLEEP` (in seconds) in the .env file, it has a value of '10' by default (to publish once a day set it to '86400')


### How to install


Python3 should be already installed. 
Then use `pip` (or `pip3`, if there is a conflict with Python2) to install dependencies:
```
pip install -r requirements.txt
```

In the `.env` file set:
1. NASA_KEY for NASA API, get it [here](https://api.nasa.gov/) after the registration.
2. TG_TOKEN for Telegram API, get it [here](https://telegram.me/BotFather) (use the token of an already cerated bot or create a new one)
3. TG_CHAT_ID - get it from the Telegram channel description where you want to post photos
4. TIME_SLEEP - set the time (in seconds) of the pause between posts in the channel

### Running the tests

If you launch the script it will post photos in the telegram channel every 10 seconds as a test. So after the test change the `TIME_SLEEP` variable as you need.


### Project Goals

The code is written for educational purposes on online-course for web-developers [dvmn.org](https://dvmn.org/).
