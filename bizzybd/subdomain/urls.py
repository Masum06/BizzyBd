from django.conf.urls import url
from subdomain import views

urlpatterns = [
    url(r'^', views.IndexView.as_view(), name='index'),
    # url(r'^mysite/$', MysiteView.as_view(), name='mysite'),

]
