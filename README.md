# Cosmic NASA photos publisher in Telegram channel

The script downloads NASA photos of the space and publishes them in a telegram channel through a telegram bot through a regulable period of time.

Set a period of time in the variable `TIME_SLEEP` (in seconds) in the .env file, it has a value of '10' by default (to publish once a day set it to '86400')

There are 4 scripts:
1. `save_img.py` with a function `save_img` which given a url of an image, a directory where to save it and the name under which to save it (all as strings) and parameters argument (a header with api key as a dictionary), downloads and saves that image. Being not given any argument it downloads an image with default values of arguments.

2. `fetch_spacex.py` with a function `fetch_spacex_imgs` with the default arguments - spacex api url with photos from the their last launches and a directory where to save images, so it doesn't need no arguments to be called.
This script uses `save_img.py` script.

3. `fetch_nasa.py` where `fetch_nasa_today_imgs` given how many photos to download in `NUM_NASA_PHOTOS` downloads "Astronomic pictures of the day", `fetch_nasa_epic_imgs` downloads photos of the Earth collected by DSCOVR's Earth Polychromatic Imaging Camera (EPIC) instrument, and `fetch_nasa_imgs` calls previous two functions.
This script also uses `save_img.py` script.

4. `post_to_telegram.py` imports and launches `fetch_spacex_imgs` and `fetch_nasa_imgs` and posts all these photos to the given telegram chat using a telegram bot.


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

Then open the command line, use `cd` command to move to the folder with the script and launch it by
```
python post_to_telegram.py
``` 
or
```
python3 post_to_telegram.py
``` 


How this script works looks like this:
1. it creates "images" folder, downloads spacex images there
2. then creates "nasa" folder in "images" and downloads astronomic pictures of the day there
3. then creates "epic" folder in "nasa" and downloads photos of the Earth there
4. launches telegram bot, prints the data about the bot in the command line, and the bot posts an image in a given period of time in the given telegram channel.


![script execution example](https://sun9-38.userapi.com/s/v1/ig2/IFMH9JY8sJ9fExUNPdLlRB1AdWxHRqCJOMODBx0x1ohwIjOshOFKraMCXl5-Vmd09SsX6Y45Nj8lRNU7aI65pOiM.jpg?size=1454x1498&quality=96&type=album)



### Running the tests

If you launch the script it will post photos in the telegram channel every 10 seconds as a test. So after the test change the `TIME_SLEEP` variable as you need.
