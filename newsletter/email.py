from newsletter.weather import get_weather_json
from django.core.mail import EmailMultiAlternatives

NICE_OUT_SUBJECT = "It's nice out! Enjoy a discount on us!"
POOR_OUT_SUBJECT = "Not so nice out? That's okay, enjoy a discount on us!"
REGULAR_SUBJECT = "Enjoy a discount on us!"

def send_email(user):
    """
    Function that handles the sending of weather-powered emails to users.
    This function takes a User instance, retrieves it's weather JSON from
    Wunderground, calculates the output for the email subject and body, then
    sends the email.
    """
    data = get_weather_json(user)

    # Exctract necessary variables from JSON
    weather_now = data['current_observation']['weather']
    temp_now = float(data['current_observation']['temp_f'])
    avg_high = float(data['almanac']['temp_high']['normal']['F'])
    icon_url = data['current_observation']['icon_url']
    readable_weather = '{} degrees, {}.'.format(temp_now, weather_now.lower())

    # Set subject based on current conditions
    if (temp_now >= avg_high+5) or ('sun' in weather_now.lower()):
        subject = NICE_OUT_SUBJECT
    elif (temp_now <= avg_high-5) or ('rain' in weather_now.lower()):
        subject = POOR_OUT_SUBJECT
    else:
        subject = REGULAR_SUBJECT

    # TODO: Replace this with send_mail code
    print(weather_now, temp_now, avg_high, icon_url)
    print(subject)
    print(readable_weather)