from django.views.generic.edit import FormView
from newsletter.forms import SubscribeForm


class SubscribeView(FormView):
    success_url = '/success'
    template_name = 'subscribe.html'
    form_class = SubscribeForm

    def form_valid(self, form):
        form.save()
        return super(SubscribeView, self).form_valid(form)
