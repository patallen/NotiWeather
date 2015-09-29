from newsletter.views import SubscribeView
from django.views.generic.base import TemplateView
from django.conf.urls import url

urlpatterns = [
    url(r'^$', SubscribeView.as_view(), name='subscribe'),
    url(r'^success/', TemplateView.as_view(template_name='success.html'), name='subscribe'),
]
