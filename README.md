# Cosmic NASA photos publisher in Telegram channel

The script downloads NASA photos of the space and publishes them in a telegram channel through a telegram bot through a regulable period of time.

Set a period of time in the variable `TIME_SLEEP` (in seconds) in the .env file, it has a value of '10' by default (to publish once a day set it to '86400')


### How to install


Python3 should be already installed. 
Then use `pip` (or `pip3`, if there is a conflict with Python2) to install dependencies:
```
pip install -r requirements.txt
```


## Running the tests

If you launch the script it will post photos in the telegram channel every 10 seconds as a test. So after the test change the `TIME_SLEEP` variable as you need.


### Project Goals

The code is written for educational purposes on online-course for web-developers [dvmn.org](https://dvmn.org/).
