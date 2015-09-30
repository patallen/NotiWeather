from django.views.generic.edit import FormView
from newsletter.forms import SubscribeForm


class SubscribeView(FormView):
    """
    Main view that handles the user's entry of email address and location.
    """
    success_url = '/success'
    template_name = 'subscribe.html'
    form_class = SubscribeForm

    def form_valid(self, form):
        """
        Save the form if the input is valid. Valid input includes a unique
        and valid email address and a non-empty location selection.
        """
        form.save()
        return super(SubscribeView, self).form_valid(form)
