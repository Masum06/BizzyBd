from django.conf.urls import url
from cards.views import IndexView, ThemesView, CardCreateView, CardView


urlpatterns = [
    url(r'^$', IndexView.as_view(), name='index'),
    url(r'^themes/$', ThemesView.as_view(), name='cards_themes'),
    url(r'^themes/(?P<theme_id>[0-9]+)/create-card/$', CardCreateView.as_view(),
        name='cards_create_card'),
    url(r'^(?P<card_url>[\w\-]+)/$', CardView.as_view(), name='cards_card'),


]
