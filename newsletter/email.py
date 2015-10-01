from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template
from django.template import Context

from newsletter.weather import get_weather_json
from NotiWeather import settings

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
    location = data['current_observation']['display_location']['full']
    weather_now = data['current_observation']['weather']
    temp_now = float(data['current_observation']['temp_f'])
    avg_high = float(data['almanac']['temp_high']['normal']['F'])
    icon_url = data['current_observation']['icon_url']
    readable_weather = '{} degrees, {}.'.format(temp_now, weather_now.lower())

    email = user.email
    # Set email's subject based on current conditions
    # NOTE: We are using the average high temperature in our comparison...
    # -- This could be done a variety of ways including using the median of the
    # -- average high and low temperature, or using the average low in the
    # -- morning/night and the average high during the day.
    subject = REGULAR_SUBJECT
    if (temp_now >= avg_high+5) or ('clear' in weather_now.lower()):
        subject = NICE_OUT_SUBJECT
    if (temp_now <= avg_high-5) or ('rain' in weather_now.lower()):
        subject = POOR_OUT_SUBJECT

    text = get_template('email/newsletter.txt')
    html = get_template('email/newsletter.html')
    context = Context(
        {
            'location': location,
            'icon_url': icon_url,
            'weather': readable_weather
        }
    )
    html_content = html.render(context)
    text_content = text.render(context)

    message = EmailMultiAlternatives(
        subject,
        text_content,
        settings.EMAIL_HOST_USER,
        [email]
    )
    message.attach_alternative(html_content, 'text/html')
    message.send()
