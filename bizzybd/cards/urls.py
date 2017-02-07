from django.conf.urls import url
from cards.views import IndexView, ThemesView


urlpatterns = [
    url(r'^$', IndexView.as_view(), name='index'),
    url(r'^themes/$', ThemesView.as_view(), name='cards_themes'),
]
