from django.core.management.base import BaseCommand
from newsletter.models import User
from newsletter.email import send_email


class Command(BaseCommand):
    """
    Custom Django manage.py command that sends a weather-powered email for
    each user that is in the database.

    Usage: `$ python manage.py sendnewsletter`
    """
    def handle(self, *args, **kwargs):
        users = User.objects.all()
        for user in users:
            try:
                send_email(user)
                print('Email Successfully sent to {}'.format(user.email))
            except:
                print('Could not send email to {}'.format(user.email))
