from django.conf.urls import url
from ajax_request import views


urlpatterns = [
    url(r'^div/$', views.UpdateDiv.as_view(), name='div'),

]
