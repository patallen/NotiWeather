from django.views.generic.edit import FormView
from newsletter.forms import SubscribeForm

class SubscribeView(FormView):
    success_url = '/success'
    template_name = 'subscribe.html'
    form_class = SubscribeForm
