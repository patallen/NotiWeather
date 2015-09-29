from newsletter.models import User
from django.forms import ModelForm
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit


class SubscribeForm(ModelForm):
    """
    Form that allows a user to input his or her email address and select a city
    from a list of the top 100 U.S. cities by population. Both fields from the
    User model are used - no exclusions.
    """
    class Meta:
        model = User
        exclude = []

    def __init__(self, *args, **kwargs):
        """
        Add crispy_forms helper for adding a submit button and override a
        couple field properties to better fit the provided screenshot.
        """
        self.helper = FormHelper()
        self.helper.add_input(Submit('submit', 'Subscribe', css_class="btn-block"))
        super(SubscribeForm, self).__init__(*args, **kwargs)

        self.fields['location'].empty_label = "Where do you live?"
        self.fields['email'].label = "Email Address"
