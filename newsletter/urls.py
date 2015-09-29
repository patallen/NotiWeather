from newsletter.views import SubscribeView
from django.conf.urls import url

urlpatterns = [
    url(r'^$', SubscribeView.as_view(), name='subscribe'),
]
