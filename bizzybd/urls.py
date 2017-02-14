from django.conf.urls import url

from ajax_request import views
# from django.views.generic import TemplateView


urlpatterns = [

    # url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^cards/url/$', views.CardsUrlView.as_view(), name='cards_url'),
    # url(r'^fpitem/$', views.FPItemView.as_view(), name='fpitem')

]