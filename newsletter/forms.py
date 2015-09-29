from newsletter.models import User
from django.forms import ModelForm


class SubscribeForm(ModelForm):
    """
    Form that allows a user to input his or her email address and select a city
    from a list of the top 100 U.S. cities by population. Both fields from the
    User model are used - no exclusions.
    """
    class Meta:
        model = User
        exclude = []
