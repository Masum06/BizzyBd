from django.conf.urls import url, include
from cards import views


urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^themes/$', views.ThemesView.as_view(), name='cards_themes'),
    url(r'^themes/(?P<theme_id>[0-9]+)/create-card/$', views.CardCreateView.as_view(),
        name='cards_create_card'),
    url(r'^all-cards/$', views.AllCardView.as_view(), name='cards_all_cards'),
    url(r'^(?P<card_url>[\w\-]+)/$', views.CardView.as_view(), name='cards_card'),
    # url(r'^captcha/', include('captcha.urls')),
    url(r'^ajax_request/url', views.UrlCheckView.as_view(), name='url_check'),

]
