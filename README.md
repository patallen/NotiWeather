# NotiWeather
Small weather notification app built using Django and Wunderground API

## Environment Setup
1. `$ mkvirtualenv notiweather`
1. `$ vim ~/.virtualenvs/notiweather/bin/postactivate`
1. Add the following:
```
export EMAIL_HOST_USER='your_gmail@gmail.com'
export EMAIL_HOST_PASSWORD='your_gmail_app_password'
export WUNDERGROUND_KEY='your_wunderground_api_key'
```

## Application Setup
1. `$ pip install -r requirements.txt`
1. `$ ./manage.py createsuperuser`
1. `$ ./manage.py seed`

## Usage
1. Start the server `$ ./manage.py runserver`
1. Navigate to `localhost:8000` in your browser
1. Subscribe using your email address and a city close to you.
1. To send the emails `$ ./manage.py sendnewsletter`
