from django.conf.urls import url
from ajax_request import views


urlpatterns = [
    url(r'^div/$', views.UpdateDiv.as_view(), name='div'),
    url(r'^slim/async/$', views.SlimAync.as_view(), name='slim_async'),
    # url(r'^slim/async/$', views.SlimAyncView, name='slim_async'),
]
