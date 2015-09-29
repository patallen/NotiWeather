from django.core.management.base import BaseCommand
from newsletter.models import User
from newsletter.email import send_email

class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        users = User.objects.all()
        for user in users:
            send_email(user)